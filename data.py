# File is responsible for creating our data vectors and outputting them to a csv
# All data points are between seasons 1992-1993 and 2015-2016, as that is all the data I was able to collect

import numpy as np
import re
import os
from utils import *

# Files and Partial Files
mm_stats = '\TeamStats\MMStats_'
rating_stats = '\RatingStats\RatingStats_'
conference_stats = '\ConferenceTournament\Conference_'
out_file = 'data\DataForML\data_'

vector_length = 24


# Returns a teams stats on a per-game basis
def per_game(games, total):
    return total / games


# Removes all old files so new ones can be made
def initialize(start_year, end_year, output_directory):
    for i in range(start_year, end_year):
        remove_file = output_directory+'\DataForML\data_' + str(i) + '.csv'
        os.remove(remove_file)


# Checks to see if string exists
def string_exists(this_string):
    return True if this_string.strip().strip('"') != '' else False


# Formats string so it can be recognized
def format_string(this_string):
    return float(this_string.strip().strip('"'))


# Append team data to corresponding output file based on year
def append_data_point(output_file, school_num, seed, data_point):
    string_to_write = [str(school_num)]
    string_to_write.append(str(seed))
    for i in data_point:
        string_to_write.append(str(i))
    string_to_write = ','.join(string_to_write)
    string_to_write = string_to_write + '\n'
    with open(output_file, 'a') as z:
        z.write(string_to_write)


def get_data(start_year, end_year, mm_seeds, base_directory):

    initialize(start_year, end_year, base_directory)

    # Only need data pertaining to the teams that made the tournament. This function finds those teams
    with open(mm_seeds) as f:
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

            this_mm_stats = mm_stats+str(season)+'.csv'
            this_rating_stats = rating_stats+str(season)+'.csv'
            this_conference_stats = conference_stats+str(season)+'.csv'

            with open(base_directory+this_mm_stats) as a:
                bxs = a.readlines()
                for bx in bxs:
                    _, school_name1, games_played, wins, _, _, _, _, _, _, _, _, _, _, _, _, _, _, fgm, _, fgp, \
                    threem, _, threep, ftm, _, ftp, orb, trb, ast, stl, blk, tov, pf = bx.split(',')
                    school_name1 = school_name1.strip('"').replace(' NCAA', '')
                    if school_name1 == team_name:
                        # Create a function that removes all the '"'s, white-space from a string
                        games_played = format_string(games_played)
                        wins = format_string(wins)
                        fgm = per_game(games_played, format_string(fgm))
                        fgp = format_string(fgp)
                        threem = per_game(games_played, format_string(threem))
                        threep = format_string(threep)
                        ftm = per_game(games_played, format_string(ftm))
                        ftp = format_string(ftp)
                        orb = per_game(games_played, format_string(orb)) if string_exists(orb) else 0
                        trb = per_game(games_played, format_string(trb)) if string_exists(trb) else 0
                        ast = per_game(games_played, format_string(ast))
                        stl = per_game(games_played, format_string(stl))
                        blk = per_game(games_played, format_string(blk))
                        tov = per_game(games_played, format_string(tov)) if string_exists(tov) else 0
                        pf = per_game(games_played, format_string(pf)) if string_exists(pf) else 0

                        data_point = assign_1(data_point, games_played, wins, fgm, fgp, threem, threep, ftm, ftp, orb,
                                              trb, ast, stl, blk, tov, pf)

            # Gets some other statistics for teams not covered in the function above
            with open(base_directory+this_rating_stats) as b:
                cxs = b.readlines()
                for cx in cxs:
                    _, school_name2, conference1, _, _, _, ppg, oppg, _, _, sos, _, osrs, dsrs, _, ortg, drtg, _ = \
                        cx.split(',')
                    school_name2 = school_name2.strip('"')
                    if school_name2 == team_name:
                        ppg = format_string(ppg)
                        oppg = format_string(oppg) if string_exists(oppg) else 0
                        sos = format_string(sos)
                        osrs = format_string(osrs)
                        dsrs = format_string(dsrs)
                        ortg = format_string(ortg) if string_exists(ortg) else 0
                        drtg = format_string(drtg) if string_exists(drtg) else 0

                        data_point = assign_2(data_point, ppg, oppg, sos, osrs, dsrs, ortg, drtg)

            # Imports data on the team's conference to infer how strong of a conference they play in
            with open(base_directory+this_conference_stats) as b:
                dxs = b.readlines()
                for dx in dxs:
                    conference2, winner, runner_up = dx.split(',')
                    winner = winner.strip()
                    runner_up = runner_up.strip()
                    data_point[22] = 1 if team_name == winner else 0
                    data_point[23] = 1 if team_name == runner_up else 0

            # Append data to output file based on corresponding year
            this_out_file = base_directory+'\DataForML\data_'+season+'.csv'
            append_data_point(this_out_file, school_num, seed, data_point)
