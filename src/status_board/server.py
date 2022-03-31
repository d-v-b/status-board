import json
from flask import Flask, Response, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/status-data')
def status_board():
    from generate_test_board import board
    response = Response(f'data:{board.json()}\n\n')
    return response


if __name__ == '__main__':
    application.run(debug=True, threaded=True)