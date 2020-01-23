from selenium import webdriver #pip3 install selenium
from time import sleep
from bs4 import BeautifulSoup #pip3 install beautifulsoup4
import urllib.request
import os
print("Example link: https://mangadex.org/chapter/775896/1")
link = input("Link of the manga's first page: ")
path = "C:\\chromedriver.exe" #IMPORTANT change the path with yours! Download: https://chromedriver.storage.googleapis.com/index.html?path=2.35/
browser = webdriver.Chrome(executable_path=path)
browser.get(link)
sleep(5) #IMPORTANT wait for load adjust for your load times
soup = BeautifulSoup(browser.page_source, "html.parser")
imgLink = soup.find_all("img", class_="noselect nodrag cursor-pointer")[0].get("src")
imageFormat = imgLink.split("/")[-1].split(".")[1] #gets the image format
charsToDelete = len(imgLink.split("/")[-1])
rawDownloadLink = imgLink[:-charsToDelete]
mode = imgLink.split("/")[-1].split(".")[0][:-1] #gets the character before number
pageCounter = 1
print("Example path: C:\\Users\\Sibyl\\Desktop\\Tensei Manga")
downloadPath = input("Provide a path for downloading images: ")
os.chdir(downloadPath)
while True:
    downloadUrlString = "{}{}{}.{}".format(rawDownloadLink, mode, pageCounter, imageFormat)
    try:
        urllib.request.urlretrieve(downloadUrlString, "{}.{}".format(pageCounter, imageFormat))
        pageCounter = pageCounter + 1
    except:
        break
