import json


# https://developer.riotgames.com/apis#match-v4/GET_getMatchlist


class MatchReferenceDto:
    lane: str
    gameId: int
    champion: int
    platformId: str
    season: int
    queue: int
    role: str
    timestamp: int

    def __init__(self, dict):
        vars(self).update(dict)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class MatchlistDto:
    matches: [MatchReferenceDto]
    totalGames: int
    startIndex: int
    endIndex: int

    def __init__(self, dict):
        for k, v in dict.items():
            if k == 'matches':
                self.matches = []
                for ary_entry in v:
                    self.matches.append(MatchReferenceDto(ary_entry))
            else:
                self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


def matchlist_from_json(json_str: str) -> MatchlistDto:
    return MatchlistDto(json.loads(json_str, object_hook=dict))


class RuneDto:
    runeId: int
    rank: int

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class MasteryDto:
    masteryId: int
    rank: int

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class PlayerDto:
    currentPlatformId: str
    summonerName: str
    matchHistoryUri: str
    platformId: str
    currentAccountId: str
    profileIcon: int
    summonerId: str
    accountId: str

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class ParticipantStatsDto:
    win: bool

    firstBloodAssist: bool
    firstInhibitorKill: bool

    totalPlayerScore: int
    objectivePlayerScore: int
    visionScore: int

    totalDamageDealt: int

    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int

    magicDamageDealtToChampions: int
    magicDamageDealt: int
    magicalDamageTaken: int

    physicalDamageDealtToChampions: int
    physicalDamageTaken: int

    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    totalDamageDealtToChampions: int

    longestTimeSpentLiving: int
    totalTimeCrowdControlDealt: int
    nodeNeutralize: int

    perk0Var1: int
    perk0Var2: int
    perk0Var3: int

    perk1Var1: int
    perk1Var2: int
    perk1Var3: int

    perk2Var1: int
    perk2Var2: int
    perk2Var3: int

    perk3Var1: int
    perk3Var2: int
    perk3Var3: int

    perk4Var1: int
    perk4Var2: int
    perk4Var3: int

    perk5Var1: int
    perk5Var2: int
    perk5Var3: int

    perk0: int
    perk1: int
    perk2: int
    perk3: int
    perk4: int
    perk5: int

    perkPrimaryStyle: int
    perkSubStyle: int

    playerScore0: int
    playerScore1: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int

    kills: int
    assists: int
    deaths: int
    wardsPlaced: int
    totalScoreRank: int
    neutralMinionsKilled: int
    nodeCapture: int
    largestMultiKill: int
    totalUnitsHealed: int
    wardsKilled: int
    largestCriticalStrike: int
    largestKillingSpree: int
    quadraKills: int
    teamObjective: int
    tripleKills: int
    nodeNeutralizeAssist: int
    combatPlayerScore: int
    turretKills: int
    firstBloodKill: bool
    killingSprees: int
    unrealKills: int
    altarsCaptured: int
    firstTowerAssist: bool
    firstTowerKill: bool
    champLevel: int
    doubleKills: int
    nodeCaptureAssist: int
    inhibitorKills: int
    firstInhibitorAssist: bool
    visionWardsBoughtInGame: int
    altarsNeutralized: int
    pentaKills: int
    totalHeal: int
    totalMinionsKilled: int
    timeCCingOthers: int

    goldSpent: int
    goldEarned: int
    participantId: int
    totalDamageTaken: int
    physicalDamageDealt: int
    sightWardsBoughtInGame: int
    neutralMinionsKilledEnemyJungle: int

    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    item7: int

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class ParticipantTimelineDto:
    lane: str
    participantId: int
    csDiffPerMinDeltas: dict
    goldPerMinDeltas: dict
    xpDiffPerMinDeltas: dict
    creepsPerMinDeltas: dict
    xpPerMinDeltas: dict
    role: str
    damageTakenDiffPerMinDeltas: dict
    damageTakenPerMinDeltas: dict

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class ParticipantDto:
    stats: ParticipantStatsDto
    participantId: int
    runes: [RuneDto]
    timeline: ParticipantTimelineDto
    teamId: int
    spell2Id: int
    masteries: [MasteryDto]
    highestAchievedSeasonTier: str
    spell1Id: int
    championId: int

    def __init__(self, dict):
        for k, v in dict.items():
            if k == 'runes':
                self.runes = []
                for ary_entry in v:
                    self.runes.append(RuneDto(ary_entry))
            elif k == 'masteries':
                self.masteries = []
                for ary_entry in v:
                    self.masteries.append(MasteryDto(ary_entry))
            else:
                self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class TeamBansDto:
    pickTurn: int
    championId: int

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class TeamStatsDto:
    firstDragon: bool
    firstInhibitor: bool
    bans: [TeamBansDto]
    baronKills: int
    firstRiftHerald: bool
    firstBaron: bool
    riftHeraldKills: int
    firstBlood: bool
    teamId: int
    firstTower: bool
    vilemawKills: int
    inhibitorKills: int
    towerKills: int
    dominionVictoryScore: int
    win: str
    dragonKills: int

    def __init__(self, dict):
        for k, v in dict.items():
            if k == 'bans':
                self.bans = []
                for ary_entry in v:
                    self.bans.append(TeamBansDto(ary_entry))
            else:
                self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class ParticipantIdentityDto:
    player: PlayerDto
    participantId: int

    def __init__(self, dict):
        for k, v in dict.items():
            self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class MatchDto:
    seasonId: int
    queueId: int
    gameId: int
    participantIdentities: [ParticipantIdentityDto]
    gameVersion: str
    platformId: str
    gameMode: str
    mapId: int
    gameType: str
    teams: [TeamStatsDto]
    participants: [ParticipantDto]
    gameDurations: int
    gameCreation: int

    def __init__(self, dict):
        for k, v in dict.items():
            if k == 'participantIdentities':
                self.participantIdentities = []
                for ary_entry in v:
                    self.participantIdentities.append(ParticipantIdentityDto(ary_entry))
            elif k == 'teams':
                self.teams = []
                for ary_entry in v:
                    self.teams.append(TeamStatsDto(ary_entry))
            elif k == 'participants':
                self.participants = []
                for ary_entry in v:
                    self.participants.append(ParticipantDto(ary_entry))
            else:
                self.__setattr__(k, v)

    def __str__(self) -> str:
        return self.__dict__.__str__()


def match_from_json(json_str: str) -> MatchDto:
    return MatchDto(json.loads(json_str, object_hook=dict))
