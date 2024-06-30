import pandas as pd
import requests
import time
import numpy as np

df = pd.read_excel('nba_player_data.xlsx', sheet_name='Sheet1')

#Delete columns
df = df.drop(columns=['PLAYER_ID', 'PLAYER'])
#writing the data frame back to the execel file
df.to_excel('nba_player_data.xlsx', sheet_name='Sheet1', index=False)