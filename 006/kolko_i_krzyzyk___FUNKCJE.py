


def pole(x,y):

    if x>100 and x<200:
        if y>100 and y<200:
            return 1
        if y>200 and y<300:
            return 2
        if y>300 and y<400:
            return 3
    if x>200 and x<300:
        if y>100 and y<200:
            return 4
        if y>200 and y<300:
            return 5
        if y>300 and y<400:
            return 6
    if x>300 and x<400:
        if y>100 and y<200:
            return 7
        if y>200 and y<300:
            return 8
        if y>300 and y<400:
            return 9
    else:
        return 0