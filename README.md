# Clinic Patient Management System

A modular, secure, and object-oriented Python project to manage clinic patients and their records. Built with MySQL as the backend database, AES encryption for password security, and structured using real-world OOP practices.

## 🔧 Features

- Add patient records: name, age, gender, department.
- Uses OOP principles: abstraction, inheritance, encapsulation.
- AES encryption for storing DB password securely.
- Modular structure with config handling and logging.
- No UI, object data passed programmatically.

## 🗃️ Project Structure

```
clinic_patient_manager/
│
├── models/
│   ├── base.py
│   ├── patient.py
│   └── __init__.py
│
├── db/
│   ├── db_handler.py
│   └── __init__.py
│
├── utils/
│   ├── encryptor.py
│   └── __init__.py
│
├── config.ini
├── main.py
└── README.md
```

## ⚙️ Setup

1. Install dependencies

```bash
pip install pycryptodome mysql-connector-python
```

2. Create MySQL schema:

```sql
CREATE DATABASE clinic_db;
USE clinic_db;
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT,
    gender VARCHAR(10),
    department VARCHAR(50)
);
```

3. Generate AES key and encrypt password using the utility script or manually.

## 🔐 Config File (config.ini)

```ini
[mysql]
host = localhost
user = root
password = <ENCRYPTED_PASSWORD>
database = clinic_db
port = 3306

[crypto]
key = <YOUR_AES_KEY>
```

## 🏃 Run the Project

```bash
python main.py
```

## ✅ Example

```python
from db.db_handler import DBHandler
from models.patient import Patient

db = DBHandler()
patient = Patient("Alice", "Smith", 29, "Female", "Neurology")
db.insert_patient(patient)
```

---

## 📌 Notes

- All inputs are trimmed and formatted (e.g., capitalization).
- Duplicate emails are skipped automatically.
- Errors and inserts are logged.

## 📄 License

This project is licensed for personal use.