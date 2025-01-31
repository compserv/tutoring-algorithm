import json

TUTORING_START_HOUR = 13
TUTORING_END_HOUR = 16

# They stack.
REVIEW_SESSION_SUBTRACTED_HOURS = 2
EXECS_SUBTRACTED_HOURS = 2
PRODEV_SUBTRACTED_HOURS = 2

excluded_ppl = []
review_session_ppl = []
prodev_ppl = []
execs = []

with open("base_params.json") as f:
    data = json.load(f)

tutors = data["tutors"]
print("Len all tutors before subtracted hours:", len(tutors), len(excluded_ppl))
tutors = list(filter(lambda t: t["name"] not in excluded_ppl, tutors))
for tutor in tutors:
   if tutor["name"] in review_session_ppl:
       tutor["numAssignments"] -= REVIEW_SESSION_SUBTRACTED_HOURS
   if tutor["name"] in prodev_ppl:
       tutor["numAssignments"] -= PRODEV_SUBTRACTED_HOURS
   if tutor["name"] in execs:
       tutor["numAssignments"] -= EXECS_SUBTRACTED_HOURS
       
tutors = list(filter(lambda t: t["numAssignments"] > 0, tutors))
print("Len all tutors after subtracted hours:", len(tutors))

data["tutors"] = tutors
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
slots = list(filter(lambda s: s["hour"] >= TUTORING_START_HOUR, slots))
slots = list(filter(lambda s: s["hour"] <= TUTORING_END_HOUR, slots))
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
