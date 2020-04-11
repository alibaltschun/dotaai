from flask import Flask
app = Flask(__name__)

import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

file_html_update = BASE + "/../temp/html_update.txt"

@app.route('/html_update')
def hello():
    with open(file_html_update, "r")  as file:
        result=file.read()
    if result == "1":
        with open(file_html_update, "w")  as file:
            file.write("0")
    return(result)

if __name__ == '__main__':
    app.run()