#the www can be represented by a directed graph
#each webpage is a vertice
#the links to other urls on a webpage are edges
#   we have to parse the html of a website looking for urls (i.e. all the edges)

import requests
import re

class WebCrawler:

    def __init__(self):
        self.discovered_websites = []

    #Standard BFS implementation
    def crawl(self, start_url):

        queue = []
        queue.append(start_url)
        self.discovered_websites.append(start_url)

        while queue:
            actual_url = queue.pop(0)
            print(actual_url)

            #raw html representaion of a website
            actual_url_html = self.read_raw_html(actual_url)

            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)
    
    def read_raw_html(self, url):
        raw_html = ''

        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass
        
        return raw_html

    def get_links_from_html(self, raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

if __name__ == "__main__":

    crawler = WebCrawler()
    crawler.crawl('https://www.marksdailyapple.com')