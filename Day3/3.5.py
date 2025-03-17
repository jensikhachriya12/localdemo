"Finding the maximum difference between tuple pairs"

def max_difference(tup):
    max_diff = float('-inf')  
    
    for i in range(len(tup)):
        for j in range(len(tup)):
            if i != j:  
                diff = abs(tup[i][0] - tup[j][1])
                max_diff = max(max_diff, diff)
    
    return max_diff


tupList = [(5, 7), (2, 6), (1, 9), (1, 3)]
print("Output:", max_difference(tupList))

