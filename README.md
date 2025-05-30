# AI SQL Agent
AI SQL Agent is a web-based assistant that translates natural language prompts into SQL queries for multiple SQL dialects (PostgreSQL, MySQL, SQLite) and executes them on your database. 
It provides an interactive interface to generate, clarify, and run SQL statements using AI, and displays the results in a user-friendly table.

## Features
+ Natural Language to SQL: Enter your request in plain English and the AI will generate precise SQL queries.
+ Supports Multiple Dialects: Choose between PostgreSQL, MySQL, or SQLite.
+ Interactive Web Interface: Submit prompts, view generated SQL, and see query results in your browser.
+ Direct Query Execution: Queries are run against your database and results are displayed in a table.
+ Customizable Schema: The AI can use your schema to tailor SQL output.

## Getting Started

### Prerequisites
+ Python 3.x
+ Required Python packages (see below)
+ Access to your target database (PostgreSQL, MySQL, or SQLite)
+ OpenAI-compatible API key (for AI model access)

### Installation
Clone the repository:
```bash
git clone https://github.com/DanialHMD/Ai_Agent.git
cd Ai_Agent
```
Install dependencies:

```bash
pip install openai python-dotenv
```
> Plus any web framework and DB connector you use (Flask, psycopg2, mysql-connector-python, etc.)\

### Configure environment variables:
Create a .env file in the root or app/ directory with your API keys and DB credentials.
Initialize the database:

> (Optional) Use the provided app/schema.sql as a starting point.

## Usage

### Start the web server:

> (Assuming usage of Flask or similar; adapt as needed)
```bash
python app/main.py  # Or the appropriate entry point for your web app
```

### Open your browser:

Navigate to http://localhost:5000 (or the configured port).\
Use the interface to select SQL dialect, mode, and enter your prompt.\


## Project Structure
- app/sql_agent.py: Backend logic for building prompts and interacting with the AI model.
- app/utils/query_init.py: Handles database connections and query execution for different SQL dialects.
- app/static/index.html: Main web interface for user interaction.
- app/schema.sql: Example SQL schema.

## Security Notice
- API Keys: Do not hardcode sensitive keys. Use environment variables for secrets.
- Database Safety: Make sure only trusted users have access, and always validate/escape inputs appropriately.

## Contributing
Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.
