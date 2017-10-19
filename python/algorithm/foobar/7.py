def reflect(point, line):
    """reflect a point according line
    line is horizontal or vertical
    
    Arguments:
        point {tuple} -- (1,2)
        line {dict} -- {'x':3}
    """
    if 'x' in line:
        return (2*line['x']-point[0], point[1])
    if 'y' in line:
        return (point[0], 2*line['y']-point[1])
    assert False

def conjuection(p1, p2, line):
    """if the connection from point1 to point2 across line segment
    line is horizontal or vertical and starts from coordinate line
    
    Arguments:
        point {tuple} -- (1,2)
        line {dict} -- {'x':2,'l':3}
    """
    if 'x' in line:
        if p1[0] < line['x'] and p2[0] < line['x'] or p1[0] > line['x'] and p2[0] > line['x']:
            return false
        if p2[1] > p1[1]:
            

def answer(dimensions, captain_position, badguy_position, distance):
    # your code here