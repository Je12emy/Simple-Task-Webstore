# Simple Flask Webstore

A lightweight Flask-based web store application designed as a starting point for building features with AI assistance.

## Requirements

- Python 3.x
- pip (Python package installer)
- SQLite3
- (Optional) Docker

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Je12emy/Simple-Task-Webstore.git
cd Simple-Task-Webstore
```

### 2. Create a Python Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**On Unix/Linux/macOS:**

```bash
source .venv/bin/activate
```

**On Windows:**

```cmd
# CMD
.venv\Scripts\activate

# PowerShell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Initialize the Database

The database migrations are managed through `init_db.py`. Run the following command to set up the SQLite database:

```bash
python init_db.py
```

This will automatically create the `instance` directory and the `store.db` database file with the required schema.

## Running the Application

After completing the setup, start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000` by default.

## Project Structure

```
simple-flask-webstore/
├── app.py              # Main application entry point
├── database.py         # Database connection and utilities
├── init_db.py          # Database initialization and migrations
├── models.py           # Data models
├── requirements.txt    # Python dependencies
├── instance/           # SQLite database storage
├── static/             # Static assets (CSS, JS, images)
└── templates/          # HTML templates
```
