
def stats():
    from . import program
    print (program.class_instance.stats.count)

stats()

from .third_module_level import second_call

#from test_module.test_module2 import second_class


#import test_module2
#import test_module.test_module2

