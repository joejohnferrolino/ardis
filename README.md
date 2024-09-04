# Console Operations

- Python 3.11
- PostgreSQL 16.4

# I. Development environment
**Python 3.11**

Download "https://www.python.org/downloads/"

**PostgreSQL 16.4**

Download "https://www.postgresql.org/download/"


# II. Getting started
## 1. Modules installation:
**PostgreSQL**

RUN `pip install psycopg`

**Environment variables**

RUN `pip install python-dotenv`

## 2. PostgreSQL Database:
Create a Database:
```bash
CREATE DATABASE console_db;
```
Connect to the Newly Created Database:
```bash 
\c console_db
```
Create a Table
add the following to create a test DB
ardis/database/users.sql
```bash
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
```

For the python environment file, change it as follows:
.env

```bash
DB_HOST=localhost
DB_NAME=console_db
DB_USER=postgres
DB_PASS=root
DB_PORT=5432
```

## 3. Console Execution:
Run `python console.py `
