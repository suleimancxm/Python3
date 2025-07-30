# Write your solution here
total_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = total_students // group_size

if total_students % group_size !=0:
    groups += 1
print(f"Number of groups formed: {groups}")