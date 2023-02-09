from flask import Flask, render_template

app = Flask(__name__,
    static_url_path='',
    static_folder='pythonhello/static',
    template_folder='pythonhello/templates')

import os

@app.route('/')
def homepage():

    title = "Hello :)"
    paragraph = ["placeholder"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except (Exception):
        pass

if __name__ == '__main__':
    ##myport = int(os.environ.get("PORT"))
    app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)