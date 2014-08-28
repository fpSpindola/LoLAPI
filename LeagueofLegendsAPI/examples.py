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

    #Retrieves summoner spell list. (REST)
    def get_summoner_spell_list(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/summoner-spell/api_key=%s' %self.api_key)


    #Retrieves summoner spell by its unique id. (REST)
    def get_summoner_spell_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/{region}/v1.2/summoner-spell/{id}/api_key=%s' %self.api_key)

    #Retrieve version data. (REST)
    def get_versions_data(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/static-data/br/v1.2/versions?api_key=%s' %self.api_key)

#################
####match-v2.2####
#################

#Retrieve match by match ID(Required). (REST)
#Able to use includeTimeline parameter
#Match queue type (legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT,
# ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3,
# GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2,
# NIGHTMARE_BOT_5x5_RANK5)
    def get_match_data(self):
        ret = requests.get('https://br.api.pvp.net/api/lol/br/v2.2/match/RANKED_SOLO_5x5?includeTimeline=1&api_key=%s' %self.api_key)

#########################
####matchhistory-v2.2####
#########################

    #Retrieve match history by summoner ID. (REST)
    def get_match_info_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v2.2/matchhistory/{summonerId}/api_key=%s' %self.api_key)

##################
####stats-v1.3####
##################

    #Get ranked stats by summoner ID. (REST)
    def get_ranked_match_status_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.3/stats/by-summoner/{summonerId}/ranked/api_key=%s' %self.api_key)

    #Get player stats summaries by summoner ID. (REST)
    def get_player_stats_summaries_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.3/stats/by-summoner/{summonerId}/summary/api_key=%s' %self.api_key)

####################
###summoner-v1.4####
####################

    #Get summoner objects mapped by standardized summoner name for a given list of summoner names. | "SummonerId, Name, ProfileIconId, revisionDate, summonerLevel"
    def get_summoner_info_by_names(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.4/summoner/by-name/{summonerNames}/api_key=%s' %self.api_key)

    #Get summoner objects mapped by standardized summoner name for a given list of summoner names. | "SummonerId, Name, ProfileIconId, revisionDate, summonerLevel"
    def get_summoner_info_by_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.4/summoner/{summonerIds}/api_key=%s' %self.api_key)

    #Get mastery pages mapped by summoner ID for a given list of summoner IDs (REST)
    def get_mastery_pages_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.4/summoner/{summonerIds}/masteries/api_key=%s' %self.api_key)

    #Get summoner names mapped by summoner ID for a given list of summoner IDs. (REST)
    def get_summoner_names_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.4/summoner/{summonerIds}/name/api_key=%s' %self.api_key)

    #Get rune pages mapped by summoner ID for a given list of summoner IDs. (REST)
    def gett_rune_pages_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v1.4/summoner/{summonerIds}/runes/api_key=%s' %self.api_key)


#################
####team-v2.3####
#################

    #Get teams mapped by summoner ID for a given list of summoner IDs. (REST)
    def get_teams_by_summoner_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v2.3/team/by-summoner/{summonerIds}/api_key=%s' %self.api_key)

    #Get teams mapped by team ID for a given list of team IDs. (REST)
    def get_teams_by_team_id(self):
        ret = requests.get(r'https://br.api.pvp.net/api/lol/br/v.2.3/team/{teamsIds}/api_key=%s' %self.api_key)