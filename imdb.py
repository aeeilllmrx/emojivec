# code to find imdb stuff
# cmd: scrapy crawl imdb -o movies.json (or .csv)

import scrapy
from bs4 import BeautifulSoup
import re


class Movie(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    director = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()

class IMDB(scrapy.Spider):
    name = 'imdb'

    # note: there are currently 2404811 entries
    start_urls = []
    for i in xrange(2788705,2788715):
        start_urls.append("http://www.imdb.com/title/tt" + str(i) + '/')

    # could loop through and concatenate to create urls

    def parse(self, response):          
            
        movie = Movie()
        # first turn html page into soup
        soup = BeautifulSoup(response.body)
        soup.prettify()
     
        # title
        title = soup.title.get_text()
        movie['title'] = title

        # description
        desc = soup.find_all("p", attrs = {"itemprop": "description"})
        souped = BeautifulSoup(str(desc))
        movie['description'] = souped.get_text()
        
        # director
        director = soup.find_all("div", attrs = \
                             {"class" : "txt-block", "itemprop": "director"})
        souped = BeautifulSoup(str(director))
        movie['director'] = souped.get_text()

        # date
        for line in soup.find_all("div", attrs = {"class" : "txt-block"}):
            if re.search("Release Date",str(line)):
		date = line.get_text(strip=True)
	movie['date'] = date

        # rating
        rating = soup.find_all("div", attrs = {"class" : "star-box giga-star", \
                                            "class" : "titlePageSprite star-box-giga-star"})
        movie['rating'] = BeautifulSoup(str(rating)).get_text()

        yield movie
