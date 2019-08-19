import commands
import time

def stopCurrentRunningFMS():
    print 'Stopping the current running FMS...'
    commands.getoutput('cd /home/admin/Quest/Foglight/bin && sudo -u admin ./fms -q')
    time.sleep(30)
    print 'The running FMS is stopped.'
    return
