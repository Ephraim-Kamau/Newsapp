import unittest
from .models import Articles

Articles = article.Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('5467','NBC America','Fight on Corruption','Is the fight on corruption going to be won?','https://newsapi.org/v2/image','https://newsapi.org/v2/bigchanges', '2019-04-12,')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))