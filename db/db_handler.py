import mysql.connector
from configparser import ConfigParser
from utils.encryptor import decrypt_password
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBHandler:
    def __init__(self):
        config = ConfigParser()
        config.read("config/config.ini")

        key = config.get("crypto", "key")
        enc_password = config.get("mysql", "password")
        password = decrypt_password(enc_password, key)

        self.conn = mysql.connector.connect(
            host=config.get("mysql", "host"),
            user=config.get("mysql", "user"),
            password=password,
            database=config.get("mysql", "database"),
            port=config.getint("mysql", "port")
        )
        self.cursor = self.conn.cursor()

    def insert_patient(self, patient):
        try:
            self.cursor.execute(
                "SELECT * FROM patients WHERE first_name=%s AND last_name=%s AND age=%s",
                (patient.first_name, patient.last_name, patient.age)
            )
            if self.cursor.fetchone():
                logger.warning(f"Duplicate entry skipped for {patient.full_name}")
                return

            self.cursor.execute("""
                INSERT INTO patients (first_name, last_name, age, symptoms, type, priority)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, patient.get_details())
            self.conn.commit()
            logger.info(f"Patient {patient.full_name} inserted successfully.")
        except Exception as e:
            logger.error(f"Failed to insert patient: {e}")
