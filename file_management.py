from PIL import Image
import csv
import os
import glob
import options

#Change File Paths to Your Local Paths
CSVPATH = 'trendy_data_set_1.csv'
IMAGEPATH = 'static/img'

#Retrive header names from DEFAULTS
def retrieveFieldNames():
    fieldnames = list()
    fieldnames.append('image_name')
    for key in options.DEFAULTS.keys():
        for value in options.DEFAULTS[key]:
            name = key + "-" + value
            fieldnames.append(name)
    fieldnames.append('score') #1 for positive class
    return fieldnames

#Writes a new row of data into csv file
def writeNewRow(data):
    file_exists = os.path.isfile(CSVPATH)
    with open(CSVPATH, 'a', newline='') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=retrieveFieldNames(), restval=0, lineterminator='\n')#
        if not file_exists:
            dataWriter.writeheader()  # file doesn't exist yet, write a header
        dataWriter.writerow(data)

#Checks if a file path already exists in CSV file
def isFileLabelled(filename):
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
def getImagesLabellingList():
    images_file_list = []
    #If CSV File Exists
    if os.path.isfile(CSVPATH):
        for filename in glob.glob('static/img/*.jpg'): #assuming jpg
            if not isFileLabelled(filename[11:]):
                images_file_list.append(filename[11:])
    else:
        for filename in glob.glob('static/img/*.jpg'): #assuming jpg
            images_file_list.append(filename[11:])
    return images_file_list
