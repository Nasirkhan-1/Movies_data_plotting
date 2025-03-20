import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot
from movie_file_link import movie_path

# load the dataset
df = pd.read_csv(movie_path)


#count occurance of each country upto 1000 values
genre_counts = df[:1000]['country'].value_counts()
print("genre count :",genre_counts)

# define the custom color for each bar
color = sns.color_palette("hsv" , len(genre_counts))

# plot the Bar graph with diffrent color
plt.figure(figsize=(10,7))
sns.barplot(x=genre_counts.index , y=genre_counts.values , palette=color)
plt.xlabel("country")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by country of origin")
plt.xticks(rotation=90)

# Adding value annotations on top of each bar
for index, value in enumerate(genre_counts.values):
    plt.text(index, value + 0.5, str(value), ha='center', color='black')

plt.show()