from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow, IMAGEPATH
from options import DEFAULTS

app = Flask(__name__)

LABEL_CLASS = 2 #1 for classic, 2 for trendy, 0 for negative
imageList = getImagesLabellingList()
count = 0

@app.route('/')
def index():
    print(imageList)
    return render_template('index.html',
        imageDir=IMAGEPATH,
        imageName=imageList[count],
        options=DEFAULTS,
        labelClass=LABEL_CLASS)

@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items())
    print(labelledDict)
    writeNewRow(dict(request.form.items()))
    global count
    count = count + 1
    return response

app.run(debug=True, port=8080, host='0.0.0.0')
