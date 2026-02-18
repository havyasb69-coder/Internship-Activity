import itertools
import random

# PART 1: Customer Action Model

print("----- CUSTOMER ACTION PROBABILITY -----\n")

actions = ["Click", "Scroll", "Exit"]

# Define Sample Space for two consecutive actions
sample_space = list(itertools.product(actions, repeat=2))

print("Sample Space S:")
for outcome in sample_space:
    print(outcome)

# Event E: At least one Click
event_E = [outcome for outcome in sample_space if "Click" in outcome]

# Calculate Probability
prob_E = len(event_E) / len(sample_space)

print("\nEvent E (At least one Click):")
for outcome in event_E:
    print(outcome)

print("\nTotal Possible Outcomes:", len(sample_space))
print("Favorable Outcomes:", len(event_E))
print("Probability of at least one Click:", prob_E)


# PART 2: Dice Simulation


print("\n----- DICE SIMULATION -----\n")

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Total Trials:", trials)
print("Number of times sum = 7:", count_sum_7)
print("Experimental Probability of sum = 7:", experimental_probability)

# Theoretical Probability
theoretical_probability = 1/6
print("Theoretical Probability of sum = 7:", theoretical_probability)