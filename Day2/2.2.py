"In cricket, an over consists of six deliveries a bowler bowls from one end. Create a program that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her."
"Return the value as a float, in the format overs.balls."

def calculate_overs(balls):
    overs=balls//6
    ball= balls%6
    return float(f"{overs}.{ball}")

balls=int(input("Enter number of balls:"))
result=calculate_overs(balls)
print("result:",result)
