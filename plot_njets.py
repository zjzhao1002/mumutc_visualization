import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

user = ""
password = ""

engine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:3306/test')

processes = ['mumutc', 'mumubb', 'mumucc', 'mumuqq', 'mumutt', 'mumuwjj', 'mumuww', 'mumuzz']

df_mumutc = pd.read_sql("SELECT * FROM mumutc", con=engine)
df_mumubb = pd.read_sql("SELECT * FROM mumubb", con=engine)
df_mumucc = pd.read_sql("SELECT * FROM mumucc", con=engine)
df_mumuqq = pd.read_sql("SELECT * FROM mumuqq", con=engine)
df_mumutt = pd.read_sql("SELECT * FROM mumutt", con=engine)
df_mumuwjj = pd.read_sql("SELECT * FROM mumuwjj", con=engine)
df_mumuww = pd.read_sql("SELECT * FROM mumuww", con=engine)
df_mumuzz = pd.read_sql("SELECT * FROM mumuzz", con=engine)

njets_mumutc = df_mumutc['njets'].to_numpy()
njets_mumubb = df_mumubb['njets'].to_numpy()
njets_mumucc = df_mumucc['njets'].to_numpy()
njets_mumuqq = df_mumuqq['njets'].to_numpy()
njets_mumutt = df_mumutt['njets'].to_numpy()
njets_mumuwjj = df_mumuwjj['njets'].to_numpy()
njets_mumuww = df_mumuww['njets'].to_numpy()
njets_mumuzz = df_mumuzz['njets'].to_numpy()

plt.hist(njets_mumutc, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='tc')
plt.hist(njets_mumubb, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='bb')
plt.hist(njets_mumucc, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='cc')
plt.hist(njets_mumuqq, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='qq')
plt.hist(njets_mumutt, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='tt')
plt.hist(njets_mumuwjj, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='Wjj')
plt.hist(njets_mumuww, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='WW')
plt.hist(njets_mumuzz, bins=11, range=[-0.5, 10.5], histtype='step', stacked=True, fill=False, density=True, label='ZZ')
plt.legend()
plt.xlabel("Number of Jets")
plt.ylabel("Fraction of Events")
plt.show()