import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
excel_file = 'covid.xlsx'
movies = pd.read_excel(excel_file, index_col=0)
movies.head()
plt.figure(figsize=(15,6)) 
for i,j in movies.iteritems(): 
        plt.clf()
        movies[i].plot(kind='bar', width = 0.8) 
        plt.xlabel("Date")
        plt.ylabel("cCFR")
        plt.yticks(np.arange(0, 100, 5))
        plt.title(i)
        plt.savefig(i)


