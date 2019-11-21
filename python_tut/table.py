# table.py

def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    for colname in colnames:
        print(f'{colname :>10s}', end=' ')
    print()

    for obj in objects:
        for colname in colnames:
            print(f'{str(getattr(obj, colname)) :>10s}', end=' ')
        print()
