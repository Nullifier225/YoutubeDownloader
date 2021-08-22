from flask import Flask,  render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/" , methods = ['GET', 'POST']) 
def getlink():

    youtube_link =YouTube(request.form['link'])
    choice = request.form['choice']
    youtube_link.streams.filter(only_audio=True).download('~/Downloads')
    return render_template('landing.html')


if __name__ == '__main__':
    app.run(debug=True)