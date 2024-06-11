# First, let's import all the required libraries
import pandas as pd

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
