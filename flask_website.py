# import fitz
from flask import Flask, render_template
# from pdf2jpg import pdf2jpg
import glob
import os.path
# from pdf2image import convert_from_path
# from frontend import *
# # import ftiz



app = Flask(__name__, static_folder='static')



@app.route("/")
def index():
    folder_path = 'static/'
    file_type = '*.pdf'
    files = glob.glob(os.path.join(folder_path, file_type))
    print(files)
    max_file = max(files, key=os.path.getctime)
    print("file")
    print(max_file)
    # inputpath = max_file
    # outputpath = r""
    # filename = os.path.splitext(os.path.basename(inputpath))[0]
    # print("filename")
    # print(filename)
    # result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
    # print("jpg file")
    # filename = "\\static\\"+result[0]['output_jpgfiles'][0]
    # print(filename)
    return render_template("home.html",resume = max_file)


if __name__ == "__main__":
    app.run(debug=True)