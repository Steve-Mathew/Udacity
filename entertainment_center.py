#Udacity
#Nanodegree Program: Introduction to Programming
#Stage: 3
#Project: Movie Website
#Filename: entertainment_center.py
#Due Date: Monday, August 24, 2015
#Student/Author: Steve Mathew
#
#Procedure for Writing this Program:
#
#Create a file (media.py) that contains a class and method.
#That file will assist in the running of this program (entertainment_center.py).
#This file (entertainment_center.py) will then contain consist of "instances" of the class that was created in media.py.  Each of these instances are referred to as "objects".
#These objects will then be listed in a one-dimensional array.
#This array will then be loaded into another program (fresh_tomatoes.py), which will take this list, and load each corresponding object on this list, and display it in a mock website.

import fresh_tomatoes
#This file converts the objects shown below into content for the mock website "Fresh Tomatoes".

import media
#This is the file that contains the class and method required for this program to run.

#Below are the "objects": movie titles and other associated pieces of information.

Ex_Machina = media.Movie("Ex Machina", "A young programmer is selected to participate in a ground-breaking experiment in artificial intelligence by evaluating the human qualities of a breath-taking female A.I.", "Alex Garland", "http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1__SX640_SY720_.jpg", "$15,000.000 (estimated)", "April 24, 2015", "https://www.youtube.com/watch?v=EoQuVnKhxaM")

It_Follows = media.Movie("It Follows", "A young woman is followed by an unknown supernatural force after getting involved in a sexual encounter.", "David Robert Mitchell", "http://ia.media-imdb.com/images/M/MV5BMzU3OTI3NTU4MF5BMl5BanBnXkFtZTgwMzk5MzY3MzE@._V1__SX640_SY720_.jpg", "$2,000,000 (estimated)", "March 13, 2015 (limited release)", "https://www.youtube.com/watch?v=OaRx7iR9kXg")

The_King_of_Kong = media.Movie("The King of Kong: A Fistful of Quarters", "Die-hard gamers compete to break world records on classic arcade games.", "Seth Gordon", "http://ia.media-imdb.com/images/M/MV5BMTc5MzU3NTkzMl5BMl5BanBnXkFtZTcwMDQwNzE1MQ@@._V1__SX1293_SY625_.jpg", "Unknown", "August 17, 2007", "https://www.youtube.com/watch?v=xMJZ-_bJKdI")

Koyaanisqatsi = media.Movie("Koyaanisqatsi", "A collection of expertly photographed phenomena with no conventional plot. The footage focuses on nature, humanity and the relationship between them.", "Godfrey Reggio", "http://ia.media-imdb.com/images/M/MV5BMjE2NzY1MDg3NV5BMl5BanBnXkFtZTcwNzk4ODg0NA@@._V1_SX640_SY720_.jpg", "Unknown", "September 14, 1983", "https://www.youtube.com/watch?v=tDW-1JIa2gI")

Powaqqatsi = media.Movie("Powaqqaatsi", "An exploration of technologically developing nations and the effect the transition to Western-style modernization has had on them.", "Godfrey Reggio", "http://ia.media-imdb.com/images/M/MV5BMTkyMDI5Mzk5NV5BMl5BanBnXkFtZTcwMzkwOTc2NA@@._V1_SX640_SY720_.jpg", "$2,500,000 (estimated)", "April 29, 1988", "https://www.youtube.com/watch?v=sNVTmWRcUbY")

Naqoyqatsi = media.Movie("Naqoyqatsi", "A visual montage portrait of our contemporary world dominated by globalized technology and violence.", "Godfrey Reggio", "http://ia.media-imdb.com/images/M/MV5BMTg2MTAyNjMyNl5BMl5BanBnXkFtZTcwMzMzNjkyMQ@@._V1__SX640_SY720_.jpg", "$3,000,000", "October 18, 2002", "https://www.youtube.com/watch?v=jl1RcfvEsiA")

movies = [Ex_Machina, It_Follows, The_King_of_Kong, Koyaanisqatsi, Powaqqatsi, Naqoyqatsi]
fresh_tomatoes.open_movies_page(movies)
