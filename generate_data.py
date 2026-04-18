import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data(records=200):
    categories = ['Food', 'Transport', 'Bills', 'Shopping', 'Rent', 'Entertainment']
    types = ['Expense', 'Expense', 'Expense', 'Expense', 'Income', 'Expense'] # Weighted towards expenses
    
    data = []
    start_date = datetime(2024, 1, 1)

    for i in range(records):
        date = start_date + timedelta(days=np.random.randint(0, 120))
        category = np.random.choice(categories)
        transaction_type = types[categories.index(category)]
        
        # Logic for realistic amounts
        if transaction_type == 'Income':
            amount = np.random.randint(40000, 60000)
        else:
            amount = np.random.randint(100, 3000)

        data.append([date, category, f"Transaction {i}", amount, transaction_type])

    df = pd.DataFrame(data, columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
    df.to_csv('data/expenses.csv', index=False)
    print("✅ Synthetic dataset 'data/expenses.csv' created successfully!")

if __name__ == "__main__":
    generate_synthetic_data()