import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from tabulate import tabulate as tb
from scipy.stats import pearsonr
hms = pd.read_csv('/Users/hudsonmitchell-pullman/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Learning to Code/Codecademy/Final Portfolio Project/HMS/HMS_2023-2024_PUBLIC_instchars.csv', low_memory = False)


# Set display options for all columns and rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows (optional)
pd.set_option('display.width', None)  # Adjust the width of the display to avoid wrapping
pd.set_option('display.colheader_justify', 'left')  # Align headers to the left for better readability

# Example of displaying the DataFrame
print(hms.head())

