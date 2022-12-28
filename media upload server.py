from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Set the directory where uploaded files will be stored
UPLOAD_FOLDER = './uploads'

# Make sure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set the allowed file extensions for uploaded files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return 'No file uploaded'

        file = request.files['file']

        # If no file was selected, skip
        if file.filename == '':
            return 'No file selected'

        # Check if the file has an allowed extension
        if file and allowed_file(file.filename):
            # Save the file to the uploads folder
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return 'File uploaded successfully'
        else:
            return 'File has an unsupported extension'
    return '''
    <!doctype html>
    <title>Upload a file</title>
    <h1>Upload a file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
