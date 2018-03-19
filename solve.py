#!/usr/bin/python3

moves = [(d_x, d_y) for d_x in [-2,-1,1,2] for d_y in [-2,-1,1,2]\
                    if abs(d_x) != abs(d_y)]


#component wise addition 
add = lambda x, y : (x[0]+y[0], x[1]+y[1])


def destinations(start, tour):

    ret = [add(start, move) for move in moves]
    ret = [dest for dest in ret if 0<=dest[0]<=7 and 0<=dest[1]<=7]
    ret = [dest for dest in ret if dest not in tour]
    return ret


def metric(square, tour):
    '''will sort the permisible destinations by 
       degree(possible number of destinations)
       tremendous improvement in time'''
    return len(destinations(square, tour))


def find_tour(current_sqr, tour=[]):

    #assign to local,  not mutate
    tour = tour + [current_sqr]
    if len(tour) == 64:
        return tour
    dests = destinations(current_sqr, tour)
    dests.sort(key = lambda x: metric(x, tour))
    for square in dests:
        new_tour = find_tour(square, tour)
        if new_tour:
                return new_tour
    return None

if __name__ == '__main__':
    pass

