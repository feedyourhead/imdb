# -*- coding: utf-8 -*-

from get_html import GetHTML
from idcollector import IdCollector
from getjsonfromapi import GetJSONfromAPI
from savecsv import SaveJSONtoCSV

ids = IdCollector()


movie_data = GetJSONfromAPI(ids.get_ids(100))
movie_data.get_data_for_list()


output = SaveJSONtoCSV('top_100.csv',movie_data.sort_list_by_value('Year')) 
output.write()