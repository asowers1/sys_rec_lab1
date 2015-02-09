__author__ = 'andrew'
import Spider


#s = Spider.Spider()

#s.fetch("http://www.amazon.com/The-Mountain-Three-Short-Sleeve/dp/B002HJ377A")

# Get the first 20 hits for "Mariposa botnet" in Google Spain

books = open("data/item/book.txt", "r")
bookList = []
for book in books:
    bookList.append(book.rstrip())
print(bookList)

movies = open("data/item/movie.txt", "r")
movieList = []
for movie in movies:
    movieList.append(movie.rstrip())
print(movieList)

songs = open("data/item/music.txt", "r")
songList = []
for song in songs:
    songList.append(song.rstrip())
print(songList)

from google import search
for url in search('apple', tld='es', lang='es', stop=20):
    print(url)