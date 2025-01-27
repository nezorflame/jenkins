#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print(f"Usage: {argv[0]} <codename>")
    exit(1)

testers = {
    'berkeley': ['srisurya95'],
    'beryllium': ['akhilnarang', 'grewal', 'gr0ndpa', 'Rokban', 'LucentW'],
    'bullhead': ['anirudhgupta109', 'Skittles8923'],
    'cheeseburger': ['HydroPetro', 'fryevia', 'gotenksIN'],
    'crosshatch': ['Fire69Flame'],
    'dipper': ['argraur'],
    'dumpling': ['divadsn', 'HydroPetro'],
    'enchilada': ['anirudhgupta109', 'ohayoubaka', 'MrWilsonxD'],
    'fajita': ['nezorflame', 'ironhydee', 'gautamhans1'],
    'jasmine_sprout': ['Artsarino', 'pqhaz', 'kenny3fcb'],
    'kiwi': ['coldhans'],
    'mata': ['KuranKaname', 'Y45HW4N7'],
    'mido': ['Adesh15'],
    'oneplus3': ['HydroPetro', 'theshinybeast', 'nezorflame'],
    'platina': ['nysadev'],
    'potter': ['NickvBokhorst', 'Deadpool_61'],
    'wayne': ['DarkAmy', 'muumen'],
    'whyred': ['iwantz', 'raiadventures', 'ahmed_tohamy', 'Sanchith_Hegde', 'anunaym14', 'bohrabhijeet', 'ZTR23'],
    'x2': ['moto999999'],
    'z2_plus': ['Pavan_Paps', 'panicker666'],
    'zl1': ['Gabronog', 'LucentW']
}

device = argv[1]

message = ""

if device in testers.keys():
    for tester in testers[device]:
        message += f'@{tester} '
    print(message)
else:
    print(f"Wrong device {device}(?)")
