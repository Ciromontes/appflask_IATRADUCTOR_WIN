from distutils.debug import DEBUG
from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')#return "Los llamo amigos,"
if __name__ == '__main__':
    app.run(DEBUG=True, PORT=5001)


# app = Flask(__name__)
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)