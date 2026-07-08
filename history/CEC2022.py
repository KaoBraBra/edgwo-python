import numpy as np 

#-------fitness functions--------- 
# Zakharov function (f1)
def Zakharov(position):
    position = np.array(position)
    first_term = np.sum(position ** 2)
    second_term = 0.5 * np.sum(position)
    return first_term + second_term**2 + second_term**4

# Rosenbrock's Function (f2)
def Rosenbrock(position):
    position = np.array(position)
    return np.sum(100 * (position[:-1]**2 - position[1:])**2 + (position[1:] - 1)**2)

def Schaffer(x, y):
    return 0.5 + (1.0 * np.sin(np.sqrt(x**2 + y**2)) ** 2 - 0.5) / ((1 + 0.001 * (x**2 + y**2))**2)

# Expanded Schaffer's Function (f3)
def Expanded_Schaffer(position):
    position = np.array(position)
    return np.sum(Schaffer(position[:-1], position[1:])) + Schaffer(position[-1], position[0])

# Rastrigin function (f4)
def Rastrigin(position):
    position = np.array(position)
    return np.sum(position**2 - 10 * np.cos(2 * np.pi * position) + 10)

def w(position, index):
    return 1.0 + (position[index] - 1) / 4

# Levy Function (f5)
def Levy(position):
    position = np.array(position)
    w1 = w(position, 0)
    wd = w(position, -1)
    fitness = np.sin(np.pi * w1)
    for i in range(len(position) - 1):
        fitness += ((w(position, i) - 1)**2) * (1 + 10 * (np.sin(np.pi * w(position, i) - 1)**2))
    fitness += ((wd - 1)**2) * (1 + np.sin(2 * np.pi * wd)**2)
    return fitness 

# Bent Cigar Function (f6)
def Bent_Cigar(position):        
    position = np.array(position)
    second_term = np.sum((position[1:]) ** 2) * 1e6
    return (position[0]) ** 2 + second_term

# HGBat Function (f7)
def HGBat(position):
    position = np.array(position)
    term1 = np.sum(position ** 2)
    term2 = np.sum(position)
    return np.sqrt(abs(term1**2 - term2**2)) + (0.5 * (term1 + term2)) / len(position) + 0.5
    

# High Conditioned Elliptic Function (f8)
def High_Conditioned_Elliptic(x):
    a = 1e6
    d = len(x)
    return np.sum([a**((i - 1) / (d - 1)) * (x[i] ** 2) for i in range(d)])

def subterm(position, index):
    term = 0.0 
    for j in range(1, 33):
        term += (abs(2**j * position[index] - round(2**j * position[index]))) / 2**j
    return (1 + (index + 1) * term) ** (10 / (len(position) ** 1.2))

# Katsuura (f9)
def Katsuura(position):
    position = np.array(position)
    fitness = np.prod([subterm(position, i) for i in range(position.ndim)])
    return (10 / (len(position) ** 2)) * (fitness - 1)

# Happycat Function (f10)
def Happycat(position):
    position = np.array(position)
    term1 = np.sum(position ** 2)
    term2 = np.sum(position)
    return (abs(term1 - len(position))) ** 0.25 + (0.5 * term1 + term2) / len(position) + 0.5
#--------------------------------------------------------------------------------------------------