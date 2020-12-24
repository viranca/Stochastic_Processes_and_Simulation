"""
prob matrix drone
p_{x_{t+1}|x_{t}}
    [0      0   0   1   0       0       0   0]
    [0      0   .5  0   .5      0       0   0]
    [0      .5  0   0   0       .5      0   0]
    [1/3    0   0   0   1/3     0       1/3 0]
    [0      1/3 0   1/3 0       0       0   1/3]
    [0      0   1   0   0       0       0   0]
    [0      0   0   .5  0       0       0.5 0]
    [0      0   0   0   .5      0       .5  0]
"""
P = [[0,0,0,1,0 ,0,0,0],
    [0,0,0.5,0,0.5,0,0,0],
    [0,0.5,0,0,0,0.5,0,0],
    [1/3,0,0,0,1/3,0,1/3,0],
    [0,1/3,0,1/3,0,0,0,1/3],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0.5,0,0,0.5,0],
    [0,0,0,0,0.5,0,0.5,0]]

for i in range(8):
    probx4x3 = P[4][i]
    #print("x4=",i+1,"probx4|x3=5",probx4x3)
    for j in range(8):
        for k in range(8):
            if P[j][3] ==0:
                P[i][j] =

        if P[j][3] !=0:
            probx5x4x3 = P[i][j]*probx4x3
            for k in range(8):
                if k == 3:
                    probx6x5x4x3 = P[j][k] * probx5x4x3
                    if probx6x5x4x3 != 0:
                        print("x6=", k + 1,"x5=",j+1, "x4=", i + 1, "p=", probx6x5x4x3)

for i in range(8):
    probx4x3 = P[4][i]
    # print("x4=",i+1,"probx4|x3=5",probx4x3)
    for j in range(8):
        if P[j][3] != 0:
            probx5x4x3 = P[i][j] * probx4x3
            for k in range(8):
                if k == 3:
                    probx6x5x4x3 = P[j][k] * probx5x4x3
                    if probx6x5x4x3 != 0:
                        print("x6=", k + 1, "x5=", j + 1, "x4=", i + 1, "p=", probx6x5x4x3)



