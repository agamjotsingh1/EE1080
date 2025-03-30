import sys
import pandas as pd
from math import sqrt
import utils
import matplotlib.pyplot as plt

def process_csv(file_path):
    """
    Reads a CSV file and returns its contents as a DataFrame.
    If there's an error (e.g., file not found or incorrect format), it prints an error message.
    """
    try:
        df = pd.read_csv(file_path, skiprows=0)
        print(f"Successfully read {file_path}!\n")
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def uniform_to_custom_cdfx(uniform_rv):
    """
    Transforms a uniform random variable into a custom CDFX distribution.
    The mapping follows a piecewise function:
      - If 0 <= x <= 1/3, it returns sqrt(3x)
      - If 2/3 <= x <= 1, it returns 6x - 2
      - Otherwise, it returns 0
    """
    if 0 <= uniform_rv <= 1/3:
        return sqrt(3 * uniform_rv)
    elif 2/3 <= uniform_rv <= 1:
        return 6 * uniform_rv - 2
    else:
        return 0  # Anything in (1/3, 2/3) gets mapped to 0

if __name__ == "__main__":
    # Print the number of arguments received
    n = len(sys.argv)
    print(f"Total arguments passed: {n}")

    # Print script name
    print(f"\nRunning script: {sys.argv[0]}")

    # Print the arguments
    print("\nArguments received:", sys.argv[1:])
    assert n >= 2, "Not enough arguments provided!"

    # Read the first argument, which determines the mode of operation
    mode_value = int(sys.argv[1])
    print(f"Operating in mode: {mode_value}")

    # Read the second argument, which should be the input file
    input_fn = sys.argv[2]
    uniform_samples = process_csv(input_fn)  # Read uniform samples from CSV
    print(uniform_samples)

    # Get the total number of samples
    N = len(uniform_samples)
    print(f"Total samples (N): {N}")

    # If mode is 0 or 1, we need a third argument (either p or lambda)
    if mode_value == 0:
        assert n >= 3, "Mode 0 requires a probability value (p)!"
        
        # Read the probability value
        p = float(sys.argv[3])
        p_str = str(p).strip("0").replace(".", "p")  # Format filename-friendly p value

        # Convert uniform samples to Bernoulli samples (0 or 1 based on p)
        bernoulli_samples = uniform_samples.map(lambda x: utils.uniform_to_bernoulli(x, p))
        bernoulli_samples.rename(columns={'Uniform Samples': 'Bernoulli Samples'}, inplace=True)
        
        # Save results to a new CSV file
        bernoulli_samples.to_csv(f"Bernoulli_{p_str}.csv")

        # Print the mean of the Bernoulli samples
        print(f"Mean of Bernoulli samples: {bernoulli_samples.mean()['Bernoulli Samples']}")

    elif mode_value == 1:
        assert n >= 3, "Mode 1 requires a lambda value!"
        
        # Read the lambda value
        lam = float(sys.argv[3])
        lam_str = str(lam).strip("0").replace(".", "p")  # Format filename-friendly lambda value

        # Convert uniform samples to exponential samples
        exp_samples = uniform_samples.map(lambda x: utils.uniform_to_exp(x, lam))
        exp_samples.rename(columns={'Uniform Samples': 'Exponential Samples'}, inplace=True)
        
        # Save results to a new CSV file
        exp_samples.to_csv(f"Exponential_{lam_str}.csv")

        # Plot a histogram of the generated exponential samples
        plt.hist(exp_samples, bins=int(sqrt(N)), rwidth=0.7, label=f"Exponential Samples, Bins = {int(sqrt(N))}")
        plt.legend()
        plt.show()

    else:
        # If mode is anything other than 0 or 1, use the custom CDFX transformation
        cdfx_samples = uniform_samples.map(lambda x: uniform_to_custom_cdfx(x))
        cdfx_samples.rename(columns={'Uniform Samples': 'CDFX Samples'}, inplace=True)
        
        # Save results to a new CSV file
        cdfx_samples.to_csv("CDFX.csv")

        # Count how many times the value 2 appears in the transformed samples
        count_2 = cdfx_samples['CDFX Samples'].value_counts().get(2.0, 0)
        print(f"Number of times 2 appears in CDFX samples: {count_2}")

        # Plot a histogram of the CDFX-transformed samples
        plt.hist(cdfx_samples, bins=int(sqrt(N)), rwidth=0.7, label=f"CDFX Samples, Bins = {int(sqrt(N))}")
        plt.legend()
        plt.show()
