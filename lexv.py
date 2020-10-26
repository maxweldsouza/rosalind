import itertools

def lexv():
    for x in itertools.product('DNA ', repeat=3):
        print x

lexv()