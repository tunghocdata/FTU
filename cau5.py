import pandas as pd
from datetime import datetime 
from collections import Counter

df = pd.read_csv('03_Customer_Behavior_Data.csv')


# Define age groups
bins = [18, 30, 60, float('inf')]  # Teenagers: 18-30, Middle Age: 31-60, Elderly: >60
labels = ['Teenagers', 'Middle Ages', 'Elderly']

# Create a new column for age groups
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
df.dropna()
df.drop_duplicates()
# Count the number of people in each age group
age_group_counts = df['Age Group'].value_counts()

# Print the result
print(age_group_counts)
