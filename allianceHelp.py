def allianceHelp(t, allianceSize):

    boost_count = min(allianceSize, 10)
    boost_effect = max(60, t // 10)
    return max(0, t - boost_effect * boost_count)
