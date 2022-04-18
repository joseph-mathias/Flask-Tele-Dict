from distutils.log import error
import os
from urllib import response
import requests
from flask import Flask


app = Flask(__name__)


@app.route('/')
def get_info(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = response.get(url)
    if response.status_code == 404:
        error_response = 'We are not able to provide any information about your word. Please confirm that the word is ' \
                         'spelled correctly or try the search again at a later time.'
        return error_response

    data = response.json()[0]

    print(data)
    return data


get_info("food")


if __name__ == "__main__":
    app.run(debug=True)
