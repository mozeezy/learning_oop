class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_and_age(self):
        return f"Hello {self.name}, You are {self.age} years old!"

    def print_age_in_months(self):
        age_in_months = self.age * 12
        return f"You're {age_in_months} months old!"

    def print_age_in_days(self):
        age_in_days = self.age * 365
        return f"You're {age_in_days} days old!"