def EmptyFunction():
    pass
def removeNone(List):
    out = []
    for i in range(len(List)):
        if List[i] != None:
            out.append(List[i])
    return out

def removeNoneItem(List, item):
    out = []
    for i in range(len(List)):
        if List[i] != None and List[i] != item:
            out.append(List[i])
    return out
def lerp(a, b, t):
    return a + t * (b - a)
def lerpPoint(p0, p1, t):
    return(lerp(p0[0], p1[0], t), lerp(p0[1], p1[1], t))
def map(z, a, b, c, d):
    x = (z/(b-a))*(d-c)
    return x if x > 0 else c + x
def checkCollision(rect1_width, rect1_height, rect1_posX, rect1_posY,
                    rect2_width, rect2_height, rect2_posX, rect2_posY):
    # Calculate the sides of each rectangle
    rect1_left = rect1_posX
    rect1_right = rect1_posX + rect1_width
    rect1_top = rect1_posY
    rect1_bottom = rect1_posY + rect1_height

    rect2_left = rect2_posX
    rect2_right = rect2_posX + rect2_width
    rect2_top = rect2_posY
    rect2_bottom = rect2_posY + rect2_height

    # Check for collision
    if (rect1_left < rect2_right and
            rect1_right > rect2_left and
            rect1_top < rect2_bottom and
            rect1_bottom > rect2_top):
        return True
    else:
        return False

def checkCollisionRect(rect1, rect2):
    # Calculate the sids of each rectangle
    rect1_left = rect1.x
    rect1_right = rect1.x + rect1.width
    rect1_top = rect1.y
    rect1_bottom = rect1.y + rect1.height

    rect2_left = rect2.x
    rect2_right = rect2.x + rect2.width
    rect2_top = rect2.y
    rect2_bottom = rect2.y + rect2.height

    # Check for collision
    if (rect1_left < rect2_right and
            rect1_right > rect2_left and
            rect1_top < rect2_bottom and
            rect1_bottom > rect2_top):
        return True
    else:
        return False

def checkCollisionVector(rect1pos, rect1dim, rect2pos, rect2dim):
    # Calculate the sids of each rectangle
    rect1_left = rect1pos.x
    rect1_right = rect1pos.x + rect1dim.x
    rect1_top = rect1pos.y
    rect1_bottom = rect1pos.y + rect1dim.y

    rect2_left = rect2pos.x
    rect2_right = rect2pos.x + rect2dim.x
    rect2_top = rect2pos.y
    rect2_bottom = rect2pos.y + rect2dim.y

    # Check for collision
    if (rect1_left < rect2_right and
            rect1_right > rect2_left and
            rect1_top < rect2_bottom and
            rect1_bottom > rect2_top):
        return True
    else:
        return False
