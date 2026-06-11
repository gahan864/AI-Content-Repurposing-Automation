# AI-Powered Business Report Automation

A Python CLI tool that automates business performance reporting by loading CSV sales data into SQLite, running predefined SQL queries to extract KPIs, detecting anomalies using z-score logic, and generating a structured natural language report (currently mocked for demonstration purposes).

## Problem It Solves
Manual business reporting is slow, repetitive, and error-prone. This tool automates the entire process — from raw data ingestion to a formatted executive summary — in a single command.

## Architecture

```text
CSV Data → SQLite In-Memory DB → SQL Queries → KPI Summary + Anomalies → Mock AI Engine → Natural Language Report
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd ai-report-automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI tool by pointing it to your input CSV file and specifying an output location for the report.

```bash
python main.py --input data/sales_data.csv --output output/report.txt
```

### Sample Output

```text
Loading data from data/sales_data.csv...
Running SQL queries...
Detecting anomalies...
Running AI analysis...

--- GENERATED REPORT ---

1. Executive Summary
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
- Increase ad spend on Campaign C001 based on its superior ROI.

------------------------

Report saved to output/report.txt
```

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Database | SQLite3 (in-memory) |
| Data Processing | Pandas |
| AI / LLM | Mocked for demonstration |
| Environment | python-dotenv |
| CLI Interface | argparse |

## How the AI prompt is engineered
The tool was originally designed with a structured approach to interact with the OpenAI API (prompts remain in the code for reference):
- **System Prompt**: Sets the persona as a "senior business analyst AI" and strictly defines the output format (Executive Summary, Revenue Analysis, Campaign ROI, Trend Analysis, Anomalies, Recommendations) with instructions to be direct and use numbers.
- **User Prompt**: Dynamically injects the computed KPI summary (from SQL queries) and any statistically significant anomalies detected using z-score logic. This ensures the LLM's analysis is strictly grounded in accurate data rather than hallucinations.
