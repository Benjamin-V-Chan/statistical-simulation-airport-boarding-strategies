import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    results_path = os.path.join("outputs", "simulation_results.csv")
    df = pd.read_csv(results_path)
    
    os.makedirs("outputs", exist_ok=True)
    
    # Boxplot: Total boarding times by Strategy
    plt.figure()
    df.boxplot(column="Total_Time", by="Strategy")
    plt.title("Boarding Time Distribution by Strategy")
    plt.suptitle("")
    plt.xlabel("Boarding Strategy")
    plt.ylabel("Total Boarding Time (seconds)")
    boxplot_path = os.path.join("outputs", "boxplot.png")
    plt.savefig(boxplot_path)
    plt.close()
    
    # Bar chart: Mean boarding times by Strategy
    mean_times = df.groupby("Strategy")["Total_Time"].mean().reset_index()
    plt.figure()
    plt.bar(mean_times["Strategy"], mean_times["Total_Time"])
    plt.title("Mean Boarding Time by Strategy")
    plt.xlabel("Boarding Strategy")
    plt.ylabel("Mean Boarding Time (seconds)")
    barchart_path = os.path.join("outputs", "barchart.png")
    plt.savefig(barchart_path)
    plt.close()

if __name__ == '__main__':
    main()
