import requests

class GetHTML(object): 
	def __init__(self, link):
		self.link = link
		
	def data_request(self):
		get_html = requests.get(self.link) 
		return get_html
		
