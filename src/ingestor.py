"""
Module for ingesting CSV data into a SQLite database.
"""
import sqlite3
import pandas as pd

def load_csv_to_sqlite(filepath: str) -> sqlite3.Connection:
    """
    Load data from a CSV file into an in-memory SQLite database.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        sqlite3.Connection: Connection object to the SQLite database.
    """
    df = pd.read_csv(filepath)
    conn = sqlite3.connect(':memory:')
    df.to_sql('sales', conn, index=False, if_exists='replace')
    return conn
