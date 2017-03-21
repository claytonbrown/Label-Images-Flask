from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow
from options import TOPS, BOTTOMS, SHOES

app = Flask(__name__)

LABEL_CLASS = 2 #1 for classic, 2 for trendy, 0 for negative

tops_count = 0
bottoms_count = 0
shoes_count = 0
TOPSPATH = 'static/Clothes/Tops'
BOTTOMSPATH = 'static/Clothes/Bottoms'
SHOESPATH = 'static/Clothes/Shoes'

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
    global tops_count
    tops_count += 1
    return response

@app.route('/save_shoes', methods=['POST'])
def save_shoes():
    response = make_response(redirect(url_for('shoes')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    writeNewRow(dict(request.form.items()), 'Shoes')
    global tops_count
    tops_count += 1
    ### HOW TO ROUTE BACK TO NEXT SHOE IMAGE???
    return response

@app.route('/tops')
def tops():
    imageList = getImagesLabellingList('Tops')
    return render_template('tops.html',
        imageName=imageList[tops_count],
        options=TOPS)

@app.route('/bottoms')
def bottoms():
    imageList = getImagesLabellingList('Bottoms')
    return render_template('bottoms.html',
        imageName=imageList[bottoms_count],
        options=BOTTOMS)

@app.route('/shoes')
def shoes():
    imageList = getImagesLabellingList('Shoes')
    return render_template('shoes.html',
        imageName=imageList[shoes_count],
        options=SHOES)

app.run(debug=True, port=8080, host='0.0.0.0')
