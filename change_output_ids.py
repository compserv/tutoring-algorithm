import json

with open("scheduler_input.json") as f:
    data = json.load(f)

with open("output.json") as f:
    assigned = json.load(f)

new_assigned = dict()

tutors = data["tutors"]
slots = data["slots"]

for slid in assigned:
    new_assigned["1" + str(slid)] = assigned[slid]

with open("upload_ready_output.json", "w") as f:
    json.dump(new_assigned, f)
