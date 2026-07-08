import numpy as np

def msgwo(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    Alpha_pos = np.zeros(dim)
    Alpha_score = float("inf")
    Beta_pos = np.zeros(dim)
    Beta_score = float("inf")
    Delta_pos = np.zeros(dim)
    Delta_score = float("inf")
    
    Convergence_curve = np.zeros(max_iter)
    
    for t in range(max_iter):
        for i in range(N):
            X[i, :] = np.clip(X[i, :], LB, UB)
            fitness = fitness_function(X[i, :])
            
            if fitness < Alpha_score:
                Delta_score, Delta_pos = Beta_score, Beta_pos.copy()
                Beta_score, Beta_pos = Alpha_score, Alpha_pos.copy()
                Alpha_score, Alpha_pos = fitness, X[i, :].copy()
            elif fitness < Beta_score:
                Delta_score, Delta_pos = Beta_score, Beta_pos.copy()
                Beta_score, Beta_pos = fitness, X[i, :].copy()
            elif fitness < Delta_score:
                Delta_score, Delta_pos = fitness, X[i, :].copy()

        a = 2 * (1 - (t / max_iter) ** 2)
        
        eps = 1e-10
        total_score = abs(Alpha_score) + abs(Beta_score) + abs(Delta_score) + eps
        w1 = abs(Alpha_score) / total_score
        w2 = abs(Beta_score) / total_score
        w3 = abs(Delta_score) / total_score
        
        for i in range(N):
            for j in range(dim):
                r1, r2 = np.random.rand(), np.random.rand()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * Alpha_pos[j] - X[i, j])
                X1 = Alpha_pos[j] - A1 * D_alpha
                
                r1, r2 = np.random.rand(), np.random.rand()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * Beta_pos[j] - X[i, j])
                X2 = Beta_pos[j] - A2 * D_beta
                
                r1, r2 = np.random.rand(), np.random.rand()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * Delta_pos[j] - X[i, j])
                X3 = Delta_pos[j] - A3 * D_delta
                
                X[i, j] = w1 * X1 + w2 * X2 + w3 * X3
                
        Convergence_curve[t] = Alpha_score
        
    return Convergence_curve