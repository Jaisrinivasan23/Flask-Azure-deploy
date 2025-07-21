# Replace these values with your actual Azure SQL DB details
DB_CONFIG = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=tcp:your-sql-server-name.database.windows.net,1433;'
    'DATABASE=flaskdb;'
    'UID=yourusername@your-sql-server-name;'
    'PWD=yourpassword;'
    'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
)
