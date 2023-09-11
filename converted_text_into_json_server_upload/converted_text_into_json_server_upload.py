#!/usr/bin/env python3
import os
import requests

# set source dir for feedback file:
src_dir = "feedback/"

# capture a list of files:
files = os.listdir(src_dir)


# function to read file lines into a list:
def read_lines(path):
    with open(src_dir + path) as f:
        text = f.read().splitlines()
    return text


# load feedback entries into dictionary:
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = read_lines(file)
    feedback.append(dict(zip(keys, lines)))

# set host url:
url = "http://localhost/feedback/"

# post-feedback entries:
for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")
