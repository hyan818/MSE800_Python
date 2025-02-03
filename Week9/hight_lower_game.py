import random

from game_data import data

if __name__ == "__main__":
    random_two = random.sample(data, 2)
    print(
        f"Compare A: {random_two[0].get('name')}, from {random_two[0].get('country')}"
    )
    print(
        f"Against B: {random_two[1].get('name')}, from {random_two[1].get('country')}"
    )
    answer = input("Who has more followers? Type 'A' or 'B': ")

    CORRECT_ANSWER = ""
    if random_two[0].get("follower_count") > random_two[1].get("follower_count"):
        CORRECT_ANSWER = "A"
    elif random_two[0].get("follower_count") > random_two[1].get("follower_count"):
        CORRECT_ANSWER = "B"
    else:
        print("They are the same.")
        CORRECT_ANSWER = ""

    if answer.upper() == CORRECT_ANSWER:
        print("correct")
    else:
        print("wrong")
