def print_left_oriented_triangle(height, symbol):
    for i in range(1, height + 1):
        print(symbol * i)

print_left_oriented_triangle(6,"*")