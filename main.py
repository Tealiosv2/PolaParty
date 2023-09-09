# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from werkzeug.utils import secure_filename

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

dummy_database = []

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
    return render_template('uploadform.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    description = request.form['description']

    #empties uploads folder
    delete_uploads()

    # Handle image file upload
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename:
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join('static/uploads', image_filename)
            image_file.save(image_path)
        else:
            image_filename = None
    else:
        image_filename = None

    #save to database here
    hold_onto(name, image_filename, description)

    return redirect(url_for('display_entries'))

def hold_onto(name, image, description):
    dummy_database.append(name)
    dummy_database.append(image)
    dummy_database.append(description)


@app.route('/entires')
def display_entries():
    return render_template('result.html', entries=dummy_database)

def delete_uploads():
    try:
        for filename in os.listdir('static/uploads'):
            file_path = os.path.join('static/uploads', filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return "Uploads folder contents deleted successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()