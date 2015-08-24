#Udacity
#Nanodegree Program: Introduction to Programming
#Stage: 3
#Project: Movie Website
#Filename: media.py
#Due Date: Monday, August 24, 2015
#Student/Author: Steve Mathew
#
#Below is a template of the pieces of information needed for each movie listed in the entertainment_center.py program.

import webbrowser
#This is required to run a program that imports this file in a web browser.

class Movie ():
	def __init__(self, movie_title, movie_storyline, movie_director, movie_poster, movie_budget, movie_release_date, movie_trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.director = movie_director
		self.poster_image_url = movie_poster
		self.budget = movie_budget
		self.release_date = movie_release_date
		self.trailer_youtube_url = movie_trailer
	
	def play_trailer(self):
		#This is method that is used to play a movie trailer using the hyperlink shown in each movie object.
		webbrowser.open(self.trailer)
