def calculate_overs(balls):
    overs=balls//6
    ball= balls%6
    return float(overs.ball)

balls=int(input("Enter number of balls:"))
result=calculate_overs(balls)
print("result:",result)
