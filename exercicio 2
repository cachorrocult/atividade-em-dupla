class InterdimensionalPortal:
    def __init__(self, name, destination, needed_power, available_power):
        self.name = name
        self.destination = destination
        self.needed_power = needed_power
        self.available_power = available_power
    def may_open(self):
        if self.available_power >= self.needed_power:
            return True
        else:
            return False
    def calculate_power_lack(self):
        if self.may_open():
            return 0
        else:
            return self.needed_power - self.available_power
    def classify_stability(self):
        falta = self.calculate_power_lack()

        if falta == 0:
            return "stable portal"
        elif falta <= 20:
            return "almost stable portal"
        else:
            return "unstable portal"
    def simplefying(self):
        print(f"Portal: {self.name}")
        print(f"destination: {self.destination}")
        print(f"Energia disponível: {self.available_power}")
        print(f"Energia necessária: {self.needed_power}")
        print(f"Situação: {self.classify_stability()}")
portal = InterdimensionalPortal(
    "Portal Alpha",
    "Mars",
    100,
    85
)
portal.simplefying()
if portal.may_open():
    print("The portal may be open.")
else:
    print(
        f"There are {portal.calculate_power_lack()} power points left to open the portal."
    )
