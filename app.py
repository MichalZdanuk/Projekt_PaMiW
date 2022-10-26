from distutils.debug import DEBUG
from flask import Flask,request, render_template
import json

app = Flask(__name__)

def read_words_from_file(file_path):
    word_file = file_path
    words = open(word_file).read().splitlines()
    return words

tab = read_words_from_file("words")
# product_list = Product.objects.all()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search")
def search():
    text = request.args['searchText']
    result = [c for c in tab if str(text).lower() in c.lower()]
    return json.dumps({"results":result})

@app.route('/with-post', methods=["POST"])
def with_post():
    username = request.form.get("username", "nothing")
    password = request.form.get("password", "nothing")

    return "Got [" + username + "] and [" + password + "]", 200

if __name__ == "__main__":
    app.run(debug=True)
