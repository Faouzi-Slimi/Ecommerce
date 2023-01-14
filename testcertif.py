def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def fawzi():
    print('fawzi')


fawzi()
