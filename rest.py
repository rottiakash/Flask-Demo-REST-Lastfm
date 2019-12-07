import requests
from flask import Flask,jsonify,render_template
result = []
r = requests.get('http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=4d717c15dac49ce34e987ebfa24d2207&format=json')
data  = r.json()
for i in data['tracks']['track']:
    dict = {
        "name" : i['name'],
        "url" : i['url']
    }
    result.append(dict)

app = Flask(__name__)

@app.route('/')
def getList():
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)