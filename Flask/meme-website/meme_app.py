#!/bin/python3

from flask import Flask, render_template  # render_templates allows reference of external html
import requests  # handles API calls
import json # notation format

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit) # take pic and subreddit and pass to html index page

app.run(host="0.0.0.0", port=5000, debug=True)
