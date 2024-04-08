import numpy as np

def newtons_law_of_cooling(T, T_env, k, dt):  
    return T - k * (T - T_env) * dt

# Example usage
T_initial = 100  # Initial temperature of the object in °C
T_env = 25  # Temperature of the surrounding environment in °C
k = 0.1  # Cooling constant
dt = 1  # Time step for simulation in seconds

# Simulate cooling for 10 time steps
for i in range(10):
    T_initial = newtons_law_of_cooling(T_initial, T_env, k, dt)
    print("Temperature after", (i + 1) * dt, "seconds:", T_initial, "°C")
