import ftplib
import re
import socket

# Visit FTP to get the FTP newest FMS build number


def GetFTPFMSNewestBuild():
    # Logon FTP and go to ACE branch
    HOST = '10.30.181.125'
    ACE_BRANCH = 'nightly/FoglightServerDist/branches/ACE.5/'
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print 'ERROR:cannot reach "%s"' % HOST
    print '***Connected to host "%s"' % HOST
    try:
        f.login('foglight', 'foglight')
    except ftplib.error_perm:
        print 'ERROR: cannot login'
        f.quit()
    print '***Logged in successfully'
    try:
        f.cwd(ACE_BRANCH)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % ACE_BRANCH
        f.quit()
    print '***Changed to "%s" folder' % ACE_BRANCH
    # Get the newest FTP ACE FMS build number
    allFolderInACEBranch = f.nlst()
    ftpNewestBuildFull = allFolderInACEBranch[-1]
    print '\nThe newest ACE.5 FMS build in FTP is: ' + ftpNewestBuildFull
    matchPosition = re.search('\d+$', ftpNewestBuildFull).span()
    ftpNewestBuild = ftpNewestBuildFull[matchPosition[0]:matchPosition[1]]

    # Quit the FTP
    f.quit()

    # Return the FTP ACE newest build number
    return ftpNewestBuild
