from scraper.dto.match_v4 import MatchDto, ParticipantIdentityDto, TeamStatsDto, ParticipantDto, ParticipantTimelineDto, \
    ParticipantStatsDto, PlayerDto
from scraper.view import PARTICIPANT_IDENTITIES_NAME, PARTICIPANTS_NAME, PARTICIPANT_ID_NAME, TEAM_ID_NAME

TEAM1_ID = 100
TEAM2_ID = 200


def participant_map(identities: [ParticipantIdentityDto], details: [ParticipantDto]) -> dict:
    identified_participants: dict = {}  # id to participant field values
    for detail in details:
        detail_dict = detail.__dict__
        participant_id = detail_dict[PARTICIPANT_ID_NAME]
        new_participant_attributes = dict()
        for fname, fval in detail_dict.items():
            if fname == 'stats':
                fval_dict = fval.__dict__
                for stats_fname, stats_fval in fval_dict.items():
                    formatted_fname = format_participant_fname(participant_id, stats_fname)
                    new_participant_attributes[formatted_fname] = stats_fval
            else:
                formatted_fname = format_participant_fname(participant_id, fname)
                new_participant_attributes[formatted_fname] = fval
        identified_participants[participant_id] = new_participant_attributes
    for id_fname, id_fval in enumerate(identities):
        id_entry_dict = id_fval.__dict__
        participant_id = id_entry_dict[PARTICIPANT_ID_NAME]
        participant_attributes = identified_participants[participant_id]
        new_participant_attributes = dict()
        for fname, fval in id_entry_dict.items():
            if fname == 'player':
                for player_fname in fval:
                    formatted_fname = format_participant_fname(participant_id, player_fname)
                    player_fval: PlayerDto = fval[player_fname]
                    new_participant_attributes[formatted_fname] = player_fval
            else:
                formatted_fname = format_participant_fname(participant_id, fname)
                new_participant_attributes[formatted_fname] = fval
        participant_attributes.update(new_participant_attributes)
    return identified_participants


def format_participant_fname(pid, field_name):
    return "p{}{}".format(pid, field_name)


def match_dto_to_view(match: MatchDto) -> dict:
    match_dict = match.__dict__
    identified_details = participant_map(match_dict.__getitem__(PARTICIPANT_IDENTITIES_NAME),
                                         match_dict.__getitem__(PARTICIPANTS_NAME))
    flattened_result = dict()
    for val in identified_details.values():
        flattened_result.update(val)
    return flattened_result
