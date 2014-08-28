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

    #Get Information from all LoL Champions
    def get_all_champ_information(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.2/champion?api_key=%s' %self.api_key)

    #Get Information from all LoL Champions by Id
    def get_all_champ_information_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.2/champion/{id}/api_key=%s' %self.api_key)

###################
#####game-v1.3#####
###################

    #Get a Game Information by Summoner Id
    def get_game_info_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent/api_key=%s' %self.api_key)

###################
####league-v2.4####
###################

    #Get leagues mapped by summoner ID for a given list of summoner IDs. (REST)
    def get_leagues_by_summoner_id_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v2.4/league/by-summoner/{summonerIds}/api_key=%s' %self.api_key)

    #Get league entries mapped by summoner ID for a given list of summoner IDs. (REST)
    def get_league_entries_by_summoner_id_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v2.4/league/by-summoner/{summonerIds}/entry/api_key=%s' %self.api_key)

    #Get leaguess mapped by team ID for a given list of team IDs. (REST)
    def  get_leagues_by_team_id_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v2.4/league/by-team/{teamIds}/api_key=%s' %self.api_key)

    #Get league entries mapped by team ID for a given list of team IDs. (REST)
    def get_league_entries_by_team_id_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v2.4/league/by-team/{teamIds}/entry/api_key=%s' %self.api_key)

    #Get challenger tier leagues. (REST)
    def get_challenger_tier_leagues(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/{region}/v2.4/league/challenger/api_key=%s' %self.api_key)

############################
####lol-static-data-v1.2####
############################

    #Retrieves champion list. Return IDs(REST)
    def get_all_champions(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/champion/api_key=%s' %self.api_key)


    #Retrieves a champion by its id. (REST)
    def get_champion_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/champion/{id}/api_key=%s' %self.api_key)

    #Retrieves item list. (REST)
    def get_item_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/item/api_key=%s' %self.api_key)

    #Retrieves item by its unique id. (REST)
    def get_item_by_unique_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/item/{id}/api_key=%s' %self.api_key)

    #Retrieves mastery list. (REST)
    def get_mastery_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/mastery/api_key=%s' %self.api_key)

    #Retrieves mastery item by its unique id. (REST)
    def get_mastery_item_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/mastery/{id}/api_key=%s' %self.api_key)

    #Retrieve realm data. (REST)
    def get_domain_information(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/realm/api_key=%s' %self.api_key)

    #Retrieves rune list. (REST)
    def get_all_runes_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/rune')

    #Retrieves rune by its unique id. (REST)
    def get_rune_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/rune/{id}/api_key=%s' %self.api_key)
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


