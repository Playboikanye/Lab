import pandas as pd
file_path = input("Enter the path of your CSV file: ")
df = pd.read_csv(file_path)
print("\nFirst five rows of the dataset:")
print(df.head())
print("\nAvailable columns:")
print(df.columns.tolist())
column_name = input("\nEnter the column name for analysis: ")
if column_name in df.columns:
    if pd.api.types.is_numeric_dtype(df[column_name]):
        total_sum = df[column_name].sum()
        mean_value = df[column_name].mean()
        std_dev = df[column_name].std()
        print(f"\n--- Data Analysis for '{column_name}' ---")
        print(f"Sum: {total_sum}")
        print(f"Mean: {mean_value}")
        print(f"Standard Deviation: {std_dev}")
    else:
        print(f"Column '{column_name}' is not numeric. Please choose a numeric column.")
else:
    print(f"Column '{column_name}' not found in the dataset.")