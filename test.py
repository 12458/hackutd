import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('IP8SS3012Q_cropped.jpeg')
print(result)