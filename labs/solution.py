from abc import ABC,abstractmethod


class AbstractObj(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def draw(self,display):
        pass


class Interactive(ABC):

    @abstractmethod
    def interact(self, hero, engine):
        pass


class Entity(AbstractObj):

    def __init__(self,stats,position):
        self.hit_points = 0
        self.max_hit_points = 0
        self.stats = stats
        self.position = position

    def draw(self,display):
        pass


class Knight(Entity):
    def __init__(self,stats):
        self.level = 1
        self.experience = 0
        super().__init__(stats, [1, 1])

    @property
    def max_experience(self):
        pass

    def level(self):
        pass


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
        if self.max_hit_points < self.hit_points:
            self.hit_points = self.max_hit_points


class Debility(Effect):
    def use_effect(self):
        self.stats["power"] -= 5
        super().use_effect()


class Buff(Effect):
    def use_effect(self):
        self.stats["power"] += 5
        self.stats["intellect"] += 5
        super().use_effect()


class Violent(Effect):
    def use_effect(self):
        self.stats["power"] += 5
        super().use_effect()

