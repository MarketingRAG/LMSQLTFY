# LMSQLTFY
AKA The Vinny Bot - A shout out to my friend who works in business intelligence and inspired this idea by saying "people are always asking me to write simple queries, it seems like AI should be able to handle that"

LMSQLTFY is an AI-powered SQL query generator and data visualization tool that helps you explore your database through natural language. It uses Google's Gemini AI to convert your questions into SQL queries and creates beautiful visualizations and presentations of the results.

## Features

- 🤖 Natural language to SQL conversion using Gemini AI
- 📊 Automatic data visualization with Plotly
- 🎨 Beautiful presentation generation with Slidev
- 🔄 Real-time query execution and results
- 📱 Modern, responsive web interface

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL database
- Google Cloud API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lmsqltfy.git
cd lmsqltfy
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies for presentation generation:
```bash
npm install
```

4. Create a `.env` file in the root directory with the following variables:
```env
GOOGLE_API_KEY=your_gemini_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/your_database
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter your question in natural language, and LMSQLTFY will:
   - Generate the appropriate SQL query
   - Execute it against your database
   - Create a visualization of the results
   - Optionally generate a presentation

## API Endpoints

- `GET /`: Main web interface
- `POST /api/chat`: Process natural language questions and return SQL results
- `POST /api/presentation/view`: Generate and view a presentation
- `POST /api/presentation/export`: Export presentation as PDF

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for natural language processing
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Plotly](https://plotly.com/) for data visualization
- [Slidev](https://sli.dev/) for presentation generation 
