"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=0, hourly_rate=0, contracts=0, rate=0, bonus=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.contracts = contracts
        self.rate = rate
        self.bonus = bonus
        self.pay_description = ""

    def get_pay(self):

        total_pay = 0
        components = []

        if any(x < 0 for x in [self.salary, self.hours, self.hourly_rate, self.contracts, self.rate, self.bonus]):
            raise ValueError("All parameters should be positive")

        pay_components = [
            (self.salary, f"works on a monthly salary of {self.salary}"),
            (self.hours * self.hourly_rate, f"works on a contract of {self.hours} hours at {self.hourly_rate}/hour"),
            (self.bonus, f"receives a bonus commission of {self.bonus}"),
            (self.contracts * self.rate, f"receives a commission for {self.contracts} contract(s) at {self.rate}/contract")]

        for value, description in pay_components:
            if value > 0:
                total_pay += value
                components.append(description)
                
        self.pay_description = " and ".join(components)
        return total_pay

    def __str__(self):
        return f"{self.name} {self.pay_description}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)
billie.get_pay()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_rate=25)
charlie.get_pay()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, rate=200)
renee.get_pay()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_rate=25, contracts=3, rate=220)
jan.get_pay()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)
robbie.get_pay()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_rate=30, bonus=600)
ariel.get_pay()
