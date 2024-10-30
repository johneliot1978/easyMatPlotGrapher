# Description: python command line script to quicly plot a theme bar or line graph of simple delimited x & y datset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_contiguous_bar_chart(datafile, delimiter, color_theme):
    # Read the data from the provided datafile
    try:
        df = pd.read_csv(datafile, delimiter=delimiter)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Check if required columns exist
    if df.shape[1] < 2:
        print("The dataset must contain at least two columns.")
        return

    # Extract the first two columns for plotting
    x_col = df.columns[0].strip()
    y_col = df.columns[1].strip()

    # Group data for plotting
    df_grouped = df.groupby(x_col)[y_col].sum().reset_index()

    # Define bar positions and width
    x = np.arange(len(df_grouped[x_col]))
    bar_width = 0.5

    # Create a color map based on selected color theme
    if color_theme == 1:
        colors = plt.cm.Blues(np.linspace(0.3, 1, len(df_grouped)))  # Light blue gradient
        line_color = plt.cm.Blues(0.8)  # Primary color from the theme
    elif color_theme == 2:
        colors = plt.cm.Reds(np.linspace(0.3, 1, len(df_grouped)))   # Red gradient
        line_color = plt.cm.Reds(0.8)  # Primary color from the theme
    elif color_theme == 3:
        colors = plt.cm.Greens(np.linspace(0.3, 1, len(df_grouped))) # Green gradient
        line_color = plt.cm.Greens(0.8)  # Primary color from the theme
    elif color_theme == 4:
        colors = plt.cm.Purples(np.linspace(0.3, 1, len(df_grouped))) # Purple gradient
        line_color = plt.cm.Purples(0.8)  # Primary color from the theme
    elif color_theme == 5:
        colors = plt.cm.Oranges(np.linspace(0.3, 1, len(df_grouped)))  # Orange gradient
        line_color = plt.cm.Oranges(0.8)  # Primary color from the theme
    elif color_theme == 6:
        # Random colors for each bar
        colors = np.random.rand(len(df_grouped), 3)  # RGB values between 0 and 1
        line_color = np.random.rand(3)  # Random color for the line graph
    else:
        print("Invalid color theme selection.")
        return

    # Plotting Bar Chart
    plt.figure(figsize=(10, 6))
    bar_container = plt.bar(x, df_grouped[y_col], width=bar_width, color=colors)

    # Adding labels on top of bars
    for bar in bar_container:
        yval = bar.get_height()
        if yval > 0:  # Only add label if bar has height
            plt.text(
                bar.get_x() + bar.get_width() / 2,  # X position of label
                yval + 1,  # Y position of label just above the bar
                str(int(yval)),  # Text for label
                ha='center', va='bottom', fontsize=8, color='white'
            )

    plt.title(datafile)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    
    # Set the x-ticks to be the labels from the x_col with vertical rotation
    plt.xticks(x, df_grouped[x_col], rotation=90)  # Ensure labels are taken from the x_col

    plt.tight_layout()
    plt.savefig(f"{datafile}_contiguous_bar_chart.png", dpi=300)
    plt.show()

def plot_line_chart(datafile, delimiter, color_theme):
    # Read the data from the provided datafile
    try:
        df = pd.read_csv(datafile, delimiter=delimiter)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Check if required columns exist
    if df.shape[1] < 2:
        print("The dataset must contain at least two columns.")
        return

    # Extract the first two columns for plotting
    x_col = df.columns[0].strip()
    y_col = df.columns[1].strip()

    # Group data for plotting
    df_grouped = df.groupby(x_col)[y_col].sum().reset_index()

    # Determine line color based on color theme
    if color_theme == 1:
        line_color = plt.cm.Blues(0.8)  # Primary color from the theme
    elif color_theme == 2:
        line_color = plt.cm.Reds(0.8)  # Primary color from the theme
    elif color_theme == 3:
        line_color = plt.cm.Greens(0.8) # Primary color from the theme
    elif color_theme == 4:
        line_color = plt.cm.Purples(0.8) # Primary color from the theme
    elif color_theme == 5:
        line_color = plt.cm.Oranges(0.8) # Primary color from the theme
    elif color_theme == 6:
        line_color = np.random.rand(3)  # Random color for the line graph

    # Plotting Line Chart
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped[x_col], df_grouped[y_col], marker='o', linestyle='-', color=line_color)

    plt.title(datafile)
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.xticks(rotation=90)  # Rotate x-tick labels for better readability
    plt.tight_layout()
    plt.savefig(f"{datafile}_line_chart.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <datafile.csv>")
        sys.exit(1)

    datafile = sys.argv[1]

    # Prompt user for delimiter
    delimiter = input("Please enter the delimiter used in the CSV file (default is ','): ") or ','

    # Prompt user for color theme selection
    print("Please select a color theme:")
    print("1: Light Blue Gradient")
    print("2: Red Gradient")
    print("3: Green Gradient")
    print("4: Purple Gradient")
    print("5: Orange Gradient")
    print("6: Random Colors")  # Added option for random colors
    
    while True:
        try:
            color_selection = int(input("Enter a number (1-6) for your color theme: "))  # Updated range to 1-6
            if 1 <= color_selection <= 6:
                break
            else:
                print("Invalid selection. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt user for graph type selection
    print("Please select the type of graph to plot:")
    print("1: Bar Chart")
    print("2: Line Chart")
    
    while True:
        try:
            graph_selection = int(input("Enter a number (1-2) for your graph type: "))  # Updated range to 1-2
            if graph_selection in [1, 2]:
                break
            else:
                print("Invalid selection. Please enter 1 for Bar Chart or 2 for Line Chart.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Plot based on the selected graph type
    if graph_selection == 1:
        plot_contiguous_bar_chart(datafile, delimiter, color_selection)
    elif graph_selection == 2:
        plot_line_chart(datafile, delimiter, color_selection)
