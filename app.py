from flask import Flask, render_template
from extractor import getInfo, performGoogleSearch

app = Flask(__name__)

@app.route('/')
def default():
    return(render_template('weather.html'))


@app.route('/home')
def home():
    x = getInfo()
    Wdata = x['weatherData']
    url = "/Volumes/dev/weather-app/conditionImages/sunny.png"
    imageLibrary = {
        "Sunny": "https://cdn-icons-png.flaticon.com/512/979/979585.png", 
        "Cloudy" : "https://cdn-icons-png.flaticon.com/512/1163/1163736.png", 
        "Haze" : "https://cdn-icons-png.flaticon.com/512/1779/1779862.png", 
        "Rain" : "https://cdn-icons-png.flaticon.com/512/4150/4150897.png"
    }
    # return(render_template('hello.html', link=imageLibrary[Wdata['condition']]))
    return(render_template('home.html', Location=x["searchData"], W=Wdata, conditionURL=imageLibrary[Wdata['condition']]))

if __name__ == '__main__':
    app.run(debug=True, port=8500)

