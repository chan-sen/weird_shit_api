import flask
from flask import request, jsonify
import requests
from bs4 import BeautifulSoup
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    # Homepage request & parsing for random image
    request = requests.get("http://www.weirdshityoucanbuy.com")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    homepage_items = soup.find_all("td", {"class": "wsite-multicol-col"})
    random_item = homepage_items[randint(0, 80)]

    # access content inside of the tag (this ex. for <a href='link'>)     <---
    link = random_item.a['href']
    link = "http://www.weirdshityoucanbuy.com" + link

    # Request page for item found
    request = requests.get(link)
    soup = BeautifulSoup(request.content, "html.parser")

    # Find heading
    heading = soup.find("h1").contents[0]
    print(heading)

    # Find image
    img = soup.find("img", {"alt": heading})
    if img:
        img = "http://www.weirdshityoucanbuy.com" + img['src']
        print(img)

    # Find description
    description = soup.find("div", {"class": "paragraph"}).text
    print(description)

    # Find price
    price = soup.find_all("font")[2].text
    print(price)

    something_weird = {
        'heading': heading,
        'description': description,
        'img_url': img,
        'price': price
    }

    return jsonify(something_weird)


app.run()
