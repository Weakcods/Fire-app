# FireApp

A simple app that monitors fire incidents from different cities and countries.

### Instructions

1. Create a Repository on GitHub:

- Log in to your GitHub account.
- Click on the "+" icon in the top-right corner of the page and select "New reposi# FireApp - Fire Incident Monitoring System

A web-based application that monitors and visualizes fire incidents across different cities and countries. Live demo available at: [joooooshua.pythonanywhere.com](https://joooooshua.pythonanywhere.com)

## 🔑 Demo Credentials

To access the system, use the following credentials:

```
Username: joshua
Password: bacay
```

## Features

- 🗺️ Interactive Maps
  - Fire station locations with detailed information
  - Real-time incident mapping
  - Fire truck deployment visualization

- 📊 Analytics Dashboard
  - Incident severity distribution
  - Monthly incident trends
  - Geographic distribution analysis
  - Multi-dimensional data visualization

- 🚒 Fire Station Management
  - Complete fire station directory
  - Fire truck inventory tracking
  - Emergency contact information

## Tech Stack

- Backend: Django 4.2
- Frontend: HTML5, CSS3, JavaScript
- Maps: Leaflet.js
- Charts: Chart.js
- Database: SQLite3
- Deployment: PythonAnywhere

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Weakcods/Fire-app.git
cd Fire-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## Deployment

The application is deployed on PythonAnywhere:
- Live URL: [joshuawa.pythonanywhere.com](https://joooooshua.pythonanywhere.com)
- Admin Interface: [joshuawa.pythonanywhere.com/admin](https://joooooshua.pythonanywhere.com/admin)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Project Link: [github.com/Weakcods/Fire-app](https://github.com/Weakcods/Fire-app)tory."
- Enter a name for your repository, choose any other settings you want, and click "Create repository."

2. Clone the Repository Locally:

- Once the repository is created, you'll see a green "Code" button. Click on it.
- Copy the URL provided (it should end with .git).
- Open your terminal or command prompt on your local machine.
- Navigate to the directory where you want to clone the repository.
- Run the following command, replacing <repository_URL> with the URL you copied:

```
git clone <repository_URL>
```

3. Clone the Content of the Boilerplate:

- Navigate into the cloned repository directory:

```
cd <repository_name>
```

- Now, clone the content of the boilerplate into this directory. If you have the URL for the boilerplate repository, you can use the following command:

```
git clone <boilerplate_repository_URL>
```

- Replace <boilerplate_repository_URL> with the URL of the boilerplate repository.

If you don't have the URL for the boilerplate repository, you can download the content as a ZIP file from the boilerplate repository on GitHub. Once downloaded, extract the contents into your local repository directory.

4. Install Required Dependencies:

- Ensure you have Python and pip installed on your machine.
- Open a terminal or command prompt in the root directory of your local repository.
- Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```
