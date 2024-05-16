import boto3

def read_data_from_s3(bucket_name, key):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    try:
        # Read data from S3
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = response['Body'].read().decode('utf-8')
        return data
    except Exception as e:
        print(f"Error reading data from S3: {str(e)}")
        return None

def push_to_rds(data):
    # Code to push data to RDS
    try:
        # Replace 'host', 'user', 'password', and 'database' with your RDS database credentials
        # Establish connection to RDS
        # Example using MySQL
        import pymysql
        connection = pymysql.connect(host='test.czmskym6sxaq.ap-south-1.rds.amazonaws.com',
                                     user='admin',
                                     password='aman8180',
                                     database='test',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        with connection.cursor() as cursor:
            # Example SQL query to insert data into a table
            sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
            # Replace 'your_table' and 'column1', 'column2' with your table name and columns
            # Execute the query
            cursor.execute(sql, ('value1', 'value2'))
        # Commit changes
        connection.commit()
        print("Data pushed to RDS successfully")
    except Exception as e:
        print(f"Error pushing data to RDS: {str(e)}")

def main():
    # Replace 'bucket_name' and 'key' with your S3 bucket name and file key
    bucket_name = 'bucketama'
    key = 'csv/customers-100.csv'
    
    # Read data from S3
    data = read_data_from_s3(bucket_name, key)
    
    if data:
        # Try pushing data to RDS
        push_to_rds(data)
    else:
        print("No data retrieved from S3. Exiting...")

if __name__ == "__main__":
    main()
