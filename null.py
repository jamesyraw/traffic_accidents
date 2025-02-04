import pandas as pd

def check_null_rows(csv_file):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Find rows with any NULL (NaN) values
        null_rows = df[df.isnull().any(axis=1)]
        
        if null_rows.empty:
            print("No rows with NULL values found.")
        else:
            print(f"Found {len(null_rows)} rows with NULL values:")
            print(null_rows)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    csv_file = input("Enter the path to your CSV file: ")
    check_null_rows(csv_file)
