from models.regular import RegularPatient
from models.emergency import EmergencyPatient
from db.db_handler import DBHandler

if __name__ == "__main__":
    db = DBHandler()

    p1 = RegularPatient("john", "doe", 35, "Fever and cough")
    p2 = EmergencyPatient("alice", "smith", 42, "Chest pain")

    db.insert_patient(p1)
    db.insert_patient(p2)
