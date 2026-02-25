# Mini Project 1 – Exploratory Data Analysis (EDA)

## Overview
This project performs an exploratory data analysis on a customer analytics dataset. The goal is to inspect the dataset's structure, understand its variables, clean missing values, and uncover patterns and relationships through univariate, bivariate, and multivariate analyses. The insights derived can inform business decisions and marketing strategies.

## Dataset
The dataset contains information about customers, including demographic attributes and purchasing behavior. Each row represents a single customer record.

**Columns:**
- `CustomerID`: Unique identifier
- `Age`: Customer's age
- `Gender`: Male / Female
- `City`: City of residence
- `Education`: Education level (e.g., Bachelors, Masters, PhD)
- `MaritalStatus`: Single / Married
- `AnnualIncome`: Annual income (float)
- `SpendingScore`: Spending score (integer)
- `YearsEmployed`: Years employed
- `PurchaseFrequency`: Purchase frequency
- `OnlineVisitsPerMonth`: Number of online visits per month
- `ReturnedItems`: Number of returned items
- `PreferredDevice`: Preferred device (Laptop, Desktop, Mobile, Tablet)
- `LastPurchaseAmount`: Amount of last purchase

Original shape: 255 rows, 14 columns. After cleaning: 250 rows.

## Project Phases

### Phase 1 – Data Inspection
- Loaded the dataset using `pandas`.
- Viewed first few rows with `df.head()`.
- Checked data types and non‑null counts using `df.info()`.
- Reviewed basic statistics with `df.describe()`.
- Examined shape and column names.

### Phase 2 – Data Preprocessing (Cleanup)
- Identified missing values in `Education` and `AnnualIncome` (≈4.7% each).
- Filled numerical missing values with the mean.
- Filled categorical missing values with the mode.
- Detected and removed duplicate rows (5 duplicates removed).
- Verified cleaned data with `df.info()`.

### Phase 3 – Univariate and Bivariate Analysis
- **Univariate:** Histograms with KDE for `Age` and `AnnualIncome` to understand distributions.
- **Categorical:** Count plot for `Gender` to see gender composition.
- **Bivariate:** Scatter plot of `AnnualIncome` vs `SpendingScore` to explore relationship; boxplot of `SpendingScore` by gender.

### Phase 4 – Multivariate Analysis and Storytelling
- Computed a correlation matrix for numerical variables.
- Visualized correlations using a heatmap to identify strong relationships (e.g., between `Age` and `YearsEmployed`, and a negative correlation between `AnnualIncome` and `SpendingScore`).
- Summarized key insights in an executive summary.

## Key Findings
1. **Income vs Spending:** Higher income does not always imply higher spending; the scatter plot shows a wide range of spending scores across income levels.
2. **Age Distribution:** Most customers are concentrated in a specific age range, suggesting the business primarily attracts that demographic.
3. **Customer Engagement:** Variables like `PurchaseFrequency` and `OnlineVisitsPerMonth` show some correlation with spending, indicating that more engaged customers tend to spend more.
4. **Correlations:** `Age` and `YearsEmployed` are strongly positively correlated (0.98), while `AnnualIncome` and `SpendingScore` have a moderate negative correlation (-0.39).

## Technologies Used
- Python 3
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## How to Run
1. Clone this repository or download the notebook.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn jupyter