import random

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
total_its = 0

# ensure expected values of each vase are within x pts of each other
# ensure lotteries are within desired expected value
# ensure blue/red is not the high/low in both vases
# ensure blue/red is not majority color in both vases
# match for similar outcome uncertainty
# prevent mirror images
while (abs(exp_val_v1 - exp_val_v2) > 3) or (exp_val_v1 > 80) \
    or (blue_percent_v1 < red_percent_v1 and blue_percent_v2 < red_percent_v2) \
    or (red_percent_v1 < blue_percent_v1 and red_percent_v2 < blue_percent_v2) \
    or (blue_value_v1 > red_value_v1 and blue_value_v2 > red_value_v2) \
    or (red_value_v1 > blue_value_v1 and red_value_v2 > blue_value_v2) \
    or (abs(outcome_uncertainty_v1 - outcome_uncertainty_v2) > 120) \
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

# log number of its
print("{} iterations to complete.".format(total_its))

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
