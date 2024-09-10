
x = -1


# raise Exception('x should be positive')
# assert(x>=0), 'x is not positive'


try:
    a = 5/1
    b = a + '1'
except ZeroDivisionError as e:
    print(e)
except Exception as ex:
    print(ex)
else: 
    print('everything went fine')
finally:
    print('wrappijng up...')


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5 :
        raise ValueTooSmallError('value is to small', x)
    



try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.messagem, e.value)
else:
    print('valid value')


        