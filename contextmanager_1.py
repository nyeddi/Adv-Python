import contextlib

@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise

with propagater("naveen", False) as f:
    print("inside context manager")
    raise Exception()

##########################
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled