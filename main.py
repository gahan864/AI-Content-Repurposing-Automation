"""
Main entry point for the AI Report Automation CLI.
"""
import argparse
import os
from src import ingestor, analyzer, anomaly_detector, ai_reporter

def main():
    """
    Main function to parse arguments and run the report generation workflow.
    """
    parser = argparse.ArgumentParser(description="AI-Powered Business Report Automation")
    parser.add_argument("--input", type=str, default="data/sales_data.csv", help="Path to input CSV data")
    parser.add_argument("--output", type=str, default="output/report.txt", help="Path to save the generated report")
    
    args = parser.parse_args()
    
    print(f"Loading data from {args.input}...")
    try:
        conn = ingestor.load_csv_to_sqlite(args.input)
    except Exception as e:
        print(f"Failed to load data: {e}")
        return
        
    print("Running SQL queries...")
    results = analyzer.run_all_queries(conn)
    kpi_string = analyzer.build_kpi_summary_string(results)
    
    print("Detecting anomalies...")
    anomalies = anomaly_detector.detect_anomalies(conn)
    
    print("Running AI analysis...")
    report = ai_reporter.generate_report(kpi_string, anomalies)
    
    print("\n--- GENERATED REPORT ---\n")
    print(report)
    print("\n------------------------\n")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
