from bs4 import BeautifulSoup
import os
from os import listdir
import pickle




def scrape():
    filename_to_case_name = dict()
    scraped_directory = os.path.join(os.getcwd(),"scraped_data")
    if not os.path.exists(scraped_directory):
        os.makedirs(scraped_directory)

    path = input("Please enter the full path to your HTML files.")
    for files in listdir(path):
        try:
            with open(os.path.join(path,files), 'r') as file:
                data = file.read()

            soup = BeautifulSoup(data, 'html.parser')
            try:
                case_name = soup.find('title').text
            except AttributeError:
                case_name = 'NA'
            filename_to_case_name[files] = case_name

            for small in soup("small"):
                soup.small.extract()

            #with open(scraped_directory + "\\" + files.split('.')[0] + "README", 'w', encoding='utf-8') as w:
            with open(os.path.join(scraped_directory, files.split('.')[0] + "README"), 'w', encoding='utf-8') as w:
                w.write(soup.text)
        except UnicodeEncodeError:
                w.close()
                os.remove(os.path.join(scraped_directory,files.split('.')[0], "README"))
        except UnicodeDecodeError:
            file.close()

    file = open('filename_to_casename.pkl','wb')
    pickle._dump(filename_to_case_name,file)
    file.close()

