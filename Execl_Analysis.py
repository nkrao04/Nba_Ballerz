import pandas as pd
import numpy as np
import openpyxl

data = pd.read_excel('nba_player_data.xlsx')
#sorting data by players 
sorted_data = data.sort_values(by='PLAYER')

#add space between players
rows_with_spaces = []
last_player = None

for index, row in sorted_data.iterrows():
    current_player = row['PLAYER']
    if last_player is not None and current_player != last_player:
        rows_with_spaces.append(pd.Series([''] * len(sorted_data.columns), index=sorted_data.columns))
        rows_with_spaces.append(row)
        last_player = current_player

with_space_data = pd.DataFrame(rows_with_spaces)

#creating the new sheet
with pd.ExcelWriter('nba_player_data.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_data.to_excel(writer, sheet_name='PlayerOrgainzed', index=False)
