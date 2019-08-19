import commands
import re
import ftplib
import socket
import os
import GetLocalFMSBuild
import GetFTPFMSNewestBuild
import DeleteOldInstallers
import DownloadNewestACE5InstallationFile
import StopCurrentRunningFMS
import SilentUpgradeFMS
import StartFMS


def main():
    # Get the local FMS build number
    localBuild = GetLocalFMSBuild.GetLocalFMSBuild()

    # Visit FTP to get the FTP newest FMS build number
    ftpNewestBuild = GetFTPFMSNewestBuild.GetFTPFMSNewestBuild()

    # If localBuild < ftpNewestBuild (local FMS is older than FTP newest FMS), download the newer FMS installation file from FTP
    # Else do nothing and exit program
    if int(localBuild) < int(ftpNewestBuild):
        print 'The FTP FMS build is newer than local FMS build, prepare to upgrade FMS...'
	print 'Deleting old installers...'
	DeleteOldInstallers.DeleteOldInstallers()
	print 'Downloading FTP newer FMS build installation bin file...'
        downloadedNewestFMSInstallationFile = DownloadNewestACE5InstallationFile.DownloadNewestACE5InstallationFile(
            ftpNewestBuild)
        StopCurrentRunningFMS.stopCurrentRunningFMS()
        SilentUpgradeFMS.silentUpgradeFMS(downloadedNewestFMSInstallationFile)
        StartFMS.startFMS()
        print 'Program executing finished. Bye~'
    else:
        print 'The local ACE build is the newest, do not need to upgrade.'
        print 'Program executing finished. Bye~'

    return

if __name__ == '__main__':
    main()
