
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership functions
energy = ctrl.Antecedent(np.arange(0, 1, 0.1), 'energy')
dist_to_base = ctrl.Antecedent(np.arange(0, 150, 10), 'dist_to_base')
comp_radius = ctrl.Consequent(np.arange(0, 61, 1), 'comp_radius')

# Custom membership functions are built interactively with a Pythonic API
energy['low'] = fuzz.trapmf(energy.universe, [-2, -1, 0.1, 0.5])
energy['medium'] = fuzz.trimf(energy.universe, [0, 0.5, 1])
energy['high'] =  fuzz.trapmf(energy.universe, [0.5, 0.9, 1.2, 1.4])

dist_to_base['close'] = fuzz.trapmf(dist_to_base.universe, [-2, -1, 10, 50] )
dist_to_base['medium'] = fuzz.trimf(dist_to_base.universe, [0, 50, 100])
dist_to_base['far'] = fuzz.trapmf(dist_to_base.universe, [50, 90, 130, 145])

comp_radius['very small'] = fuzz.trapmf(comp_radius.universe, [-2, -1, 2.5, 5])
comp_radius['small'] = fuzz.trimf(comp_radius.universe, [0, 5, 10])
comp_radius['rather small'] = fuzz.trimf(comp_radius.universe, [5, 7, 10])
comp_radius['medium small'] = fuzz.trimf(comp_radius.universe, [10, 15, 20])
comp_radius['medium'] = fuzz.trimf(comp_radius.universe, [10, 20, 30])
comp_radius['medium large'] = fuzz.trimf(comp_radius.universe, [20, 25, 30])
comp_radius['rather large'] = fuzz.trimf(comp_radius.universe, [30, 35, 40])
comp_radius['large'] = fuzz.trimf(comp_radius.universe, [30, 42, 45])
comp_radius['very large'] = fuzz.trapmf(comp_radius.universe, [40, 47, 62, 65])


# To see how these look with .view()
#energy.view()



rule1 = ctrl.Rule(energy['low'] & dist_to_base['close'], comp_radius['very small'])
rule2 = ctrl.Rule(energy['medium'] & dist_to_base['close'], comp_radius['small'])
rule3 = ctrl.Rule(energy['high'] & dist_to_base['close'], comp_radius['rather small'])
rule4 = ctrl.Rule(energy['low'] & dist_to_base['medium'], comp_radius['medium small'])
rule5 = ctrl.Rule(energy['medium'] & dist_to_base['medium'], comp_radius['medium'])
rule6 = ctrl.Rule(energy['high'] & dist_to_base['medium'], comp_radius['medium large'])
rule7 = ctrl.Rule(energy['low'] & dist_to_base['far'], comp_radius['rather large'])
rule8 = ctrl.Rule(energy['medium'] & dist_to_base['far'], comp_radius['large'])
rule9 = ctrl.Rule(energy['high'] & dist_to_base['far'], comp_radius['very large'])


radius_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

radius = ctrl.ControlSystemSimulation(radius_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)