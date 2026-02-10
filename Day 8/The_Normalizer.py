import numpy as np


scores = np.random.randint(50, 101, size=(5, 3))
subject_mean = scores.mean(axis=0)

centered_scores = scores - subject_mean

print("Original scores:\n", scores)
print("\nSubject means:\n", subject_mean)
print("\nCentered scores:\n", centered_scores)
