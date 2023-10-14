import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from loguru import logger


df1 = pd.read_excel("2021.xlsx")
df2 = pd.read_excel("2022.xlsx")
df3 = pd.read_excel("2023.xlsx")

df = pd.concat([df1, df2, df3])

dates = df["date"]
df[df["visiters"] == 'close'] = 0
visiters = df["visiters"]

logger.debug(visiters)
logger.debug(dates)

plt.plot(visiters)
plt.show()