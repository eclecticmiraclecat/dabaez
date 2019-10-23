class Manager:

    def __enter__(self):
        print('entering')
        return 'some value'

    def __exit__(self, ty, val, tb):
        print('exiting')
        print(ty, val, tb)