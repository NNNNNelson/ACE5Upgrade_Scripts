import ftplib
import commands


def DownloadNewestACE5InstallationFile(ftpNewestBuild):
    HOST = '10.30.181.125'
    ACE_BRANCH = '/nightly/FoglightServerDist/branches/ACE.5/'
    INSTALL_OS_TYPE = 'linux-x86_64'
    FILE = 'Foglight-5_9_5-install_linux-x86_64.bin'
    downloadDestinationPrefix = '/home/admin/Downloads/ACE5_'
    # Login FTP
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print 'ERROR: cannot reach "%s"' % HOST
    try:
        f.login('foglight', 'foglight')
    except ftplib.error_perm:
        print 'ERROR: cannot login'
        f.quit()
    # Go to newest ACE build linux x64 path
    try:
        f.cwd(ACE_BRANCH)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % ACE_BRANCH
        f.quit()
    allFolderInACEBranch = f.nlst()
    ftpNewestBuildFull = allFolderInACEBranch[-1]
    ftpNewestBuildPath = ACE_BRANCH + ftpNewestBuildFull + '/'
    ftpNewestBuildLinuxX64Path = ftpNewestBuildPath + INSTALL_OS_TYPE + '/'
    try:
        f.cwd(ftpNewestBuildLinuxX64Path)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % ftpNewestBuildLinuxX64Path
        f.quit()
    downloadFolder = downloadDestinationPrefix + ftpNewestBuild
    commands.getoutput('mkdir ' + downloadFolder)
    downloadDestination = downloadDestinationPrefix + ftpNewestBuild + '/' + FILE
    try:
        f.retrbinary('RETR %s' % FILE, open(downloadDestination, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to "%s"' % (FILE, downloadDestination)
    f.quit()
    return downloadDestination
