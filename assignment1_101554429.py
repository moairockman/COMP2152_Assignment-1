"""
Author: Isaac Natera
Assignment: #1
"""

gym_member = "Isaac Natera"
preferred_weight_kg = 20.5
highest_reps = 20
membership_active = True

workout_stats = {
    "Isaac": (20, 30, 40),
    "Ethan": (50, 70, 90),
    "Beray": (40, 55, 70)
}

# Add totals safely
totals = {}
for friend, minutes in workout_stats.items():
    totals[friend + "Total"] = sum(minutes)

workout_stats.update(totals)

# Build workout list
workout_list = []
for friend, minutes in workout_stats.items():
    if not friend.endswith("Total"):
        workout_list.append(list(minutes))

print("Yoga and Running minutes for all my friends:")
for row in workout_list:
    print(row[0:2])

print("Weightlifting minutes of last two friends")
for row in workout_list[-2:]:
    print(row[2])

print("Friends with 120 or more total workout minutes:")
for key, value in workout_stats.items():
    if key.endswith("Total") and value >= 120:
        friend_name = key.replace("Total", "")
        print(f"Good job! Keep up the good work, {friend_name}.")

friend_input = input("Please Enter a Friend's Name: ")

if friend_input in workout_stats:
    print(f"{friend_input}'s workout minutes (Yoga, Running, Weightlifting): {workout_stats[friend_input]}")

    total_key = friend_input + "Total"
    if total_key in workout_stats:
        print(f"Total workout minutes: {workout_stats[total_key]}")
else:
    print(f"Friend {friend_input} not found in the records.")
for key, value in workout_stats.items():
    totals_only = {}

    if key.endswith("Total"):
        friend_name = key.replace("Total", "")
        totals_only[friend_name] = value

highest_friend = max(totals_only, key=totals_only.get)
lowest_friend = min(totals_only, key=totals_only.get)

print("Friend with the highest total workout minutes:")
print(highest_friend, "-", totals_only[highest_friend])

print("Friend with the lowest total workout minutes:")
print(lowest_friend, "-", totals_only[lowest_friend])


