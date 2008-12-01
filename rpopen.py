from subprocess import Popen, PIPE

class RemoteError(Exception):
    def __init__(self, message, stderr):
        super(RemoteError, self).__init__(message)
        self.stderr = stderr


class RPopen(object):

    def __init__(user, host, *args, **kwargs):

        if cmd is None:
            cmd = []
        p = Popen(['ssh',
                   '-n',
                   '-o', 'StrictHostKeyChecking no',
                   '-l', 'root',
                   host,
                   ] + cmd,
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if return_both:
            return stdout, stderr

        if p.returncode:
            raise RemoteError("Error running %r at %s@%r" % (cmd, 'root', host), stderr)
        else:
            return stdout
