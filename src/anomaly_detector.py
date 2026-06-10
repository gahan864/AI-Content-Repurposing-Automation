"""
Module for detecting anomalies in daily revenue data.
"""
import sqlite3
import pandas as pd
from config import QUERIES

def detect_anomalies(conn: sqlite3.Connection) -> list[dict]:
    """
    Detect statistical anomalies in daily revenue using z-score logic.
    Anomalies are flagged if they deviate more than 1.5 standard deviations from the mean.
    
    Args:
        conn (sqlite3.Connection): SQLite database connection.
        
    Returns:
        list[dict]: List of dictionaries containing anomaly details (date, revenue, deviation).
    """
    df = pd.read_sql_query(QUERIES['daily_revenue_trend'], conn)
    
    mean_revenue = df['daily_revenue'].mean()
    std_revenue = df['daily_revenue'].std()
    
    anomalies = []
    
    # Avoid division by zero if std is zero
    if std_revenue == 0:
        return anomalies
        
    for _, row in df.iterrows():
        date = row['date']
        revenue = row['daily_revenue']
        
        z_score = (revenue - mean_revenue) / std_revenue
        
        if abs(z_score) > 1.5:
            direction = "+" if z_score > 0 else "-"
            deviation = f"{direction}{abs(z_score):.1f} std {'above' if z_score > 0 else 'below'} mean"
            anomalies.append({
                "date": date,
                "revenue": revenue,
                "deviation": deviation
            })
            
    return anomalies
