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
        information = txtBooks['Biological Science']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="Biological Science", information=information, shortcut='bio')

    elif 'chem' in file:
        information = txtBooks['Chemistry']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="Chemistry", information=information, shortcut='chem')

    elif 'phy' in file:
        information = txtBooks['Physics']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="Physics", information=information, shortcut='phy')

    elif 'cs' in file:
        information = txtBooks['Computer Science']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="Computer Science", information=information, shortcut='cs')

    elif 'math' in file:
        information = txtBooks['Mathematics']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="Mathematics", information=information, shortcut='math')

    elif 'eeeng' in file:
        information = txtBooks['E&E Engineering']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="E&E Engineering", information=information, shortcut='eeeng')

    elif 'gesp' in file:
        information = txtBooks['GESP']
        files = [books['file'] for books in information]
        types = [books['type'] for books in information]
        return render_template("subject.html", files=files, types=types, subject="GESP", information=information, shortcut='gesp')

@app.route("/health")
def health():
    return ""

@app.route("/book/<name>", methods = ['POST', 'GET'])
def openBook(name):
    jsonFile = open("textbooks.json")
    txtBooks = json.load(jsonFile)
    jsonFile.close()

    if 'bio' in name:
        information = txtBooks['Biological Science']
        return render_template("book.html", information=information, shortcut='bio')

    elif 'chem' in name:
        information = txtBooks['Chemistry']
        return render_template("book.html", information=information, shortcut='chem')

    elif 'phy' in name:
        information = txtBooks['Physics']
        return render_template("book.html", information=information, shortcut='phy')

    elif 'cs' in name:
        information = txtBooks['Computer Science']
        return render_template("book.html", information=information, shortcut='cs')

    elif 'math' in name:
        information = txtBooks['Mathematics']
        return render_template("book.html", information=information, shortcut='math')

    elif 'eeeng' in name:
        information = txtBooks['E&E Engineering']
        return render_template("book.html", information=information, shortcut='eeeng')

    elif 'gesp' in name:
        information = txtBooks['GESP']
        return render_template("book.html", information=information, shortcut='gesp')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
