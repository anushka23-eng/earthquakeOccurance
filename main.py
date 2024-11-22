import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
csv_file = 'path_to_dataset.csv'  # Replace with the correct path to your CSV file
try:
    data = pd.read_csv(csv_file, encoding='utf-8')
except FileNotFoundError:
    print(f"Error: File not found at '{
          csv_file}'. Please check the file path.")
    exit()
except UnicodeDecodeError:
    print("Error: Encoding issue encountered. Try changing the encoding to 'latin-1'.")
    exit()

# Print the original column names for verification
print("Original Columns:", data.columns)

# Rename columns explicitly to English
column_mapping = {
    'continente': 'continent',
    'magnitud_media': 'average_magnitude',
    'ocurrencias': 'occurrences'
}

# Ensure the columns match the expected ones, else notify
if not all(col in data.columns for col in column_mapping.keys()):
    print("Error: The dataset does not have the expected columns. Check the dataset's structure.")
    exit()

data.rename(columns=column_mapping, inplace=True)

# Verify column names after renaming
print("Translated Dataset:")
print(data)

# Plotting a bar chart for earthquake occurrences by continent
plt.figure(figsize=(10, 6))
bars = plt.bar(data['continent'], data['occurrences'],
               color='skyblue', alpha=0.8)

# Adding bar labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
             f'{bar.get_height()}', ha='center', va='bottom', fontsize=10)

# Adding titles and labels
plt.title('Global Earthquake Occurrences by Continent', fontsize=16)
plt.suptitle('Using Simulated Earthquake Data', fontsize=10)
plt.xlabel('Continent', fontsize=12)
plt.ylabel('Number of Earthquake Occurrences', fontsize=12)
plt.xticks(rotation=30)

# Optimize layout and display the plot
plt.tight_layout()
plt.show()
