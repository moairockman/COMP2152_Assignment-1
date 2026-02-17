"""
Author: Isaac Natera
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Isaac Natera"
preferred_weight_kg = 20.5
highest_reps = 20
membership_active = True




# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Isaac": (20, 30, 40),
    "Ethan": (50, 70, 90),
    "Beray": (40, 55, 70)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friends, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats = [friends + "Total"]
# Step e: Create a 2D nested list called workout_list
workout_list = []
for friend, minutes in workout_stats.items():
    if not friends.endswith("Total"):
        workout_list.append(list(minutes))

# Step f: Slice the workout_list
# Yoga and running minutes for my friends
print("Yoga and Running minutes for all my friends:")
for row in workout_list:
    print(row[0:2])

#weightlifting minutes for last two friends
print("Weightlifting minutes of last two friends")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120
print("Friends with 120 or more total workout minutes:")
for key, value in workout_stats.items():
    if key.endswith("Total") and value >= 120:
        friend_name = key.replace("Total", "")
        print(f"Good job! Keep up the good work, {friend_name}.")
# Step h: User input to look up a friend
friend_input = input("Please Enter a Friend's Name: ")

if friend_input in workout_stats:
    print(f"{friend_input}'s workout minutes (Yoga, Running, Weightlifting): {workout_stats[friend_input]}")

    total_key = friend_input + "Total"
    if total_key in workout_stats:
        print(f"Total workout minutes: {workout_stats[total_key]}")

else:
    print(f"Friend {friend_input} not found in the records.")
# Step i: Friend with highest and lowest total workout minutes
totals_only={}

for key, value in workout_stats.items():
    if key.endswith("Total"):
        friend_name = key.replace("Total", "")
        total_only[friend_name] = value

highest_friend = max(totals_only, key=totals_only.get)
lowest_friend = min(totals_only, key=totals_only.get)

print("Friend with the highest total workout minutes:")
print(highest_friend, "-", totals_only[highest_friend])

print("Friend with the lowest total workout minutes:")
print(lowest_friend, "-", totals_only[lowest_friend])