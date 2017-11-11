
def get_value(l, r, c):
    return l[r][c]

def find(l, x):
    m = len(1) - 1
    n = len(1[0]) - 1
    r = 0
    c = n
    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1
        return False