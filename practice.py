from bs4 import BeautifulSoup
import lxml


with open('index.html', 'r') as file:
	body = file.read()

#import os
#path = os.getcwd()
#print(path)

#html = os.path.join(path, 'index.html')
#print(html)


soup = BeautifulSoup(body, 'lxml')
#print(soup)
#print('-----')
#print(soup.prettify())


# get the title
title = soup.title
#print(title)
#print(title.name)
#print(title.getText())


# get paragraph
paragraph = soup.p
#print(paragraph) 
#print(paragraph.name)
#print(paragraph.getText())



# get the first div
first_div = soup.find('div')
#print(first_div)
#print(first_div.getText())



# get all the divs
all_divs = soup.find_all('div')
#print(all_divs)
#for div in all_divs:
#	print('----')
#	print(div)


# get the first movie

#first_movie = soup.find('div', class_ = 'movie')
#print(first_movie)
#print(first_movie.getText())

first_movie = soup.select('.movie')[0]
#print(first_movie)
#print(first_movie.getText())


#get all movies
#all_movies = soup.find_all('div', class_='movie')
all_movies = soup.select('.movie')
#print(all_movies)


#for movie in all_movies:
#	print('----')
#	print(movie.getText())


# get all the links

links = soup.find_all('a')
#for link in links:
#	print(link)
#	print(link.getText())
#	print(link.get('href'))


#get element by id

movie_box = soup.select_one('#movie-box')
#print(movie_box)
#print(movie_box.getText())	


# parent / children

parent = movie_box.parent
#print(parent)
children = movie_box.children
#for child in children:
#	print(child)

movie = soup.find('div', class_='movie')
parent = movie.find_parent()
#print(parent)
parent = movie.find_parent('div')
#print(parent)


