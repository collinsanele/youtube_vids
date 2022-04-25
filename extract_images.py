#A simple python script to download all images from a site

#pip install requests bs4 tqdm

import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def download_image(img_url, filename, dist_path):
    #create destination folder for the images if it does not exist
    if not os.path.exists(dist_path):
        os.mkdir(dist_path)
    r = requests.get(img_url)
    with open(f"{dist_path}/{filename}.png", "wb") as f:
        for chunk in r:
            f.write(chunk)

def main(site_url):
    r = requests.get(site_url)
    soup = BeautifulSoup(r.content, "html.parser")
    img_urls = [img.get("src") for img in soup.findAll("img")]
    for index, img_url in tqdm(enumerate(img_urls)):
        download_image(img_url=img_url, filename=str(index), dist_path="./images")


#please wait for few secs while i run 'python extract_images.py'
#in the terminal
#The link to the code would be in the description

if __name__ == "__main__":
    main(site_url="http://canews.herokuapp.com/aljazeera/")