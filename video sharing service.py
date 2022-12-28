import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Get a list of all the available video filenames
    video_files = os.listdir('static')

    # Render the home page template, passing in the list of video filenames
    return render_template('index.html', video_files=video_files)

# Route for handling the video upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the file from the POST request
    file = request.files['file']

    # Save the file to the server
    file.save(f'static/{file.filename}')

    # Redirect the user to the home page
    return redirect(url_for('index'))

# Route for displaying the uploaded video
@app.route('/video/<filename>')
def video(filename):
    return render_template('video.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
