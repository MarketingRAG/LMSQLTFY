from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px
import json
import re
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Database connection
engine = create_engine(os.getenv('DATABASE_URL'))

def clean_sql_query(sql):
    # Remove triple backticks and optional 'sql' after them
    return re.sub(r"^```sql\s*|^```|```$", "", sql, flags=re.MULTILINE).strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Get database schema information
        with engine.connect() as connection:
            result = connection.execute(text("""
                SELECT table_name, column_name, data_type 
                FROM information_schema.columns 
                WHERE table_schema = 'public'
            """))
            schema_info = result.fetchall()
        
        # Create prompt for Gemini
        prompt = f"""Given the following database schema:
        {schema_info}
        
        User question: {user_message}
        
        Please provide a SQL query to answer this question. Only return the SQL query, nothing else."""
        
        # Get SQL query from Gemini
        response = model.generate_content(prompt)
        print("Gemini response:", response)  # For debugging
        
        # Try to extract the text from the response
        try:
            sql_query = response.candidates[0].content.parts[0].text.strip()
        except Exception as e:
            print("Error extracting SQL from Gemini response:", e)
            sql_query = None
        
        if not sql_query:
            raise Exception("Failed to extract SQL query from Gemini response.")
        
        print("SQL Query from Gemini:", sql_query)  # Debug print
        sql_query = clean_sql_query(sql_query)
        print("Cleaned SQL Query:", sql_query)  # Debug print
        
        # Execute the query
        df = pd.read_sql_query(sql_query, engine)
        print("Query result DataFrame:", df)
        
        # Filter out NaN results
        df = df.fillna(0)
        
        # Create visualization if appropriate
        visualization = None
        if len(df.columns) == 2:  # Simple case for x,y plot
            fig = px.bar(df, x=df.columns[0], y=df.columns[1])
            visualization = fig.to_json()
        
        print("Response JSON:", {
            'sql_query': sql_query,
            'data': df.to_dict(orient='records'),
            'visualization': visualization
        })
        return jsonify({
            'sql_query': sql_query,
            'data': df.to_dict(orient='records'),
            'visualization': visualization
        })
    except Exception as e:
        import traceback
        print("Exception:", e)
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'sql_query': None,
            'data': [],
            'visualization': None
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 