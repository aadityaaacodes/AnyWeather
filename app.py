from flask import Flask, render_template, request, redirect, url_for
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
    elif request.method == 'POST':
        query = request.form.get('query')
        performGoogleSearch(query=f'{query}')
        return (redirect(url_for('default')))


if __name__ == '__main__':
    app.run(debug=True, port=8500)

