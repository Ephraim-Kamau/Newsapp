from app import app
import urllib.request,json
from .models import news


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
individual_news = app.config['NEWS_API_NEWS_CHANEL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            
    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country  = news_item.get('country')

        if url:
            news_object = news.News(id,name,description,url,category,language, country)
            news_results.append(news_object)

    return news_results

def get_news_item(id):
    get_new_details_url = individual_news.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = []
        if new_details_response:
            id = new_item.get('id')
            name = new_item.get('name')
            description = new_item.get('description')
            url = new_item.get('url')
            category = new_item.get('category')
            language = new_item.get('language')
            country  = news_item.get('country')

            new_object = news.News(id,name,description,url,category,language, country)

    return new_object

    