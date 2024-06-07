chars = ["a","a","a","b","b","a","a"]
curr = chars[0]
curr_index = 0
curr_len = 0
for i in chars:
    if curr == i:
        curr_len += 1
    else:
        chars[curr_index] = curr
        if curr_len == 1:
            curr_index += 1
        else:
            p = str(curr_len)
            if len(p) == 1:
                chars[curr_index+1] = str(curr_len)
                curr_index += 2
            else:
                for idx, p1 in enumerate(p):
                    chars[curr_index+1+idx] = p1
                curr_index += 1 + len(p)
        curr = i
        curr_len = 1
chars[curr_index] = curr
if curr_len != 1:
    p = str(curr_len)
    if len(p) == 1:
        chars[curr_index+1] = str(curr_len)
    else:
        for idx, p1 in enumerate(p):
            chars[curr_index+1+idx] = p1

print(chars)