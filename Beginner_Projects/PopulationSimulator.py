import random

print("Welcome to the Population Simulator!")
initial_population = int(input("Enter the initial population: "))
growth_rate = float(input("Enter the annual growth rate (as a percentage, e.g., 5 for 5%): ")) / 100
years = int(input("Enter the number of years to simulate: "))

with open("population_simulation.txt", "w") as f:
        f.write(f"Initial Population: {initial_population}\n")
        f.write(f"Growth Rate: {growth_rate * 100}%\n")
        f.write(f"Number of Years: {years}\n")

population = initial_population
print(f"\nYear 0: Population = {population}") 
for year in range(1, years + 1):
    # Simulate random events affecting population growth
    event_chance = random.random()
    if event_chance < 0.1:  # 10% chance of a disaster reducing population by 10-30%
        disaster_impact = random.randint(10, 30) / 100
        population -= int(population * disaster_impact)
        print(f"  A disaster occurred! Population reduced by {int(disaster_impact * 100)}%.")
    elif event_chance > 0.9:  # 10% chance of a boom increasing population by 10-30%
        boom_impact = random.randint(10, 30) / 100
        population += int(population * boom_impact)
        print(f"  A population boom occurred! Population increased by {int(boom_impact * 100)}%.")
    
    # Apply growth rate
    population += int(population * growth_rate)
    print(f"Year {year}: Population = {population}")
    
    #print each year's data to file
    with open("population_simulation.txt", "a") as f:
        f.write(f"Y:{year}\t {population}\n")
print("\nSimulation complete!")


    