MAX_BONUS=150

class BonusValidationError(Exception):
    pass

class Employeer:
    def __init__(self, first_name, last_name, job, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = 0

    def __repr__(self):
        return f'Employer({self.first_name},{self.last_name})'

    @property
    def total_salary(self):
        return self.bonus + self.salary

    def add_bonus(self, bonus):
        if bonus > MAX_BONUS:
            raise BonusValidationError(f'Bonus is larger then {MAX_BONUS}')  

        self.bonus += bonus

class Departament:
    def __init__(self, name):
        self.name = name
        self.employers = []

    def __iter__(self):
        return (emp for emp in self.employers)

    def add_employer(self, employer):
        self.employers.append(employer)    

def entry():
    departament = Departament(name="test departament")

    employer1 = Employeer(
        first_name = "John",
        last_name = "Travolta",
        age = 10,
        job = "CEO",
        salary = 900
    )

    employer2 = Employeer(
        first_name = "Steve",
        last_name = "Jobs",
        age = 50,
        job = "Programmers",
        salary = 5000
    )

    employer1.add_bonus(111)

    departament.add_employer(employer1)
    departament.add_employer(employer2)

    for emp in departament:
        print(emp, '-->', emp.total_salary)

if __name__ == '__main__ ':
    entry

