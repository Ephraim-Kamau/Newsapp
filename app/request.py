import urllib.request,json
from .models import News, Article


# Getting api key
api_key = 'db80159a19ff4fceac0d1b09a7288d5a'

# Getting the news base url
base_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def configure_request(app): 
    global api_key, base_url
    api_key = app.config[NEWS_API_KEY]
    base_url = app.config[NEWS_API_BASE_URL]

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

        #if url:
        news_object = News(id,name,description,url,category,language, country)
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

def get_articles(id):
    '''
    Function that gets the articles data for each id
    '''
    get_article_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain the articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results= None
    
    for article_item in articles_results:
        id = article_item.get('id')
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        # if urlToImage:
        articles_object = Article(id, source, author, title, description, url, urlToImage, publishedAt, content)
        articles_results.append(articles_object)   
    return articles_results