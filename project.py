import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/marico_historicals.csv")
    return df

def calculate_metrics(df):
    df = df.copy()

    df["revenue_growth"] = df["revenue_from_operations"].pct_change()

    df["ebitda"] = (
        df["profit_before_tax"]
        + df["finance_costs"]
        + df["depreciation_amortisation"]
        - df["other_income"]
    )
    df["ebitda_margin"] = df["ebitda"] / df["revenue_from_operations"]

    df["ebit"] = df["ebitda"] - df["depreciation_amortisation"]

    df["effective_tax_rate"] = df["income_tax_expense"] / df["profit_before_tax"]

    df["nopat"] = df["ebit"] * (1 - df["effective_tax_rate"])

    df["operating_nwc"] = (
        df["inventories"]
        + df["trade_receivables"]
        - df["trade_payables"]
    )

    df["change_in_nwc"] = df["operating_nwc"].diff()

    df["fcff"] = (
        df["nopat"]
        + df["depreciation_amortisation"]
        - df["capex"]
        - df["change_in_nwc"]
      )

    return df

def summarize_performance(df):
    years = len(df) - 1

    revenue_cagr = (
        (df["revenue_from_operations"].iloc[-1] /
        df["revenue_from_operations"].iloc[0]) ** (1 / years) - 1
    )
    ebitda_cagr = (
        (df["ebitda"].iloc[-1] /
        df["ebitda"].iloc[0]) ** (1 / years) - 1
    )
    summary = {
        "Revenue CAGR": revenue_cagr,
        "EBITDA CAGR": ebitda_cagr,
        "Average EBITDA Margin": df["ebitda_margin"].mean(),
        "Latest EBITDA Margin": df["ebitda_margin"].iloc[-1]
    }
    return summary

def plot_metrics(df):
    plt.figure(figsize=(8, 5))
    plt.plot(df["fiscal_year"], df["revenue_from_operations"], marker="o")
    plt.title("Marico Revenue Trend")
    plt.xlabel("Financial Year")
    plt.ylabel("Revenue (₹ Cr)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/revenue_trend.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.plot(df["fiscal_year"], df["ebitda_margin"] * 100, marker="o")
    plt.title("Marico EBITDA Margin Trend")
    plt.xlabel("Financial Year")
    plt.ylabel("EBITDA Margin (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/ebitda_margin.png")
    plt.close()

def main():
    df = load_data()

    df = calculate_metrics(df)

    print("\nMARICO LIMITED - HISTORICAL FINANCIAL ANALYSIS\n")

    columns = [
        "fiscal_year",
        "revenue_from_operations",
        "revenue_growth",
        "ebitda",
        "ebitda_margin",
        "ebit",
        "nopat",
        "operating_nwc",
        "fcff"
    ]
    print(df[columns].round(2).to_string(index=False))

    df.to_csv("output/marico_historical_analysis.csv", index=False)
    print("\nAnalysis exported successfully!")

    plot_metrics(df)

if __name__ == "__main__":
    main()
