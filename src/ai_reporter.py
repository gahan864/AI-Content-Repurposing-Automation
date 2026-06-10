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
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_key_here":
        return "Error: OPENAI_API_KEY not found or not set properly in .env file."
        
    client = openai.OpenAI(api_key=api_key)
    
    user_prompt = build_user_prompt(kpi_summary, anomalies)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with OpenAI API: {str(e)}"
