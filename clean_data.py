import pandas as pd
import os

def clean_expense_data():
    # Set paths [cite: 79-82]
    input_path = 'data/expenses.csv'
    output_path = 'data/cleaned_expenses.csv'

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Run generate_data.py first.")
        return

    # Load raw dataset [cite: 236]
    df = pd.read_csv(input_path)
    
    # Step 1: Remove duplicates [cite: 237]
    df = df.drop_duplicates()
    
    # Step 2: Handle missing values by dropping incomplete rows [cite: 237]
    df = df.dropna(subset=['Date', 'Amount', 'Category', 'Type'])
    
    # Step 3: Convert data types for analysis [cite: 237]
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    
    # Step 4: Standardize text (Title Case) to group categories correctly [cite: 237]
    df['Category'] = df['Category'].astype(str).str.strip().str.title()
    df['Type'] = df['Type'].astype(str).str.strip().str.title()
    
    # Step 5: Feature Engineering (Create columns for trends) [cite: 238]
    df['Month'] = df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    
    # Save the cleaned file [cite: 238]
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_expense_data()