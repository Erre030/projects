
#description: user chooses a level (1-3) which determines how many places the ints used in the exercises shall have. Afterwards, 10 exercises are created.
            # The user has three tries for each exercises. If he fails all three, the answer of the specific exercises is shown and the next exercise is displayed.
            # At the end a counter hands back the number of exercises answered correctly by the user.

import random

def main():
    number_size = get_level()
    #print(number_size)
    first_int, second_int = generate_exercises(number_size)
    solve(first_int,second_int)






















#check for valid level input(1,2,3) --> if not int--> reprompt / if not 1,2,3 --> raise ValueError and repromt
def get_level():
    number_volume= input("Level: ")

    while True:
        try:
            number_volume = int(number_volume)
            if number_volume in [1,2,3]:
                return number_volume
            else:
                raise ValueError
        except ValueError:
            number_volume= input("Level: ")


# handles int generation with given amount of places (--> level)
def generate_intlength(level):
    if level == 1:
        lower_bound = 10**(level-1) -1                     #otherwise 0 is not included
        upper_bound = (10**level)-1
        return random.randint(lower_bound, upper_bound)
    else:
        lower_bound = 10**(level-1)
        upper_bound = (10**level)-1
        return random.randint(lower_bound, upper_bound)


#generate 10 random math problems and their answers
def generate_exercises(level):

    first_int = []
    second_int = []

    for i in range(10):         #no need to create loop variable or add one in the loop (i =+ 1) --> python does it automatically
        int_1 = generate_intlength(level)
        int_2 = generate_intlength(level)
        first_int.append(int_1)
        second_int.append(int_2)

    return first_int, second_int


def solve(first_int, second_int):
    answers_solved = 0

    for i in range(10):
        tries = 0

        while tries < 3:

            try:
                user_answer = int(input(f"{first_int[i]} + {second_int[i]} = "))

                if user_answer == first_int[i] + second_int[i]:     #right answer
                    answers_solved += 1
                    break               #break out of while-loop and start interation with next i
                else:
                    raise ValueError                                #wrong answer or not int

            except ValueError:
                print("EEE")
                tries += 1

        if tries >= 3:
            answer = first_int[i] + second_int[i]
            print(f"{first_int[i]}+{second_int[i]}={answer}")           #displays correct answer if three tries exhausted

    print(f"You've answered {answers_solved} exercises correctly.")


if __name__ == "__main__":          #needed, because tests often import your script --> execution beneath here only allowed if the script is the "main" program
    main()
