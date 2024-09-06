import pandas as pd
from datetime import datetime 
from collections import Counter

df = pd.read_csv('03_Customer_Behavior_Data.csv')


def age_group(age):
    if 18 <= age <= 30:
        return 'Teenagers'
    elif 31 <= age <= 60:
        return 'Middle age'
    else:
        return 'Senior'

# Apply age group function
df['Age Group'] = df['Age'].apply(age_group)

# Filter data where 'Picking up item' and 'Putting item into bag' are TRUE
filtered_data = df[(df['Picking up item'] == True) & (df['Putting item into bag'] == True)]

# Group by 'Age Group' and 'Item ID', and count the occurrences
item_counts = filtered_data.groupby(['Age Group', 'Item ID', 'Shelf ID']).size().reset_index(name='Count')

# Find the most purchased item per age group
most_purchased = item_counts.loc[item_counts.groupby('Age Group')['Count'].idxmax()]

print(most_purchased)


##   Age Group  Item ID  Shelf ID  Count
#10   Middle age        1         2    108
#144      Senior        1         2     57
#278   Teenagers        1         2     56
