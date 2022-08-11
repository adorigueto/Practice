import pandas as pd
import numpy as np

file = pd.read_csv('electionpoll.csv')
file.sum(axis=0)
file.mean().round(1)
file.median().round(1)
file.std().round(1)

file[59:90].max()["Workers' Party"] - file[59:90].min()["Workers' Party"]

file.max()
file.min()

a = file["Civic Party"] == 37
file["Date \ Party"][a]

