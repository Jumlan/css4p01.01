# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:02:30 2024

@author: LANRE
"""

# Answers to Question 1
import pandas as pd
df = pd.read_csv("C:/Users/LANRE/Downloads/CSS2024_Day06/movie_dataset.csv")
print(df)
print(df.info())
df.dropna(inplace = True)
df = df.reset_index(drop=True)
print (df)
print (df.info())
#filtering data for 'rated column'
import pandas as pd

#Henceforth dataframe refeered as 'movie_data' 
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]
print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

#Answer to Question 2
# Calculate the average revenue of movies
average_revenue = df['revenue (Millions)'].mean()
print("average revenue of all Movies: ${:,.2f}".format(average_revenue))
print(f"The average revenue of all movies in the dataset is {average_revenue:.2f} million dollars.")

#Question 3
#Change the 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
#dataframe filtered to indicate 2015 to 2017 movies
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]
#average revenue of 2015 to 2017 movies
average_revenue_2015_to_2017 = filtered_df['revenue(Millions)'].mean()
print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_to_2017:.2f} million dollars.")

#Question 4
import pandas as pd
df = pd.read_csv("C:/Users/LANRE/css2024_day02/movie_dataset.csv")
print(df)
print(df.info())
movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print(f"The number of movies released in the year 2016 is: {num_movies_2016}")

#Question 5
import pandas as pd
#filter dataframe for  christopher nolan movie directed
nolan_movies = df[df['Director'] == 'Christopher Nolan']
#Get the number of movies by christopher Nolan
num_nolan_movies = len(nolan_movies)
print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")
 #Question 6
import pandas as pd
high_rated_movies= df[df['Rating'] >= 8.0]
#no of highrated movies
number_of_high_rated_movies = len(high_rated_movies)
print(f"The number of movies in the dataset with a rating of at least 8.0 is {number_of_high_rated_movies}.")
# Question 7
import pandas as pd
nolan_movies = df[df['Director'] == 'Christopher Nolan'] 
#calculate the median of christopher Nolan directed movies
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")
#Question 8
import pandas as pd
# Each year's average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
#Year with highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")
#Question 9
import pandas as pd
count_2006 = df[df['Year'] == 2006]
count_2016 = df[df['Year'] == 2016]
#deriving the percentage increase
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is {percentage_increase:.2f}%.")
#Question 10
import pandas as pd
actors_df = df['Actors'].str.split(', ', expand=True)
actors_list = actors_df.values.flatten()
actors_count = pd.Series(actors_list).value_counts()
#most common actor is:
most_common_actor = actors_count.idxmax()
print(f"The most common actor in all the movies is: {most_common_actor}")

import pandas as pd

#Filtering columns with numerical features
numerical_df = df.select_dtypes(include=['number'])
df1=numerical_df
print(df1)

#Correlating matrix printing
correlation_matrix = df1.corr()
print(correlation_matrix)

#Printing insights

#Plotting the correlation Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

