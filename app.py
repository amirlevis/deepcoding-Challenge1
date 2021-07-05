from flask import Flask, Response, request, jsonify
from requests import get, post

app = Flask(__name__)
METHODS = ["POST"]

END_POINT_URL = 'https://postman-echo.com/post'


@app.route('/', methods=METHODS)
def proxy():

    print(request.data)
    resp = post(f'{END_POINT_URL}', request.data).json()
    print(resp)

    def encrypt_response():
        pass


    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)
