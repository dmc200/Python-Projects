    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
	return self.original_function(*args, **kwargs)