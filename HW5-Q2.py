import numpy as np

def simulate_random_walk(steps, runs):
    # Simulating 'runs' number of random walks, each with 'steps' steps
    crossings = []
    for _ in range(runs):
        walk = np.random.choice([-1, 1], size=steps)
        # Compute the cumulative sum to get the position at each step
        positions = np.cumsum(walk)
        # Count the number of times the walk crosses the origin
        cross = np.sum(positions == 0)
        # cross = np.sum((positions[:-1] * positions[1:]) < 0)
        crossings.append(cross)
    return np.mean(crossings)

# Define the number of steps and runs
steps_list = [4 * 10**4, 9 * 10**4, 16 * 10**4]
runs = 50

# Run simulations and collect average crossings
average_crossings = [simulate_random_walk(steps, runs) for steps in steps_list]
print(average_crossings)