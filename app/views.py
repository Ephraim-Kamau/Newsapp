from flask import render_template
from app import app
from .request import get_news, get_news_item, Article

#movies is news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting general news
    general_news = get_news('general')
    business_news = get_news('business')
    sports_news = get_news('sports')

    title = 'Home - Welcome To The Best News Website Online'
    return render_template('index.html', title = title, general = general_news, business = business_news, sports = sports_news ) 

@app.route('/news/<id>')
def new(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    new = get_news_item(id)
    title = f'{new.title}'

    return render_template('news.html',title = title,new = new)    

@app.route('/articles/<id>')
def articles(id):
    '''
    View Source page function that returns news source details and its data
    '''

    news = get_articles(id)
    return render_template('articles.html', id = id,  news = news)