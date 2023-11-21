import numpy as np

def simulate_majority_vote(sample_size, population_distribution, runs):
    # Simulating 'runs' number of experiments for each sample size
    majority_counts = 0
    
    np.random.seed(3)
    
    for _ in range(runs):
        # Randomly picking a sample from the population
        sample = np.random.choice(population_distribution, size=sample_size)
        # Check if +1 is the majority
        if np.sum(sample == 1) > sample_size / 2:
            majority_counts += 1
    
    # Calculate the probability of +1 being the majority
    probability = majority_counts / runs
    return probability

# Define the population distribution: 52% +1, 48% -1
population_distribution = np.array([1] * 520000 + [-1] * 480000)

# Define the sample sizes and the number of runs
sample_sizes = [20, 100, 400]
runs = 100
probabilities = [simulate_majority_vote(size, population_distribution, runs) for size in sample_sizes]

# Determine the sample size needed for a probability of 0.9
target_probability = 0.9
sample_size = 400  # Starting from 400
while True:
    prob = simulate_majority_vote(sample_size, population_distribution, runs)
    if prob >= target_probability:
        break
    sample_size += 1  # Increment sample size

print("probabilities: ")
print(probabilities)

print("sample size to become 0.9: ")
print(sample_size)