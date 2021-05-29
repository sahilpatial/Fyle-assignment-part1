from sqlalchemy import create_engine
import pandas as pd

alchemy = 'postgresql+psycopg2://sahil:2001@localhost/bank'
engine = create_engine(alchemy)

df = pd.read_csv('https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv')

df.to_sql('branches',engine, if_exists="replace", index= False, chunksize= 10000, method="multi")