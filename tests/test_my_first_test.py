def square(x):
    return x**2

def test_square():
    assert square(2) == 4

def test_square1():
    assert square(4) == 16




import requests

class GetHTML(object): 
    def __init__(self, link):
        self.link = link
        
    def data_request(self):
        get_html = requests.get(self.link) 
        return get_html
        
def test_data_request():
    x = requests.get("http://www.imdb.com")
    assert x.status_code == 200

def test_request_www():
    x = requests.get("http://www.imdb.comm")
    assert x.status_code == 200