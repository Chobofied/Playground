class Class1(object):
    def __init__(self,A):
        self.stats = counter('test')
        self.stats.count = 10

class counter:
    def __init__(self, name):
        self.name = name
        self.count = 0
    def __string__(self):
        message = self.name + self.count
        return message

class_instance = Class1(5)