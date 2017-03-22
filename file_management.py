from PIL import Image
import csv
import os
import glob
import options

#Change File Paths to Your Local Paths
TOPSCSV = 'tops.csv'
BOTTOMSCSV = 'bottoms.csv'
SHOESCSV = 'shoes.csv'


#Retrive header names from DEFAULTS
def retrieveFieldNames(clothing_type):
    if clothing_type == 'Tops':
        OPTS = options.TOPS
    elif clothing_type == 'Bottoms':
        OPTS = options.BOTTOMS
    elif clothing_type == 'Shoes':
        OPTS = options.SHOES
    fieldnames = list()
    fieldnames.append('image_name')
    for key in OPTS.keys():
        for value in OPTS[key]:
            name = key + "-" + value
            fieldnames.append(name)
    return fieldnames

#Writes a new row of data into csv file
def writeNewRow(data, clothing_type):
    if clothing_type == 'Tops':
        CSVPATH = TOPSCSV
    elif clothing_type == 'Bottoms':
        CSVPATH = BOTTOMSCSV
    elif clothing_type == 'Shoes':
        CSVPATH = SHOESCSV
    file_exists = os.path.isfile(CSVPATH)
    with open(CSVPATH, 'a', newline='') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=retrieveFieldNames(clothing_type), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()  # file doesn't exist yet, write a header
        dataWriter.writerow(data)

#Checks if a file path already exists in CSV file
def isFileLabelled(filename, CSVPATH):
    with open(CSVPATH, newline='') as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        is_labelled = False

        for row in my_content:
            if filename == row[0]:
                is_labelled = True
                return True
        if not is_labelled:
            return False

#Gets list of images to be labelled
def getImagesLabellingList(clothing_type):
    images_file_list = []
    if clothing_type == 'Tops':
        CSVPATH = TOPSCSV
    elif clothing_type == 'Bottoms':
        CSVPATH = BOTTOMSCSV
    elif clothing_type == 'Shoes':
        CSVPATH = SHOESCSV
    path = 'static/Clothes/'+clothing_type+'/'
    #If CSV File Exists
    if os.path.isfile(CSVPATH):
        for filename in sorted(glob.glob(path+'*.jpg')): #assuming jpg
            if not isFileLabelled(filename, CSVPATH):
                images_file_list.append(filename)
    else:
        for filename in sorted(glob.glob(path+'*.jpg')): #assuming jpg
            images_file_list.append(filename)
    return images_file_list
