"""
This file acts as the backend server for the web application.
Accesses the subjects to display the textbooks.

Created By Joseph Menezes
"""
import json

from flask import Flask, render_template

app = Flask(__name__, template_folder="static/templates")

print("Running!")


@app.route("/")
def openHome():
    return render_template("index.html")


@app.route("/about")
def openAbout():
    return render_template("about.html")


@app.route("/contact")
def openContact():
    return render_template("contact.html")


@app.route("/subject/<file>")
def openTextBook(file):
    jsonFile = open("textbooks.json")
    txtBooks = json.load(jsonFile)
    jsonFile.close()
    if 'bio' in file:
        information = txtBooks['Biology']
        files = [books['file'] for books in information]
        return render_template("subject.html", files=files, subject="Biology", information=information, shortcut='bio')
    elif 'chem' in file:
        information = txtBooks['Chemistry']
        files = [books['file'] for books in information]
        return render_template("subject.html", files=files, subject="Chemistry", information=information,
                               shortcut='chem')


@app.route("/health")
def health():
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
