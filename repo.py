from sqlalchemy import create_engine
import pandas as pd

alchemy = 'postgresql+psycopg2://fdcdeuozoifpje:ebfab39c4ee0381543e77981369698f533e2607d322ee495a04a5c62ebe6abc8@ec2-35-174-35-242.compute-1.amazonaws.com:5432/d1ruejc17i3vba'
engine = create_engine(alchemy)

df = pd.read_csv('https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv')

df.to_sql('branches',engine, if_exists="replace", index= False, chunksize= 10000, method="multi")
