import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data_hora.csv')

# Convert the 'converted_date' column to datetime
df['converted_date'] = pd.to_datetime(df['converted_date'])

# Format the 'converted_date' column to 'D M Y' format
df['converted_date'] = df['converted_date'].dt.strftime('%Y %m %d')

# Save the DataFrame back to CSV
df.to_csv('myhora_converted_dates_DMY.csv', index=False)

# Print a success message
print("The dates in the 'converted_date' column have been successfully converted to 'D M Y' format and saved to 'myhora_converted_dates_DMY.csv'.")

