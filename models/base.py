from abc import ABC, abstractmethod

class BasePatient(ABC):
    def __init__(self, first_name, last_name, age, symptoms):
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.age = int(age)
        self.symptoms = symptoms.strip()
        self.full_name = f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_details(self):
        pass
