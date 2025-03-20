
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from movie_file_link import movie_path

#Load the data

df = pd.read_csv(movie_path)


#Average Rating on the Basis of Genre
sns.lineplot(x='genre', y='score',data=df)
plt.show()
