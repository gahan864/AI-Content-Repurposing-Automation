"""
Module for executing SQL queries on the SQLite database to extract KPIs.
"""
import sqlite3
import pandas as pd
from config import QUERIES

def run_all_queries(conn: sqlite3.Connection) -> dict:
    """
    Execute all predefined SQL queries to extract key performance indicators (KPIs).
    
    Args:
        conn (sqlite3.Connection): SQLite database connection.
        
    Returns:
        dict: A dictionary where keys are query names and values are formatted string results.
    """
    results = {}
    for query_name, query_sql in QUERIES.items():
        df = pd.read_sql_query(query_sql, conn)
        results[query_name] = df.to_string(index=False)
    return results

def build_kpi_summary_string(results: dict) -> str:
    """
    Build a single formatted string that concatenates all query results.
    
    Args:
        results (dict): Dictionary of query results from run_all_queries.
        
    Returns:
        str: Formatted KPI summary string.
    """
    summary_parts = []
    for query_name, result_str in results.items():
        title = query_name.replace('_', ' ').upper()
        summary_parts.append(f"=== {title} ===\n{result_str}\n")
    return "\n".join(summary_parts)
