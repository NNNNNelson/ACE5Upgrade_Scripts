import ftplib
import re
import socket

# Visit FTP to get the FTP newest Infrastructure Car build number


def GetFTPNewestInfrastructureCarBuild():
    # Logon FTP and go to Infrastructure 5.8.5.7 branch
    HOST = '10.30.155.32'
    Infrastructure_5857_branch = 'nightly/Infrastructure/5.8.5.7/'

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
        f.cwd(Infrastructure_5857_branch)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % Infrastructure_5857_branch
        f.quit()
    print '***Changed to "%s" folder' % Infrastructure_5857_branch

    # Get the newest FTP Domino.7 FMS build number
    allFolderInInfrastructure5857Branch = f.nlst()
    ftpNewestBuildFull = allFolderInInfrastructure5857Branch[-1]
    print '\nThe newest Infrastructure 5.8.5.7 build in FTP is: ' + ftpNewestBuildFull
    # matchPosition = re.search('\d+$', ftpNewestBuildFull).span()
    # ftpNewestBuild = ftpNewestBuildFull[matchPosition[0]:matchPosition[1]]

    # Quit the FTP
    f.quit()

    # Return the FTP Domino.7 newest build number
    return ftpNewestBuildFull
