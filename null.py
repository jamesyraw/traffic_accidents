# The first step is to test for null values. The dataset appears clean, but I want to verify, so I made a Python script that will ask you to import a CSV, and will then check it for NULL and NaN values.

import pandas as pd

# Defining the function
def check_null_rows(csv_file):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Find rows with any NULL (NaN) values
        null_rows = df[df.isnull().any(axis=1)]
        
        # Output based on result. If no results found, it will say no rows found. If null values are found, it will tell you how many, and display the null rows. If an error occurs, it will print that as well.
        if null_rows.empty:
            print("No rows with NULL values found.")
        else:
            print(f"Found {len(null_rows)} rows with NULL values:")
            print(null_rows)
    except Exception as e:
        print(f"Error: {e}")

# Prompt for the path to the CSV file. Can right-click -> copy path but must remove quotations to work.
if __name__ == "__main__":
    csv_file = input("Enter the path to your CSV file: ")
    check_null_rows(csv_file)
