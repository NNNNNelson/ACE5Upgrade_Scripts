import os

def DeleteOldInstallers():
    os.system('ls -1d /home/admin/Downloads/* | grep -P ACE5_\\\\d+ | xargs -I {} rm -rf {}')
