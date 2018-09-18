class decoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function


@decoratorClass
def display():
    print('display func ran')


abc = display()
abc()
