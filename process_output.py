import json


INPUT_FNAME = "input.json"
OUTPUT_FNAME = "output.json"
PROCESSED_OUTPUT_FNAME = "processed_output.json"

ROOM_TO_REPLACE = "ProDevCory"
ROOM_REPLACE_WITH = "Cory"

ROOM_TO_STACK = "Soda"
ROOM_TO_UNSTACK = "Cory"

read_json_from_file = lambda path: json.load(open(path))
d = read_json_from_file(INPUT_FNAME)
output = read_json_from_file(OUTPUT_FNAME)
slots = d["slots"]

# Map all the rooms
filter_by_office = lambda office: {(slot["day"], slot["hour"]): slot["name"].removeprefix("InternalSlot") for slot in slots if slot["office"] == office}
to_replace = filter_by_office(ROOM_TO_REPLACE)
replace_with = filter_by_office(ROOM_REPLACE_WITH)
replace_mapping = {to_replace[k]: replace_with[k] for k in to_replace}

# Apply mapping to data destructively
for r1, r2 in replace_mapping.items():
    output[r2] = output[r1]
    del output[r1]

# For all the people with only one slot, move them to the room that we're stacking
to_stack = filter_by_office(ROOM_TO_STACK)
to_unstack = filter_by_office(ROOM_TO_UNSTACK)
stack_mapping = {to_unstack[k]: to_stack[k] for k in to_unstack}
slot_id_to_internal = {slot["sid"]: slot["name"].removeprefix("InternalSlot") for slot in slots}
adjacent_slot_ids = {slot["name"].removeprefix("InternalSlot"): [slot_id_to_internal[adj_slot_id] for adj_slot_id in slot["adjacentSlotIDs"] if adj_slot_id in output] for slot in slots}

tutor_to_stack = None
for slot_id in list(output):
    if slot_id not in stack_mapping:
        continue

    tutors_in_slot = output[slot_id]
    for tutor_in_slot in list(tutors_in_slot):
        has_adj_slot = False
        for adjacent_slot_id in adjacent_slot_ids[slot_id]:
            has_adj_slot &= tutor_in_slot in output[adjacent_slot_id]

        if not has_adj_slot:
            tutors_in_slot.remove(tutor_in_slot)
            tutor_to_stack = tutor_in_slot
            break

    if tutor_to_stack is not None:
        output[stack_mapping[slot_id]].append(tutor_to_stack)
        tutor_to_stack = None


json.dump(output, open(PROCESSED_OUTPUT_FNAME, "w"))
