from flask import Flask,  render_template, request,redirect
import pytubedownloader as pd

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/" , methods = ['GET', 'POST']) 
def getlink():
    youtube_link = request.form['link']
    print(pd.video_download(youtube_link))
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)