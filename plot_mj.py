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

mj1_mumutc = df_mumutc['mj1'].to_numpy()
mj1_mumubb = df_mumubb['mj1'].to_numpy()
mj1_mumucc = df_mumucc['mj1'].to_numpy()
mj1_mumuqq = df_mumuqq['mj1'].to_numpy()
mj1_mumutt = df_mumutt['mj1'].to_numpy()
mj1_mumuwjj = df_mumuwjj['mj1'].to_numpy()
mj1_mumuww = df_mumuww['mj1'].to_numpy()
mj1_mumuzz = df_mumuzz['mj1'].to_numpy()

mj2_mumutc = df_mumutc['mj2'].to_numpy()
mj2_mumubb = df_mumubb['mj2'].to_numpy()
mj2_mumucc = df_mumucc['mj2'].to_numpy()
mj2_mumuqq = df_mumuqq['mj2'].to_numpy()
mj2_mumutt = df_mumutt['mj2'].to_numpy()
mj2_mumuwjj = df_mumuwjj['mj2'].to_numpy()
mj2_mumuww = df_mumuww['mj2'].to_numpy()
mj2_mumuzz = df_mumuzz['mj2'].to_numpy()

fig, axs = plt.subplots(1, 2, figsize=(10,5))
axs[0].hist(mj1_mumutc, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='tc')
axs[0].hist(mj1_mumubb, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='bb')
axs[0].hist(mj1_mumucc, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='cc')
axs[0].hist(mj1_mumuqq, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='qq')
axs[0].hist(mj1_mumutt, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='tt')
axs[0].hist(mj1_mumuwjj, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='Wjj')
axs[0].hist(mj1_mumuww, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='ww')
axs[0].hist(mj1_mumuzz, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='zz')

axs[1].hist(mj2_mumutc, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='tc')
axs[1].hist(mj2_mumubb, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='bb')
axs[1].hist(mj2_mumucc, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='cc')
axs[1].hist(mj2_mumuqq, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='qq')
axs[1].hist(mj2_mumutt, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='tt')
axs[1].hist(mj2_mumuwjj, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='wjj')
axs[1].hist(mj2_mumuww, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='ww')
axs[1].hist(mj2_mumuzz, bins=30, range=[0.0, 300.0], histtype='step', stacked=True, fill=False, density=True, label='zz')

axs[0].legend()
axs[0].set_xlabel("M(HJ) [GeV]")
axs[0].set_ylabel("Fraction of Events")

axs[1].legend()
axs[1].set_xlabel("M(LJ) [GeV]")
axs[1].set_ylabel("Fraction of Events")

plt.show()