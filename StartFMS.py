import subprocess

def startFMS():
	print 'Has started the upgraded FMS'
	subprocess.call('sudo -u admin /home/admin/Quest/Foglight/bin/fms -d', shell=True)
	return
