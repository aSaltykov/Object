from abc import ABC,abstractmethod

class AbstractObj(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def draw(self,display):
        pass

class Entity(AbstractObj):

    def __init__(self,stats,position):
        self.hit_points = 0
        self.max_hit_points = 0
        self.stats = stats
        self.position = position


class Knight(Entity):
    def __init__(self,stats):
        self.level = 1
        self.experience = 0
        super().__init__(stats, [1, 1])

    def level(self):
        pass

class Effect(Knight):

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


    @abstractmethod
    def use_effect(self):
        if self.max_hit_points < self.hit_points:
            self.hit_points = self.max_hit_points

