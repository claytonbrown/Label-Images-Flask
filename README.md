# Label-Images-Flask
A minimal Flask web application for labelling images into a CSV dataset

##Instructions
1. You need Flask and Python 3 to run this application. (Setting up https://teamtreehouse.com/community/how-to-run-flask-locally)
2. Place images you would like to label for a single class (positive/negative)
into static/img folder.
3. Edit LABEL_CLASS in app.py to reflect the class you are labelling (1 for positive,
  0 for negative)

##Note:
1. Headers for your CSV file will be generated from the labels in options.py
2. When all images in your static/img folder are labelled, the app will exit with
index_out_of_bounds
3. Only .jpg images are handled by file_management
