class Something:
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def get(self, val):
        self.val = val

    def func(self):
        return 