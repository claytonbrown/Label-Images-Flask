from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow
from options import TOPS, BOTTOMS, SHOES
import time

app = Flask(__name__)

LABEL_CLASS = 2 #1 for classic, 2 for trendy, 0 for negative

tops_count = 0
bottoms_count = 0
shoes_count = 0
TOPSPATH = 'static/Clothes/Tops'
BOTTOMSPATH = 'static/Clothes/Bottoms'
SHOESPATH = 'static/Clothes/Shoes'

imageList = list()

# @app.route('/')
# def index():
#     print(imageList)
#     return render_template('index.html',
#         # imageDir=IMAGEPATH,
#         imageName=imageList[count],
#         options=DEFAULTS,
#         labelClass=LABEL_CLASS)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/save_tops', methods=['POST'])
def save_tops():
    response = make_response(redirect(url_for('tops')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    writeNewRow(dict(request.form.items()), 'Tops')
    global tops_count
    tops_count += 1
    return response

@app.route('/save_bottoms', methods=['POST'])
def save_bottoms():
    response = make_response(redirect(url_for('bottoms')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    writeNewRow(dict(request.form.items()), 'Bottoms')
    global bottoms_count
    bottoms_count += 1
    return response

@app.route('/save_shoes', methods=['POST'])
def save_shoes():
    response = make_response(redirect(url_for('shoes')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    writeNewRow(dict(request.form.items()), 'Shoes')
    global shoes_count
    shoes_count += 1
    return response

@app.route('/tops')
def tops():
    global imageList
    if len(imageList) == 0:
        imageList = getImagesLabellingList('Tops')
    else:
        print("Images Left:", len(imageList)-tops_count)
    return render_template('tops.html',
        imageName=imageList[tops_count],
        options=TOPS)

@app.route('/bottoms')
def bottoms():
    global imageList
    if len(imageList) == 0:
        imageList = getImagesLabellingList('Bottoms')
    else:
        print("Images Left:", len(imageList)-bottoms_count)
    return render_template('bottoms.html',
        imageName=imageList[bottoms_count],
        options=BOTTOMS)

@app.route('/shoes')
def shoes():
    global imageList
    if len(imageList) == 0:
        imageList = getImagesLabellingList('Shoes')
    else:
        print("Images Left:", len(imageList)-shoes_count)
    return render_template('shoes.html',
        imageName=imageList[shoes_count],
        options=SHOES)


app.run(debug=True, port=8080, host='0.0.0.0')
