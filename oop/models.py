import random

class RobotFactory:
    robots_created = []

    def __init__(self, name, identifier, color, type):

        self.name = name
        self.identifier = identifier
        self.color = color
        self.type = type

    @staticmethod
    def new_robot(name, identifier, color, type):
        if type == "fighter":
            robot = FighterRobot(name, identifier, color)
        elif type == "cook":
            robot = CookRobot(name, identifier, color)
        elif type == "firefighter":
            robot = FirefighterRobot(name, identifier, color)
        else:
            return False
        RobotFactory.robots_created.append(robot)
        return True

    @staticmethod
    def create_fighter_bots(n):
        for i in range(n):
            name = "fighter_bot" + str(i)
            identifier = str(random.randint(1, 1000))
            color = "metallic"
            robot = FighterRobot(name, identifier, color)
            RobotFactory.robots_created.append(robot)
        return True

    def __len__(self):
        return len(RobotFactory.robots_created)

    def __repr__(self):

        return f"{self.identifier} - {self.name} ({self.type}) - {self.color}"

class Robot:
    def __init__(self, name, identifier, color):
        self.name = name
        self.identifier = identifier
        self.color = color

class FighterRobot(Robot):
    def __init__(self, name, identifier, color):
        super().__init__(name, identifier, color)

    def fight(self):
        return "Fight in progress ..."

    def interact(self):
        return "Hello Sir, Please show me your ID"

    def walk(self):
        return "I am walking safely"

class CookRobot(Robot):
    def __init__(self, name, identifier, color):
        super().__init__(name, identifier, color)

    def cook(self):
        return "Cooking in progress"

    def interact(self):
        return "What can I cook for you today?"

    def walk(self):

        return "I am walking slowly"

class FirefighterRobot(Robot):
    def __init__(self, name, identifier, color):
        super().__init__(name, identifier, color)

    def put_out_fire(self):
        return "Putting out the fire ..."

    def interact(self):
        return "We are there to protect you. Please stay behind the line"

    def walk(self):
        return "I am walking fast"

assert RobotFactory.new_robot(name="scythe", identifier="00001", color="metallic", type="cook")
assert RobotFactory.new_robot(name="de303", identifier="00002", color="red", type="cook")
assert RobotFactory.new_robot(name="de313", identifier="00003", color="red", type="fighter")
assert RobotFactory.new_robot(name="arm303", identifier="00004", color="red", type="firefighter")
assert len(RobotFactory.robots_created) == 4

assert RobotFactory.new_robot(name="Arm303", identifier="00004", color="red", type="doctor") is False
assert len(RobotFactory.robots_created) == 4
assert RobotFactory.create_fighter_bots(100)
assert len(RobotFactory.robots_created) == 104

cook_bot = RobotFactory.robots_created[0]
assert cook_bot.identifier == "00001"
assert cook_bot.walk() == "I am walking slowly"
assert cook_bot.cook() == "Cooking in progress"

fighter_bot = RobotFactory.robots_created[2]
assert fighter_bot.identifier == "00003"
assert fighter_bot.walk() == "I am walking safely"
assert fighter_bot.fight() == "Fight in progress ..."

fire_fighter_bot = RobotFactory.robots_created[3]
assert fire_fighter_bot.identifier == "00004"
assert fire_fighter_bot.walk() == "I am walking fast"
assert fire_fighter_bot.put_out_fire() == "Putting out the fire ..."