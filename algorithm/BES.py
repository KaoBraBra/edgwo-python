import numpy as np

def bes(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    Best_pos = np.zeros(dim)
    Best_score = float("inf")
    Convergence_curve = np.zeros(max_iter)

    for t in range(max_iter):
        Mean_pos = np.mean(X, axis=0)
        for i in range(N):
            X[i] = np.clip(X[i], LB, UB)
            fitness = fitness_function(X[i])
            if fitness < Best_score:
                Best_score = fitness
                Best_pos = X[i].copy()
                
        for i in range(N):
            new_X1 = Best_pos + 1.5 * np.random.rand() * (Mean_pos - X[i])
            new_X1 = np.clip(new_X1, LB, UB)
            if fitness_function(new_X1) < fitness_function(X[i]):
                X[i] = new_X1

            idx = np.random.permutation(N)
            new_X2 = X[i] + 1.5 * np.random.rand() * (X[i] - X[idx[i]])
            new_X2 = np.clip(new_X2, LB, UB)
            if fitness_function(new_X2) < fitness_function(X[i]):
                X[i] = new_X2

            new_X3 = np.random.rand() * Best_pos + 1.5 * np.random.rand() * (X[i] - Mean_pos)
            new_X3 = np.clip(new_X3, LB, UB)
            if fitness_function(new_X3) < fitness_function(X[i]):
                X[i] = new_X3

        for i in range(N):
            fit = fitness_function(X[i])
            if fit < Best_score:
                Best_score = fit
                Best_pos = X[i].copy()
                
        Convergence_curve[t] = Best_score
        
    return Convergence_curve