# xkcd_downloader.py
# automated download of xkcd comics from web

import os
import requests
import bs4

# Set up the url for xkcd
url = "https://xkcd.com"
# Create a folder to store the comics
os.makedirs("xkcd_pictures", exist_ok=True)
# Loop to download all the comics
while not url.endswith("#"):
    # TODO: download the page(html)
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html")
    # TODO: find the URL using bs4
    # TODO: download the image
    # TODO: save the image
    # TODO: get the previous button url
    prev_link = soup.select('a[rel="prev"]')[0] #find text in []
    url = "https://xkcd.com" + prev_link.get("href")


print("Done")