def df_dx(f, x, y, h):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def df_dy(f, x, y, h):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)






