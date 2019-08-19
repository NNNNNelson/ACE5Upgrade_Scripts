import commands
import re


def GetLocalFMSBuild():
    # Use 'fms -v' command to get the FMS version content
    localFMSVersionFull = commands.getoutput(
        'cd /home/admin/Quest/Foglight/bin && ./fms -v')
    print "Executing 'fms -v' command to get FMS version content...\nGot result below:\n##########################\n" + localFMSVersionFull + '\n##########################\n'

    # Use regex to get the full build string part from FMS version content
    matchPosition = re.search('\d\..*\-\d+\-\w+\-\d+',
                              localFMSVersionFull).span()
    localBuildFull = localFMSVersionFull[matchPosition[0]:matchPosition[1]]

    # Use regex to get the final build number part form full build string
    matchPosition = re.search('\d+$', localBuildFull).span()
    localBuild = localBuildFull[matchPosition[0]:matchPosition[1]]
    print 'The local FMS build is: ' + localBuildFull + '\n'

    # Return the localBuild
    return localBuild
