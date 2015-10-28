# -*- coding: utf-8 -*-

from dbhelper import DBhelper
from get_html import GetHTML
from getjsonfromapi import GetJSONfromAPI
from idcollector import IdCollector


ids = IdCollector()
movie_data = GetJSONfromAPI(ids.get_ids(100))
movie_data.get_data_for_list()
db = DBhelper()
#output = SaveJSONtoCSV('top_100.csv',movie_data.sort_list_by_value('Year')) 
#output.write()

db.insert_many(movie_data.data_list)

