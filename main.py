# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
import os

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index_page():
    return render_template('index.html')

@app.route('/test')
def test_page():
    return render_template('test.html')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        image = request.form.get('image')
        description = request.form['description']

        #option to process data here

        return render_template('result.html', name=name, date=date, image=image, description=description)

    return render_template('uploadform.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        return "upload logic here"


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()