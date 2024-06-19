def solve(difficulty, profit, worker):
    jobs = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
    jobs.sort()
    worker.sort()
    print(jobs)
    j, max_profit, res = 0, 0, 0
    for i in worker:
        while i>=jobs[j][0] and j<len(jobs):
            max_profit = max(max_profit, jobs[j][1])
            j += 1
        print(max_profit)
        res += max_profit
    return res

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(solve(difficulty, profit, worker))