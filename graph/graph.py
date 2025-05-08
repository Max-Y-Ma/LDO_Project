import os
import pandas as pd
import matplotlib.pyplot as plt

# Use Agg backend to avoid GUI errors
plt.switch_backend('Agg')

# Function to parse CSV and create a log-scale plot
def plot_csv(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Extract axis labels from the headers
    xlabel = data.columns[0]
    ylabel = data.columns[1]

    # Extract the X and Y data
    x_values = data.iloc[:, 0].to_numpy()
    y_values = data.iloc[:, 1].to_numpy()

    # Create the plot in log-log scale
    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, linestyle='-')
    plt.xscale('log')
    
    # Set labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(os.path.splitext(csv_file)[0].replace('_', ' '))
    
    # Save and close
    output_png = os.path.splitext(csv_file)[0] + '.png'
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.close()

# Loop through all CSVs in the current directory
for file_name in os.listdir():
    if file_name.lower().endswith('.csv'):
        plot_csv(file_name)

print("Log-scale graphs generated for all CSV files.") 
