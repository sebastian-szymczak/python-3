import random
import time

class Player:
    def __init__(self, nick, health, exp):
        self.nick = nick
        self._health = health
        self._maxhealth = health
        self._exp = exp

    def __str__(self):
        return f'{self.nick}: health={self.health}, exp={self._exp}, level={self.level}'
        
    def attack(self, other):
        time.sleep(2)
        if isinstance(other, Player):
            dmg = random.randint(1, 40) + self._level * 10 - 10
            other._set_health(other._get_health() - dmg)
            print(f'\n{self.nick} attacked {other.nick} for {dmg} damage!')
            self._exp += dmg
            time.sleep(1)
            print(f'{self.nick} has gained {dmg} experience points!')
            if self._exp >= self._level * 100:
                print(f'{self.nick} has advanced to level {self._level + 1}!')
            if other._get_health() <= 0:
                print(f'\n{self.nick} has defeated {other.nick}!')
                other._set_health(0)
                print(f'\n{player1}')
                print(player2)

    def heal(self):
        time.sleep(3)
        hp = random.randint(1, 10)
        if self._get_health() + hp > self._maxhealth:
            hp = self._maxhealth - self._get_health()
        self._set_health(self._get_health() + hp)
        print(f'\n{self.nick} healed himself for {hp} hp!')
        
    def _get_health(self):
        return self._health

    def _set_health(self, value):
        self._health = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._set_health(value)
        print(f"\n{self.nick}'s health value changed to {self._health}!")
        self._maxhealth = self._health
        print(self)
        
    @property
    def level(self):
        self._level = self._exp // 100 + 1
        return self._level

player1 = Player('Vidharr', 100, 1)
player2 = Player('Raest', 100, 1)

print(player1)
print(player2)

player1.health = 110

while True:
    player1.attack(player2)
    if player2._get_health() > 0:
        player2.heal()
    else:
        break
    player2.attack(player1)
    if player1._get_health() > 0:
        player1.heal()
    else:
        break
    time.sleep(1)
    print(f'\n{player1}')
    print(player2)
