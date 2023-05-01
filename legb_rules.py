# LEGB - rule
# L -local
# E - enclosed
# G - global
# B - builtins
import builtins

builtins.scope = 'builtins'

scope = 'global'


def outer():
    scope = 'enclosed'

    def inner():
        scope = 'local'
        print(scope)

    inner()


if __name__ == '__main__':
    outer()
