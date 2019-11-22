# energy_calculation.py
# coding=utf-8

def calculate_energy(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    And prints the consumption together with the name
    """
    energy = effect * time_in_microwave / 1000
    return energy

jonas_time = 2.5 / 60
jonas_energy = calculate_energy(jonas_time)

susanne_time = 4.5 / 60
susanne_energy = calculate_energy(susanne_time)

def calculate_cost(energy, price_per_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_per_kwh / 100
    return cost

jonas_time = 2.5 / 60
jonas_energy = calculate_energy(jonas_time)
jonas_cost = calculate_cost(jonas_energy)

susanne_time = 4.5 / 60
susanne_energy = calculate_energy(susanne_time)
susanne_cost = calculate_cost(susanne_energy)

j_string = "Jonas använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=jonas_energy,
    cost=jonas_cost
)
s_string = "Susanne använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=susanne_energy,
    cost=susanne_cost
)

print(j_string + "\n" + s_string)
