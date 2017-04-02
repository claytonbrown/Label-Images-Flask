import csv
import os
import glob
import options
import time
import file_management as fm
from collections import OrderedDict

#Change File Paths to Your Local Paths
READ_CSVPATH = 'read.csv'
WRITE_CSVPATH = 'write.csv'
IMAGEPATH = 'static/Clothes/Outfit/'


read_fieldnames=['image_name', 'top-primary-color-white', 'top-primary-color-beige', 'top-primary-color-black',
'top-primary-color-brown', 'top-primary-color-grey', 'top-primary-color-blue', 'top-primary-color-navy-blue',
'top-primary-color-teal', 'top-primary-color-green', 'top-primary-color-olive-green', 'top-primary-color-pink',
'top-primary-color-red', 'top-primary-color-burgundy', 'top-primary-color-purple', 'top-primary-color-orange',
'top-primary-color-yellow', 'top-secondary-color-white', 'top-secondary-color-beige', 'top-secondary-color-black',
'top-secondary-color-brown', 'top-secondary-color-grey', 'top-secondary-color-blue', 'top-secondary-color-navy-blue',
'top-secondary-color-teal', 'top-secondary-color-green', 'top-secondary-color-olive-green', 'top-secondary-color-pink',
'top-secondary-color-red', 'top-secondary-color-burgundy', 'top-secondary-color-purple', 'top-secondary-color-orange',
'top-secondary-color-yellow', 'top-type-short-sleeve-shirt', 'top-type-long-sleeve-shirt', 'top-type-short-sleeve-t-shirt',
'top-type-long-sleeve-t-shirt', 'top-type-polo', 'top-type-singlet', 'top-patterns-animal-print', 'top-patterns-argyle',
'top-patterns-horizontal-stripe', 'top-patterns-vertical-stripe', 'top-patterns-checkered', 'top-patterns-dotted', 'top-patterns-floral',
'top-patterns-plaid', 'top-style-oxford', 'top-style-dress', 'top-style-round-neck', 'top-style-henley', 'top-style-graphic',
'top-style-pocket', 'top-style-acid-wash', 'top-style-granddad-collar', 'top-style-placket', 'top-material-denim', 'top-material-dry-fit',
'bottom-primary-color-white', 'bottom-primary-color-beige', 'bottom-primary-color-black', 'bottom-primary-color-brown',
'bottom-primary-color-grey', 'bottom-primary-color-blue', 'bottom-primary-color-navy-blue', 'bottom-primary-color-teal',
'bottom-primary-color-green', 'bottom-primary-color-olive-green', 'bottom-primary-color-pink', 'bottom-primary-color-red',
'bottom-primary-color-burgundy', 'bottom-primary-color-purple', 'bottom-primary-color-orange', 'bottom-primary-color-yellow',
'bottom-secondary-color-white', 'bottom-secondary-color-beige', 'bottom-secondary-color-black', 'bottom-secondary-color-brown',
'bottom-secondary-color-grey', 'bottom-secondary-color-blue', 'bottom-secondary-color-navy-blue', 'bottom-secondary-color-teal',
'bottom-secondary-color-green', 'bottom-secondary-color-olive-green', 'bottom-secondary-color-pink', 'bottom-secondary-color-red',
'bottom-secondary-color-burgundy', 'bottom-secondary-color-purple', 'bottom-secondary-color-orange', 'bottom-secondary-color-yellow',
'bottom-type-pants', 'bottom-type-shorts', 'bottom-type-jeans', 'bottom-patterns-animal-print', 'bottom-patterns-argyle',
'bottom-patterns-horizontal-stripe', 'bottom-patterns-vertical-stripe', 'bottom-patterns-checkered', 'bottom-patterns-dotted',
'bottom-patterns-floral', 'bottom-patterns-plaid', 'bottom-style-cargo', 'bottom-style-dress', 'bottom-style-chinos', 'bottom-style-sweatpants',
'bottom-style-ripped', 'bottom-style-acid-wash', 'bottom-style-washed', 'bottom-material-denim', 'bottom-material-dry-fit', 'shoes-primary-color-white',
'shoes-primary-color-beige', 'shoes-primary-color-black', 'shoes-primary-color-brown', 'shoes-primary-color-grey', 'shoes-primary-color-blue',
'shoes-primary-color-navy-blue', 'shoes-primary-color-teal', 'shoes-primary-color-green', 'shoes-primary-color-olive-green', 'shoes-primary-color-pink',
'shoes-primary-color-red', 'shoes-primary-color-burgundy', 'shoes-primary-color-purple', 'shoes-primary-color-orange', 'shoes-primary-color-yellow',
'shoes-secondary-color-white', 'shoes-secondary-color-beige', 'shoes-secondary-color-black', 'shoes-secondary-color-brown', 'shoes-secondary-color-grey',
'shoes-secondary-color-blue', 'shoes-secondary-color-navy-blue', 'shoes-secondary-color-teal', 'shoes-secondary-color-green',
'shoes-secondary-color-olive-green', 'shoes-secondary-color-pink', 'shoes-secondary-color-red', 'shoes-secondary-color-burgundy',
'shoes-secondary-color-purple', 'shoes-secondary-color-orange', 'shoes-secondary-color-yellow', 'shoes-type-boat', 'shoes-type-boots',
'shoes-type-loafers', 'shoes-type-trainers', 'shoes-type-sandals', 'shoes-type-dress-shoes', 'shoes-type-casual-shoes', 'shoes-type-plimsolls',
'shoes-others-leather', 'shoes-others-canvas', 'score']

new_fieldnames={'top-style-round-neck':'t-shirt-style-round-neck', 'top-style-henley': 't-shirt-style-henley',
'top-style-oxford':'shirt-style-oxford', 'top-style-dress':'shirt-style-dress', 'bottom-type-pants':'bottom-type-long pants',
'bottom-material-denim':'bottom-material-denim/jeans', 'bottom-style-ripped':'denim-style-ripped',
'bottom-style-acid-wash': 'denim-style-acid-wash', 'bottom-style-washed':'denim-style-washed'}




# def getFieldNames():
#     with open(READ_CSVPATH, newline='') as csvfile:
#         my_content = csv.reader(csvfile, delimiter=',')
#         for row in
#         #print(fieldnames)

#Writes a new row of data into csv file
def writeNewRow(data, clothing_type):
    file_exists = os.path.isfile(WRITE_CSVPATH)
    with open(WRITE_CSVPATH, 'a', newline='') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=fm.retrieveFieldNames(clothing_type), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()  # file doesn't exist yet, write a header
        dataWriter.writerow(data)

def retrieveImageData(filename, csvpath):
    with open(csvpath, newline='') as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        for row in my_content:
            if filename == row[0]:
                data = dict()
                for i in range(len(row)):
                    if read_fieldnames[i] in new_fieldnames:
                        data[new_fieldnames[read_fieldnames[i]]] = row[i]
                    else:
                        data[read_fieldnames[i]] = row[i]
                print(data)
                return data
        return None

#Checks if a file path already exists in CSV file
def isFileLabelled(filename, CSVPATH):
    if os.path.isfile(CSVPATH):
        with open(CSVPATH, newline='') as csvfile:
            my_content = csv.reader(csvfile, delimiter=',')
            is_labelled = False

            for row in my_content:
                if filename == row[0]:
                    is_labelled = True
                    return True
            if not is_labelled:
                return False
    else:
        return False

#Gets list of image data for images already labelled
def getImagesLabellingList():
    images_data_list = []
    #If CSV File Exists
    if os.path.isfile(READ_CSVPATH):
        for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
             basename = (os.path.basename(filename))
             if not isFileLabelled(basename, WRITE_CSVPATH):
                 print(basename)
                 image_data = retrieveImageData(basename, READ_CSVPATH)
                 if image_data:
                    images_data_list.append(image_data)
    #READ CSV DOES NOT EXIST
    else:
        if os.path.isfile(WRITE_CSVPATH):
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
                basename = (os.path.basename(filename))
                if not isFileLabelled(basename, WRITE_CSVPATH):
                    images_data_list.append({'image_name': basename})
        else:
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
                images_data_list.append({'image_name': os.path.basename(filename)})
    return images_data_list
