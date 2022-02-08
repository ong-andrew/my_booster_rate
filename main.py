import pandas as pd
import datetime
from datetime import date, timedelta

data = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/vaccination/vax_state.csv'

mergeKV = {'Selangor': 'Sel & WP',
'W.P. Kuala Lumpur': 'Sel & WP',
'W.P. Putrajaya': 'Sel & WP'
}

labuan = {'W.P. Labuan': 'Labuan'}

malaysia = {'Johor': 'Malaysia',
'Kedah': 'Malaysia',
'Kelantan': 'Malaysia',
'Melaka': 'Malaysia',
'Negeri Sembilan': 'Malaysia',
'Pahang': 'Malaysia',
'Perak': 'Malaysia',
'Perlis': 'Malaysia',
'Pulau Pinang': 'Malaysia',
'Sabah': 'Malaysia',
'Sarawak': 'Malaysia',
'Selangor': 'Malaysia',
'Terengganu': 'Malaysia',
'Sel & WP': 'Malaysia',
'W.P. Kuala Lumpur': 'Malaysia',
'W.P. Labuan': 'Malaysia',
'W.P. Putrajaya': 'Malaysia'
}

#Write Malaysia
df = pd.read_csv(data, usecols=['date','state','cumul_booster'], parse_dates=['date'])
df['state'] = "Malaysia"
df = df.groupby(['date','state']).sum().reset_index()
df = df[df.date.dt.date == date.today() - timedelta(days = 1)]
df['population'] = 32657400
df['booster_rate'] = df['cumul_booster'] / df['population'] * 100
df['boost_rate'] = df['booster_rate'].round(decimals=1).astype(str) + '%'
df[['state','boost_rate']].to_csv('boost_rate.csv',mode='w',index=False)

#Append states
df = pd.read_csv(data, usecols=['date','state','cumul_booster'], parse_dates=['date'])
df.state = df.state.replace(mergeKV)
df.state = df.state.replace(labuan)
df = df.groupby(['date','state']).sum().reset_index()
df = df[df.date.dt.date == date.today() - timedelta(days = 1)]
df['population'] = [3781000,2185100,1906700,99600,932700,1128800,1678700,2510300,254900,1773600,3908500,2816500,8421700,1259300]
df['booster_rate'] = df['cumul_booster'] / df['population'] * 100
df['boost_rate'] = df['booster_rate'].round(decimals=1).astype(str) + '%'
df[['state','boost_rate']].to_csv('boost_rate.csv',mode='a',header=False,index=False)
