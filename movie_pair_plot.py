import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_file_link import movie_path

df = pd.read_csv(movie_path)

#pair plot on the basis of diffrent genre movies
sns.pairplot(df.drop(['rating'],axis=1),hue="genre")
plt.show()