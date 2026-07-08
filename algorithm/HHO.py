import numpy as np
import math

def hho(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    Rabbit_Location = np.zeros(dim)
    Rabbit_Energy = float("inf")
    
    Convergence_curve = np.zeros(max_iter)
    
    for t in range(max_iter):
        for i in range(N):
            X[i, :] = np.clip(X[i, :], LB, UB)
            fitness = fitness_function(X[i, :])
            
            if fitness < Rabbit_Energy:
                Rabbit_Energy = fitness
                Rabbit_Location = X[i, :].copy()
                
        E1 = 2 * (1 - (t / max_iter))
        
        for i in range(N):
            E0 = 2 * np.random.rand() - 1 
            Escaping_Energy = E1 * E0 
            
            if abs(Escaping_Energy) >= 1:
                q = np.random.rand()
                rand_Hawk_index = math.floor(N * np.random.rand())
                X_rand = X[rand_Hawk_index, :]
                if q < 0.5:
                    X[i, :] = X_rand - np.random.rand() * abs(X_rand - 2 * np.random.rand() * X[i, :])
                else:
                    X_mean = np.mean(X, axis=0)
                    X[i, :] = (Rabbit_Location - X_mean) - np.random.rand() * ((UB - LB) * np.random.rand() + LB)
            else:
                r = np.random.rand()
                if r >= 0.5 and abs(Escaping_Energy) < 0.5:
                    X[i, :] = Rabbit_Location - Escaping_Energy * abs(Rabbit_Location - X[i, :])
                elif r >= 0.5 and abs(Escaping_Energy) >= 0.5:
                    Jump_strength = 2 * (1 - np.random.rand()) 
                    X[i, :] = (Rabbit_Location - X[i, :]) - Escaping_Energy * abs(Jump_strength * Rabbit_Location - X[i, :])
                else:
                    X[i, :] = Rabbit_Location - Escaping_Energy * abs(Rabbit_Location - X[i, :])
                    
        Convergence_curve[t] = Rabbit_Energy
        
    return Convergence_curve