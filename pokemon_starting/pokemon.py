
class Pokemon:
    def __init__(self, name, level, pock_type, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = pock_type
        self.current_health = current_health
        self.maximum_health = current_health + level * 0.5
        self.is_knocked_out = is_knocked_out

        print('New Pockemon named {} created!'.format(self.name))

    def lose_health(self, points):
        self.current_health -= points
        print("{name} has lost {points} points! {name}'s health is {health}".format(name=self.name,
                                                                                    points=points,
                                                                                    health=self.current_health))

        if self.current_health <= 0:
            self.is_knocked_out = True
            print('{} has been knocked out!!!'.format(self.name))

    def gain_health(self, points):
        if not self.is_knocked_out and points+self.current_health < self.maximum_health:
            self.current_health += points
            print("{name} has gained {points} points! {name}'s health is {health}".format(name=self.name,
                                                                                          points=points,
                                                                                          health=self.current_health))
        elif not self.is_knocked_out and points+self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
            print("{} has maximum health of {}!".format(self.name, self.current_health))
        else:
            print('{} is knocked out. Can\'t gain health.'.format(self.name))

    def revive(self):
        self.is_knocked_out = False
        self.current_health = self.maximum_health * 0.1
        print("{name} has revived! {name} as {points} health points".format(name=self.name, points=self.current_health))


test_pockemon = Pokemon('Sam', 5, 'fire', 10, False)
test_pockemon.lose_health(2)
test_pockemon.lose_health(10)
test_pockemon.gain_health(1)
test_pockemon.revive()
