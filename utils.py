# Used to sync up certain school names and team IDs, as some IDs return inconsistent team names
def fix_teamname(name, num):
    name = name.split()
    for i, item in enumerate(name):
        if item == 'St' and i != 0:
            name[i] = 'State'
        if item == 'St' and i == 0:
            name[i] = 'St.'
            name.append('(NY)')
        if item == 'Univ':
            name[i] = 'University'
        if item == 'TX':
            name[i] = 'Texas'
        if item == 'Intl':
            name[i] = 'International'
    name = ' '.join(name)
    if num == 1335:
        name = 'Pennsylvania'
    if num == 1143:
        name = 'University of California'
    if num == 1140:
        name = 'Brigham Young'
    if num == 1374:
        name = "Saint Mary's (CA)"
    if num == 1261:
        name = 'Louisiana State'
    if num == 1356:
        name = 'Southern Illinois'
    if num == 1443:
        name = 'Western Kentucky'
    if num == 1419:
        name = 'Louisiana-Monroe'
    if num == 1203:
        name = 'George Washington'
    if num == 1380:
        name = 'Southern'
    if num == 1157:
        name = 'Coastal Carolina'
    if num == 1412:
        name = 'Alabama-Birmingham'
    if num == 1418:
        name = 'Louisiana-Lafayette'
    if num == 1416:
        name = 'Central Florida'
    if num == 1387:
        name = 'Saint Louis'
    if num == 1299:
        name = 'North Carolina A&T'
    if num == 1453:
        name = 'Green Bay'
    if num == 1259:
        name = 'Loyola (MD)'
    if num == 1158:
        name = 'College of Charleston'
    if num == 1389:
        name = "Saint Peter's"
    if num == 1275:
        name = 'Miami (OH)'
    if num == 1291:
        name = "Mount St. Mary's"
    if num == 1284:
        name = 'Monmouth'
    if num == 1296:
        name = 'Northern Illinois'
    if num == 1290:
        name = 'Mississippi Valley State'
    if num == 1433:
        name = 'Virginia Commonwealth'
    if num == 1422:
        name = 'North Carolina-Greensboro'
    if num == 1185:
        name = 'Eastern Michigan'
    if num == 1354:
        name = 'South Carolina State'
    if num == 1441:
        name = 'Western Carolina'
    if num == 1254:
        name = 'Long Island University'
    if num == 1425:
        name = 'Southern California'
    if num == 1149:
        name = 'Charleston Southern'
    if num == 1386:
        name = "Saint Joseph's"
    if num == 1388:
        name = "Saint Mary's (CA)"
    if num == 1227:
        name = 'Illinois-Chicago'
    if num == 1424:
        name = 'Nevada-Las Vegas'
    if num == 1192:
        name = 'Fairleigh Dickinson'
    if num == 1395:
        name = 'Texas Christian'
    if num == 1178:
        name = 'Detroit Mercy'
    if num == 1444:
        name = 'Western Michigan'
    if num == 1274:
        name = 'Miami (FL)'
    if num == 1245:
        name = 'Kent State'
    if num == 1427:
        name = 'Texas-San Antonio'
    if num == 1423:
        name = 'North Carolina-Wilmington'
    if num == 1382:
        name = 'St. Bonaventure'
    if num == 1148:
        name = 'Central Connecticut State'
    if num == 1369:
        name = 'Southeast Missouri State'
    if num == 1169:
        name = 'Cal State Northridge'
    if num == 1183:
        name = 'Eastern Illinois'
    if num == 1322:
        name = 'Northwestern State'
    if num == 1301:
        name = 'North Carolina State'
    if num == 1194:
        name = 'Florida Atlantic'
    if num == 1364:
        name = 'UC-Santa Barbara'
    if num == 1190:
        name = 'East Tennessee State'
    if num == 1421:
        name = 'North Carolina-Asheville'
    if num == 1141:
        name = 'Central Michigan'
    if num == 1454:
        name = 'Milwaukee'
    if num == 1431:
        name = 'Texas-El Paso'
    if num == 1186:
        name = 'Eastern Washington'
    if num == 1368:
        name = 'Southeastern Louisiana'
    if num == 1184:
        name = 'Eastern Kentucky'
    if num == 1107:
        name = 'Albany (NY)'
    if num == 1394:
        name = 'Texas A&M-Corpus Christi'
    if num == 1110:
        name = 'American'
    if num == 1168:
        name = 'Cal State Fullerton'
    if num == 1420:
        name = 'Maryland-Baltimore County'
    if num == 1426:
        name = 'Texas-Arlington'
    if num == 1372:
        name = 'Stephen F. Austin'
    if num == 1295:
        name = 'North Dakota State'
    if num == 1115:
        name = 'Arkansas-Pine Bluff'
    if num == 1294:
        name = 'Northern Colorado'
    if num == 1114:
        name = 'Arkansas-Little Rock'
    if num == 1379:
        name = 'Southern Mississippi'
    if num == 1355:
        name = 'South Dakota State'
    if num == 1195:
        name = 'Florida Gulf Coast'
    if num == 1292:
        name = 'Middle Tennessee'
    if num == 1300:
        name = 'North Carolina Central'
    if num == 1142:
        name = 'Cal Poly'
    if num == 1414:
        name = 'UC-Irvine'
    if num == 1167:
        name = 'Cal State Bakersfield'
    if num == 1297:
        name = 'Northern Kentucky'
    if num == 1205:
        name = 'Gardner-Webb'
    if num == 1101:
        name = 'Abilene Christian'
    return name


# Returns the school's id
def get_team_id(this_school_num):
    with open('data\Team_IDs.csv') as h:
        exs = h.readlines()
        for ex in exs:
            num, this_team_name = ex.split(',')
            if num == 'Team_Id':
                continue
            num = int(num)
            if this_school_num == num:
                return this_team_name
    return False


# Assigns data to an np.array
def assign_1(data_point, games_played, wins, fgm, fgp, threem, threep, ftm, ftp, orb, trb,
             ast, stl, blk, tov, pf):
    data_point[0] = games_played
    data_point[1] = wins
    data_point[2] = fgm
    data_point[3] = fgp
    data_point[4] = threem
    data_point[5] = threep
    data_point[6] = ftm
    data_point[7] = ftp
    data_point[8] = orb
    data_point[9] = trb
    data_point[10] = ast
    data_point[11] = stl
    data_point[12] = blk
    data_point[13] = tov
    data_point[14] = pf
    return data_point


# Assigns data to an np.array
def assign_2(data_point, ppg, oppg, sos, osrs, dsrs, ortg, drtg):
    data_point[15] = ppg
    data_point[16] = oppg
    data_point[17] = sos
    data_point[18] = osrs
    data_point[19] = dsrs
    data_point[20] = ortg
    data_point[21] = drtg
    return data_point
