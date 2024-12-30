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
#print(hms.head())
hms = hms[['educ_par1', 'educ_par2', 'gr_A', 'gr_B', 'gr_C', 'gr_D', 'gr_F', 'gr_none', 'gr_dk', 'belong1', 'aca_impa', 'positiveMH', 'dep_any', 'sui_idea', 'exerc', 'internet_1', 'stig_pcv_1', 'stig_per_1', 'percneed', 'know_sp']]
#print(hms.head())
#print(hms.info())
#print(hms.describe(include = 'all'))
hms.columns = ['education_parent1', 'educ_parent2', 'grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk', 'belonging', 'mh_academic_impact', 'positiveMH', 'depression', 'suicide_ideation', 'exercise', 'internet_usage', 'pcv_mh_stigma', 'per_mh_stigma', 'perceived_need', 'perceived_mh_knowledge']
# Sample syntax: df['First Season'] = np.where(df['First Season'] > 1990, 1, df['First Season'])
hms[['grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk']] = hms[['grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk']].fillna(value = 0)
hms.grade_b = np.where(hms.grade_b == 1, 2, hms.grade_b)
hms.grade_c = np.where(hms.grade_c == 1, 3, hms.grade_c)
hms.grade_d = np.where(hms.grade_d == 1, 4, hms.grade_d)
hms.grade_f = np.where(hms.grade_f == 1, 5, hms.grade_f)
hms = hms.fillna(value = hms.mean())
# I created a completely subjective definition of 'academic_success', which I defined as having a's and b's or just having b's.
hms['academic_success'] = hms.apply(lambda row: 1 if (row.grade_a == 1 and (row.grade_a + row.grade_b + row.grade_c + row.grade_d + row.grade_f <= 3)) or row.grade_a + row.grade_b + row.grade_c + row.grade_d + row.grade_f <= 2 else 0, axis = 1)
print(hms.describe(include = 'all'))
print(hms.head(28))

define, pearson = pearsonr(hms['academic_success'], hms['positiveMH'])
define_2, pearson_2 = pearsonr(hms['academic_success'], hms['depression'])

print('The pearson correlation coefficient between academic_success and positiveMH is ', define)
print('The pearson correlation coefficient between academic_success and depression is ', define_2)
sns.boxplot(data=hms, x='positiveMH', y='academic_success')
plt.title('Positive Mental Health by Academic Success')
plt.show()

sns.boxplot(data=hms, x='depression', y='academic_success')
plt.title('Depression by Academic Success')
plt.show()


