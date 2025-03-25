# Poigne d'Acier Project

## Description
The **Poigne d'Acier** project is a fitness management application built using Streamlit and SQLModel. It allows gym administrators to manage coaches, courses, and members, while also enabling members to view available courses, register for them, and track their history.

## Features
### Admin Features
- **Manage Coaches**: Add, update, and delete coaches.
- **Manage Courses**: Add, update, and delete courses.
- **View Enrollments**: View members enrolled in specific courses.

### Member Features
- **View Courses**: Browse available courses.
- **Register for Courses**: Enroll in courses of interest.
- **Cancel Registrations**: Cancel course registrations.
- **View History**: Access a history of past course enrollments.

## Directory Structure
```
raoufaddeche-brief_poigne_d_acier/
├── generales_fonctions.py
├── init_db.py
├── main.py
├── models.py
├── populate_db.py
├── requirements.txt
├── utils.py
├── pages/
│   ├── app_admin.py
│   └── app_membre.py
└── .streamlit/
    └── config.toml
```

## Files
- **generales_fonctions.py**: Contains utility functions for navigation and data manipulation.
- **init_db.py**: Initializes the SQLite database.
- **main.py**: The main entry point of the application.
- **models.py**: Defines the database models using SQLModel.
- **populate_db.py**: Populates the database with fake data for testing purposes.
- **requirements.txt**: Lists the Python dependencies required to run the project.
- **utils.py**: Contains helper functions for database operations.
- **pages/app_admin.py**: Admin interface for managing coaches and courses.
- **pages/app_membre.py**: Member interface for viewing and managing course registrations.
- **.streamlit/config.toml**: Configuration file for Streamlit.

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:RaoufAddeche/Brief_Poigne_D_Acier.git
   cd raoufaddeche-brief_poigne_d_acier
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Initialize the database:
   ```bash
   python init_db.py
   ```
2. Populate the database with fake data (optional):
   ```bash
   python populate_db.py
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```
4. Use the sidebar menu to navigate between admin and member functionalities.

## Dependencies
- Streamlit
- Faker
- SQLModel

## Notes
- Ensure that the `database.db` file is in the same directory as the application files.
- Images used in the application should be placed in the appropriate directory and their paths updated in the code if necessary.

## License
This project is licensed under the MIT License.
