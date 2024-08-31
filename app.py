from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "This is simple hello from GCP GKE"


if __name__ == '__main__':
    app.run(debug=True)

