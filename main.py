from human import Human

john = Human("John", 25)

greet_john = john.print_name_and_age()
john_age_in_days = john.print_age_in_days()
john_age_in_months = john.print_age_in_months()

print(greet_john)
print(john_age_in_days)
print(john_age_in_months)