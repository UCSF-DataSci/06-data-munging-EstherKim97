# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 rows
- **Columns**: 5 columns

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [object]    | [119412]  | [8]    | [Mean] |
| [age]  | [float]  |  [119495]  |  [101] |  [50.01]  |
| [gender] |  [float]  | [119811]  |  [3]  |  [1.58]  |
| [year]  |  [float]  |  [119516]  |  [169]  |  [2025.07]  |
| [population]  | [float]  | [119378]  |  [114925]   |  [1.11e+08]  |
|-------------|-----------|----------------|---------------|--------|

### Identified Issues

1. **[Missing Values]**
    - Description: Missing values found in messy_population_data.csv
    - Affected Columns: All 5 columns - income groups, age, gender, year and population - are contain missing values.
    - Example: NaN values are found in income_groups column.
    - Potential Impact: If missing values are not handled, it will cause bias and lead to invalid conclusion.

2. **[Invalid Data Type]**
   - Description: Data types for age, gender, year and population is incorrect. Gender should be categorical data type with 1 indicating male, 2 indicating female, etc. Based on the characteristics of age, year, and population, these cannot be "float", but should be integer.
   - Affected Column(s): age, gender, year and population columns
   - Example: Gender identified as "float"
   - Potential Impact: Incorrect data types will result in incorrect summary statistics.

3. **[Duplicate Values]**
    - Description: Duplicates found in messy_population_data.csv
    - Affected Columns: All columns are affected with 2960 duplicates.
    - Example: Row 1254 with values of high-income, 11.0 of age and male (and missing values in year and population) is a duplicate. 
    - Potential Impact: Duplicates will lead to misleading result, effecting quality and accuracy of the analysis.

4. **[Outlier Values]**
    - Description: Outliers identified using IQR
    - Affected Columns: Population Columns
    - Example: Row 45 with 6.78e+09 value of population was identified to be an outlier.
    - Potential Impact: Based on the outliers, it will lead to underestimation or overestimation.

5. **[Invalid Categorical Values]**
   - Description: Invalid categorical data for income_groups and gender
   - Affected Column(s): income_group and gender
   - Example: Income group column has data with "high_income_typo" or "lower_middle_income_typo" which does not fall into the categories of income groups.
   - Potential Impact: Based on the categorical groups, it will result in incorrect summary statistics or incorrect demographic analysis.



## 2. Data Cleaning Process

### Issue 1: [Missing Values]
- **Cleaning Method**: Missing values were removed using .dropna() function.
- **Implementation**:
  ```python
    cleaning = messy_Data.dropna()
  ```
- **Justification**: When dealing with missing values, removing the data containing NaN was the most suitable method. By removing the missing values, unbiased and accurate result could be obtained from consistent dataset. 
- **Impact**: 
  - Rows affected: All columns were affected, resulting in removal of 28,079 rows.

  |  Columns  |  Number of NA  |
  |-----------|----------------|
  | [income_groups] |   6306  |
  | [age]  |  6223  |
  | [gender] |  5907  |
  | [year] |  6202  |
  | [population] |  6340  |
  |--------------|------------|

  - Data distribution change: After removing missing data, there was not a big change in the data distribution except for a slight different in mean age.

  | Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [object]    | [97639]  | [8]    | [-] |
| [age]  | [float]  |  [97639]  |  [101] |  [50.04]  |
| [gender] |  [float]  | [97639]  |  [3]  |  [1.58]  |
| [year]  |  [float]  |  [97639]  |  [169]  |  [2025.12]  |
| [population]  | [float]  | [97639]  |  [94156]   |  [1.11e+08]  |
|-------------|-----------|----------------|---------------|--------|

### Issue 2: [Invalid Data Type]
- **Cleaning Method**: Using .astype() function, each columns were changed to appropriate data types.
- **Implementation**:
  ```python
    cleaning["income_groups"] = cleaning["income_groups"].astype("category")

    cleaning["gender"] = cleaning["gender"].astype(int)
    cleaning["gender"] = cleaning["gender"].astype("category")

    cleaning["age"] = cleaning["age"].astype(int)

    cleaning["year"] = cleaning["year"].astype(int)

    cleaning["population"] = cleaning["population"].astype(int)
  ```
- **Justification**: By changing to the appropriate data types, accurate summary statistics are available and correct interpretation is possible. 
- **Impact**: 
  - Rows affected: All rows and columns are affected.

    | Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [category]    | [97639]  | [8]    | [-] |
| [age]  | [integer]  |  [97639]  |  [101] |  [50.04]  |
| [gender] |  [category]  | [97639]  |  [3]  |  [-]  |
| [year]  |  [integer]  |  [97639]  |  [169]  |  [2025.12]  |
| [population]  | [integer]  | [97639]  |  [94156]   |  [1.11e+08]  |
|-------------|-----------|----------------|---------------|--------|

  - Data distribution change: Income groups and gender does not have mean or standard deviation values anymore. Data can be appropriately distinguished based on gender and income groups.

### Issue 3: [Duplicate Values]
- **Cleaning Method**: Duplicates were removed by .drop_duplicate()
- **Implementation**:
  ```python
  cleaning = cleaning.drop_duplicates()
  ```
- **Justification**: Duplicates were removed using drop_duplicate and allowed correct unique data in each columns. Using accurate and unbiased data, the conclusion will be reliable. 
- **Impact**: 
  - Rows affected: 2950 rows were affected.
  - Data distribution change: There were slight changes in the mean values of age, year and population. 


  ### Issue 4: [Outlier Value]
- **Cleaning Method**: Outliers were identified using the z-score and were removed.
- **Implementation**:
  ```python
  z_scores = np.abs(stats.zscore(cleaning["population"]))
  cleaning = cleaning[z_scores <= 3]
  ```
- **Justification**: The z-score of the "population" column was calculated using scripy zscore and were removed. After removing outliers, the data are less skewed, resulting in more accurate results. 
- **Impact**: 
  - Rows affected: The population column was affected. 
  - Data distribution change: Before removing outliers, boxplot for population column was unreadable. However; after removing outliers, the graph looked more readable and clear.


  ### Issue 5: [Invalid Categorical Values]
- **Cleaning Method**: Recategorized income groups into 3 groups (high income, low income, and low middle income) and renamed the categories for gender (male, female and others).
- **Implementation**:
  ```python
  # Recategorizing for income groups
  cleaning["income_groups"] = cleaning["income_groups"].replace({"high_income_typo" : "high_income", "low_income_typo"  : "low_income", "lower_middle_income_typo" : "lower_middle_income", "upper_middle_income_typo" : "upper_middle_income"})

  # Relabeling gender
  cleaning["gender"] = cleaning["gender"].cat.rename_categories({1 : "Male", 2 : "Female", 3 : "Others"})
  ```
- **Justification**: Income groups had various groups that can be simplified into 3 groups. After recategorizing the groups, trends between income groups became clearer. Gender was renamed to male, female and others instead of code numbers. This allows easier interpretation of the demographic.
- **Impact**: 
  - Rows affected: For income groups, groups labeled as high income typo, low income typo and lower middle income typo are affected. For gender, all genders were affected. 
  - Data distribution change: Recategorizing did not change data distribution.









## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv
- **Rows**: 94759 rows
- **Columns**: 5 columns

### Column Details

| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [category]    | [94759]  | [4]    | [-] |
| [age]  | [integer]  |  [94759]  |  [101] |  [101]  |
| [gender] |  [category]  | [94759]  |  [3]  |  [-]  |
| [year]  |  [integer]  |  [94759]  |  [169]  |  [2025]  |
| [population]  | [integer]  | [94759]  |  [93490]   |  [21894323]  |
|-------------|-----------|----------------|---------------|--------|

### Summary of Changes
- Major changes made to the dataset:
    - Handled missing values: All rows containing NaN values were removed, resulting in deletion of 28,079 rows. 
    - Data type correction: Data types were converted to appropriate data types to ensure accuracy in analysis. 
    - Removed duplicates: 2950 duplicates were dropped to maintain only unique data for analysis.
    - Removed outliers: Outliers identified using IQR and z-score were removed.
    - Recategorized data: Income groups column was recategorized into main categories and gender was relabeled using descriptive names for clarity.
- [Discuss any significant changes in data distribution]
    One of the significant changes is that the raw data contained 125718 rows of data, but has dropped to 94759 rows after data cleaning. The dataset has become smaller, but contains more consistent and accurate data without missing values, duplicates and outliers. Also, the removal of outliers and duplicates resulted in slight adjustments in mean and standard deviation of the data, especilly population. Also, after recategorizing and renaiming the columns into main groups and descriptive names, the dataset has higher clarity and is easy to interprete for analysis.
