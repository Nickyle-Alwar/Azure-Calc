import os
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService
import string, random, requests

app = Flask(__name__, instance_relative_config=True)

# app.config.from_pyfile('config.py')
# account = app.config['ACCOUNT']   # Azure account name
# key = app.config['STORAGE_KEY']      # Azure Storage account access key  
# container = app.config['CONTAINER'] # Container name

account = "autopricing"   # Azure account name
key = "z+hBvJzSDUokiPxKfiSbxcWdMwgtG0ftlcZubzvl3TzXzYX+SDe8JDA1ypboL0fcFrxPp+vpJSR6+AStdT+4Fw=="     # Azure Storage account access key  
container = "excel-input" # Container name

blob_service = BlockBlobService(account_name=account, account_key=key)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      fileextension = filename.rsplit('.',1)[1]
      Randomfilename = id_generator()
      filename = Randomfilename + '.' + fileextension
      try:
         blob_service.create_blob_from_stream(container, filename, file)
      except Exception:
         print('Exception=' + Exception)
         pass
      ref =  'http://'+ account + '.blob.core.windows.net/' + container + '/' + filename
      return '''
      <!doctype html>
      <html style="background-color:#69be28;" text-align:center;>
      <title>File Link</title>
         <div style="display:flex; justify-content: center">
      <img src="https://autopricing.blob.core.windows.net/static-files/dd8.png" alt="Mountain" align="center" width="300px" />
   </div> 
      <h1 style="color:black; text-align:center; font-family:arial;">File Uploaded Succesfully</h1>
      <p style="color:black; text-align:center; font-family:arial;">''' + ref + '''</p>
      <!-- img src="'''+ ref +'''" -->
      </html>
      '''
   return '''
   <!doctype html >
   <html style="background-color:#69be28;" text-align:center;>
   <title style="text-align:center;">Quote Calculator</title>
   <div style="display:flex; justify-content: center">
      <img src="https://autopricing.blob.core.windows.net/static-files/dd8.png" alt="Mountain" align="center" width="300px" />
   </div> 
   <h1 style="color:black; text-align:center; font-family:arial;" >Quote Calculator</h1>
   <form action="" method=post enctype=multipart/form-data>
   <p style="color:black; text-align:center; font-family:arial;"><input type=file name=file>
      <input type=submit value="Upload Template"  style="font-family:arial;">
   </form>
   </html>
   '''
   
   # return render_template('index.html')

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    app.run()

# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return    


# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploaded_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'


# if __name__ == "__main__":
#     app.run()

#     CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=autopricing;AccountKey=z+hBvJzSDUokiPxKfiSbxcWdMwgtG0ftlcZubzvl3TzXzYX+SDe8JDA1ypboL0fcFrxPp+vpJSR6+AStdT+4Fw==;EndpointSuffix=core.windows.net"

#     CONTAINER_NAME = "excel-input"

#     output = df.to_csv(index_label="idx", encoding = "utf-8")

#     output_blob_name = "output_blob3.csv"

#     container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

#from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


