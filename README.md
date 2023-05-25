# python-django-app-starter
Starter kit to start coding web-AI apps with Python and Django in as few steps as possible. (WIP)

## Prerequisites

To run this project, you need to have the following installed on your system:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/letam/python-django-app-starter.git
```

2. Navigate to the project directory:
```bash
cd python-django-app-starter.git
```

3. Install project dependencies:
```bash
python install
```

4. Activate the virtual environment:

- For Windows:

  ```bash
  .venv\Scripts\activate
  ```

- For Mac or Linux:

  ```bash
  . .venv/bin/activate
  ```

5. Start the Django app development server:
```bash
python src/manage.py runserver
```

6. Visit the website at [http://localhost:8000](http://localhost:8000).

7. Start hacking/building code:

- To edit backend/server code, edit `src/web/views.py`. Note that the development server restarts automatically when changes are saved to disk.
- To edit frontend/web code, edit `src/web/templates/index.html`. Reload the webpage in the browser to see changes.
