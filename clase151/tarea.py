import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


turismo = pd.read_csv('turismo.csv')

turismo.plot(y='Ingreso_Turistas', x='class')
plt.savefig("plot.png")

turismo.plot.bar(y=['Interes','Publicidad'], x='Ingreso_Turistas', subplots=True)
plt.savefig("bar.png")



libro = pd.read_csv("Libro1.csv", index_col = 0)
libro2 = pd.read_csv("Libro2.csv", index_col = 0)

libro.plot.pie(subplots=True)
plt.savefig("pie1.png")
libro2.plot.pie(subplots=True)
plt.savefig("pie2.png")


plt.show()

