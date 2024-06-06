import pandas as pd
import requests
import time
import numpy as np

pd.set_option('display.max_columns', None)

# Function to get data for a specific season and season type
def get_data(season, season_type):
    api_url = f'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season={season}&SeasonType={season_type}&StatCategory=PTS'
    r = requests.get(api_url).json()
    temp_df = pd.DataFrame(r['resultSet']['rowSet'], columns=r['resultSet']['headers'])
    temp_df.insert(0, 'Season_type', season_type)
    temp_df.insert(0, 'Year', season)
    return temp_df

# Initialize DataFrame and parameters
df = pd.DataFrame()
season_types = ['Regular%20Season', 'Playoffs']
years = ['2014-15', '2015-16', '2016-17', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24']

# Loop to collect data
begin_loop = time.time()
for y in years:
    for s in season_types:
        data = get_data(y, s)
        df = pd.concat([df, data], axis=0)
        print(f'Finished scraping data for the {y} {s}.')
        lag = np.random.uniform(low=5, high=40)
        print(f'...waiting {round(lag, 1)} seconds')
        time.sleep(lag)

print(f'Process Complete! Total run time: {round((time.time() - begin_loop) / 60, 2)} minutes')
df.to_excel('nba_player_data.xlsx', index=False)