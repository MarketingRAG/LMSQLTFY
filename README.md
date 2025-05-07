# LMSQLTFY - Let Me SQL That For You

A chatbot that helps users query airline delay data using natural language. The application uses Gemini 1.5-flash to convert natural language questions into SQL queries and provides visualizations of the results.

## Prerequisites

- Python 3.8+
- PostgreSQL
- Google Cloud API key with Gemini access

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the airline delay dataset from [Kaggle](https://www.kaggle.com/datasets/sriharshaeedala/airline-delay) and place it in the project root directory as `airline_delay.csv`

4. Copy `.env.example` to `.env` and fill in your configuration:
   ```bash
   cp .env.example .env
   ```

5. Set up the database:
   ```bash
   python setup_db.py
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Type your question about airline delays in natural language
2. The chatbot will:
   - Convert your question to SQL
   - Execute the query
   - Display the results in a table
   - Show a visualization if applicable

## Example Questions

- "Which day of the year has the most delayed flights?"
- "What is the average delay time by airline?"
- "Show me the top 5 airports with the most delays"
- "What is the correlation between weather conditions and flight delays?" 