print("----- BAYES SPAM FILTER -----\n")

# Given probabilities
P_spam = 0.1              # P(Spam)
P_ham = 0.9               # P(Ham)
P_free_given_spam = 0.9   # P(Free | Spam)
P_free_given_ham = 0.05   # P(Free | Ham)

# Step 1: Total probability of seeing "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Step 2: Bayes theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

# Output
print("P(Spam):", P_spam)
print("P(Ham):", P_ham)
print("P(Free | Spam):", P_free_given_spam)
print("P(Free | Ham):", P_free_given_ham)

print("\nTotal Probability P(Free):", P_free)
print("P(Spam | Free):", P_spam_given_free)

print("\nInterpretation:")
print("If an email contains 'Free', there is about",
      round(P_spam_given_free * 100, 2),
      "% chance it is Spam.")
