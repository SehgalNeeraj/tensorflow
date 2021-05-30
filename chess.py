#!/usr/bin/env python3
import numpy as np
import matplotlib_terminal
import matplotlib.pyplot as plt
import pandas as pd

# set font and plot size to be larger
df_chess = pd.read_csv('./datasets/chess_data.csv')
df_chess['white_rating'].plot(kind='hist', title='White Rating')

plt.show('block')
plt.close()
