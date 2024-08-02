from flask import Flask, render_template, request
from extractor import getInfo, performGoogleSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'GET':
        x = getInfo()
        weatherData = x['weatherData']
        imageLibrary = {
            "sunny" : "", 
            "windy" : "",
            "cloudy" : "", 
            None : "" 
        }
        return(render_template('weather.html', IMG_URL=imageLibrary["cloudy"], info=weatherData))
    else:
        return("hello")



if __name__ == '__main__':
    app.run(debug=True, port=8500)

