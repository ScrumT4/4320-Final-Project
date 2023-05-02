def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def get_empty_seating_chart():
    chart = [['O', 'O', 'O', 'O'] for row in range(12)]
    return chart

def make_ticket(name):
    course = "INFOTC4320"
    name_character_list = split_name(name)
    course_character_list = split_name(course)

    ticket = ""

    if len(name_character_list) < len(course_character_list):
        for i in range(len(name_character_list)):
            ticket += name_character_list[i] + course_character_list[i]
        else: 
            for j in range(len(course_character_list) - i - 1):
                ticket += course_character_list[j + i + 1]


    elif len(name_character_list) > len(course_character_list):
        for i in range(len(course_character_list)):
            ticket += name_character_list[i] + course_character_list[i]
        else: 
            for j in range(len(name_character_list) - i - 1):
                ticket += name_character_list[j + i + 1]

                
    elif len(name_character_list) == len(course_character_list):
        for i in range(len(name_character_list)):
            ticket += name_character_list[i] + course_character_list[i]

    print(ticket)
    return ticket
        
def split_name(name):
    return [char for char in name]

def get_login_dict():
    f = open("passcodes.txt", "r")
    f_contents_list = f.readlines()
    f.close()

    logins = dict()

    for t in f_contents_list:
        split_t  = t.split(', ')
        logins[split_t[0]] = split_t[1].replace("\n", "")

    return logins

def get_reservations_list():
    f = open("reservations.txt", "r")
    f_contents_list = f.readlines()
    f.close()

    reservations = list()

    for r in f_contents_list:
        single_reservation_data = []

        split_t  = r.split(', ')

        single_reservation_data.append(split_t[0])
        single_reservation_data.append(split_t[1])
        single_reservation_data.append(split_t[2])
        single_reservation_data.append(split_t[3].replace('\n', ''))

        reservations.append(single_reservation_data)

    return reservations

def generate_seating_chart():
    chart = get_empty_seating_chart()

    reservations = get_reservations_list()

    for r in reservations:
        chart[int(r[1])][int(r[2])] = 'X'

    return chart

def get_sales():
    sales = 0

    cost_matrix = get_cost_matrix()
    chart = generate_seating_chart()

    for i in range(len(chart)):
        for j in range(len(chart[i])):
            if chart[i][j] == 'X':
                sales += cost_matrix[i][j]

    return sales

def make_reservation(first_name, row, seat, e_ticket):
    reservation_string = first_name + ', ' + row + ', ' + seat + ', ' + e_ticket + "\n"

    append_to_reservations_document(reservation_string)

def append_to_reservations_document(string):
    f = open('reservations.txt', 'a')
    f.write(string)
    f.close()


