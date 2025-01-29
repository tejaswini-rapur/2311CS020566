students = {
    1: {"name":"google","age":430},
    2: {"name":"shashank","age":48},
    3: {"name":"thanush","age":422},
    4: {"name":"chetan","age":234},
    5: {"name":"siri","age":984},
}
for students_id,details in students.items():
    print(f"student ID: {students_id},Name:{details['name']}, Age: {details['age']}")