__author__ = 'Filipe'

import requests

api_key = 'f905f608-0cca-4262-8c2a-ffb26d2dd246'

###################
###champion-v1.2###
###################

#Get Information from all LoL Champions
ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.2/champion?api_key=%s' %api_key)

#Get Information from all LoL Champions by Id
ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.2/champion/{id}/api_key=%s' %api_key)


###################
#####game-v1.3#####
###################

#Get a Game Information by Summoner Id
ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent/api_key=%s' %api_key)

###################
####league-v2.4####
###################

#





