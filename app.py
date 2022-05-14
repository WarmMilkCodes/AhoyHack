from flask import Flask, render_template, request, redirect, url_for, Response
from rsa import verify
import config
from bs4 import BeautifulSoup
import json
import requests
import html5lib


app = Flask(__name__)
app.secret_key = config.secret_key


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    if request.method == "POST":
        zipCode = request.form['zipCode']
        params = {
        'api_key': 'DDAF9CB2D47F40509CEEE78979E44654',
        'type': 'search',
        'search_term': 'baby formula',
        'category_id': '5427',
        'customer_zipcode': zipCode,
        'pages' :'1'
        }      
        
        # make the http GET request to BlueCart API
        url = requests.get('https://api.bluecartapi.com/request', params)
        
        json_result = json.dumps(url.json())
        print('Store ID: ["store_id"]')            
        return render_template('results.html')
    
    

    
      
    

        



if __name__ == "__main__":
    app.run(debug=True)