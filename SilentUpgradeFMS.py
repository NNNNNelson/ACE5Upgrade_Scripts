import subprocess
import time


def silentUpgradeFMS(downloadedNewestFMSInstallationFile):
    print 'Upgrading FMS to new version...'
    subprocess.call(
        'chmod +x ' + downloadedNewestFMSInstallationFile, shell=True)
    subprocess.call('cd /home/admin/Downloads/ && sudo -u admin ' + downloadedNewestFMSInstallationFile +
                    ' -i silent -f /home/admin/Downloads/ACE5_fms_silent_install.properties', shell=True)
    time.sleep(180)
    return
