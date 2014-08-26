__author__ = 'Filipe'
# noinspection PyStatementEffect

import requests

class LolApi:
    def __init__(self):
        self.api_key = api_key = 'f905f608-0cca-4262-8c2a-ffb26d2dd246'
        self.default_url = 'https://br.api.pvp.net/api/lol'
        self.region = 'br'
        self.api_reference_version = None

###################
###champion-v1.2###
###################

    def get_all_champ_information(self):
        #Get Information from all LoL Champions
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.2/champion?api_key=%s' %self.api_key)

    def get_all_champ_information_by_id(self):
        #Get Information from all LoL Champions by Id
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.2/champion/{id}/api_key=%s' %self.api_key)

###################
#####game-v1.3#####
###################

#Get a Game Information by Summoner Id
ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent/api_key=%s' %self.api_key)

###################
####league-v2.4####
###################

#Get leagues mapped by summoner ID for a given list of summoner IDs. (REST)
ret = request.get(r'GET /api/lol/{region}/v2.4/league/by-summoner/{summonerIds}

#Get league entries mapped by summoner ID for a given list of summoner IDs. (REST)
GET /api/lol/{region}/v2.4/league/by-summoner/{summonerIds}/entry

#Get leagues mapped by team ID for a given list of team IDs. (REST)
GET /api/lol/{region}/v2.4/league/by-team/{teamIds}

#Get league entries mapped by team ID for a given list of team IDs. (REST)
GET /api/lol/{region}/v2.4/league/by-team/{teamIds}/entry

#Get challenger tier leagues. (REST)
GET /api/lol/{region}/v2.4/league/challenger

############################
####lol-static-data-v1.2####
############################

#Retrieves champion list. (REST)
GET /api/lol/static-data/{region}/v1.2/champion

#Retrieves a champion by its id. (REST)
GET /api/lol/static-data/{region}/v1.2/champion/{id}

#Retrieves item list. (REST)
GET /api/lol/static-data/{region}/v1.2/item

#Retrieves item by its unique id. (REST)
GET /api/lol/static-data/{region}/v1.2/item/{id}

#Retrieves mastery list. (REST)
GET /api/lol/static-data/{region}/v1.2/mastery

#Retrieves mastery item by its unique id. (REST)
GET /api/lol/static-data/{region}/v1.2/mastery/{id}

#Retrieve realm data. (REST)
GET /api/lol/static-data/{region}/v1.2/realm

#Retrieves rune list. (REST)
GET /api/lol/static-data/{region}/v1.2/rune

#Retrieves rune by its unique id. (REST)
GET /api/lol/static-data/{region}/v1.2/rune/{id}

#Retrieves summoner spell list. (REST)
GET /api/lol/static-data/{region}/v1.2/summoner-spell

#Retrieves summoner spell by its unique id. (REST)
GET /api/lol/static-data/{region}/v1.2/summoner-spell/{id}

#Retrieve version data. (REST)
GET /api/lol/static-data/{region}/v1.2/versions

#################
####marchv2.2####
#################

#Retrieve match by match ID. (REST)
GET /api/lol/{region}/v2.2/match/{matchId}

#########################
####matchhistory-v2.2####
#########################

#Retrieve match history by summoner ID. (REST)
GET /api/lol/{region}/v2.2/matchhistory/{summonerId}

##################
####stats-v1.3####
##################

#Get ranked stats by summoner ID. (REST)
GET /api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked

#Get player stats summaries by summoner ID. (REST)
GET /api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/summary

####################
###summoner-v1.4####
####################

#Get summoner objects mapped by standardized summoner name for a given list of summoner names. (REST)
GET /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}

#Get objects mapped by summoner ID for a given list of summoner IDs. (REST)
GET /api/lol/{region}/v1.4/summoner/{summonerIds}

#Get mastery pages mapped by summoner ID for a given list of summoner IDs (REST)
GET /api/lol/{region}/v1.4/summoner/{summonerIds}/masteries

#Get summoner names mapped by summoner ID for a given list of summoner IDs. (REST)
GET /api/lol/{region}/v1.4/summoner/{summonerIds}/name

#Get rune pages mapped by summoner ID for a given list of summoner IDs. (REST)
GET /api/lol/{region}/v1.4/summoner/{summonerIds}/runes


#################
####team-v2.3####
#################

#Get teams mapped by summoner ID for a given list of summoner IDs. (REST)
GET /api/lol/{region}/v2.3/team/by-summoner/{summonerIds}

#Get teams mapped by team ID for a given list of team IDs. (REST)
GET /api/lol/{region}/v2.3/team/{teamIds}


