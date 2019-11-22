#main.py
# coding=utf-8

import energy_calculation2 as jc

jonas_time = 2.5 / 60
jonas_energy = jc.calculate_energy(jonas_time)
jonas_cost = jc.calculate_cost(jonas_energy)

jonas_string = "jonas använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=jonas_energy,
    cost=jonas_cost
)
print(jonas_string)
