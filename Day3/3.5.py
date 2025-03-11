"Finding the maximum difference between tuple pairs"

def difference(tuple):
    diff=float('-int')

    for i in range(len(tuple)):
        for j in range(len(tuple)):
            if i!=j:
                d=abs(tuple[i][0]-tuple[j][1])
                diff=max(diff,d)
            return diff
    tuple=[(5, 7), (2, 6), (1, 9), (1, 3)]
    print("tuple list is :",difference(tuple))
        
