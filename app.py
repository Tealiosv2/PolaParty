# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, redirect, url_for
import os
from backend import database_operations
from PIL import Image

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

# routes to index
@app.route('/')
def index_page():
    delete_uploads()
    return render_template('index.html')


@app.route('/display')
def display():
    records = database_operations.db_read()
    return render_template('display.html', records=records)

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        date = request.form['date']
        description = request.form['description']


        # Handle uploaded image
        if 'image' in request.files:
            image = request.files['image']
            if image.filename:
                image_path = 'static/uploads/' + image.filename

                image.save(image_path)

                img = Image.open(image_path)
                average_color = img.convert('RGB').resize((1, 1)).getpixel((0, 0))
                average_r, average_g, average_b = average_color

                # need to change 1 to user id
                database_operations.db_write(1, name, description, date, image_path, average_r, average_g, average_b)


        # Do something with the form data, e.g., store it in a database

        return redirect(url_for('index_page'))


#clears uploads dir
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
