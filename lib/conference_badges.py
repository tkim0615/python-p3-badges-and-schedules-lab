import ipdb
def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # badge_batch = list()                                      #for loop
    # for i in names:
    #     badge_batch.append(f'Hello, my name is {i}.')
    # return badge_batch
    badge_batch =[f'Hello, my name is {i}.' for i in names]      # list constructor
    return badge_batch


# index = animals.index('dog')

def assign_rooms(names):
    # room_list = []  #for loop
    # for name in names:
    #     index= names.index(name)
    #     room_list.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    # return room_list
    room_list = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]  #list constructor
    return room_list


def printer(names):
    list=batch_badge_creator(names)
    for name in list:
        print(name)

    list2=assign_rooms(names)
    for name in list2:
        print(name)

printer(['ty', 'tptptp'])

