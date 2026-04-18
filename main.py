
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="FinTrack: AI Expense Analytics", layout="wide")

# --- STEP 1: DATA LOADING & CLEANING --- [cite: 233, 236]
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv('data/expenses.csv')
    
    # Standardize formats [cite: 237]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Category'] = df['Category'].str.strip().str.title()
    df['Type'] = df['Type'].str.strip().str.title()
    
    # Feature Engineering [cite: 238]
    df['Month'] = df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    return df

try:
    df = load_and_clean_data()
except FileNotFoundError:
    st.error("Dataset not found! Please run the data generator script first.")
    st.stop()

# --- STEP 2: SIDEBAR FILTERS --- [cite: 250]
st.sidebar.header("🔍 Filter Analytics")
selected_categories = st.sidebar.multiselect(
    "Select Categories", 
    options=df['Category'].unique(), 
    default=df['Category'].unique()
)
type_filter = st.sidebar.radio("Transaction Type", ["All", "Expense", "Income"])

# Apply Filters
filtered_df = df[df['Category'].isin(selected_categories)]
if type_filter != "All":
    filtered_df = filtered_df[filtered_df['Type'] == type_filter]

# --- STEP 3: KPI METRICS --- [cite: 246]
total_income = df[df['Type'] == 'Income']['Amount'].sum()
total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
savings = total_income - total_expense

st.title("💰 Expense Tracker Analytics")
m1, m2, m3 = st.columns(3)
m1.metric("Total Income", f"₹{total_income:,}")
m2.metric("Total Expenses", f"₹{total_expense:,}")
m3.metric("Net Savings", f"₹{savings:,}")

st.markdown("---")

# --- STEP 4: VISUALIZATIONS --- [cite: 240, 243]
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📊 Category-wise Spending")
    # Interactive Bar Chart using Plotly
    fig_bar = px.bar(
        filtered_df.groupby('Category')['Amount'].sum().reset_index(),
        x='Category', y='Amount', color='Category',
        template="seaborn"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with row1_col2:
    st.subheader("🍕 Expense Distribution")
    # Pie chart for expense breakdown [cite: 243]
    expense_data = filtered_df[filtered_df['Type'] == 'Expense']
    if not expense_data.empty:
        fig_pie = px.pie(expense_data, values='Amount', names='Category', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.write("No expense data available for selected filters.")

# --- STEP 5: TREND ANALYSIS --- 
st.subheader("📈 Monthly Cash Flow Trend")
trend_data = filtered_df.groupby([filtered_df['Date'].dt.to_period('M'), 'Type'])['Amount'].sum().reset_index()
trend_data['Date'] = trend_data['Date'].astype(str)

fig_line = px.line(trend_data, x='Date', y='Amount', color='Type', markers=True)
st.plotly_chart(fig_line, use_container_width=True)

# --- STEP 6: DATA TABLE --- [cite: 250]
if st.checkbox("Show Raw Transaction History"):
    st.dataframe(filtered_df.sort_values(by='Date', ascending=False), use_container_width=True)

# --- STEP 7: AUTOMATED INSIGHTS --- [cite: 275, 276]
st.sidebar.markdown("---")
st.sidebar.subheader("💡 Quick Insights")
top_cat = expense_data.groupby('Category')['Amount'].sum().idxmax()
st.sidebar.info(f"Your highest spending category is **{top_cat}**.")