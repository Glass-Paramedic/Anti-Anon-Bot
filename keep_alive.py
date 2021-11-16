from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Flask app is running. Make sure to ping your repl url with uptimerobot to keep it online 24/7"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
