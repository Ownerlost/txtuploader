from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Զเधे Զเधे'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Explicitly set port 8080
