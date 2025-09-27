import pandas as pd
import sqlite3

# Step 1: Read the Excel file
excel_file_path = 'your_excel_file.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file_path)

# Step 2: Connect to the SQLite database (or create it if it doesn't exist)
sqlite_db_path = 'your_sqlite_db.db'  # Replace with your SQLite database path
conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()

# Step 3: Create a table in the SQLite database
# Assuming your DataFrame has columns: 'column1', 'column2', 'column3', etc.
table_name = 'your_table_name'  # Replace with your table name

# Generating SQL statement for creating table based on DataFrame columns
create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    {', '.join([f'{col} TEXT' for col in df.columns])}
);
'''
cursor.execute(create_table_query)

# Step 4: Insert data from the DataFrame into the SQLite database
# Convert DataFrame to a list of tuples
data_tuples = [tuple(x) for x in df.to_numpy()]

# Generating SQL statement for inserting data
placeholders = ', '.join(['?' for _ in df.columns])
insert_query = f'INSERT INTO {table_name} VALUES ({placeholders})'

# Executing the insertion
cursor.executemany(insert_query, data_tuples)

# Committing the transaction
conn.commit()

# Closing the connection
conn.close()
