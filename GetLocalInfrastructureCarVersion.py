import commands
import re

def GetLocalInfrastructureCarVersion():
    # Use "./fglcmd.sh -cmd cartridge:list to get all cartridges' information
    allLocalCartridgesInformation = commands.getoutput('cd /home/admin/Dell/Foglight/bin && ./fglcmd.sh -cmd cartridge:list')

    # Use regex to get the Infrastructure Cartridge part information
    matchPosition = re.search('.*Infrastructure\n.*\n.*\n.*', allLocalCartridgesInformation).span()
    infrastructureCarInformation = allLocalCartridgesInformation[matchPosition[0]:matchPosition[1]]

    # Use regex to get the Infrastructure Cartridge version build
    matchPosition = re.search('\d(\.\d)+\-\d+.*', infrastructureCarInformation).span()
    infrastructureCarVersion = infrastructureCarInformation[matchPosition[0]:matchPosition[1]]
    print "\nThe local Infrastructure version is: " + infrastructureCarVersion + "\n"

    return infrastructureCarVersion
