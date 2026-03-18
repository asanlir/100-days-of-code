import random
from art.hi_lo import logo, vs
from hi_lo_data import data


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    compare_B = random.choice(data)

    while game_should_continue:
        compare_A = compare_B
        compare_B = random.choice(data)

        if compare_A == compare_B:
            compare_B = random.choice(data)

        print(f"Compare A: {compare_A['name']}, a {compare_A['description']} from {compare_A['country']}.")
        print(vs + "\n")
        print(f"Against B: {compare_B['name']}, a {compare_B['description']} from {compare_B['country']}." + "\n")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_follower_count = compare_A["follower_count"]
        b_follower_count = compare_B["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}." + "\n")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
