# import ipdb

def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # list_names = []
    # for name in names:
    #     list_names.append(badge_maker(name))
    # return list_names
    names= [badge_maker(name) for name in names]
    return names

def assign_rooms(names):
    list = []
    for i in range(len(names)):
        list.append(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')
    return list
# def assign_rooms(names):
#     rooms = range(1, 9)
    
#     assignments = []
#     for room in rooms:
#         assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
#     return assignments
# print(assign_rooms(['s','ee','esss','s','ee','ess','s','ee']))

def printer(names):
    list_badge= batch_badge_creator(names)
    for name in list_badge:
        print (name)
    list_rooms = assign_rooms(names)  
    for name in list_rooms:
        print(name)

# def printer(names):
#     for badge in batch_badge_creator(names):          # function returns list so can run for loop directly
#         print(badge)
    
#     for assignment in assign_rooms(names):
#         print(assignment)
    
























# def badge_maker(name):
#     return f'Hello, my name is {name}.'

# def batch_badge_creator(names):
#     # badge_batch = list()                                      #for loop
#     # for i in names:
#     #     badge_batch.append(f'Hello, my name is {i}.')
#     # return badge_batch
#     badge_batch =[f'Hello, my name is {i}.' for i in names]      # list constructor
#     return badge_batch


# # index = animals.index('dog')

# def assign_rooms(names):
#     # room_list = []  #for loop
#     # for name in names:
#     #     index= names.index(name)
#     #     room_list.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
#     # return room_list
#     room_list = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]  #list constructor
#     return room_list


# def printer(names):
#     list=batch_badge_creator(names)
#     for name in list:
#         print(name)

#     list2=assign_rooms(names)
#     for name in list2:
#         print(name)

# printer(['ty', 'tptptp'])

