from flask import Flask, Response, request, jsonify
from requests import get, post

from masks.masks import TextMasker
from masks.seekers import SSNSeeker, NameSeeker

app = Flask(__name__)
METHODS = ["POST"]

END_POINT_URL = 'https://postman-echo.com/post'


@app.route('/', methods=METHODS)
def proxy():
    resp = post(f'{END_POINT_URL}', request.data).json()
    text_masker = TextMasker([SSNSeeker(), NameSeeker()])
    resp['data'] = text_masker.mask(resp['data'])
    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)
