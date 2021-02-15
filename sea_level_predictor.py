import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv (r'./epa-sea-level.csv', delimiter=',', float_precision='legacy')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    bestFit = linregress(df['Year'], df['CSIRO Adjusted Sea Level']);
    xBestFit = np.arange(df['Year'].min(), 2050,1)
    yBestFit = xBestFit * bestFit.slope + bestFit.intercept
    plt.plot(xBestFit, yBestFit, color="green");

    # Create second line of best fit


    # Add labels and title
    plt.title('Rise in Sea Level');
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
