import pandas as pd
import numpy as np
import openpyxl

data = pd.read_excel('nba_player_data.xlsx')
#sorting data by players 
sorted_data = data.sort_values(by='PLAYER')

#creating the new sheet
with pd.ExcelWriter('nba_player_data.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_data.to_excel(writer, sheet_name='PlayerOrgainzed', index=False)
