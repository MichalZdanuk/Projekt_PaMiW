import time
import re
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("forms.html")

@app.route('/with-get', methods=["GET"])
def with_get():
    username = request.args.get("username", "nothing")
    password = request.args.get("password", "nothing")

    return "Got [" + username + "] and [" + password + "]", 200

@app.route('/products', methods=["GET"])
def find_product():
    product = request.args.get("search_product", "nothing")
    return render_template("products.html",data=[find(product)])
    #return "Got [" + str(find(product)) + "]", 200

def read_words_from_file(file_path):
    word_file = file_path
    words = open(word_file).read().splitlines()
    return words

tab = read_words_from_file("words")
def find(prod_name):
    tab_found = []
    prod_name = '^' + prod_name
    for i in tab:
        x = re.search(prod_name,i)
        if(x!=None):
            tab_found.append(i)
    return tab_found


# @app.route('/with-post', methods=["POST"])
# def with_post():
#     username = request.form.get("username", "nothing")
#     password = request.form.get("password", "nothing")

#     return "Got [" + username + "] and [" + password + "]", 200

# @app.route('/with-file', methods=["POST"])
# def with_file():
#     username = request.form.get("username", "nothing")
#     password = request.form.get("password", "nothing")
#     license  = request.files.get("license")

#     if license:
#         return "Got [" + username + "] and [" + password + "] and [" + license.filename + "]", 200
#     else:
#         return "Got [" + username + "] and [" + password + "] and no file", 200
    
# @app.route('/with-json', methods=["POST"])
# def with_json():
#     data = request.get_json(silent=True)
#     if data:
#         username = data.get("username", "nothing")
#         password = data.get("password", "nothing")
#         return "Got JSON [" + username + "] and [" + password + "]", 200
#     else:
#         username = request.form.get("username", "nothing")
#         password = request.form.get("password", "nothing")
#         return "Got form [" + username + "] and [" + password + "]", 200

# @app.route('/with-url/<argument>', methods=["GET"])
# def with_url(argument):
#     return "Got argument [" + argument + "]", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
