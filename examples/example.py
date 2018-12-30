from errs import errs

@errs
def raises(): #type () -> int
    raise Exception()
    return 0

def check_error(): #type: () -> None
    out, err = raises()
    print('Error: {err}'.format(err.check()))

if __name__ == '__main__':
    check_error() #prints Error: True
