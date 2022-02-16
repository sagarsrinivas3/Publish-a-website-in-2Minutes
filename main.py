from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
  return "welcome to HOME PAGE"

app.run(host="0.0.0.0")