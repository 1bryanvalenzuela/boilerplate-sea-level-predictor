import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    minyear = df["Year"].loc[df["Year"].idxmin()]
    predict = intercept + slope * range(minyear,2051)
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level", alpha=0.5, color="blue")

    # Create first line of best fit
    plt.plot(range(minyear,2051),predict, color="red")

    # Create second line of best fit
    x2 = df[df["Year"] >= 2000]["Year"]
    y2 = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x2,y2)
    predict2 = intercept + slope * range(2000,2051)
    plt.plot(range(2000,2051),predict2, color="red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()