import numpy as np

data = np.arange(24)

data_reshaped = data.reshape(4, 3, 2)
final = data_reshaped.transpose(0, 2, 1)

print("Final shape:", final.shape)
print("Final array:\n", final)