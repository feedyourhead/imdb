# -*- coding: utf-8 -*-
import sys
from get_html import GetHTML

class GetJSONfromAPI(object):

    def __init__(self,id_list):
        self.id_list = id_list
        self.data_list =[]

    def get_movie_data(self, id):
        self.movie_data = GetHTML('http://www.omdbapi.com/?i=' + id).data_request()
        return self.movie_data.json()
        
    def get_data_for_list(self):
    #appends get request result to a list
        rank = 1
        for id in self.id_list:
            try:
                dat = self.get_movie_data(id)
                print 'Fetching:', str(rank), dat["Title"], dat["Year"]
                dat['Rank'] = rank
                self.data_list.append({"Rank":rank,"Title":dat["Title"],"Year":dat["Year"]})                             
            except Exception as e:
                print "exception: ", type(e), e
            rank += 1

        return self.data_list


    def sort_list_by_value(self, value):
        # ????? I dont know how to split lambada function to a private function
        self.data_list = sorted(self.data_list, key=lambda k: k[value])

        return self.data_list