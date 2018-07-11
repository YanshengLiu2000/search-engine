from bs4 import BeautifulSoup
import os


def scrape(path):
    destination_directory = os.path.join(os.getcwd(), "folder name here")

    try:
        with open(path, 'r') as file:
            data = file.read()

        soup = BeautifulSoup(data, 'html.parser')

        for small in soup("small"):
            soup.small.extract()

        return(soup.text)
        #with open(os.path.join(destination_directory, files.split('.')[0] + ".txt"), 'w', encoding='utf-8') as w:
        #    w.write(soup.text)
    except UnicodeEncodeError:
        print("Error Unicode encode error!")
        #w.close()
        #os.remove(os.path.join(destination_directory, files.split('.')[0], ".txt"))
    except UnicodeDecodeError:
        print("Error in unicode")
        #file.close()
