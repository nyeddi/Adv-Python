class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        pass

class email_logit(logit):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''
    def __init__(self, func, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super().__init__(func, *args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        print("sending email to ", self.email)
        pass

logit._logfile = 'out2.log' # if change log file
#@logit
@email_logit
#@logit
def myfunc1():
    pass

myfunc1()