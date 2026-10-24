
import random
import math

def objective(x):
    return x * x

def simulated_annealing():
    current = random.uniform(-10, 10)
    best = current
    temperature = 100.0
    cooling_rate = 0.95

    while temperature > 0.01:
        neighbor = current + random.uniform(-1, 1)

        delta = (
            objective(neighbor) - objective(current)
        )

        if delta < 0:
            current = neighbor
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbor

        if objective(current) < objective(best):
            best = current

        temperature *= cooling_rate

    return best


answer = simulated_annealing()

print("Best solution x:", round(answer, 4))
print("Minimum value:", round(objective(answer), 6))
