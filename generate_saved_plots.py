import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- STEP 0: SETUP DIRECTORIES & LOAD CLEAN DATA ---
# Ensure directories exist [cite: 78-84]
os.makedirs('outputs', exist_ok=True)
os.makedirs('images', exist_ok=True)

try:
    # Adjust path if running from src or notebooks folder
    if os.getcwd().endswith('src') or os.getcwd().endswith('notebooks'):
        df = pd.read_csv('../data/cleaned_expenses.csv')
    else:
        df = pd.read_csv('data/cleaned_expenses.csv')

    # Essential conversion for time-based plotting
    df['Date'] = pd.to_datetime(df['Date'])
except FileNotFoundError:
    print("Error: 'cleaned_expenses.csv' not found. Please run your cleaning script first.")
    exit()

print("✅ Directories verified. Data loaded successfully.")
print("--- Starting image generation ---")

# --- IMAGE 1: Saving Existing KPI Dashboard Snapshot ---
# (Simulating taking a snapshot of the metrics from image_2.png)
# In a real project, you would take a browser screenshot.
# Here, we will create a text summary report instead.
with open('outputs/financial_summary_report.txt', 'w', encoding='utf-8') as f:
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    f.write(f"EXPENSE TRACKER - SNAPSHOT REPORT\n")
    f.write(f"---------------------------------\n")
    f.write(f"Total Transactions Analyzed: {len(df)}\n")
    f.write(f"Total Income Recorded:   ₹{total_income:,.2f}\n")
    f.write(f"Total Expenses Recorded: ₹{total_expense:,.2f}\n")
    f.write(f"Net Savings Pipeline:    ₹{(total_income - total_expense):,.2f}\n")
print("✅ Created 'outputs/financial_summary_report.txt'")


# --- IMAGE 2: HEATMAP (Weekday vs Hour Spending) ---
# A new, intermediate-level complexity visualization.
# (This requires that your cleaning script added a 'Weekday' column)

if 'Weekday' in df.columns:
    st_vis_2 = px.density_heatmap(
        df[df['Type'] == 'Expense'],
        x="Weekday",
        y="Category",
        z="Amount",
        histfunc="sum",
        title="Spending Density: Category vs Day of Week",
        color_continuous_scale="Viridis",
        category_orders={"Weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
    )

    # Save to IMAGES folder for README [cite: 84, 162-164]
    try:
        st_vis_2.write_image("images/density_heatmap.png", engine="kaleido")
        print("✅ New chart saved: 'images/density_heatmap.png'")
    except ValueError:
        print("Error: Saving Plotly heatmaps requires 'kaleido'. Install with `pip install kaleido`.")
else:
    print("Skipping Density Heatmap: 'Weekday' column missing from dataset.")


# --- IMAGE 3: BOXPLOT (Amount Distribution by Category) ---
# Another new visualization showing outliers and average spending per category.
st_vis_3 = px.box(
    df[df['Type'] == 'Expense'],
    x="Category",
    y="Amount",
    color="Category",
    notched=True, # Shows confidence interval
    title="Spending Distribution and Outlier Analysis by Category"
)

# Save to IMAGES folder for README [cite: 84, 161]
try:
    st_vis_3.write_image("images/boxplot_outliers.png", engine="kaleido")
    print("✅ New chart saved: 'images/boxplot_outliers.png'")
except ValueError:
    print("Error: Saving Plotly boxplots requires 'kaleido'.")


# --- IMAGE 4: SUMMARY REPORT BAR CHART (Matplotlib) ---
# Saving a summary bar chart to the outputs folder (instead of images).
# (Using Seaborn for a clean aesthetic)

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.barplot(
    data=df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum().reset_index().sort_values('Amount', ascending=False),
    x='Category',
    y='Amount',
    palette='Set2'
)
plt.title("Summary: Total Spent by Category", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("Total Amount (₹)")
plt.tight_layout()

# Save to OUTPUTS folder for a downloadable report [cite: 83, 163]
plt.savefig('outputs/category_summary_report_chart.png', dpi=150)
print("✅ Report chart saved: 'outputs/category_summary_report_chart.png'")
plt.close()

print("--- Image Generation Complete ---")