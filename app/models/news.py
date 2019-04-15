class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,language, country):
        self.id =id
        self.name= name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Article:
    '''
    Articles class to define the news articles
    '''

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
