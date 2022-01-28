import pandas as pd
import matplotlib.pyplot as plt
link='https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018?select=meal_info.csv'
data=pd.read_csv(link, sep='\t')


plt.hist(data.category)

