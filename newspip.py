from flask import Flask, render_template, url_for
import requests
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()
Api_Key = os.getenv("API_KEY")

@app.route('/')
@app.route('/home')
def home():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='+Api_Key+''
    response = requests.get(url)   
    data = response.json()
    title = 'Top Articles around the world.'
    return render_template('home.html', data=data, title=title)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cnn')
def cnn():
    url = 'http://newsapi.org/v2/top-headlines?''sources=cnn&''apiKey='+Api_Key+''
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on CNN.'
    return render_template('cnn.html', data=data, title=title)

@app.route('/foxnews')
def foxnews():
    url = 'http://newsapi.org/v2/top-headlines?''sources=fox-news&''apiKey='+Api_Key+'' 
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on Fox News'
    return render_template('foxnews.html', data=data, title=title)

@app.route('/ustoday')
def ustoday():
    url = 'http://newsapi.org/v2/top-headlines?''sources=usa-today&''apiKey='+Api_Key+''    
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on USA Today'
    return render_template('ustoday.html', data=data, title=title)

@app.route('/cbsnews')
def cbsnews():
    url = 'http://newsapi.org/v2/top-headlines?''sources=cbs-news&''apiKey='+Api_Key+''   
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on CBS News'
    return render_template('cbsnews.html', data=data, title=title)

@app.route('/theverge')
def theverge():
    url = 'http://newsapi.org/v2/top-headlines?''sources=the-verge&''apiKey='+Api_Key+''   
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on The Verge'
    return render_template('theverge.html', data=data, title=title)

@app.route('/cnbc')
def cnbc():
    url = 'http://newsapi.org/v2/top-headlines?''sources=cnbc&''apiKey='+Api_Key+''   
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on CNBC'
    return render_template('cnbc.html', data=data, title=title)

@app.route('/bitcoin')
def bitcoin():
    url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey='+Api_Key+''    
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on Bitcoin'
    return render_template('bitcoin.html', data=data, title=title)

@app.route('/trump')
def trump():
    url = 'https://newsapi.org/v2/top-headlines?q=trump&apiKey='+Api_Key+''   
    response = requests.get(url)
    data = response.json()
    title = 'Top Articles on Trump'
    return render_template('trump.html', data=data, title=title)

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404


if __name__ == '__main__':
    app.run(debug=True)
    