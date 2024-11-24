import time
import random
# Initial thresholds and default levels
HIGH_THRESHOLD = 80     # High server load percentage threshold
MEDIUM_THRESHOLD = 50   # Medium server load percentage threshold
HIGH_TEMP = 30          # High temperature threshold (°C)
# Initial levels for cooling and power
cooling_level = "default"
power_level = "default"
# Function to predict future load based on recent activity
def predict_load(recent_activity_data):
    # Simulate load prediction by averaging recent activity
    avg_load = sum(recent_activity_data) / len(recent_activity_data)
    return avg_load
# Function to adjust cooling level
def adjust_cooling(level):
    if level == "HIGH":
        print("Setting cooling to high.")
    elif level == "MEDIUM":
        print("Setting cooling to medium.")
    else:
        print("Setting cooling to low.")
# Function to adjust power level
def adjust_power(level):
    if level == "BALANCED":
        print("Setting power to balanced.")
    elif level == "MODERATE":
        print("Setting power to moderate.")
    else:
        print("Setting power to reduced.")
# Main function to run the energy optimization loop
def energy_optimization():
    global cooling_level, power_level
    recent_activity_data = [random.randint(30, 90) for _ in range(5)]  # Simulate initial server activity data
    while True:
        # Step 1: Collect data
        current_activity = random.randint(30, 90)  # Simulate real-time server load
        external_temp = random.randint(20, 40)     # Simulate real-time external temperature
        recent_activity_data.append(current_activity)      
        # Keep only recent 5 activity data points
        if len(recent_activity_data) > 5:
            recent_activity_data.pop(0)
        # Step 2: Predict future load
        predicted_load = predict_load(recent_activity_data)   
        # Step 3: Adjust cooling and power based on load and temperature
        if predicted_load > HIGH_THRESHOLD or external_temp > HIGH_TEMP:
            cooling_level = "HIGH"
            power_level = "BALANCED"
        elif predicted_load > MEDIUM_THRESHOLD:
            cooling_level = "MEDIUM"
            power_level = "MODERATE"
        else:
            cooling_level = "LOW"
            power_level = "REDUCED"
        # Step 4: Execute adjustments
        adjust_cooling(cooling_level)
        adjust_power(power_level)
        # Step 5: Log data for analysis
        print(f"Activity: {current_activity}% | Temp: {external_temp}°C | Predicted Load: {predicted_load:.2f}%")
        print(f"Cooling: {cooling_level} | Power: {power_level}\n")
        # Wait for the next cycle (simulate delay)
        time.sleep(2)
# Run the energy optimization simulation
energy_optimization()
