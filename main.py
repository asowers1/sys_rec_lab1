__author__ = 'andrew'
import Spider
from google import search
import time, random


#

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
bookSpider = Spider.Spider()
for item in bookList:
    for url in search(item + " book", tld='es', lang='es', stop=10):
        time.sleep(random.uniform(.3, 3))
        if(type(url) is str):
            bookSpider.fetch(url, "book")

#for item in movieList:
#    for url in search(item + " movie", tld='es', lang='es', stop=10):
#        print(url)
#
#for item in songList:
#    for url in search(item + " song", tld='es', lang='es', stop=10):
#        print(url)

books.close()
movies.close()
songs.close()