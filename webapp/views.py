from flask import render_template, request
import os
from werkzeug.utils import secure_filename
from time import time

from webapp import search_function
from webapp import config
from webapp import load_models
from webapp import app


"""
This is script used to receive the information from users and transfer necessary information to doc2vec part and
fast query part.
After our system gets the results, this script will transfer the script to html and give it back to users. 

"""
ROOT_DIR = config.ROOT_DIR  # root directory of the project
UPLOAD_FOLDER = config.UPLOAD_FOLDER_DIR  # upload directory of the project. use to save the upload txt/html files
ALLOWED_EXTENSIONS = {'txt', 'html'}  # set allowed files here
model = load_models.model  # be used in search_function.py
dataset = load_models.dataset  # be used in search_function.py
print("This is the views.py.")


def allowed_file(filename):
    """this function can check if the upload file is txt or html"""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    """This function catch the users first request and give users welcome page of our website."""
    return render_template("welcome.html")


@app.route('/results', methods=['GET', 'POST'])
@app.route('/article_details/results', methods=['GET', 'POST'])
def results():
    """
    This function catch the search request and target sentences from website.
    Then, it will pass the target sentences to search_function and start record the searching time.
    After search_function give it back the results, it will give user the search result and search time.
    """
    target = request.form.get('target', '')  # get the search sentences
    if not target:
        return render_template("results.html", search_error=1,
                               search_target=target)  # if there is no input string, return error message
    start_time = time()  # record searching time
    search_words = search_function.get_results(target, model, dataset)  # get the search result
    end_time = time()
    return render_template("results.html", search_results=search_words, search_target=target,
                           search_time=str(round(end_time - start_time, 3)))  # return search results


@app.route('/article_details', methods=['GET', 'POST'])
def article_details():
    """
    After user want to check the details of an article and click the link, it will give the article details to user.
    """
    file_name = request.args.get("file_name", "")  # get the file name
    file_dir = 'models/NSWSC/' + file_name  # get the file directory.
    return render_template("article_details.html", file_name=file_dir)  # return the article details to user


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    """
    This function is used to handle upload behaviour.
    After user uploads a file, this function will check if the file is txt or html.
    If the file format is allowed. The function will read the whole file and pass the string to search_function.py.
    After search_function.py give results back to this function, it will give the results to user.
    """
    if request.method == 'POST':
        try:
            file = request.files['file']  # try to catch the upload file
        except:
            return render_template("results.html", search_error=2,
                                   search_target="")  # if user upload nothing, return error message to user.
        filename = secure_filename(file.filename)  # in case bad guys use special file names to destroy our website.
        if file and allowed_file(file.filename):  # check if the file is allowed
            start_time = time()  # record search time
            file.save(os.path.join(UPLOAD_FOLDER, filename))  # save file to upload folder
            target_file = os.path.join(UPLOAD_FOLDER, file.filename)
            combined_string = ""
            with open(target_file, 'r') as f:  # read file and pass the string to search function
                lines = f.readlines()
                for line in lines:
                    combined_string += line
            search_words = search_function.get_results(combined_string, model,
                                                       dataset)  # give target string to search_function
            end_time = time()#use to calcullate the search time
            return render_template("results.html", search_results=search_words, search_target=target_file,
                                   search_time=str(round(end_time - start_time, 3)))  # return results to user.

    return render_template("upload.html")
