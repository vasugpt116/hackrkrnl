Hello HackerKernel,
This is a project that adds users and task and then one can export it as excel sheets on thier personal computer.

I have added the virtual environment named "vasutask" which enables user to not install different packages multiple times.

The project is saved inside "taskproject" which have an application named "taskapp".

All the database queries are done in DjangoORM and have an sqllite database(as provided by django).

Application have 6 html files: 1 index.html, 1 base.html(which provides base to other 4), 4 different html files for different pages.

Download to excel do not have an webpage since it can directly be downloaded.

Project Structure
- taskproject/: The main project directory.
- taskapp/: The Django application containing the core functionality.
- templates/: Contains 6 HTML files for the user interface.
- index.html: The main landing page.
- base.html: Base template providing a consistent layout for other pages.
- Four other HTML files for various functionalities.


Setup and Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory and activate the virtual environment.
3. Run the Django migrations to set up the database.
4. Start the development server.
