from langchain_core.tools import tool

from src.crawler import Crawler


@tool
def web_crawl(url: str) -> str:
    """Crawl the web page and return the content as markdown."""
    crawler = Crawler()
    article = crawler.crawl(url)
    return article.to_markdown()
