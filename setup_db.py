import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def setup_database():
    # Create database connection
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database='postgres',  # Connect to default database first
        user=os.getenv('DB_USER', 'lmsqltfy'),
        password=os.getenv('DB_PASSWORD', 'demo')
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'airline_delays'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE airline_delays')
    
    cursor.close()
    conn.close()
    
    # Create SQLAlchemy engine for pandas
    engine = create_engine(f'postgresql://{os.getenv("DB_USER", "lmsqltfy")}:{os.getenv("DB_PASSWORD", "demo")}@{os.getenv("DB_HOST", "localhost")}/airline_delays')
    
    # Read and import the data
    print("Reading CSV file...")
    df = pd.read_csv('Airline_Delay_Cause.csv')
    
    # Import data to PostgreSQL
    print("Importing data to PostgreSQL...")
    df.to_sql('airline_delays', engine, if_exists='replace', index=False)
    
    print("Database setup complete!")

if __name__ == '__main__':
    setup_database() 