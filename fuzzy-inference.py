import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Define the output variable
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define the membership functions for the input variables
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['warm'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['hot'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['comfortable'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['humid'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Define the membership functions for the output variable
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define the rules
rule1 = ctrl.Rule(temperature['cold'] & humidity['dry'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['comfortable'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['cold'] & humidity['humid'], fan_speed['high'])
rule4 = ctrl.Rule(temperature['warm'] & humidity['dry'], fan_speed['medium'])
rule5 = ctrl.Rule(temperature['warm'] & humidity['comfortable'], fan_speed['medium'])
rule6 = ctrl.Rule(temperature['warm'] & humidity['humid'], fan_speed['high'])
rule7 = ctrl.Rule(temperature['hot'] & humidity['dry'], fan_speed['medium'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['comfortable'], fan_speed['high'])
rule9 = ctrl.Rule(temperature['hot'] & humidity['humid'], fan_speed['high'])

# Define the control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Define the simulation
simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Set the input values
simulation.input['temperature'] = 70
simulation.input['humidity'] = 40

# Compute the output value
simulation.compute()

# Print the output value
print(simulation.output['fan_speed'])
