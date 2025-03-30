import sys
import pandas as pd
from math import sqrt, log
import numpy as np
import main
import matplotlib.pyplot as plt

def process_csv(file_path):
    # Read and display the CSV file
    try:
        df = pd.read_csv(file_path, skiprows=0)
        print("Reading contents of ",  file_path, ":\n")
        return df;
    except Exception as e:
        print("Error reading CSV file: {e}")

if __name__ == "__main__":        
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:",n)
    assert(n >= 2)

    mode_value = int(sys.argv[1]);
    print("Testing mode:", mode_value)

    #read the samples file
    input_fn= sys.argv[2];
    uniform_samples = process_csv(input_fn);
    print(uniform_samples)

    N = len(uniform_samples);
    print("N =",N);
    #similarly parse the third argument if mode is 0 or 1 to get p or lambda

    if mode_value == 0:
        assert(n >= 3)
        p = float(sys.argv[3])
        p_str = str(p).strip("0").replace(".", "p")

        bernoulli_samples = uniform_samples.map(lambda x: main.gen_bernoulli(x, p))
        bernoulli_samples.rename(columns={'Uniform Samples': 'Bernoulli Samples'}, inplace=True)
        bernoulli_samples.to_csv(f"Bernoulli_{p_str}.csv")

        print("Mean of Sample mean of the Bernoulli Samples = ", bernoulli_samples.mean()["Bernoulli Samples"])
    elif mode_value == 1:
        assert(n >= 3)
        lam = float(sys.argv[3])
        lam_str = str(lam).strip("0").replace(".", "p")

        exp_samples = uniform_samples.map(lambda x: main.gen_exp(x, lam))
        exp_samples.rename(columns={'Uniform Samples': 'Exponential Samples'}, inplace=True)
        exp_samples.to_csv(f"Exponential_{lam_str}.csv")

        plt.hist(exp_samples, bins=int(sqrt(N)), rwidth=0.7, label=f"Exponential Samples, Bins = {int(sqrt(N))}")
        plt.legend()
        plt.show()
    else:
        cdfx_samples = uniform_samples.map(lambda x: main.gen_cdfx(x))
        cdfx_samples.rename(columns={'Uniform Samples': 'CDFX Samples'}, inplace=True)
        cdfx_samples.to_csv(f"CDFX.csv")

        count_2 = cdfx_samples['CDFX Samples'].value_counts().get(2.0, 0)
        print("Number of 2's in CDFX Samples = ", count_2)


        plt.hist(cdfx_samples, bins=int(sqrt(N)), rwidth=0.7, label=f"CDFX Samples, Bins = {int(sqrt(N))}")
        plt.legend()
        plt.show()
