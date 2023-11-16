# Variable Initialization
train_mass = 22680  # Mass of the train in kilograms
train_acceleration = 10  # Acceleration of the train in meters per second squared
train_distance = 100  # Distance over which the train travels in meters
bomb_mass = 1  # Mass of the bomb in kilograms

# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
  # Formula to convert Fahrenheit to Celsius
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Convert 100 degrees Fahrenheit to Celsius and print the result
f100_in_celsius = f_to_c(100)
print(f"Fahrenheit to Celsius: {f100_in_celsius} C")

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
  # Formula to convert Celsius to Fahrenheit
  f_temp = (c_temp * 9/5) + 32
  return f_temp

# Convert 0 degrees Celsius to Fahrenheit and print the result
c0_in_fahrenheit = c_to_f(0)
print(f"Celsius to Fahrenheit: {c0_in_fahrenheit} F")

# Function to calculate force
def get_force(mass, acceleration):
  # Formula for calculating force (Newton's Second Law)
  return mass * acceleration

# Calculate the force of the train and print the result
train_force = get_force(train_mass, train_acceleration)
print(f"Train Force: {train_force}") 
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function to calculate energy using mass-energy equivalence
def get_energy(mass, c = 3*10**8):
  # E=mc^2: Calculate energy
  return mass * c**2

# Calculate the energy of a 1kg bomb and print the result
bomb_energy = get_energy(bomb_mass)
print(f"Bomb Energy: {bomb_energy}")
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function to calculate work done
def get_work(mass, acceleration, distance):
  # Calculate force using get_force function
  force = get_force(mass, acceleration)
  # Work done is force times distance
  return force * distance

# Calculate the work done by the train and print the result
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"Train Work: {train_work}")
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
