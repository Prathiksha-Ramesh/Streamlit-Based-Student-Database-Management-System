# Streamlit-Based Student Database Management System

This project showcases a student database management system built using Streamlit. The system integrates with a SQLite database to perform CRUD (Create, Read, Update, Delete) operations. The application leverages SQLAlchemy for database interaction and dotenv for environment variable management.

## Project Structure
```
project-directory/
 │ ├── app.py 
 ├── final.py 
 ├── requirements.txt 
 ├── .env 
 ├── student.db 
 ├── README.md 
 ├── LICENSE 
 └── .gitignore
```

 
## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student-db-management.git
cd student-db-management
```

2. Install the required Python packages:

```bash 
pip install -r requirements.txt
```

3.  Set up your environment variables in the `.env` file:

```bash 
DB_URL=sqlite:///student.db
SECRET_KEY=your_secret_key
```

Replace your_secret_key with a secure key of your choice.

## Running the Application
- Ensure your .env file is properly configured with your database URL and secret key.

- Run the Streamlit application:

```bash 
streamlit run app.py
```

- Open your web browser and go to http://localhost:8501 to interact with the student database management system.

## Example Usage

1. Add new student records to the database.
2. View the list of all students currently stored in the database.
3. Update details of existing student records.
4. Delete student records as needed.

## Integration Details

- `Streamlit`: Provides the user interface for interacting with the database.
- `SQLAlchemy`: Manages the interaction with the SQLite database (student.db) using ORM (Object-Relational Mapping).
- `dotenv`: Loads environment variables from the .env file to configure the database connection and other sensitive information.

## Files

- `app.py`: The main Python script that sets up the Streamlit interface, handles CRUD operations, and interacts with the SQLite database.
- `final.py`: An additional script that may contain advanced operations or specific functionalities for the database management.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
- `.env`: Contains the database URL and other environment variables. This file should not be included in version control.
- `student.db`: The SQLite database file that stores the student records.
- `README.md`: This file, providing an overview of the project.
- `LICENSE`: The project's license, specifying how others may use the code.
- `.gitignore`: Specifies files and directories that should be ignored by Git, such as the .env file and any other sensitive information.

## .gitignore
The following files are ignored in the version control:


```bash
.env
__pycache__/
*.pyc
*.pyo
*.pyd
student.db

```

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
- Thanks to Streamlit for providing a user-friendly interface for building web applications.
- Thanks to SQLAlchemy for simplifying database interactions.
- Thanks to dotenv for securely managing environment variables.

