# Marico Limited – Python Financial Analytics

## Description

This project is a Python-based financial analysis of Marico Limited, covering its consolidated historical financial performance from FY2023 to FY2026.

The objective is to apply Python programming to financial statement analysis and demonstrate how programming can be used to process financial data, calculate important financial metrics, analyse business performance and generate visualisations.

The project uses Pandas for financial data processing and calculations, and Matplotlib for creating financial charts. Instead of manually calculating every metric, the program processes the historical financial dataset and produces a structured analysis that can be reproduced whenever the underlying data is updated.

The project complements a separate Excel financial modelling and DCF valuation exercise. Excel remains the primary tool for forecasting and valuation, while Python is used for historical financial analysis and data visualisation.

## Features

- Historical consolidated financial data analysis for FY2023–FY2026.
- Automated calculation of revenue growth and profitability metrics.
- EBITDA, EBITDA margin, EBIT and NOPAT calculations.
- Working capital analysis, including operating NWC and changes in NWC.
- Free Cash Flow to Firm (FCFF) calculation.
- Revenue CAGR and EBITDA CAGR calculations.
- Historical profitability analysis.
- Revenue and EBITDA margin trend charts.
- Export of calculated financial metrics into a CSV file.
- Automated testing using pytest.

## Functions

The project contains five functions in `project.py`:

**1. load_data()**

Uses Pandas to read the historical financial data from `marico_historicals.csv` and load it into a DataFrame.

**2. calculate_metrics()**

Calculates financial metrics including revenue growth, EBITDA, EBITDA margin, EBIT, effective tax rate, NOPAT, operating net working capital, change in NWC and FCFF.

The FCFF calculation follows:

FCFF = NOPAT + Depreciation and Amortisation - Capital Expenditure - Change in NWC

**3. summarize_performance()**

Calculates historical performance indicators, including revenue CAGR, EBITDA CAGR, average EBITDA margin and the latest EBITDA margin.

**4. plot_metrics()**

Uses Matplotlib to generate revenue and EBITDA margin trend charts. The charts are saved as PNG files in the output directory.

**5. main()**

Coordinates the execution of the program by loading the data, calculating financial metrics, displaying the results, exporting the processed dataset and generating visualisations.
