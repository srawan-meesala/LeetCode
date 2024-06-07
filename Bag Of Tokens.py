tokens = [100,200,300,400]
power = 200

def bag(tokens, power):
    tokens.sort()
    i, j = 0, len(tokens)-1
    score = 0

    while i<j:
        if power >= tokens[i]:
            power -= tokens[i]
            score += 1
            i += 1
        else:
            if score >= 1:
                power += tokens[j]
                score -= 1                    
                j -= 1
            else:
                break
    if i==j:
        if power >= tokens[i]:
            power -= tokens[i]
            score += 1

    return score

print(bag(tokens, power))