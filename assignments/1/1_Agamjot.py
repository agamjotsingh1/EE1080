import random
import utils

# Set the seed for reproducibility
random.seed(42)

# Define the maximum number of trials
# To avoid overflow, we set a limit for maximum number of trails
max_trials = int(1e10)

def sim_petersburg(m):
    """
    Simulates St. Petersburg paradox.

    m -> The number of times the game is played.
    Returns the average reward over m simulations.
    """
    total_reward = 0 # Total reward in m games
    p = 0.5 # Fair coin is assumed

    for _ in range(m):  # Repeat the game m times
        
        # Coin is tossed until tails appear
        # or when number of tosses exceeds max_trials
        for i in range(max_trials):
            is_heads = utils.bernoulli(p) # Bernoulli sample with parameter = p

            if not is_heads:  # Stop when tails appears
                total_reward += pow(2, i + 1)  # Adding reward to cummulative sum
                break

    return (total_reward/m) 

# Run the simulation with different numbers of games
print(sim_petersburg(100))
print(sim_petersburg(10000))
print(sim_petersburg(10000000))

