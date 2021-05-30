from sqlalchemy import create_engine
import pandas as pd

alchemy = 'postgres://lptzfenupmbzuj:33302222e95e7355014d650f5a4e264a4c2431fe668d7a33842539a4f081f209@ec2-35-174-35-242.compute-1.amazonaws.com:5432/dcvic7e9ur27ku'
engine = create_engine(alchemy)

df = pd.read_csv('https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv')

df.to_sql('branches',engine, if_exists="replace", index= False, chunksize= 10000, method="multi")