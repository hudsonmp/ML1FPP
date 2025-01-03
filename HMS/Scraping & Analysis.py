import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
import random
hms = pd.read_csv('/Users/hudsonmitchell-pullman/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Learning to Code/Codecademy/Final Portfolio Project/HMS/HMS_2023-2024_PUBLIC_instchars.csv', low_memory = False)


# Set display options for all columns and rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows (optional)
pd.set_option('display.width', None)  # Adjust the width of the display to avoid wrapping
pd.set_option('display.colheader_justify', 'left')  # Align headers to the left for better readability

# Example of displaying the DataFrame
#print(hms.head())
hms = hms[['educ_par1', 'educ_par2', 'gr_A', 'gr_B', 'gr_C', 'gr_D', 'gr_F', 'gr_none', 'gr_dk', 'belong1', 'aca_impa', 'positiveMH', 'dep_any', 'sui_idea', 'exerc', 'internet_1', 'stig_pcv_1', 'stig_per_1', 'percneed', 'know_sp', 'lonely']]
#print(hms.head())
#print(hms.info())
#print(hms.describe(include = 'all'))
hms.columns = ['education_parent1', 'education_parent2', 'grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk', 'belonging', 'mh_academic_impact', 'positiveMH', 'depression', 'suicide_ideation', 'exercise', 'internet_usage', 'pcv_mh_stigma', 'per_mh_stigma', 'perceived_need', 'perceived_mh_knowledge', 'lonely']
# Sample syntax: df['First Season'] = np.where(df['First Season'] > 1990, 1, df['First Season'])
hms[['grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk']] = hms[['grade_a', 'grade_b', 'grade_c', 'grade_d', 'grade_f', 'grade_none', 'grade_dk']].fillna(value = 0)
hms.grade_b = np.where(hms.grade_b == 1, 2, hms.grade_b)
hms.grade_c = np.where(hms.grade_c == 1, 3, hms.grade_c)
hms.grade_d = np.where(hms.grade_d == 1, 4, hms.grade_d)
hms.grade_f = np.where(hms.grade_f == 1, 5, hms.grade_f)
hms = hms.fillna(value = hms.mean())
# I created a completely subjective definition of 'academic_success', which I defined as having a's and b's or just having b's.
hms['academic_success'] = hms.apply(lambda row: 1 if (row.grade_a == 1 and (row.grade_a + row.grade_b + row.grade_c + row.grade_d + row.grade_f <= 3)) or row.grade_a + row.grade_b + row.grade_c + row.grade_d + row.grade_f <= 2 else 0, axis = 1)
#print(hms.describe(include = 'all'))
print(hms.head(28))
##### I made a mistake here. I used Pearson to describe two binary categorical variables, which did allow me to properly calculate association between the variables.
#define, pearson = pearsonr(hms['academic_success'], hms['positiveMH'])
#define_2, pearson_2 = pearsonr(hms['academic_success'], hms['depression'])

#print('The pearson correlation coefficient between academic_success and positiveMH is ', define)
#print('The pearson correlation coefficient between academic_success and depression is ', define_2)
## Analyze how an openness or reduction in stigma is associated with mental health status
crosstab1 = pd.crosstab(hms['positiveMH'], hms['academic_success'])
chi2, pval, dof, expected1 = chi2_contingency(crosstab1)
print(expected1)
print(crosstab1)
print('The chi-square is ', np.round(chi2, 2))
print(hms.shape)
print('The Cramer V is ', np.round(np.sqrt(chi2 / (104729 * 2)), 2))
print('________________________________________________________________________________')
crosstab2 = pd.crosstab(hms['depression'], hms['academic_success'])
chi2_1, pval, dof, expected2 = chi2_contingency(crosstab2)
print(expected2)
print(crosstab2)
print('The chi-square is ', np.round(chi2_1, 2))

print('The Cramer V is ', np.round(np.sqrt(chi2_1 / (104729 * 2)), 2))
print('________________________________________________________________________________')
crosstab3 = pd.crosstab(hms['positiveMH'], hms['pcv_mh_stigma'])
chi2_2, pval, dof, expected3 = chi2_contingency(crosstab3)
print(expected3)
print(crosstab3)
print('The chi-square is ', np.round(chi2_2, 2))

print('The Cramer V is ', np.round(np.sqrt(chi2_2 / (104729 * 2)), 2))
print('________________________________________________________________________________')
crosstab5 = pd.crosstab(hms['depression'], hms['per_mh_stigma'])
chi2_5, pval, dof, expected5 = chi2_contingency(crosstab5)
print(expected5)
print(crosstab5)
print('The chi-square is ', np.round(chi2_5, 2))

print('The Cramer V is ', np.round(np.sqrt(chi2_5 / (104729 * 2)), 2))

### Probability of being depressed given suicidal thoughts
dep_sui = pd.crosstab(index = hms.depression, columns = hms.suicide_ideation, margins = True)
print(dep_sui)
print(dep_sui.iloc[2, 3] / dep_sui.iloc[3, 3])


prob_dep_given_sui = dep_sui.iloc[2, 2] / dep_sui.iloc[3, 2]
print('The probability of feeling depressed given having suicidal ideations is {}%'.format(prob_dep_given_sui * 100))
prob_sui_given_dep = dep_sui.iloc[2, 2] / dep_sui.iloc[2, 3]
print('The probability of having suicidal ideation given that one already feels depressed is {}%'.format(prob_sui_given_dep * 100))
lonely_belonging = pd.crosstab(hms['lonely'], hms.belonging, margins = True, normalize = True)
print(lonely_belonging)
depression_belonging = pd.crosstab(hms['depression'], hms.belonging, margins = True, normalize = True)
print(depression_belonging)
## Sum of probabilities
sum_prob_no_belonging = depression_belonging.iloc[3, [4, 5, 6]].sum()
sum_prob_lonely_belonging = lonely_belonging.iloc[2, [4, 5, 6]].sum()
sum_prob_depression_belonging = depression_belonging.iloc[2, [4, 5, 6]].sum()
prob_lonely_giv_belonging = sum_prob_lonely_belonging / sum_prob_no_belonging
prob_depression_giv_belonging = sum_prob_depression_belonging / sum_prob_no_belonging
prob_lonely_depression_giv_belonging = prob_lonely_giv_belonging * prob_depression_giv_belonging
prob_lonely_depression_and_belonging = prob_lonely_depression_giv_belonging * sum_prob_lonely_belonging
prob_lonely_or_depression_given_belonging =  ((sum_prob_depression_belonging + sum_prob_lonely_belonging - prob_lonely_depression_and_belonging) / sum_prob_no_belonging)
print('The probability of feeling lonely or depressed given a lack of a sense of belonging is {}%'.format(np.round(prob_lonely_or_depression_given_belonging * 100, 1)))

### Continue analyzing parents' effect on education after exercise and internet

hms['avg_parent_education'] = hms.apply(lambda row: ((row.education_parent1 + row.education_parent2) / 2), axis = 1)
edu_par_std = hms.avg_parent_education.std()

edu_par_mean = hms.avg_parent_education.mean()
## Probability of having parents who don't have college degrees.
print(stats.norm.cdf(4, edu_par_mean, edu_par_std))


#print(hms.avg_parent_education.head(25))
avg_par_edu_samp = np.random.choice(hms['avg_parent_education'], size = 25, replace = False)

# Converting exercise and internet usage into numeric values

print(hms.info())

students = 104729
zero_exercise = 0.267
no_exercise_count = students * zero_exercise



