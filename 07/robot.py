from random import randrange

class Robot():
    max_damage = 5

    def __init__(self, lifes):
        self.lifes = lifes
    
    def is_alive(self):
        """Returns True if robot has any lifes left."""
        return self.lifes > 0

    def defend(self, damage):
        """Default defend. Simply takes damage."""
        self._take_damage(damage)

    def attack(self, target_robot):
        """Default attack. Simply makes damage."""
        self._make_damage(target_robot)

    def _make_damage(self, target_robot):
        """Generates random damage and forces the
        other robot to defend."""
        damage = randrange(0, self.max_damage)
        target_robot.defend(damage)

    def _take_damage(self, damage):
        """Sets new number of lifes when not already 0."""
        if self.lifes - damage < 0:
            self.lifes = 0
        else:
            self.lifes -= damage


class Aggressive(Robot):
    max_damage = 7
    def attack(self, target_robot):
        """Makes damage to the other robot twice. Special for aggresive robot."""
        self._make_damage(target_robot)
        self._make_damage(target_robot)


class Defensive(Robot):
    max_damage = 3    
    def defend(self, damage):

        """Special for deffensive robot, takes only half damage."""
        self._take_damage(damage // 2)


class Shielded(Robot):
    def __init__(self, lifes, shields, attacking_robot):
        """Value of shields reflects shields coverage of robot. Number from 0 to 1."""
        self.shields = shields
        self.attacking_robot = attacking_robot
        super().__init__(lifes)

    def defend(self, damage):
        """Special for shielded robot, reflects attack to attacking robot."""
        reflected = int(damage * self.shields)
        absorbed_by_shields = int(damage * self.shields // 2)
        self._take_damage(damage - reflected - absorbed_by_shields)
        self.attacking_robot.defend(reflected)


class Zombie(Robot):
    """Always returns that is alive."""
    def is_alive(self):
        return True
   

first = Aggressive(10)
#second = Defensive(50)
second = Shielded(20, 0.5, first)
#second = Zombie(2)
while True:
    first.attack(second)
    print('{}: {}'.format(second.__class__.__name__, second.lifes))
    if not second.is_alive():
        print('{} won'.format(first.__class__.__name__,))
        break
    
    second.attack(first)
    print('{}: {}'.format(first.__class__.__name__,first.lifes))   
    if not first.is_alive():
        print('{} won'.format(second.__class__.__name__))
        break