import preprocess
import scraper
import os
from os import listdir

scraper.scrape()

files = [ file for file in listdir(os.path.join(os.getcwd(),"scraped_data"))]

preprocess.preprocess(files,train=1)
