# Data Summary Report: `customer_analytics.csv`

## 1. Overview
- **Number of rows:** 250 (after deduplication, original file may contain duplicates; see below)
- **Number of columns:** 14

## 2. Column Information

| Column                | Non-Null Count | Dtype   | Missing Values | Missing % |
|-----------------------|----------------|---------|----------------|-----------|
| CustomerID            | 250            | int64   | 0              | 0.0%      |
| Age                   | 250            | int64   | 0              | 0.0%      |
| Gender                | 250            | object  | 0              | 0.0%      |
| City                  | 250            | object  | 0              | 0.0%      |
| Education             | 238            | object  | 12             | 4.8%      |
| MaritalStatus         | 250            | object  | 0              | 0.0%      |
| AnnualIncome          | 238            | float64 | 12             | 4.8%      |
| SpendingScore         | 250            | int64   | 0              | 0.0%      |
| YearsEmployed         | 250            | int64   | 0              | 0.0%      |
| PurchaseFrequency     | 250            | int64   | 0              | 0.0%      |
| OnlineVisitsPerMonth  | 250            | int64   | 0              | 0.0%      |
| ReturnedItems         | 250            | int64   | 0              | 0.0%      |
| PreferredDevice       | 250            | object  | 0              | 0.0%      |
| LastPurchaseAmount    | 250            | int64   | 0              | 0.0%      |

## 3. Duplicate Rows
- **Number of duplicate rows:** 5  
  Duplicates were identified and removed for the purpose of this summary. The row counts above reflect the deduplicated dataset (250 rows). The original file contained 255 rows.

## 4. Descriptive Statistics (Numeric Columns)

| Statistic        | CustomerID        | Age          | AnnualIncome     | SpendingScore  | YearsEmployed  | PurchaseFrequency | OnlineVisitsPerMonth | ReturnedItems  | LastPurchaseAmount |
|------------------|-------------------|--------------|------------------|----------------|----------------|-------------------|----------------------|----------------|---------------------|
| count            | 250.0             | 250.0        | 238.0            | 250.0          | 250.0          | 250.0             | 250.0                | 250.0          | 250.0               |
| mean             | 1126.94           | 37.73        | 74499.90         | 45.72          | 14.68          | 11.57             | 16.08                | 1.86           | 2795.07             |
| std              | 72.40             | 9.77         | 43939.86         | 17.87          | 9.65           | 7.08              | 7.91                 | 1.41           | 1328.77             |
| min              | 1001.0            | 21.0         | 16062.0          | 5.0            | 1.0            | 1.0               | 3.0                  | 0.0            | 566.0               |
| 25%              | 1064.5            | 29.0         | 56353.0          | 34.5           | 6.0            | 5.0               | 10.0                 | 1.0            | 1542.5              |
| 50% (median)     | 1128.0            | 38.0         | 69629.0          | 47.0           | 15.0           | 11.0              | 16.0                 | 2.0            | 2705.0              |
| 75%              | 1190.5            | 46.0         | 84030.5          | 57.5           | 23.0           | 18.0              | 23.0                 | 3.0            | 4001.0              |
| max              | 1250.0            | 54.0         | 474327.0         | 95.0           | 34.0           | 24.0              | 29.0                 | 4.0            | 4996.0              |

## 5. Notes on Missing Values
- **Education** and **AnnualIncome** each have 12 missing values (≈4.8% of rows).  
- These missing values are relatively few; depending on the analysis, they could be imputed (e.g., mode for Education, mean/median for AnnualIncome) or rows with missing values could be dropped.

## 6. Data Quality Observations
- All columns have appropriate data types.
- No unexpected negative values or outliers were detected in numeric columns (though AnnualIncome shows a wide range with a maximum of 474,327, which may be a legitimate high‑income customer).
- Duplicate records were present and have been accounted for.

---

*Report generated using pandas.*