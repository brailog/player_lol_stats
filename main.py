from player_lol_stats.constantes import STATS


def get_geral_values(values=[]):
    kda = STATS['GERAL']['KDA'] * values[0]
    cspm = STATS['GERAL']['CSPM'] * values[1]
    gpm = STATS['GERAL']['GPM'] * values[2]
    wrt = STATS['GERAL']['WRT'] * values[3]
    kp = STATS['GERAL']['KP'] * values[4]

    return kda, cspm, gpm, wrt, kp


def get_visao_values(values=[]):
    vspm = STATS['VISAO']['VSPM'] * values[0]
    wpm = STATS['VISAO']['WPM'] * values[1]
    wcpm = STATS['VISAO']['WCPM'] * values[2]

    return vspm, wpm, wcpm


def get_agressividade_values(values=[]):
    dpm = STATS['AGRESSIVIDADE']['DPM'] + values[0]
    wpm = STATS['AGRESSIVIDADE']['WPM'] + values[1]
    wcpm = STATS['AGRESSIVIDADE']['WCPM'] + values[2]

    return dpm, wpm, wcpm


def get_early_game_values(values=[]):
    aics = STATS['EARLY GAME']['AICS'] + values[0]
    xpdiff = STATS['EARLY GAME']['XPDIFF'] + values[1]
    golddiif = STATS['EARLY GAME']['GOLDDIFF'] + values[2]
    csdiff = STATS['EARLY GAME']['CSDIFF'] + values[3]

    return aics, xpdiff, golddiif, csdiff


def get_ajuste_values(values=[]):
    mental = STATS['AJUSTE']['MENTAL'] + values[0]
    orgdiff = STATS['AJUSTE']['ORGDIFF'] + values[1]
    nmvp = STATS['AJUSTE']['NMVP'] + values[2]
    nbagre = STATS['AJUSTE']['NBAGRE'] + values[3]
    pool = STATS['AJUSTE']['POOL'] + values[4]

    return mental, orgdiff, nmvp, nbagre, pool


if __name__ == '__main__':
    pass
