from models.base import BasePatient

class RegularPatient(BasePatient):
    def __init__(self, first_name, last_name, age, symptoms):
        super().__init__(first_name, last_name, age, symptoms)
        self.type = "Regular"
        self.priority = "Low"

    def get_details(self):
        return (self.first_name, self.last_name, self.age, self.symptoms, self.type, self.priority)
