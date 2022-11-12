import random
import time


def generate_lottos():
    x_valid = False
    while x_valid == False:
        x = input("Enter maximum difference in expected values: ")
        if x == "":
            print("Please enter a number between 0 and 100 (<5 will yield close lotteries).")
            continue
        eval_range = int(x)
        if (0 <= eval_range <= 100):
            x_valid = True
        else:
            print("Please enter a number between 0 and 100 (<5 will yield close lotteries).")
    
    y_valid = False
    while y_valid == False:
        y = input("Enter maximum difference in outcome uncertainties: ")
        if y == "":
            print("Enter a number between 10 and 10,000. ~150 will yield lotteries with similar uncertainty.")
            continue
        ou_range = int(y)
        if (9 < ou_range < 10001):
            y_valid = True
        else:
            print("Enter a number between 10 and 10,000. ~150 will yield lotteries with similar uncertainty.")

    rand_colors_v1 = []
    rand_colors_v2 = []
    exp_val_v1 = 0
    exp_val_v2 = 50
    blue_value_v1 = 0
    red_value_v1 = 0
    blue_value_v2 = 0
    red_value_v2 = 0
    blue_percent_v1 = 0
    blue_percent_v2 = 0
    red_percent_v1 = 0
    red_percent_v2 = 0
    num_blues_v1 = 0
    num_reds_v2 = 0
    outcome_uncertainty_v1 = 0
    outcome_uncertainty_v2 = 0
    total_its = 0

    # ensure expected values of each vase are within x pts of each other
    # ensure lotteries are within desired expected value
    # ensure blue/red is not the high/low in both vases
    # ensure blue/red is not majority color in both vases
    # match for similar outcome uncertainty
    # prevent mirror images
    while (abs(exp_val_v1 - exp_val_v2) > eval_range) or (exp_val_v1 > 80) \
        or (blue_percent_v1 < red_percent_v1 and blue_percent_v2 < red_percent_v2) \
        or (red_percent_v1 < blue_percent_v1 and red_percent_v2 < blue_percent_v2) \
        or (blue_value_v1 > red_value_v1 and blue_value_v2 > red_value_v2) \
        or (red_value_v1 > blue_value_v1 and red_value_v2 > blue_value_v2) \
        or (abs(outcome_uncertainty_v1 - outcome_uncertainty_v2) > ou_range) \
        or (num_blues_v1 == num_reds_v2 and blue_value_v1 == red_value_v2) \
        or (blue_value_v1 == red_value_v2 and blue_value_v2 == red_value_v1):

        # re-initialize values to prevent memory overwrites
        exp_val_v1 = 0
        exp_val_v2 = 50
        blue_value_v1 = 0
        red_value_v1 = 0
        blue_value_v2 = 0
        red_value_v2 = 0
        blue_percent_v1 = 0
        blue_percent_v2 = 0
        red_percent_v1 = 0
        red_percent_v2 = 0
        outcome_uncertainty_v1 = 0
        outcome_uncertainty_v2 = 0
        num_blues_v1 = 0
        num_reds_v2 = 0

        # determine lottery distributions and values
        blue_percent_v1 = (random.randrange(5, 100, 5)) / 100
        red_percent_v1 = 1 - blue_percent_v1
        blue_percent_v2 = (random.randrange(5, 100, 5)) / 100
        red_percent_v2 = 1 - blue_percent_v2
        num_blues_v1 = round(20*blue_percent_v1)
        num_reds_v2 = round(20*red_percent_v2)

        while blue_value_v1 == red_value_v1:
            blue_value_v1 = random.randrange(10, 100, 10)
            red_value_v1 = random.randrange(10, 100, 10)
        while blue_value_v2 == red_value_v2:
            blue_value_v2 = random.randrange(10, 100, 10)
            red_value_v2 = random.randrange(10, 100, 10)

        # calculate expected values and outcome uncertainties
        exp_val_v1 = (blue_percent_v1 * blue_value_v1) + (red_percent_v1 * red_value_v1)
        exp_val_v2 = (blue_percent_v2 * blue_value_v2) + (red_percent_v2 * red_value_v2)

        outcome_uncertainty_v1 = (blue_percent_v1*(blue_value_v1 - exp_val_v1)**2) \
                                + (red_percent_v1*(red_value_v1 - exp_val_v1)**2)
        outcome_uncertainty_v2 = (blue_percent_v2*(blue_value_v2 - exp_val_v2)**2) \
                                + (red_percent_v2*(red_value_v2 - exp_val_v2)**2)

        total_its += 1

        if total_its > 100000:
            raise RuntimeError("Timeout. Could not find unique lotteries that match these requirements.")

    # log number of its
    # print("{} iterations to complete.".format(total_its))

    num_reds_v1 = round(20*red_percent_v1)
    num_blues_v2 = round(20*blue_percent_v2)

    rand_colors_v1 = []
    rand_colors_v2 = []
    # create list of blues/reds
    for i in range(num_blues_v1):
        rand_colors_v1.append("blue")
    for j in range(num_reds_v1):
        rand_colors_v1.append("red")

    assert len(rand_colors_v1) == 20
    # shuffle the list
    random.shuffle(rand_colors_v1)

    # make five rows of four marbles each for lottery layout
    vase1 = []
    n = 4
    i = 0
    while i < len(rand_colors_v1):
        row = []
        while i < n:
                row.append(rand_colors_v1[i])
                i += 1
        n += 4
        vase1.append(row)

    # repeat for vase 2
    for i in range(int(num_blues_v2)):
        rand_colors_v2.append("blue")
    for j in range(int(num_reds_v2)):
        rand_colors_v2.append("red")

    assert len(rand_colors_v2) == 20
    random.shuffle(rand_colors_v2)

    vase2 = []
    n = 4
    i = 0
    while i < len(rand_colors_v2):
        row = []
        while i < n:
                row.append(rand_colors_v2[i])
                i += 1
        n += 4
        vase2.append(row)

    # display results
    print("Vase 1:")
    for row in vase1:
        print(row)
    print("{} blues, blue = {} pts".format(num_blues_v1, blue_value_v1))
    print("{} reds, red = {} pts".format(num_reds_v1, red_value_v1))
    print("Expected value = {} pts".format(round(exp_val_v1, 1)))
    print("Outcome uncertainty = {}".format(round(outcome_uncertainty_v1, 1)))
    print("------------------------------")
    print("Vase 2:")
    for row in vase2:
        print(row)
    print("{} blues, blue = {} pts".format(num_blues_v2, blue_value_v2))
    print("{} reds, red = {} pts".format(num_reds_v2, red_value_v2))
    print("Expected value = {} pts".format(round(exp_val_v2, 1)))
    print("Outcome uncertainty = {}".format(round(outcome_uncertainty_v2, 1)))

    return [rand_colors_v1, rand_colors_v2, blue_value_v1, red_value_v1, blue_value_v2, red_value_v2, exp_val_v1, exp_val_v2]


def main():
    play_again = "y"
    score = 0
    total_eval = 0
    while play_again == "y":
        results = generate_lottos()
        rand_colors_v1, rand_colors_v2 = results[0], results[1]
        blue_value_v1, red_value_v1 = results[2], results[3]
        blue_value_v2, red_value_v2 = results[4], results[5]
        exp_val_v1, exp_val_v2 = results[6], results[7]

        valid_choice = False
        while valid_choice == False:
            x = input("Choose a vase (Enter 1 or 2): ")
            if x == "":
                print("Please enter either 1 or 2.")
                continue
            choice = int(x)
            if not (choice == 1 or choice == 2):
                print("Please enter either 1 or 2.")
            else:
                valid_choice = True

        i = random.randint(0, 19)
        print("Drawing a marble...")
        time.sleep(1)
        if choice == 1:
            total_eval += exp_val_v1
            if rand_colors_v1[i] == "blue":
                print("You got marble #{}, which is blue (+{} points).".format(i+1, blue_value_v1))
                score += blue_value_v1
            elif rand_colors_v1[i] == "red":
                print("You got marble #{}, which is red (+{} points).".format(i+1, red_value_v1))
                score += red_value_v1
        elif choice == 2:
            total_eval += exp_val_v2
            if rand_colors_v2[i] == "blue":
                print("You got marble #{}, which is blue (+{} points).".format(i+1, blue_value_v2))
                score += blue_value_v2
            elif rand_colors_v2[i] == "red":
                print("You got marble #{}, which is red (+{} points).".format(i+1, red_value_v2))
                score += red_value_v2
        print("Your score = {}. Total expected value = {}.".format(score, round(total_eval)))
        play_again = ""
        while not (play_again == "y" or play_again == "n"):
            play_again = input("Play again? (y or n): ")
            if not (play_again == "y" or play_again == "n"):
                print("Must enter either y or n.")

    print("You got {} points out of {} total expected points.".format(score, round(total_eval)))
    percent = score/total_eval * 100
    message = ""
    if percent > 150:
        message = " DAMN you're lucky."
    if 150 > percent > 120:
        message = " WOW!"
    if 120 > percent > 100:
        message = " Wow!"
    if 100 > percent > 90:
        message = " Good job!"
    elif percent < 60:
        message = " Better luck next time."
    print("You were {:.0%} successful.{} Thanks for playing.".format(round((score/total_eval),10), message))

if __name__ == "__main__":
    main()