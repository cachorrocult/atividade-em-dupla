class MissionBackpack:
    def __init__(self, agent, equipment, max_capacity):
        self.agent = agent
        self.equipment = equipment
        self.max_capacity = max_capacity
    def add_equipment(self, equip):
        if equip.strip() != "" and len(self.equipment) < self.max_capacity:
            self.equipment.append(equip)
            print(f"Equipamento '{equip}' successfully added!")
        else:
            print("Not possible to add equipment.")
    def list_equipment(self):
        print("Backpack equiped:")
        for equip in self.equipment:
            print(f"- {equip}")
    def count_equipment(self):
        return len(self.equipment)
    def check_espaco(self):
        if len(self.equipment) >= self.max_capacity:
            return "Backpack is full."
        else:
            return "There's more room inside the backpack."
    def show_report(self):
        print(f"Agent: {self.agent}")
        print(f"Equipment quantity: {self.count_equipment()}")
        print(f"Max capacity: {self.max_capacity}")
        print(f"Situation: {self.check_espaco()}")
mochila = MissionBackpack("Agent Maria", ["Pills", "Energy drinks"], 4)
mochila.add_equipment("Condoms")
mochila.list_equipment()
print()
mochila.show_report()
