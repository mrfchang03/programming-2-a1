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
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Can't find the image...")
    else:
        if comic_elim[0].get("src").startswith("/2067/"):
            comic_url = "https://kxcd.com" + comic_elem[0].get("src")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
    # TODO: find the URL using bs4
    # TODO: download the image
    res = requests.get(comic_url)
    print(f"\tDownloading image at (comic_url)...")
    # TODO: save the image
    image_file = open(os.path.join("xkcd_pictures", os.path.basename(comic_url)), "wb")
    for chunk in res.iter_content(1000000):
        image_file.write(chunk)

    # TODO: get the previous button url
    prev_link = soup.select('a[rel="prev"]')[0] #find text in []
    url = "https://xkcd.com" + prev_link.get("href")


print("Done")