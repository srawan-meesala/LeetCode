A = [[0, 14],[6, 25],[12, 19],[13, 19],[5, 9]]
def solve(A):
    rooms = []
    A.sort(key = lambda k: k[0])
    for i, j in A:
        if not rooms:
            rooms.append(j)
            print(rooms)
        else:
            flag = False
            for p in range(len(rooms)):
                if rooms[p] <= i and not flag:
                    rooms[p] = j
                    print(rooms)
                    flag = True
            if not flag:
                rooms.append(j)
                print(rooms)
    print(rooms)
    return len(rooms)
print(solve(A))