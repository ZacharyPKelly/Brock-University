"""
This file acts as the backend server for the web application.
Accesses the subjects to display the textbooks.

Created By Joseph Menezes
Modified by Zachary Kelly
"""
import json
from flask import Flask, render_template, request

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
        return render_template("1-biologicalScience.html", subject="Biological Science", information=information, len = len(information), shortcut='bio')

    elif 'chem' in file:
        information = txtBooks['Chemistry']
        return render_template("2-chemistry.html", subject="Chemistry", information=information, len = len(information), shortcut='chem')

    elif 'cs' in file:
        information = txtBooks['Computer Science']
        return render_template("3-computerScience.html", subject="Computer Science", information=information, len = len(information), shortcut='cs')
    
    elif 'math' in file:
        information = txtBooks['Mathematics']
        return render_template("4-mathematics.html", subject="Mathematics", information=information, len = len(information), shortcut='math')

    elif 'phy' in file:
        information = txtBooks['Physics']
        return render_template("5-physics.html", subject="Physics", information=information, len = len(information), shortcut='phy')

@app.route("/book/<subject>/<topic>/<int:book>")
def openBook(subject, topic, book):
    jsonFile = open("textbooks.json")
    txtBooks = json.load(jsonFile)
    jsonFile.close()

    if 'bio' in subject:

        if 'AUBIO-111' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 111']
            return render_template("book.html", information=information[book], subject="Biological Science", shortcut='bio')
        
        if 'AUBIO-112' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 112']
            return render_template("book.html", information=information[book], subject="Biological Science", shortcut='bio')
        
        if 'AUBIO-253' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 253']
            return render_template("book.html", information=information[book], subject="Biological Science", shortcut='bio')
        
        if 'AUBIO-260' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 260']
            return render_template("book.html", information=information[book], subject="Biological Science", shortcut='bio')

########################################################################################################################################

    elif 'chem' in subject:

        if 'AUCHE-111' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 111']
            return render_template("book.html", information=information[book], subject="AUCHE 111", shortcut='chem')
        
        if 'AUCHE-112' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 112']
            return render_template("book.html", information=information[book], subject="AUCHE 112", shortcut='chem')
        
        if 'AUCHE-213' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 213']
            return render_template("book.html", information=information[book], subject="AUCHE 213", shortcut='chem')
        
        if 'AUCHE-214' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 214']
            return render_template("book.html", information=information[book], subject="AUCHE 214", shortcut='chem')

########################################################################################################################################

    elif 'cs' in subject:

        if 'python' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Python']
            return render_template("book.html", information=information[book], subject="Python", shortcut='cs')
        
        elif 'java' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Java']
            return render_template("book.html", information=information[book], subject="Java", shortcut='cs')
        
        elif 'js' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Javascript']
            return render_template("book.html", information=information[book], subject="Javascript", shortcut='cs')
        
        elif 'c' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['C/C++/C#']
            return render_template("book.html", information=information[book], subject="C/C++/C#", shortcut='cs')

########################################################################################################################################

    elif 'math' in subject:

        if 'calculus' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Calculus']
            return render_template("book.html", information=information[book], subject="Calculus", shortcut='math')
        
        elif 'geometry' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Geometry']
            return render_template("book.html", information=information[book], subject="Geometry", shortcut='math')
        
        elif 'discrete' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Discrete Math']
            return render_template("book.html", information=information[book], subject="Discrete Math", shortcut='math')
        
        elif 'trigonometry' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Trigonometry']
            return render_template("book.html", information=information[book], subject="Trigonometry", shortcut='math')

########################################################################################################################################

    elif 'phy' in subject:

        if 'classical-mechanics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Classical Mechanics']
            return render_template("book.html", information=information[book], subject="Classical Mechanics", shortcut='phy')
        
        elif 'thermodynamics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Thermodynamics']
            return render_template("book.html", information=information[book], subject="Thermodynamics", shortcut='phy')
        
        elif 'electromagnetism' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Electromagnetism']
            return render_template("book.html", information=information[book], subject="Electromagnetism", shortcut='phy')
        
        elif 'quantum-mechanics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Quantum Mechanics']
            return render_template("book.html", information=information[book], subject="Quantum Mechanics", shortcut='phy')

@app.route("/book/<subject>/<topic>")
def openSubject(subject, topic):
    jsonFile = open("textbooks.json")
    txtBooks = json.load(jsonFile)
    jsonFile.close()

    if 'bio' in subject:

        if 'AUBIO-111' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 111']
            return render_template("subject.html", information=information, len = len(information), subject="AUBIO 111", shortcut='bio/AUBIO-111')
        
        if 'AUBIO-112' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 112']
            return render_template("subject.html", information=information, len = len(information), subject="AUBIO 112", shortcut='bio/AUBIO-112')
        
        if 'AUBIO-253' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 253']
            return render_template("subject.html", information=information, len = len(information), subject="AUBIO 253", shortcut='bio/AUBIO-253')
        
        if 'AUBIO-260' in topic:
            subjectInfo = txtBooks['Biological Science']
            information = subjectInfo['AUBIO 260']
            return render_template("subject.html", information=information, len = len(information), subject="AUBIO 260", shortcut='bio/AUBIO-260')
        
########################################################################################################################################

    if 'chem' in subject:

        if 'AUCHE-111' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 111']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 111", shortcut='chem/AUCHE-111')
        
        if 'AUCHE-112' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 112']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 112", shortcut='chem/AUCHE-112')
        
        if 'AUCHE-213' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 213']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 213", shortcut='chem/AUCHE-213')
        
        if 'AUCHE-214' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 214']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 214", shortcut='chem/AUCHE-214')
        
        if 'AUCHE-230' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 230']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 230", shortcut='chem/AUCHE-230')
        
        if 'AUCHE-250' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 250']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 250", shortcut='chem/AUCHE-250')
        
        if 'AUCHE-252' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 252']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 252", shortcut='chem/AUCHE-252')
        
        if 'AUCHE-279' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 279']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 279", shortcut='chem/AUCHE-279')
        
        if 'AUCHE-323' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 323']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 323", shortcut='chem/AUCHE-323')
        
        if 'AUCHE-324' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 324']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 324", shortcut='chem/AUCHE-324')
        
        if 'AUCHE-325' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 325']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 325", shortcut='chem/AUCHE-325')
        
        if 'AUCHE-341' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 341']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 341", shortcut='chem/AUCHE-341')
        
        if 'AUCHE-450' in topic:
            subjectInfo = txtBooks['Chemistry']
            information = subjectInfo['AUCHE 450']
            return render_template("subject.html", information=information, len = len(information), subject="AUCHE 450", shortcut='chem/AUCHE-450')
        
########################################################################################################################################

    if 'cs' in subject:

        if 'python' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Python']
            return render_template("subject.html", information=information, len = len(information), subject="Python", shortcut='cs/python')
        
        elif 'java' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Java']
            return render_template("subject.html", information=information, len = len(information), subject="Java", shortcut='cs/java')
        
        elif 'js' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['Javascript']
            return render_template("subject.html", information=information, len = len(information), subject="Javascript", shortcut='cs/js')
        
        elif 'c' in topic:
            subjectInfo = txtBooks['Computer Science']
            information = subjectInfo['C/C++/C#']
            return render_template("subject.html", information=information, len = len(information), subject="C/C++/C#", shortcut='cs/c')
        
########################################################################################################################################

    if 'math' in subject:

        if 'calculus' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Calculus']
            return render_template("subject.html", information=information, len = len(information), subject="Calculus", shortcut='math/calculus')
        
        elif 'geometry' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Geometry']
            return render_template("subject.html", information=information, len = len(information), subject="Geometry", shortcut='math/geometry')
        
        elif 'discrete' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Discrete Math']
            return render_template("subject.html", information=information, len = len(information), subject="Discrete Math", shortcut='math/discrete')
    
        elif 'trigonometry' in topic:
            subjectInfo = txtBooks['Mathematics']
            information = subjectInfo['Trigonometry']
            return render_template("subject.html", information=information, len = len(information), subject="Trigonometry", shortcut='math/trigonometry')
        
########################################################################################################################################

    if 'phy' in subject:
        
        if 'classical-mechanics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Classical Mechanics']
            return render_template("subject.html", information=information, len = len(information), subject="Classical Mechanics", shortcut='phy/classical-mechanics')
        
        if 'thermodynamics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Thermodynamics']
            return render_template("subject.html", information=information, len = len(information), subject="Thermodynamics", shortcut='phy/thermodynamics')
        
        if 'electromagnetism' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Electromagnetism']
            return render_template("subject.html", information=information, len = len(information), subject="Electromagnetism", shortcut='phy/electromagnetism')
        
        if 'quantum-mechanics' in topic:
            subjectInfo = txtBooks['Physics']
            information = subjectInfo['Quantum Mechanics']
            return render_template("subject.html", information=information, len = len(information), subject="Quantum Mechanics", shortcut='phy/quantum-mechanics')
        
@app.route("/health")
def health():
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)