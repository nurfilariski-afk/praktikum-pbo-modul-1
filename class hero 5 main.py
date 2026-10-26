class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} menyerang dengan power {self.power}!")

    def upgrade(self, tambahan):
        self.power += tambahan
        print(f"Power {self.name} naik menjadi {self.power}")

hero_1 = Hero("Goku", 100)
hero_1.attack()
hero_1.upgrade(20)
hero_1.attack()