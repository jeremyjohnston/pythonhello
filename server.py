from flask import Flask, render_template

server = Flask(__name__)

import os

@app.route('/')
def homepage():

    title = "Hello :)"
    paragraph = ["placeholder"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    server.run(debug = True, host='0.0.0.0', port, passthrough_errors=True)