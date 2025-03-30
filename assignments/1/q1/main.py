import random
import '../utils.py'

# Set the seed for reproducibility
random.seed(123)

# Define the maximum number of trials
# To avoid overflow, we set a limit for maximum number of trails
max_trials = int(1e10)

def sim_petersburg(m):
    """
    Simulates St. Petersburg paradox.

    m -> The number of times the game is played.
    Returns the average payout over m simulations.
    """
    avg = 0
    p = 0.5 # Fair coin is assumed

    for _ in range(m):  # Repeat the game m times
        for i in range(max_trials):  # Simulate coin tosses
            if not bernoulli_coin_toss(p):  # Stop when tails appears
                avg += pow(2, i + 1)  # Compute reward based on the number of heads
                break  # Exit the inner loop and start a new game

    return avg / m  # Return the average payout

# Run the simulation with different numbers of games
print(sim_petersburg(100))        # Simulate 100 games
print(sim_petersburg(10000))      # Simulate 10,000 games
print(sim_petersburg(10000000))   # Simulate 10,000,000 games

