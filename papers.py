import logging
from urllib.request import urlopen
from bs4 import BeautifulSoup

HUGGINGFACE_BASE_URL = 'https://huggingface.co'

logger = logging.getLogger(__name__)

# Generic paper classes. When there are others sources of papers, they can also extend these classes
class Paper:
    title: str
    abstract: str

    def __init__(self, title: str, abstract: str):
        self.title = title
        self.abstract = abstract


class Papers:
    papers: list[Paper]

    def __init__(self, papers: list[Paper]):
        self.papers = papers


class HuggingFacePaper(Paper):

    @classmethod
    def from_url(cls, url):
        article_soup = BeautifulSoup(urlopen(url).read(), features="html.parser")
        title = article_soup.find('main').find('h1').get_text()   # first <h1> is the Title
        abstract = article_soup.find('main').find('p').get_text() # first <p> is the Abstract

        return cls(title, abstract)


class HuggingFacePapers(Papers):

    @classmethod
    def from_year_month(cls, year: str, month: str, top_k: int = 5):
        try:
            url = f'{HUGGINGFACE_BASE_URL}/papers/month/{year}-{month}'
            top_articles = BeautifulSoup(urlopen(url).read(), features="html.parser").find_all('article')
            top_articles = top_articles[0:min(top_k, len(top_articles))]
            articles_urls = [f'{HUGGINGFACE_BASE_URL}{article.find('a').get('href')}' for article in top_articles]
            papers = [ HuggingFacePaper.from_url(url) for url in articles_urls ]
            return cls(papers)

        except Exception:
            logger.warning(f"Could not load year {year}, month {month} from HuggingFace papers, returning empty list")
            return cls([])


