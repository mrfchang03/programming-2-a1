# requests_test.py
# read and get information from http

import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# raise an error if there is one
response.raise_for_status()

# create a variable to store the file
f = open("Rome_and_Juliet.txt", "wb")

# grab info from http and svae it in the variable
for chunk in response.iter.content(1000000):
    f.write(chunk)
# Write the file to disc
f.close()

                        