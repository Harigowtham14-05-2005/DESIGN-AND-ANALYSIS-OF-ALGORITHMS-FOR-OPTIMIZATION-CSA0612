import random
import time
import matplotlib.pyplot as plt

# Step 1: Simulate real-time data collection
def collect_traffic_data():
    # Simulate traffic data: vehicle count at different intersections
    # For simplicity, we use random values between 0 and 100 for traffic density
    return [random.randint(0, 100) for _ in range(5)]  # 5 intersections

# Step 2: Analyze traffic patterns and predict congestion
def analyze_traffic_patterns(traffic_data):
    # Predict traffic load (simple average of all intersection vehicle counts)
    predicted_load = sum(traffic_data) / len(traffic_data)
    return predicted_load

# Step 3: Adjust traffic signals based on predicted load
def adjust_traffic_signals(predicted_load, average_load=50):
    if predicted_load > average_load:
        # Increase green light duration for heavy traffic
        return "Increase green light duration"
    else:
        # Decrease or maintain normal signal timings
        return "Maintain or decrease green light duration"

# Step 4: Check for emergency vehicles (simulated)
def emergency_vehicle_detected():
    # Random chance for an emergency vehicle to be detected
    return random.choice([True, False])

# Step 5: Grant priority to emergency vehicles
def grant_priority_to_emergency_vehicle():
    return "Grant priority to emergency vehicle"

# Main program with graphing capabilities
def traffic_optimization_system():
    traffic_data_history = []
    signal_adjustment_history = []
    predicted_load_history = []

    # Simulating the system running for 10 cycles
    for cycle in range(10):
        # Step 1: Collect real-time traffic data
        traffic_data = collect_traffic_data()
        print(f"Cycle {cycle+1} - Collected traffic data: {traffic_data}")

        # Step 2: Analyze traffic data to predict congestion
        predicted_load = analyze_traffic_patterns(traffic_data)
        print(f"Cycle {cycle+1} - Predicted load: {predicted_load}")

        # Step 3: Adjust traffic signals based on the predicted load
        signal_adjustment = adjust_traffic_signals(predicted_load)
        print(f"Cycle {cycle+1} - Traffic signal adjustment: {signal_adjustment}")

        # Step 4: Handle emergency vehicle priority
        if emergency_vehicle_detected():
            priority_action = grant_priority_to_emergency_vehicle()
            print(f"Cycle {cycle+1} - Priority action: {priority_action}")

        # Store data for graphing
        traffic_data_history.append(traffic_data)
        signal_adjustment_history.append(signal_adjustment)
        predicted_load_history.append(predicted_load)

        # Simulate waiting for next cycle (5 seconds)
        time.sleep(1)

    # After all cycles, plot the graph
    plot_graph(traffic_data_history, predicted_load_history, signal_adjustment_history)

# Function to plot the traffic data and signal adjustments
def plot_graph(traffic_data_history, predicted_load_history, signal_adjustment_history):
    # Create subplots for traffic data and signal adjustment history
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot traffic data (bar graph)
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Traffic Load (Vehicles)', color='tab:blue')
    ax1.bar(range(1, len(traffic_data_history) + 1), [sum(data) for data in traffic_data_history], color='tab:blue', alpha=0.6, label="Total Traffic Load")
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second y-axis for the predicted load and signal adjustments
    ax2 = ax1.twinx()
    ax2.set_ylabel('Predicted Load and Adjustments', color='tab:green')
    ax2.plot(range(1, len(predicted_load_history) + 1), predicted_load_history, color='tab:green', label="Predicted Load", marker='o')
    ax2.set_ylim(0, 100)
    ax2.tick_params(axis='y', labelcolor='tab:green')

    # Add a legend and show the plot
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.title("Traffic Optimization in Smart City - Traffic Load and Signal Adjustments")
    plt.show()

# Start the traffic optimization system
traffic_optimization_system()
