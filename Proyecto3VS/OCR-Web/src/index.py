
from flask import Flask, render_template, request, redirect
import pytesseract
from pytesseract import Output
import operator
try:
    from PIL import Image
except:
    import Image

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def ocr_core_lines(filename):
    data = pytesseract.image_to_data(Image.open(filename), output_type=Output.DICT)
    length = len(data['line_num'])
    lines = data['line_num'][length-1]
    return lines

wordsQ = 7
def ocr_core_words(textoStr):
    textoStr = textoStr.replace(".","")
    textoStr = textoStr.replace(",","")
    arr = textoStr.split()
    #print(arr)
    countedWords = {}
    for w in arr:
        if ( w not in countedWords ):
            countedWords[w] = arr.count(w)
    sortedList = sorted(countedWords.items(), key=operator.itemgetter(1), reverse=True)
    #print(sortedList)
    res = {}
    cont = 0
    for item in sortedList:
        if cont < wordsQ:
            new_key = item[0]
            new_value = item[1]
            res [new_key] = new_value
            cont += 1
    #print(res)
    return res


app = Flask(__name__)

@app.route('/')
def test():
    return render_template("home.html")
    
    
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            imagen = request.files["image"]
            print(imagen)
            img = imagen.filename
            extracted_text = ocr_core(imagen)
            lines_text = ocr_core_lines(imagen)
            print(lines_text)
            words = ocr_core_words(extracted_text)
            print(words)
            return render_template('upload_image.html',
                                   extracted_text=extracted_text,
                                   lines_text=lines_text,
                                   words=words,
                                   img=img)
    return render_template("upload_image.html")



if __name__ == '__main__':
    app.run(debug=True)