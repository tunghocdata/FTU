﻿import pandas as pd
from datetime import datetime 
from collections import Counter

df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])

# Sort by user_id and timestamp to ensure the stall visits are in order
df = df.sort_values(by=['Person ID', 'Timestamp'])

#user_paths = df.groupby('Person ID')['Shelf ID'].apply(lambda x: ' -> '.join(map(str, x))).reset_index()


# Remove consecutive duplicate shelves for each user
df['previous_shelf'] = df.groupby('Person ID')['Shelf ID'].shift(1)
df_filtered = df[df['Shelf ID'] != df['previous_shelf']]

# Create a list of shelves visited for each user
#shelves_visited = df_filtered.groupby('Person ID')['Shelf ID'].apply(list).reset_index()

df_filtered['transition'] = list(zip(df_filtered['previous_shelf'], df_filtered['Shelf ID']))

df_filtered = df_filtered.dropna(subset=['previous_shelf'])
transition_counts = Counter(df_filtered['transition'])

top_transitions = transition_counts.most_common(6)


for transition, count in top_transitions:
    print(f"Transition from {transition[0]} to {transition[1]}: {count} times")
