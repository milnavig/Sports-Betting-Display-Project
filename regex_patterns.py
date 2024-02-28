market_patterns = {
    "WIN_HALF_MATCH": "!^(?P<basis>WIN_HALF_MATCH)__(?P<pivot>(?:P[12X]|12|1X|X2)_(?:P[12X]|12|1X|X2))$!",
    "CORRECT_SCORE": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>CORRECT_SCORE)(?:_(?P<ot_rt>OT|RT|ET))?\\((?P<pivot>[0-9]+:[0-9]+|ANY_OTHER|ANY_P[12])\\)$!",
    "TEAMS_TO_SCORE": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(((BOTH_TEAMS|ONLY_ONE_TEAM|NO_ONE)_TO_SCORE|(ONLY_)?(?P<basis>TEAM_TO_SCORE)__(?P<plr>P[12]))__(?P<dst>YES|NO))$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?LAST_(?P<basis>TEAM_TO_SCORE)__(?P<plr>(?:P[12]|NO))$!"
    ],
    "WHO_SCORE": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WHO_SCORE)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]))$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WHO_SCORE)_?(?P<_3w>3W)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]|NO))$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WHO_SCORE)_?(?P<ot_rt>OT|RT|ET|CT)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]|NO))$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WHO_SCORE)_(?P<_3w>3W)_(?P<ot_rt>OT|RT|ET|CT)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]|NO))$!"
    ],
    "WILL_BE_OT": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WILL_BE_OT)__(?P<dst>YES|NO)$!",
    "FIRST_TO_SCORE": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>FIRST_TO_SCORE)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]))$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>FIRST_TO_SCORE)_?(?P<_3w>3W)__(?P<pivot>\\d\\d\\d?(?:_\\d\\d)?)__(?P<plr>(?:P[12]|NO))$!"
    ],
    "TOTALS_ODD": [
        "!^(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>ODD|EVEN)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>ODD|EVEN)$!"
    ],
    "TEAM_TOTALS_ODD": [
        "!^(?:(?P<plr>P[12])__)(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>ODD|EVEN)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)(?:(?P<plr>P[12])__)(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>ODD|EVEN)$!"
    ],
    "TOTALS_CORNERS_ODD": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?:(?P<plr>P[12])__)?(?P<basis>TOTALS_CORNERS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>ODD|EVEN)$!",
    "CLEAN_SHEET": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>CLEAN_SHEET)__(?P<plr>P[12])__(?P<dst>YES|NO)$!",
    "SETS_TOTALS": [
        "!^(?P<basis>SETS_TOTALS)__(?P<dst>UNDER|OVER)\\((?P<pivot>\\d+\\.(?:25|5|75))\\)$!",
        "!^(?P<basis>SETS_TOTALS)__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!"
    ],
    "SETS_HANDICAP": [
        "!^(?P<basis>SETS_HANDICAP)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<plr>P[12])\\((?P<pivot>-?[\\d]+(?:\\.(?:25|5|75))?)\\)$!"
    ],
    "WIN": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WIN)(?:_(?P<ot_rt>OT|RT|ET))?__(?P<plr>P[12X]|1X|2X|X2|12)$!",
    "WIN_CORNERS": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>WIN_CORNERS)?__(?P<plr>P[12X]|1X|2X|X2|12)$!",
    "ASIAN_TOTALS": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+\\.(\\d\\d))\\)$!",
    "ASIAN_TOTALS_CORNERS": "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS_CORNERS?)(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+\\.(\\d\\d))\\)$!",
    "TOTALS": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+(?:\\.(?:25|5|75))?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS)_?(?P<_3w>3W)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>OVER|UNDER)\\((?P<pivot>\\d+)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS)_?(?P<_3w>3W)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!"
    ],
    "TOTALS_CORNERS": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS_CORNERS)?(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+(?:\\.(?:25|5|75))?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS_CORNERS)?(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS_?(?P<_3w>3W)_CORNERS)?(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>OVER|UNDER)\\((?P<pivot>\\d+)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>TOTALS_?(?P<_3w>3W)_CORNERS)?(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!"
    ],
    "TEAM_TOTALS": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+(?:\\.(?:25|5|75))?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS)_?(?P<_3w>3W)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+(?:\\.(?:25|5|75))?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS)_?(?P<_3w>3W)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!"
    ],
    "TEAM_TOTALS_CORNERS": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS_CORNERS?)(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>OVER|UNDER)\\((?P<pivot>[\\d]+(?:\\.\\d+)?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<plr>P[12])__(?P<basis>TOTALS_CORNERS?)(?:_(?P<ot_rt>OT|RT|ET))?__(?P<dst>EXACT)\\((?P<pivot>\\d+\\-\\d+|\\d+)\\)$!"
    ],
    "HANDICAP": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>HANDICAP)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<plr>P[12])\\((?P<pivot>-?[\\d]+(?:\\.(?:25|5|75))?|PK)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>HANDICAP)_?(?P<_3w>3W)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<plr>P[12X])\\((?P<pivot>-?[\\d]+(?:\\.(?:25|5|75))?)\\)$!"
    ],
    "HANDICAP_CORNERS": [
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>HANDICAP_CORNERS?)(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<plr>P[12])\\((?P<pivot>-?[\\d]+(?:\\.(?:25|5|75))?)\\)$!",
        "!^(?:(?P<period_name>SET|HALF)_(?P<period_no>\\d\\d)__)?(?P<basis>HANDICAP)_?(?P<_3w>3W)_CORNERS?(?:_(?P<ot_rt>OT|RT|ET|CT))?__(?P<plr>P[12X])\\((?P<pivot>-?[\\d]+(?:\\.(?:25|5|75))?)\\)$!"
    ],
    "GAME_WIN": "!^(?P<basis>GAME)(?:_(?P<ot_rt>CT))?__(?P<pivot>\\d\\d_\\d\\d)__(?P<plr>P[12])$!",
    "WIN_PLACE": "!^(?P<plr>P\\d{1,2})__(?P<basis>PLACE)\\(\\d{1,2}[-+]?\\)$!",
    "TO_QUALIFY": "!^(?P<basis>TO_QUALIFY)\\((?P<plr>P[12])\\)$!",
    "PLAYER_TO_SCORE": "!^(?P<basis>PLAYER_TO_SCORE)__(?P<pivot>0\\d|\\d{2,2}|ANYTIME)\\((?P<plr>\\w+)\\)$!"
}