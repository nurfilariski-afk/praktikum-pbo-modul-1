class Hero:
    role = "Fighter"  # class attribute (sama untuk semua objek)

    def __init__(self, name, power):
        self.name = name    # instance attribute (berbeda tiap objek)
        self.power = power

hero_1 = Hero("Goku", 100)
hero_2 = Hero("Vegeta", 90)

print(hero_1.name, hero_1.role)
print(hero_2.name, hero_2.role)
print(hero_1.__dict__)