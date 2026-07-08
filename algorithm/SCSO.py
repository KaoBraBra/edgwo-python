import numpy as np
import math

def scso(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    Best_pos = np.zeros(dim)
    Best_score = float("inf")
    Convergence_curve = np.zeros(max_iter)

    for i in range(N):
        X[i, :] = np.clip(X[i, :], LB, UB)
        fitness = fitness_function(X[i, :])
        if fitness < Best_score:
            Best_score = fitness
            Best_pos = X[i, :].copy()

    for t in range(max_iter):
        S = 2
        rg = S - (S * t / max_iter)

        for i in range(N):
            r = rg * np.random.rand()
            R = 2 * rg * np.random.rand() - rg

            for j in range(dim):
                tetha = np.random.rand() * 2 * math.pi
                rand_pos = abs(np.random.rand() * Best_pos[j] - X[i, j])

                if abs(R) <= 1:
                    X[i, j] = Best_pos[j] - r * math.cos(tetha) * rand_pos
                else:
                    random_index = math.floor(N * np.random.rand())
                    X[i, j] = r * (X[random_index, j] - np.random.rand() * X[i, j])

            X[i, :] = np.clip(X[i, :], LB, UB)
            fitness = fitness_function(X[i, :])

            if fitness < Best_score:
                Best_score = fitness
                Best_pos = X[i, :].copy()

        Convergence_curve[t] = Best_score

    return Convergence_curve