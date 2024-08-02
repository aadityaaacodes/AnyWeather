from flask import Flask, render_template, request, redirect, url_for
from extractor import getInfo, performGoogleSearch, putInfo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'GET':
        x = getInfo()
        searchdata = x['searchData']
        weatherData = x['weatherData']
        imageLibrary = {
            "Sunny" : "https://i.gifer.com/Iqp.gif", 
            "Windy" : "https://i.gifer.com/fzmZ.gif",
            "Storm" : "https://i.gifer.com/604.gif", 
            "Snow" : "https://i.gifer.com/3gF.gif",
            "Hail" : "https://i.gifer.com/Cba.gif",
            "Cloudy" : "https://i.gifer.com/srG.gif", 
            "Rain" : "https://i.gifer.com/AcU9.gif",
            None : "" 
        }

        url = ""

        i = (weatherData['condition']).split(' ')
        for j in imageLibrary:
            if j in i:
                url = imageLibrary[f'{j}']

        return(render_template('weather.html', Img_URL=url, info=weatherData, city=searchdata['city']))
    elif request.method == 'POST':
        query = request.form.get('query')
        x = getInfo()
        searchData = x['searchData']
        searchData['city'] = query
        putInfo(x)
        performGoogleSearch(query=f'{query}')
        return (redirect(url_for('default')))


if __name__ == '__main__':
    app.run(debug=True, port=8500)

