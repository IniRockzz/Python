row = 1

while True:
    col = 1
    while col <=5 :
        print(row*col, end=" ")
        col += 1

    print("\n")

    row += 1
    if row > 5:
        break