# First, let's import all the required libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

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

