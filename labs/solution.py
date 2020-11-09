from abc import ABC,abstractmethod


class AbstractObj(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def draw(self,display):
        pass


class AbsAction(ABC):
    @classmethod
    @abstractmethod
    def use(cls, level, hero):
        pass


class NextLevel(AbsAction):
    @classmethod
    def use(cls, level, hero):
        level.next_level()



class Interactive(ABC):
    @abstractmethod
    def interact(self, hero, engine):
        pass


class HpError(Exception):

    def __init__(self, hp, message = "little health"):
        self.hp = hp
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.hp} -> {self.message}'


class Map:

    def __init__(self,_map):
        self._map = _map

    @property
    def size(self):
        return len(self._map[0]),len(self._map)

    def __getitem__(self, number):
        if not isinstance(number, tuple):
            raise TypeError
        elif number[0] < len(self._map[0]) and number[1] < len(self._map):
            return self._map[number[1]][number[0]]
        else:
            raise IndexError


class ObjGenerate:

    def __init__(self):
        self.enemy = dict()

    def get(self, _map):
        return {}


class MapGenerate(ObjGenerate):

    def get(self, _map):
        return {(1, 1): "Knight"}


class Entity(AbstractObj):

    def __init__(self,stats,position):
        self.hit_points = 0
        self.max_hit_points = 0
        self.stats = stats
        self.position = position

    def draw(self,display):
        pass

    def max_hit_points(self):
        self.max_hit_points = 8 + self.stats["stamina"] + self.stats["power"]
        if self.max_hit_points < self.hit_points:
            self.hit_points = self.max_hit_points


class Knight(Entity):
    def __init__(self,stats):
        self.level = 1
        self.experience = 0
        super().__init__(stats, [1, 1])

    @property
    def max_experience(self):
        pass


    def level(self):
        while self.experience >= self.max_experience:
            self.max_hit_points()
            self.hit_points = self.max_hit_points
            self.level += 1
            self.stats["stamina"] += 3
            self.stats["power"] += 3
            yield "Level up"

class Mate(AbstractObj, Interactive):
    def __init__(self, position, action):
        self.position = position
        self.action = action

    def interact(self, hero, engine):
        self.action(engine, hero)

    def draw(self,display):
        pass

class Effect(Entity):

    def __init__(self,basic):
        self.basic = basic
        self.use_effect()


    @property
    def hit_points(self):
        return self.basic.hit_points

    @hit_points.setter
    def hit_points(self,value):
        self.basic.hit_points = value

    @property
    def max_hit_points(self):
        return self.basic.max_hit_points

    @max_hit_points.setter
    def max_hit_points(self,value):
            self.basic.max_hit_points = value

    @property
    def gold(self):
        return self.basic.gold

    @gold.setter
    def gold(self, value):
        self.basic.gold = value

    @property
    def experience(self):
        return self.basic.experience

    @experience.setter
    def experience(self, value):
        self.basic.experience = value


    @abstractmethod
    def use_effect(self):
        self.max_hit_points()
        try:
            if self.max_hit_points < self.hit_points:
                self.hit_points = self.max_hit_points
            else:
                raise HpError(int(self.hit_points))
        except HpError as e:
            pass


class Debility(Effect):
    def use_effect(self):
        self.stats["power"] -= 5
        self.stats["stamina"] -= 5
        super().use_effect()


class Buff(Effect):
    def use_effect(self):
        self.stats["power"] += 5
        self.stats["intellect"] += 5
        self.stats["stamina"] += 3
        super().use_effect()


class Violent(Effect):
    def use_effect(self):
        self.stats["power"] += 5
        self.stats["intellect"] -= 2
        self.stats["stamina"] += 5
        super().use_effect()

