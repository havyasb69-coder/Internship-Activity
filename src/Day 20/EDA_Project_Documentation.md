# Customer Analytics -- Exploratory Data Analysis (EDA) Project Documentation

## 1. Introduction

This project performs Exploratory Data Analysis (EDA) on a customer
analytics dataset containing demographic and behavioral attributes such
as Age, Gender, City, Education, Marital Status, Annual Income, Spending
Score, online activity, and purchase history.\
Each row represents a unique customer identified by `CustomerID`.

The objective of this project is to understand the structure, quality,
and relationships in the data before applying any machine learning or
advanced analytics. This supports customer segmentation and business
decision-making.

------------------------------------------------------------------------

## 2. Tools & Libraries Used

-   **Python 3.x**
-   **Pandas** -- data loading & manipulation
-   **NumPy** -- numerical operations
-   **Matplotlib** -- plotting
-   **Seaborn** -- statistical visualization
-   **Jupyter Notebook** -- interactive analysis

### Installation

``` bash
pip install pandas numpy matplotlib seaborn
```

------------------------------------------------------------------------

## 3. Phase 1: The Detective Work (Setup & Inspection)

**Goal:** Understand the context and structure of the raw data.

### Steps

1.  Create a notebook: `MiniProject1_EDA.ipynb`
2.  Load dataset using Pandas
3.  Inspect using `.head()`, `.info()`, `.describe()`

### Code

``` python
import pandas as pd

df = pd.read_csv("customer_data.csv")
df.head()
df.info()
df.describe()
```

### Outcome

-   Identified dataset shape and column types\
-   Found missing values in `Education` and `AnnualIncome`

------------------------------------------------------------------------

## 4. Phase 2: The Cleanup (Data Preprocessing)

**Goal:** Transform raw data into a reliable foundation for analysis.

### Steps

-   Identify missing values with `.isnull().sum()`
-   Impute missing values
-   Remove duplicate rows

### Code

``` python
# Missing values
df.isnull().sum()

# Imputation
df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].median())
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])

# Remove duplicates
df = df.drop_duplicates()
```

### Justification

-   Median used for income to reduce outlier impact\
-   Mode used for categorical education values\
-   Duplicates removed to avoid biased results

------------------------------------------------------------------------

## 5. Phase 3: The Deep Dive (Univariate & Bivariate Analysis)

**Goal:** Uncover distributions and relationships between features.

### Univariate Plots

``` python
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Age'], kde=True)
plt.title("Distribution of Customer Age")
plt.show()

sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

sns.histplot(df['AnnualIncome'], kde=True)
plt.title("Annual Income Distribution")
plt.show()
```

**Observations** - Customers mostly in working-age range\
- Gender fairly balanced\
- Income right-skewed with outliers

### Bivariate Plots

``` python
sns.scatterplot(x='Age', y='AnnualIncome', data=df)
plt.title("Age vs Annual Income")
plt.show()

sns.boxplot(x='Education', y='SpendingScore', data=df)
plt.xticks(rotation=45)
plt.title("Spending Score by Education")
plt.show()
```

**Observations** - Income rises with age until mid-career\
- Higher education shows slightly higher spending

------------------------------------------------------------------------

## 6. Phase 4: The Big Picture (Multivariate & Storytelling)

**Goal:** Synthesize findings into a cohesive narrative.

### Correlation Heatmap

``` python
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

### Insights

-   Online visits correlate with purchase frequency\
-   Income relates to spending behavior\
-   Age correlates with years employed

------------------------------------------------------------------------

## 7. Executive Summary (Top 3 Insights)

1.  **Digital engagement drives sales:** More online visits → more
    purchases.\
2.  **Income shapes spending:** Higher income → higher spending score
    and purchase amount.\
3.  **Life-stage patterns are realistic:** Age and years employed
    strongly correlate.

------------------------------------------------------------------------

## 8. Conclusion & Next Steps

The dataset is cleaned and suitable for: - Customer segmentation
(K-Means clustering)\
- Spending prediction (regression)\
- Marketing strategy optimization

------------------------------------------------------------------------

## 9. Final Checklist

-   Notebook runs top-to-bottom\
-   All phases completed\
-   Visualizations included\
-   Executive summary added
