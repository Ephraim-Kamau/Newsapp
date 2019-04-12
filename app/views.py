from flask import render_template
from app import app

#movies is news

# Views
@app.route('/news/<int:news_id>')
def news():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome To The Best News Website Online'
    return render_template('index.html',title = title)