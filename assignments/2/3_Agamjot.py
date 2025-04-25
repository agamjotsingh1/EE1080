import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
# random.seed(42)

def process_csv(file_path):
    # Read and display the CSV file
    try:
        df = pd.read_csv(file_path, skiprows=0)
        print("Reading contents of ",  file_path, ":\n")
        return df;
    except Exception as e:
        print("Error reading CSV file: {e}")

def mmse_estimator(y, sigma_sq, mu_x, var_x):
    estimator = mu_x/var_x
    denom = 1/var_x

    for i in range(len(y)):
        estimator += y[i]/sigma_sq[i]
        denom += 1/sigma_sq[i]

    return estimator/denom

if __name__ == "__main__":        
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:",n)
    assert(n >= 2)

    mu_x = int(sys.argv[1]);
    print("mean of X", mu_x)

    var_x = int(sys.argv[2]);
    print("Variance of X", var_x)

    #read the mmse samples file
    input_fn= sys.argv[3];
    print(input_fn)

    mmse_samples = process_csv(input_fn);
    #if mmse_samples == None: exit(1);
    print(mmse_samples)

    N = len(mmse_samples);
    print("N=",N);

    mmse_samples_array = mmse_samples.to_numpy();
    print(mmse_samples_array)

    # prints below 0th sample value
    print(mmse_samples_array[0][0])

    #prints below sigmasquare corresponding to 0th sample
    print(mmse_samples_array[0][1])

    # For plotting the MMSE estimates vs N
    estimates = []
    x_axis = []

    for i in range(1, N + 1):
        y = mmse_samples_array[:i, 0]       # First i samples
        sigma_sq = mmse_samples_array[:i, 1]  # First i variances
        est = mmse_estimator(y, sigma_sq, mu_x, var_x)
        estimates.append(est)
        x_axis.append(i)

    # Create scatter plot
    plt.scatter(x_axis, estimates, color='#4169E1', label='MMSE Estimate of X')
    plt.xlabel('Number of Observations (N)')
    plt.ylabel('MMSE Estimate of X')
    plt.title('MMSE Estimate of X vs N')
    plt.legend(loc="lower right")
    plt.show()
