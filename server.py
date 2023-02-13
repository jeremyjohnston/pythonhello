from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates')

import os

@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

@app.route('/')
@app.route('/index')
@app.route('/home')
def homepage():

    mytitle = "Hello :)"
    myparagraph = ["placeholder"]

    try:
        return render_template("index.html")
    except Exception as e:
        print(e)
        return 'oops'

if __name__ == '__main__':
    ##myport = int(os.environ.get("PORT"))
    app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)