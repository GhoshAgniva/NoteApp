# NoteApp

## Project Description
NoteApp is a Flask-based web application that allows users to manage notes seamlessly. This application supports user authentication, note creation, editing, deletion, and exporting notes as PDFs. It also includes features like a responsive design, dark mode toggle, and integration with Excalidraw for whiteboarding.

## Features

### Notes Management
- **Create Notes**: Add new notes by typing in the text area and clicking the "Add Note" button.
- **Edit Notes**: Modify your existing notes by clicking the "Edit" button.
- **Delete Notes**: Remove notes using the "Delete" button.
- **Export Notes as PDF**: Download notes as PDF files using the "Export as PDF" button.

### Whiteboard Integration
- **Excalidraw Support**: Access a whiteboard for drawing or diagramming directly from the application.

### User Authentication
- Secure login and registration functionality.

### Dark Mode
- Toggle between light and dark modes for a better user experience.

### Responsive Design
- Works seamlessly across desktop and mobile devices.

## Installation Guide

### 1. Clone the Repository
Clone the project to your local machine using the following command:

```bash
git clone https://github.com/GhoshAgniva/NoteApp.git
cd NoteApp
```

### 2. Set up a Virtual Environment
Create and activate a virtual environment for the project:

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Database Setup
The app uses SQLite for storing user and note data. The database will be automatically created on the first run; no manual setup is required.

### 5. Run the Flask App
Start the development server:

```bash
flask run
```

This will start the app on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 6. Access the Application
Once the server is running, open your browser and navigate to:

```url
http://127.0.0.1:5000/
```

### 7. User Registration & Login
On the landing page, you can:
- Register a new account.
- Log in with an existing account to access your notes.

## Project Structure
```plaintext
NoteApp/
│
├── app.py                # Main Flask app file
├── config.py             # Configuration file (database and secret keys)
├── requirements.txt      # Project dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template for common elements
│   ├── home.html         # Home page template
│   └── edit_note.html    # Edit note template
├── static/               # Static files (CSS, JS, images)
│   ├── style.css         # Custom CSS file
│   └── script.js         # Custom JavaScript file
├── models.py             # Database models (User and Note)
└── database.db           # SQLite database file
```

## Application Features

### Notes Management
- Add, edit, delete, and export notes as PDFs.

### Whiteboard Integration
- Embedded Excalidraw whiteboard for drawing.

### Dark Mode Toggle
- A slider button allows toggling between dark and light modes.

### Responsive Design
- Optimized for both desktop and mobile devices.

## Running the Project in Production
To deploy this project for production, follow these steps:

1. **Choose a Platform**: Use platforms like Heroku, AWS, or DigitalOcean.
2. **Use a WSGI Server**: Deploy the app using Gunicorn or uWSGI.
3. **Environment Variables**: Store sensitive data like `FLASK_SECRET_KEY` securely.
4. **Database Configuration**: For production, switch to a scalable database like PostgreSQL.

## Contributing
We welcome contributions! Feel free to:

- Fork the repository.
- Submit issues or feature requests.
- Create pull requests to improve the application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, please reach out to:

- **Email**: ghoshagniva52@gmail.com
- **GitHub**: [GhoshAgniva](https://github.com/GhoshAgniva)

---
Thank you for using NoteApp! We hope it helps you stay organized and productive.
