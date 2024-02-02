import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import A

# Generate a random dataset
n = 16
data = [A.countCircles(A.createRandomPermutation(n)) for _ in range(100000)]
average = np.mean(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the plot
plt.figure(figsize=(10, 6))
sns.histplot(data, kde=False, color='blue', bins=range(n+1))

#
plt.axvline(average, color='red', linestyle='dashed', linewidth=2)
plt.text(average, plt.ylim()[1] * 0.95, f'Mean: {average:.2f}', color='red', ha='center')

# Adding titles and labels
plt.title(f'Distribution of circles on a permutation with a length of {n}')
plt.xlabel('Value')
plt.xticks(range(n+1))
plt.ylabel('Frequency')

# Display the plot
plt.show()
