import pandas as pd
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt


# Remove missing, duplicate values 
def remove_na_duplicates(messy_Data):
    #check for missing values
    no_missing_values = messy_Data.isna().sum()
    print(f"\nThe number of missing values are \n{no_missing_values}.")

    #check for duplicates
    no_duplicates = messy_Data.duplicated().sum()
    print(f"\nThe number of duplicate values are {no_duplicates}.")
    
    #remove missing values and duplicates
    cleaning = messy_Data.dropna()
    cleaning = cleaning.drop_duplicates()

    return cleaning

# Change data types
def convert_data_types(cleaning):
    # check for data types
    print(f"\nInformation of cleaning dataset is \n")
    cleaning.info()

    # convert data types
    cleaning["income_groups"] = cleaning["income_groups"].astype("category")

    cleaning["gender"] = cleaning["gender"].astype(int)
    cleaning["gender"] = cleaning["gender"].astype("category")

    cleaning["age"] = cleaning["age"].astype(int)
    cleaning["year"] = cleaning["year"].astype(int)
    cleaning["population"] = cleaning["population"].astype(int)

    pd.options.display.float_format = '{:.0f}'.format
    
    # check for converted data types
    print(f"\nInformation of dataset after data type conversion is \n")
    cleaning.info()

    return cleaning

# Remove outliers values
def remove_outliers(cleaning):
    # Identify outliers using IQR
    Q1 = cleaning['population'].quantile(0.25)
    Q3 = cleaning['population'].quantile(0.75)
    IQR = Q3 - Q1

    cleaning[((cleaning['population'] < (Q1 - 1.5 * IQR)) | (cleaning['population'] > (Q3 + 1.5 * IQR)))]

    # Remove outliers using zscore
    z_scores = np.abs(stats.zscore(cleaning["population"]))
    cleaning = cleaning[z_scores <= 3]


    return cleaning

# Recategozie the data
def recategorize(cleaning):
    # Recategorize income groups
    cleaning["income_groups"] = cleaning["income_groups"].replace({"high_income_typo" : "high_income", "low_income_typo"  : "low_income", "lower_middle_income_typo" : "lower_middle_income", "upper_middle_income_typo" : "upper_middle_income"})
    # Recategorize gender
    cleaning["gender"] = cleaning["gender"].cat.rename_categories({1 : "Male", 2 : "Female", 3 : "Others"})

    print(f"\nInformation of dataset after data recategorization is \n")
    cleaning.info()

    return cleaning

def main():
    messy_Data = pd.read_csv("messy_population_data.csv")

    # Raw Data Overview
    print("\n")
    print(messy_Data.info())
    print("\n")
    print(messy_Data.describe())
    print("\n")
    print(messy_Data.nunique())

    # Data Cleaning
    data_cleaning = remove_na_duplicates(messy_Data)
    data_cleaning = convert_data_types(data_cleaning)
    data_cleaning = remove_na_duplicates(data_cleaning)
    data_cleaning = remove_outliers(data_cleaning)
    data_cleaning = recategorize(data_cleaning)

    # Cleaned Data Overview
    print(f"\nInformation of dataset after data cleaning is \n")
    print(data_cleaning.info())
    print("\n")
    print(data_cleaning.describe())
    print("\nUnique numbers of each columns after data cleaning is")
    print(data_cleaning.nunique())

    # Save to .csv file
    data_cleaning.to_csv("cleaned_population_data.csv")

main()

