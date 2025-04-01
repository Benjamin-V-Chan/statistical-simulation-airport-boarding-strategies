import os
import pandas as pd

def main():
    results_path = os.path.join("outputs", "simulation_results.csv")
    df = pd.read_csv(results_path)
    
    summary = df.groupby("Strategy")["Total_Time"].agg(['mean', 'median', 'std']).reset_index()
    summary.rename(columns={'mean': 'Mean_Time', 'median': 'Median_Time', 'std': 'Std_Dev'}, inplace=True)
    
    os.makedirs("outputs", exist_ok=True)
    summary.to_csv(os.path.join("outputs", "analysis_results.csv"), index=False)
    print(summary)

if __name__ == '__main__':
    main()