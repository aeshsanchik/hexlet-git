import random
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def even_game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        number = random.randint(1, 777)
        print(f"Question: {number}")

        user_answer = input("Your answer: ")
        correct_answer = "yes" if is_even(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"{user_answer} is wrong answer :( Correct answer was {correct_answer}"
            )
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")


def main():
    even_game()


if __name__ == "__main__":
    main()
