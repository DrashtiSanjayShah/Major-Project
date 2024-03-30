import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split

# Database connection details
db_host = "5432"
db_user = "postgres"
db_password = "2002"
db_name = "BankChrun"

# Connect to the database
conn = psycopg2.connect(host=db_host, user=db_user, password=db_password, database=db_name)

# SQL query
sql = "SELECT RowNumber, CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance,	NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited from major"
 

# Execute query and fetch data
cursor = conn.cursor()
cursor.execute(sql)
data = cursor.fetchall()

# Create Pandas DataFrame
df = pd.DataFrame(data, columns=["RowNumber", "CustomerId", "Surname", "CreditScore", "Geography", "Gender", "Age", "Tenure", "Balance", "NumOfProduct", "HasCrCard", "IsActiveMember", "EstimatedSalary", "Exited" ])

# Preprocess data (example: handle missing values)
# df.fillna(df.mean(), inplace=True)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[["RowNumber", "CustomerId", "Surname", "CreditScore", "Geography", "Gender", "Age", "Tenure", "Balance", "NumOfProduct", "HasCrCard", "IsActiveMember", "EstimatedSalary"]], df["Exited"], test_size=0.2)

# Train your ML model using X_train and y_train


# Evaluate model performance on X_test and y_test
# ...

# Close the database connection
cursor.close()
conn.close()
