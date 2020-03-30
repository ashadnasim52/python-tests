# To ran all test
#  python3 -m unittest


def funcname(num):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter any number'
    except ValueError as err:
        return err
