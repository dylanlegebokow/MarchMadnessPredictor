# File is responsible for creating our data vectors and outputting them to a csv
# All data points are between seasons 1992-1993 and 2015-2016, as that is all the data I was able to collect

import numpy as np
import re
import os
from utils import *

vector_length = 26


# Returns a teams stats on a per-game basis
def per_game(games, total):
    return total / games


# Removes old files so new ones can be made
def initialize():
    for i in range(1993, 2017):
        remove_file = 'data\DataForML\data_' + str(i) + '.csv'
        os.remove(remove_file)


if __name__ == '__main__':

    initialize()

    # Only need data pertaining to the teams that made the tournament. This function finds those teams
    with open('data\MMSeeds_with_Team_IDs.csv') as f:
        lines = f.readlines()
        for line in lines:
            season, seed, school_num = line.split(',')
            # Because the first instance is the title 'Season' and that isn't a year
            if season == 'Season':
                continue

            seed = int(re.sub('[^0-9]', '', seed))
            school_num = int(school_num)
            team_name = get_team_id(school_num).strip()
            team_name = fix_teamname(team_name, school_num)

            if team_name == False:
                print("Error: Couldn't find team name for ID ", school_num)
                break

            # Creates an empty vector of length 'vector_length' which will store all the data for that data point
            data_point = np.zeros((vector_length,))

            mm_stats = 'data\TeamStats\MMStats_'+str(season)+'.csv'
            rating_stats = 'data\RatingStats\RatingStats_'+str(season)+'.csv'
            conference_stats = 'data\ConferenceTournament\Conference_'+str(season)+'.csv'

            # Gets a team's statistics for a particular season, depending on file
            # Definitions of terms found at:
            # https://www.basketball-reference.com/about/glossary.html

            with open(mm_stats) as a:
                bxs = a.readlines()
                for bx in bxs:
                    _, school_name1, games_played, wins, _, _, _, _, _, _, _, _, _, _, _, _, _, _, fgm, _, fgp, \
                    threem, _, threep, ftm, _, ftp, otb, trb, ast, stl, blk, tov, pf = bx.split(',')
                    school_name1 = school_name1.strip('"')
                    if school_name1 == team_name:
                        # Create a function that removes all the '"'s, white-space from a string
                        games_played = int(games_played.strip().strip('"'))
                        wins = int(wins.strip().strip('"'))
                        fgm = per_game(games_played, float(fgm.strip().strip('"')))
                        fgp = float(fgp.strip().strip('"'))
                        threem = per_game(games_played, int(threem.strip().strip('"')))
                        threep = float(threep.strip().strip('"'))
                        ftm = per_game(games_played, int(ftm.strip().strip('"')))
                        ftp = float(ftp.strip().strip('"'))
                        if otb.strip().strip('"') != '':
                            otb = per_game(games_played, int(otb.strip().strip('"')))
                        else:
                            otb = 0
                        if trb.strip().strip('"') != '':
                            trb = per_game(games_played, int(trb.strip().strip('"')))
                        else:
                            trb = 0
                        ast = per_game(games_played, int(ast.strip().strip('"')))
                        stl = per_game(games_played, int(stl.strip().strip('"')))
                        blk = per_game(games_played, int(blk.strip().strip('"')))
                        if tov.strip().strip('"') != '':
                            tov = per_game(games_played, int(tov.strip().strip('"')))
                        else:
                            tov = 0
                        if pf.strip().strip('"') != '':
                            pf = per_game(games_played, int(pf.strip().strip('"')))
                        else:
                            pf = 0

                        data_point = assign_1(data_point, games_played, wins, fgm, fgp, threem, threep, ftm, ftp,
                                              otb, trb, ast, stl, blk, tov, pf)

            # Gets some other statistics for teams not covered in the function above
            with open(rating_stats) as b:
                cxs = b.readlines()
                for cx in cxs:
                    _, school_name2, conference1, _, _, _, ppg, oppg, _, _, sos, _, osrs, dsrs, srs, ortg, drtg, \
                    nrtg = cx.split(',')
                    school_name2 = school_name2.strip('"')

                    if school_name2 == team_name:

                        ppg = float(ppg.strip().strip('"'))
                        if oppg.strip().strip('"') != '':
                            oppg = float(oppg.strip().strip('"'))
                        else:
                            oppg = 0
                        sos = float(sos.strip().strip('"'))
                        osrs = float(osrs.strip().strip('"'))
                        dsrs = float(dsrs.strip().strip('"'))
                        srs = float(srs.strip().strip('"'))
                        if ortg.strip().strip('"') != '':
                            ortg = float(ortg.strip().strip('"'))
                        else:
                            ortg = 0
                        if drtg.strip().strip('"') != '':
                            drtg = float(drtg.strip().strip('"'))
                        else:
                            drtg = 0
                        if nrtg.strip().strip('"') != '':
                            nrtg = float(nrtg.strip().strip('"'))
                        else:
                            nrtg = 0

                        data_point = assign_2(data_point, ppg, oppg, sos, osrs, dsrs, srs, ortg, drtg, nrtg)

            # Imports data on the team's conference to infer how strong of a conference they play in
            with open(conference_stats) as b:
                dxs = b.readlines()
                for dx in dxs:
                    conference2, winner, runner_up = dx.split(',')
                    winner = winner.strip()
                    runner_up = runner_up.strip()
                    if team_name == winner:
                        data_point = assign_3(data_point, True)
                    if team_name == runner_up:
                        data_point = assign_3(data_point, False)

            if np.count_nonzero(data_point) < 5:
                print('\n' + team_name + '\t\t' + str(school_num))
                print(data_point)

            out_file = 'data\DataForML\data_'+season+'.csv'

            string_to_write = [str(school_num)]
            string_to_write.append(str(seed))
            for i in data_point:
                string_to_write.append(str(i))
            string_to_write = ','.join(string_to_write)
            string_to_write = string_to_write + '\n'

            with open(out_file, 'a') as z:
                z.write(string_to_write)
