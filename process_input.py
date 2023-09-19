import json


with open("base_params.json") as f:
    data = json.load(f)

tutors = data["tutors"]
slots = data["slots"]


d = {
    "cory": dict(),
    "prodevcory": dict(),
}
for slot in slots:
    curr_d = d.get(slot["office"].lower(), None)
    if curr_d is None:
        continue
    curr_d[(slot["day"], slot["hour"])] = slot["sid"]

slots = list(filter(lambda s: s["office"].lower() != "prodevcory", slots))
data["slots"] = slots

mapping = dict()
for time, cory_id in d["cory"].items():
    prodev_id = d["prodevcory"][time]
    mapping[prodev_id] = cory_id


for tutor in tutors:
    batch_prefs = [tutor["timeSlots"], tutor["officePrefs"]]
    for prefs in batch_prefs:
        for prodev_id, cory_id in mapping.items():
            prefs[cory_id], prefs[prodev_id] = prefs[prodev_id], prefs[cory_id]


with open("scheduler_input.json", "w") as f:
    json.dump(data, f)
