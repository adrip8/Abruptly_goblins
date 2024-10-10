gamers = [ ]


def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)
    else:
        print('need more info')


kimberly = {'name': 'Kimberly Warner ', 'availability': ['Monday', 'Tuesday', 'Friday']  }
add_gamer(kimberly, gamers)



add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

##print(gamers)

def build_daily_frequency_table ():
    return {
        'Monday':0,
        'Tuesday':0,
        'Wednesday':0,
        'Thursday':0,
        'Friday':0,
        'Saturday':0,
        'Sunday':0
            }

count_availability = build_daily_frequency_table ()



def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability'] :
            available_frequency[day] += 1


calculate_availability(gamers, count_availability )
print(count_availability)

def find_best_night(availability_table):
    best_night = max(availability_table, key = availability_table.get)
    return best_night
    
game_night = find_best_night(count_availability)

print(game_night)

