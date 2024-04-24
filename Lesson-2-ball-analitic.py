import matplotlib.pyplot as plt

vs = 2 # vertical speed
hs = 10 # horizontal speed
g = 10  # g - acceletarion of free falling, indeed g=9.8.....

def get_ball_y(x):
    # to avoid division by zero in the formula, let's return 0
    if x==0: return(0)

    # global vs, hs, ga

    y = (vs/hs) * x - (g*x**2) / (2*hs**2)
    return(y)

ball_x = [x/100 for x in list(range(401))]
ball_y = [get_ball_y(x) for x in ball_x]

plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal Position of Ball')
plt.ylabel('Vertical Position of Ball')

plt.plot(ball_x, ball_y)
plt.show()


