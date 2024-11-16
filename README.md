# FastAPI Project
## Outline
- This project is designed to provide a robust and scalable web application framework with various functionalities.
- The project uses FastAPI for building APIs(or Web), SQLAlchemy for ORM, and Alembic for database migrations. 

## Requirements
- **Python 3.11 or later**: This project requires Python version 3.11 or higher.
- FastAPI
- websockets
- Jinja2
- SQLAlchemy
- pymysql
- Alembic

**Note:** Ensure you have Python 3.11 or later installed.

## Project Structure
```
/
├── alembic/
├── app/
│ ├── .env
│ ├── main.py
│ ├── api/
│ │ └── routers/
│ ├── core/
│ │ ├── config.py
│ │ └── utils.py
│ ├── db/
│ │ ├── database.py
│ │ ├── models/
│ │ ├── schema/
│ ├── static/
│ ├── templates/
│ └── utils/
│ ├── init.py
│ └── migration.py
```
### alembic/
- Contains migration scripts and configurations for Alembic.
### app/
- Main application directory containing the core logic and configurations.
### app/.env
-  Environment configuration files.
### app/api/routers/
-  Contains individual route modules
### app/core/
- **config.py**: Configuration settings for the application.
### app/db/
- **database.py**: Database connection setup.
- **models/**: Contains SQLAlchemy models.
- **schemas/**: Contains Pydantic schemas for data validation and serialization.
### app/static/
- Contains static files served by the application.
### app/templates/
- Contains HTML templates for rendering web pages.


## DataBase Migration
This project uses Alembic for Database migration. 
 Run the following commands to set up and apply database migrations
```bash
alembic revision --autogenerate -m "[Mesaage]"
alembic upgrade head
```
**Note:** Ensure `app/db/models/__init__.py` imports all models.