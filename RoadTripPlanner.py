print("===============================")
print("Welcome to the Road Trip Planner!")
print("===============================")

traveler_name = input("What is your name? ")

destination = input("Where are you traveling?")

one_way_miles = float(input("How many miles is the one-way trip? "))

miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))

gas_price = float(input("What is the price of gas per gallon? "))

number_of_travelers = int(input("How many travelers are going? "))

total_miles = one_way_miles * 2

gallons_needed = total_miles / miles_per_gallon

gas_cost = gallons_needed * gas_price

cost_per_traveler = gas_cost / number_of_travelers

print(f"traveler: [{traveler_name.upper()}]")
print(f"destination: [{destination.upper()}]")
print(f"total miles: [{total_miles}]")
print(f"gas cost: [${gas_cost:.2f}]")
print(f"cost per traveler: [${cost_per_traveler:.2f}]")

print("================================")
print("TRIP SUMMARY")
print("================================")
print(f"Traveler: {traveler_name.upper()}")
print(f"Destination: {destination}")
print(f"Gallons of Gas: {gallons_needed:.2f}")
print(f"Gas Cost: ${gas_cost:.2f}")
print(f"Cost per Traveler: ${cost_per_traveler:.2f}")
print("================================")
print("Have a great trip!")