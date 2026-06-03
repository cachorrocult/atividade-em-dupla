class DroneTournament:
    def __init__(self, name_tourney, tests, starting_battery):
        self.name_tourney = name_tourney
        self.tests = tests
        self.battery = starting_battery
        self.scores = 0
        self.concluded_tests = []
    def list_tests(self):
        print("Available tests:")
        for i, test in enumerate(self.tests, start=1):
            name, spending, scoreboard = test.split("/")
            print(f"{i}. {name} | Spending: {spending} | Scoreboard: {scoreboard}")
    def try_test(self, test_number):
        if test_number < 1 or test_number > len(self.tests):
            print("Error: Test number invalid.")
            return
        test = self.tests[test_number - 1]
        if test in self.concluded_tests:
            print("This test was already concluded.")
            return
        name, spending, scoreboard = test.split("/")
        spending = int(spending)
        scoreboard = int(scoreboard)
        if self.battery >= spending:
            self.battery -= spending
            self.scores += scoreboard
            self.concluded_tests.append(test)
            print(f"Test '{name}' concluded!")
        else:
            print("Battery insufficient for this test.")
    def calculate_progress(self):
        return len(self.concluded_tests)
    def check_situation(self):
        if len(self.concluded_tests) == len(self.tests):
            return "Tournament concluded"
        elif self.battery == 0:
            return "Tournament done with no battery"
        else:
            return "Tournament is due"
    def show_report(self):
        print(f"Tourney: {self.name_tourney}")
        print(f"Battery left: {self.battery}")
        print(f"Score: {self.scores}")
        print(f"Concluded test: {self.calculate_progress()}")
        print(f"Situation: {self.check_situation()}")
tourney = DroneTournament(
    "Drone Challenge",
    [
        "zig-zag/20/30",
        "low_flight/15/20",
        "simulate_rescue/40/80"
    ],
    60
)
tourney.list_tests()
print()
tourney.try_test(1)
tourney.try_test(2)
tourney.try_test(3)
print()
tourney.show_report()
