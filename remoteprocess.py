from subprocess import Popen, PIPE

class RPopen(Popen):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', 'root')
        host = kwargs.pop('host')
        self.user, self.host = user, host

        if 'cmd' in kwargs:
            cmd = kwargs['cmd']
        else:
            cmd = args[0]

        cmd = ['ssh',
               '-n',
               '-l', user,
               host,
               ] + cmd

        if 'cmd' in kwargs:
            kwargs['cmd'] = cmd
        else:
            args = (cmd,) + args[1:]

        super(RPopen, self).__init__(*args, **kwargs)

