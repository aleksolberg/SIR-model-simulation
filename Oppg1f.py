import random
import numpy as np
import matplotlib.pyplot as plt

Y_0 = [950, 50, 0]
population = 1000
steps = 300

gamma = 0.10
alpha = 0.01

Y = np.zeros((steps, 3), int)
Y[0] = Y_0


def make_step(pop, chance):     # Calculates new infected, susceptible or recovered
    counter = 0
    for i in range(pop):
        roll = random.uniform(0, 1)
        if roll <= chance:
            counter += 1
    return counter


for n in range(steps - 1):
    beta = (0.5 * Y[n, 1]) / population     # Update probability of getting infected each step
    new_I = make_step(Y[n, 0], beta)
    new_R = make_step(Y[n, 1], gamma)
    new_S = make_step(Y[n, 2], alpha)

    Y[n + 1, 0] = Y[n, 0] + new_S - new_I
    Y[n + 1, 1] = Y[n, 1] + new_I - new_R
    Y[n + 1, 2] = Y[n, 2] + new_R - new_S

print(Y)
print(np.max(Y[0:steps, 1]), np.argmax(Y[0:steps, 1]))

plt.figure()
lineObjects = plt.plot(Y)
plt.legend(iter(lineObjects), ('Susceptible', 'Infected', 'Recovered'))
plt.ylim(0, population)
plt.xlim(0, steps)
plt.ylabel('Population')
plt.xlabel('Step')
plt.show()