import time
import random
import matplotlib.pyplot as plt
from collections import deque

# Define thresholds for load and temperature
HIGH_LOAD_THRESHOLD = 80         # Load threshold for high usage (%)
MEDIUM_LOAD_THRESHOLD = 50       # Load threshold for medium usage (%)
HIGH_TEMPERATURE_THRESHOLD = 30  # Temperature threshold for high cooling needs (°C)

# Define cooling and power settings
cooling_level = "Default"
power_level = "Default"

# History data for graph
time_steps = deque(maxlen=20)  # Keep only the last 20 time steps
cooling_levels = deque(maxlen=20)
power_levels = deque(maxlen=20)
server_loads = deque(maxlen=20)
external_temps = deque(maxlen=20)

# Function to predict future server load based on recent activity
def predict_future_load(recent_activity):
    # Predictive model: here we use a simple average of recent activity data
    average_load = sum(recent_activity) / len(recent_activity)
    return average_load

# Function to adjust cooling level based on predicted load and temperature
def adjust_cooling(predicted_load, external_temp):
    global cooling_level
    if predicted_load > HIGH_LOAD_THRESHOLD or external_temp > HIGH_TEMPERATURE_THRESHOLD:
        cooling_level = "High"
    elif predicted_load > MEDIUM_LOAD_THRESHOLD:
        cooling_level = "Medium"
    else:
        cooling_level = "Low"

# Function to adjust power level based on predicted load
def adjust_power(predicted_load):
    global power_level
    if predicted_load > HIGH_LOAD_THRESHOLD:
        power_level = "Balanced"  # Distribute power evenly
    elif predicted_load > MEDIUM_LOAD_THRESHOLD:
        power_level = "Moderate"  # Reduce power to non-critical servers
    else:
        power_level = "Reduced"  # Minimize power to inactive servers

# Function to log and collect data for plotting
def log_and_collect_data(time_step, cooling_level, power_level, current_load, external_temp, predicted_load):
    time_steps.append(time_step)
    cooling_levels.append(cooling_level)
    power_levels.append(power_level)
    server_loads.append(current_load)
    external_temps.append(external_temp)

# Function to convert cooling and power levels to numeric values for plotting
def level_to_numeric(level, level_type="cooling"):
    mapping = {"High": 3, "Medium": 2, "Low": 1, "Balanced": 3, "Moderate": 2, "Reduced": 1}
    return mapping.get(level, 0)

# Function to plot data
def plot_data():
    plt.clf()
    plt.subplot(2, 1, 1)
    plt.plot(time_steps, server_loads, label="Server Load (%)", color="blue")
    plt.plot(time_steps, external_temps, label="External Temp (°C)", color="orange")
    plt.ylabel("Load/Temp")
    plt.legend(loc="upper left")
    
    plt.subplot(2, 1, 2)
    plt.plot(time_steps, [level_to_numeric(cl, "cooling") for cl in cooling_levels], label="Cooling Level", color="green")
    plt.plot(time_steps, [level_to_numeric(pl, "power") for pl in power_levels], label="Power Level", color="red")
    plt.xlabel("Time Steps")
    plt.ylabel("Levels")
    plt.legend(loc="upper left")

    plt.tight_layout()
    plt.pause(0.1)  # Pause to update the graph

# Main function to manage energy optimization cycle
def energy_optimization_cycle():
    # Initialize recent activity data (simulate recent load history)
    recent_activity_data = [random.randint(30, 90) for _ in range(5)]
    time_step = 0

    plt.ion()  # Enable interactive mode for live updating
    plt.figure(figsize=(10, 6))

    while True:
        # Step 1: Collect current server activity and external temperature
        current_load = random.randint(30, 90)  # Simulate real-time server load percentage
        external_temp = random.randint(20, 40) # Simulate real-time external temperature in °C

        # Update recent activity data with the current load
        recent_activity_data.append(current_load)
        if len(recent_activity_data) > 5:
            recent_activity_data.pop(0)  # Keep only the last 5 readings

        # Step 2: Predict future load
        predicted_load = predict_future_load(recent_activity_data)

        # Step 3: Adjust cooling and power based on predictions and temperature
        adjust_cooling(predicted_load, external_temp)
        adjust_power(predicted_load)

        # Step 4: Log data for monitoring and analysis
        log_and_collect_data(time_step, cooling_level, power_level, current_load, external_temp, predicted_load)

        # Step 5: Plot data
        plot_data()

        # Increment time step and wait before the next cycle
        time_step += 1
        time.sleep(2)  # Simulate delay

# Run the energy optimization simulation with live graph
energy_optimization_cycle()
