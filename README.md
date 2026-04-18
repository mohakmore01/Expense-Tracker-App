💰 Expense Tracker App: Data Science Portfolio Project

📌 Project OverviewThe Expense Tracker App is a data-driven personal finance tool designed to help users track, categorize, and visualize their spending habits. This project demonstrates an end-to-end data science workflow—from synthetic data generation and rigorous cleaning to interactive dashboard deployment—enabling better financial decision-making through actionable insights.

🚀 Key Features
Interactive Dashboard: A web-based interface built with Streamlit for real-time data exploration.

Automated Data Cleaning: Robust preprocessing scripts that standardize categories and handle missing values.

Advanced Visualizations: Dynamic bar charts, doughnut charts, and time-series line graphs for spending trends .

Synthetic Data Pipeline: A custom script to generate realistic financial transaction logs for analysis.

Financial Insights: Automatic detection of highest spending categories and monthly cash flow patterns.

🛠️ Tech Stack
Language: Python 3.x
 Data Manipulation: Pandas, NumPy Visualization: Matplotlib, Seaborn, Plotly 
 Web Framework: Streamlit 
 Expense-Tracker-App/
├── data/           # Raw (expenses.csv) and processed (cleaned_expenses.csv) data
├── images/         # High-resolution charts and dashboard snapshots for documentation 
├── notebooks/      # Jupyter notebooks for exploratory data analysis (EDA) 
├── outputs/        # Generated financial reports and summary charts 
├── src/            # Core Python scripts (Generation, Cleaning, Plotting)
├── main.py         # Entry point for the Streamlit dashboard 
└── requirements.txt # Project dependencies

⚙️ Installation & Usage

Clone the Repository:
git clone https://github.com/mohakmore01/Expense-Tracker-App.git

Set up Virtual Environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:
Bash
pip install -r requirements.txt

Run the Pipeline:
Generate Data: python src/generate_data.py
Clean Data: python src/clean_data.py
Save Plots: python src/generate_saved_plots.py

Launch the Dashboard:
Bash
streamlit run main.py

📊💡 Future Enhancements
Implementing AI-based spending predictions using machine learning.
Adding real-time bank API integration for live transaction tracking.
Developing a budgeting alert system to notify users of overspending.

Author: [Mohak Rajendra More]