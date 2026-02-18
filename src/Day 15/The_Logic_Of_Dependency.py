import random

# Independent Events
# Coin = Heads AND Die = 6
trials = 10000
count_heads_and_6 = 0

for _ in range(trials):
    coin = random.choice(["Heads", "Tails"])
    die = random.randint(1, 6)

    if coin == "Heads" and die == 6:
        count_heads_and_6 += 1

exp_prob_independent = count_heads_and_6 / trials
theoretical_prob_independent = (1/2) * (1/6)

print("----- Independent Events -----")
print("Experimental Probability (Heads & 6):", exp_prob_independent)
print("Theoretical Probability (Heads & 6):", theoretical_prob_independent)


# Dependent Events
# Pick 2 red marbles without replacement

count_both_red = 0

for _ in range(trials):
    bag = ["Red"] * 5 + ["Blue"] * 5   # 5 Red, 5 Blue marbles
    first = random.choice(bag)
    bag.remove(first)                # without replacement
    second = random.choice(bag)

    if first == "Red" and second == "Red":
        count_both_red += 1

exp_prob_dependent = count_both_red / trials
theoretical_prob_dependent = (5/10) * (4/9)

print("\n----- Dependent Events -----")
print("Experimental Probability (Both Red):", exp_prob_dependent)
print("Theoretical Probability (Both Red):", theoretical_prob_dependent)