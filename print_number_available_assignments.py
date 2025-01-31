import json

with open("scheduler_input.json") as f:
    data = json.load(f)
    
tutors = data["tutors"]
slots = data["slots"]

total_assignments = 0

for tutor in tutors:
    total_assignments += tutor["numAssignments"]
    print(tutor["name"], ":", tutor["numAssignments"])
    
print("Total number of hours available for assignment: ", total_assignments) 