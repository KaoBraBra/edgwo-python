import numpy as np
import math

def chgwosca(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    P_best = X.copy()
    P_best_score = np.full(N, float("inf"))
    
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
            
            if fitness < P_best_score[i]:
                P_best_score[i] = fitness
                P_best[i, :] = X[i, :].copy()
                
            if fitness < Alpha_score:
                Delta_score, Delta_pos = Beta_score, Beta_pos.copy()
                Beta_score, Beta_pos = Alpha_score, Alpha_pos.copy()
                Alpha_score, Alpha_pos = fitness, X[i, :].copy()
            elif fitness < Beta_score:
                Delta_score, Delta_pos = Beta_score, Beta_pos.copy()
                Beta_score, Beta_pos = fitness, X[i, :].copy()
            elif fitness < Delta_score:
                Delta_score, Delta_pos = fitness, X[i, :].copy()

        a = 2 * (1 - math.sin((math.pi / 2) * (t / max_iter)))
        
        for i in range(N):
            for j in range(dim):
                r2, r3, r4 = 2 * math.pi * np.random.rand(), 2 * np.random.rand(), np.random.rand()
                if r4 < 0.5:
                    X1 = Alpha_pos[j] - a * math.sin(r2) * abs(r3 * Alpha_pos[j] - X[i, j])
                else:
                    X1 = Alpha_pos[j] - a * math.cos(r2) * abs(r3 * Alpha_pos[j] - X[i, j])
                    
                r2, r3, r4 = 2 * math.pi * np.random.rand(), 2 * np.random.rand(), np.random.rand()
                if r4 < 0.5:
                    X2 = Beta_pos[j] - a * math.sin(r2) * abs(r3 * Beta_pos[j] - X[i, j])
                else:
                    X2 = Beta_pos[j] - a * math.cos(r2) * abs(r3 * Beta_pos[j] - X[i, j])
                    
                r2, r3, r4 = 2 * math.pi * np.random.rand(), 2 * np.random.rand(), np.random.rand()
                if r4 < 0.5:
                    X3 = Delta_pos[j] - a * math.sin(r2) * abs(r3 * Delta_pos[j] - X[i, j])
                else:
                    X3 = Delta_pos[j] - a * math.cos(r2) * abs(r3 * Delta_pos[j] - X[i, j])
                
                X_new = (X1 + X2 + X3) / 3.0
                
                if np.random.rand() < 0.5:
                    X[i, j] = X_new
                else:
                    w = np.random.rand()
                    X[i, j] = w * P_best[i, j] + (1 - w) * X_new
                    
        Convergence_curve[t] = Alpha_score
        
    return Convergence_curve