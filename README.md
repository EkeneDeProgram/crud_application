# Simple CRUD Application

### Description
This is a simple CRUD application built with FastAPI and SQLAlchemy for managing a collection of books.

### Swagger Documentation

You can view the Swagger documentation for the API endpoints by visiting the following URL:

[Swagger Documentation](http://localhost:8000/docs)


### Installation

**Prerequisites**
Before installing the Simple CRUD Application API, ensure you have the following prerequisites installed:

* Python (version 3.6 or higher)
* PostgreSQL database (Optional)
* Docker (Optional)

**Setting Up**

1. Clone the repository to your local machine:
```bash
git clone https://github.com/EkeneDeProgram/crud_application.git
cd <project directory>
```

2. Create and activate a virtual environment:

* On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

* On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies using pip:
```bash
pip install -r requirements.txt
```

4. Set up the environment variables:
* Copy the `.env.example` file and rename it to `.env`.
* Open the `.env` file and set the `DATABASE_URL` and `DOCKER_DATABASE_URL` variable to your local PostgreSQL connection string.
```bash
DATABASE_URL=postgresql://{username}:{password}@localhost:{port}/{your-database-name}
DOCKER_DATABASE_URl=postgresql://{username}:{password}@host.docker.internal:{port}/{your-database-name}
```

5. Run the development server:
```bash
uvicorn main:app
```

6. Access the API at http://localhost:8000/api/.

### Testing

1. To run test for the routes, execute:
```bash
cd <test>
python test_routes.py
```

2. To run test for the models, execute:
```bash
cd <test>
python test_models.py
```

3. To run test for the schemas, execute:
```bash
cd<test>
python test_schemas.py
```

### Docker

To run the Simple CRUD Application using Docker, follow these steps:

1. Build the Docker image:
```bash
cd <project directory>
docker build -t app .
```

2. Run the Docker container:
```bash
docker run -d -p 8000:8000 app.
```

3. Access the application:
Once the container is running, you can access the Simple CRUD Application at http://localhost:8000/api
