paths = [["A","Z"]]

    linear = [i for arr in paths for i in arr]

    count = {}

    for idx, val in enumerate(linear):
        if val not in count:
            count.__setitem__(val, idx)
        else:
            count.__delitem__(val)

    for k in count.keys():
        if count[k]%2 == 1:
        print(k)
        quit(23)