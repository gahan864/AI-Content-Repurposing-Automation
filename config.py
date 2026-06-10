"""
Configuration file containing SQL queries for the AI Report Automation tool.
"""

QUERIES = {
    "total_revenue": """
        SELECT SUM(revenue) as total_revenue FROM sales
    """,
    
    "revenue_by_region": """
        SELECT region, SUM(revenue) as revenue, SUM(units_sold) as units
        FROM sales
        GROUP BY region
        ORDER BY revenue DESC
    """,
    
    "revenue_by_product": """
        SELECT product, SUM(revenue) as revenue, AVG(revenue) as avg_daily_revenue
        FROM sales
        GROUP BY product
        ORDER BY revenue DESC
    """,
    
    "top_campaign_by_roi": """
        SELECT campaign_id, 
               SUM(revenue) as total_revenue, 
               SUM(ad_spend) as total_spend,
               ROUND((SUM(revenue) - SUM(ad_spend)) * 100.0 / SUM(ad_spend), 2) as roi_percent
        FROM sales
        GROUP BY campaign_id
        ORDER BY roi_percent DESC
    """,
    
    "daily_revenue_trend": """
        SELECT date, SUM(revenue) as daily_revenue
        FROM sales
        GROUP BY date
        ORDER BY date ASC
    """,
    
    "worst_performing_region": """
        SELECT region, SUM(revenue) as revenue
        FROM sales
        GROUP BY region
        ORDER BY revenue ASC
        LIMIT 1
    """
}
