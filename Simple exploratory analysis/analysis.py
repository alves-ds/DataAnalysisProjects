# First, let's import all the required libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from scipy.stats import ttest_1samp

# Now, let's import our database. It is in a .sav format, so we need to 
dados = pd.read_spss('dados_lista1.sav')

# Let's have a look in our data
dados

# We have a database with 36 workers in a company. So, let's do an exploratory analysis, following pre-established questions


# Question 1 - Build frequency tables for data relating to level of education, marital status and region of origin.
# For this, let's use the 'crosstab' method from pandas. 
frequency_table = pd.crosstab(dados['grau_de'], 'count')

# Let's compute a variable to see the relative proportions
frequency_table['percentage'] = frequency_table/len(dados)

# To improve the interpretation, let's multiply the relative proportion by 100
frequency_table['percentage'] = frequency_table['percentage']*100

# Let's have a look in our frequency table
frequency_table

# Now, let's do the same for the other categorical variables

frequency_marital = pd.crosstab(dados['estado_c'], 'count')

frequency_marital['percentage'] = frequency_marital/len(dados)*100

frequency_marital

frequency_origin_region = pd.crosstab(dados['origem'], 'count')

frequency_origin_region['percentage'] = frequency_origin_region/len(dados)*100

frequency_origin_region

# Question 2 - graph these tables
# Let's do it using subplots:
    
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 6), sharey=True)
ax1.bar(frequency_table.index, frequency_table['percentage'])
ax1.set_ylabel('Proportion of total sample')
ax2.bar(frequency_origin_region.index, frequency_origin_region['percentage'])
ax3.bar(frequency_marital.index, frequency_marital['percentage'])
plt.show()

# Question 3 - Compare, statistically (α=5%), whether there are differences in the distribution of the number of children and the average age depending on the regions of origin of the workers.

# First, let's have a look in the distribution of our dependent variables (age and number of childs), using histograms.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
ax1.hist(dados['idade'])
ax1.set_ylabel('Idade (anos)')
ax2.hist(dados['n_mero_d'])
ax2.set_ylabel('Número de filhos')
plt.show()

# We can note an assymetric distribution for both variables, but let's compare these variables by using analysis of variance
anova_age = f_oneway(dados['idade'][dados['origem'] == 'Interior'],
                     dados['idade'][dados['origem'] == 'Capital'],
                     dados['idade'][dados['origem'] == 'Outro'])

anova_childs = f_oneway(dados['n_mero_d'][dados['origem'] == 'Interior'],
                     dados['n_mero_d'][dados['origem'] == 'Capital'],
                     dados['n_mero_d'][dados['origem'] == 'Outro'])

# For both tests it was not possible to see any effect of origin. 


# Question 4 - Calculate the average salary and average age of single and married people
age_marital = dados.groupby('estado_c')['idade'].describe()
salary_marital = dados.groupby('estado_c')['sal_rio1'].describe()

# Question 5 - Check the association between marital status and level of education. Is it possible to say that there is a significant association between marital status and level of education (α=5%)?
# To test this association, let's to use a qui-square test. 

# First, let's calculate the contingency table
contingency_marital_edu = pd.crosstab(dados['estado_c'], dados['grau_de'])

# Now let's to apply the test to our contingency table

chi2, p_value, _, _ = chi2_contingency(contingency_marital_edu)

# Let's see the contingency table
contingency_marital_edu

# Let's see the p value
p_value

# Based on the p-value we can see that there is not a relationship between marital status and level of education

# Question 6 - According to IBGE data, the average age of the population of SP is 31 years old. Does the sample presented have a significant difference in mean age in relation to the population mean estimate?

# To answear this question, let's use a one-sample t test

age_one_sample_t_test = ttest_1samp(dados['idade'], 31)

# By means of a one sample t test it is possible to see a significante difference (p = 0.003) between the age of our sample and the population mean, with a mean difference of 3.58 years.

# Question 7 - The salary of this sample was measured in three consecutive years (06,07 and 08). Was there a difference between the salary over time? (α=5%).

# First, let's have a look into the distribution of our data in the 3 different times


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))
ax1.hist(dados['sal_rio'])
ax1.set_ylabel('Salary (first measure)')
ax2.hist(dados['sal_rio1'])
ax2.set_ylabel('Salary (second measure)')
ax3.hist(dados['sal_rio2'])
ax3.set_ylabel('Salary (third measure)')
plt.show()

# We can see that our measures aren't symetric, but we will use a repeated measures anova
