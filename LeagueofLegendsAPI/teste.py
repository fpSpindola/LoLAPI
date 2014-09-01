import urllib3
import json
import unicodedata
import re
from __builtin__ import iter
import lolapi_wrapper
import pprint

api_key = 'f905f608-0cca-4262-8c2a-ffb26d2dd246'
API_BASE_URL = 'https://br.api.pvp.net/api/lol'
#api_version = {'champion':'1.2', 'game':'1.3', 'league':'2.4', 'lol-static-data': '1.2', 'match':'2.2', 'matchhistory':'2.2','stats':'1.3', 'summoner':'1.4', 'team':'2.3'}
api_version = '1.2'
api_region = 'br'
api_url = API_BASE_URL + '/' + api_region + '/' + 'v' + api_version + '/'
season = 'SEASON4'

api_test = lolapi_wrapper.LeagueOfLegends('f905f608-0cca-4262-8c2a-ffb26d2dd246')
summoner_info_by_name = api_test.get_summoner_by_name('Stormy')

dict_values = summoner_info_by_name[next(iter(summoner_info_by_name.keys()))]

ranked_stats = api_test.get_summoner_ranked_stats(dict_values['id'], 'SEASON4')
#pprint.pprint(ranked_stats)

champions_info = api_test.get_summoner_by_name()
