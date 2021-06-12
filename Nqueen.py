# Hill-Climbing for N-queen

import copy
import random
N = 8

# Random Initial State
B = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    J = random.randint(0, N-1)
    B[J][i] = 1

# B = [[0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 0],
#      [1, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0, 0, 0, 0]]


def Board(B):  # Repersentaion
    for L in B:
        for i in L:
            if i == 1:
                print("Ï", end="  ")
            else:
                print("▢", end="  ")
        print("")


def Harms(B):  # Heuristic
    H = 0
    Q = []
    for j in range(N):
        for i in range(N):
            if B[i][j] == 1:
                t = [i, j]
                Q.append(t)
    if len(Q) != N:
        return -1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if Q[i][0] == Q[j][0]:
                H += 1
            if Q[i][1] == Q[j][1]:
                H += 1
            if (abs(Q[i][0]-Q[j][0]) == abs(Q[i][1]-Q[j][1])):
                H += 1
    return H


print("----Initial----")  # Print Initial State
print(Harms(B))
Board(B)

ITR = 0


def Hill_Climb(B, ITR):  # Main Function
    M = Harms(B)
    if M == 0:
        print("Final State is achived")
        print("H = ", Harms(B))
        Board(B)
        return
    T = copy.deepcopy(B)
    G = []

    for i in range(N):
        G.clear()
        for t in range(N):
            T[t][i] = 0
        for j in range(N):
            S = copy.deepcopy(T)
            S[j][i] = 1
            Y = Harms(S)
            Y = [S, Y]
            G.append(Y)
        K = min(x[1] for x in G)

        if K == M:
            ITR += 1
            if ITR > 2500:
                print(
                    "State of Plateau is achived so the \nBest Solution We Can Achieve Is")
                print("H = ", Harms(B))
                Board(B)
                return

        if K < M:
            M = K
            for p in G:
                if p[1] == K:
                    T = p[0]
                    B = copy.deepcopy(T)
                    break
            if K == 0:
                print(
                    "Final State is achived")
                print("H = ", Harms(B))
                Board(B)
                return
            print(K)
            Board(B)
        else:
            T = copy.deepcopy(B)

    if M != 0:
        Hill_Climb(B, ITR)


Hill_Climb(B, ITR)
