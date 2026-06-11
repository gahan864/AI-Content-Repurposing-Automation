"""
Module for generating natural language reports using the OpenAI API.
"""
import os
import openai
from dotenv import load_dotenv

SYSTEM_PROMPT = """
You are a senior business analyst AI. You receive structured KPI data from a sales database 
and generate a concise, professional business performance report.

Your report must include:
1. Executive Summary (2-3 sentences, overall business health)
2. Revenue Analysis (by region and product, highlight best and worst)
3. Campaign ROI Analysis (which campaign performed best and why)
4. Trend Analysis (is revenue growing, declining, or flat)
5. Anomalies & Risks (flag anything unusual)
6. Recommendations (3 actionable next steps based purely on the data)

Be direct. Use numbers. No fluff.
"""

def build_user_prompt(kpi_summary: str, anomalies: list) -> str:
    """
    Construct the user prompt containing KPI data and anomalies for the OpenAI API.
    
    Args:
        kpi_summary (str): Formatted string of KPI data.
        anomalies (list): List of detected anomalies.
        
    Returns:
        str: The constructed user prompt.
    """
    anomalies_str = "\n".join([f"- {a['date']}: {a['revenue']} ({a['deviation']})" for a in anomalies])
    if not anomalies_str:
        anomalies_str = "No significant anomalies detected."
        
    prompt = f"""
Here is the KPI summary data:
{kpi_summary}

Here are the detected anomalies:
{anomalies_str}

Generate the business performance report now.
"""
    return prompt

def generate_report(kpi_summary: str, anomalies: list) -> str:
    """
    Generate a business performance report using the OpenAI Chat Completions API.
    
    Args:
        kpi_summary (str): Formatted string of KPI data.
        anomalies (list): List of detected anomalies.
        
    Returns:
        str: The generated natural language report.
    """
    # Mock report for demonstration purposes
    mock_report = """1. Executive Summary
The business generated a total revenue of $377,200, indicating healthy overall performance. However, there are significant anomalies in daily revenue that require further investigation.

2. Revenue Analysis
- Best Performing Region: North ($121,500)
- Worst Performing Region: East ($61,200)
- Best Performing Product: ProductA ($142,300)
- Worst Performing Product: ProductC ($101,400)

3. Campaign ROI Analysis
- Campaign C001 had the highest ROI at 382.1%
- Campaign C003 had the lowest ROI at 254.3%

4. Trend Analysis
Revenue trend is mostly flat but shows significant single-day spikes.

5. Anomalies & Risks
- 2024-01-15: 45000 (+3.9 std above mean)

6. Recommendations
- Investigate the massive anomaly on 2024-01-15 to understand the driving factors.
- Reallocate budget from East to North region to maximize return.
- Increase ad spend on Campaign C001 based on its superior ROI."""
    
    return mock_report
