import os
import sys
import csv
from pprint import pprint


def checkFolder(folder):
    print("Accessing folder: " + folder)
    if os.path.exists(folder):
        print("Folder exists.")
        if os.path.isdir(folder):
            print("Given folder is a directory.")
        else:
            print("Given folder is not a directory.")
            print("Exiting.")
            sys.exit(1)
    else:
        print("Fodler doesn't exist.")
        print("Exiting...")
        sys.exit(1)

    os.chdir(folder)


def checkFiles():
    files = [
        "Bam-tbl_TrunkGroup.csv",
        #"Bam-tbl_SubTrkGrp.csv",
        #"Bam-tbl_CalleeAna.csv",
        #"Bam-tbl_CallerDistGroupISP.csv",
        #"Bam-tbl_CallPreProc.csv",
        #"Bam-tbl_DBChange.csv",
        #"Bam-tbl_Route.csv",
        #"Bam-tbl_RouteAna.csv",
        #"Bam-tbl_SipIPPairConfig.csv",
        #"Bam-tbl_SubRoute.csv",
        #"Bam-tbl_TrkGrpToDistGrp.csv",
        #"BOSBC4_Dump_20180603.txt",
        #"SOSBC4_Dump_20180603.txt",
        #"table_bitField_sCodecList.xlsx",
        ]
    print ("Checking files...")

    dirList = os.listdir()
    missing = False
    missingFiles = []
    for required in files:
        if (required in dirList) and os.path.isfile(required):
            print("Found file: ", str(required))
        else:
            print("Not found file: ", str(required))
            missing = True
            missingFiles.append(required)
    if missing:
        print("Following Files are missing:")
        pprint(missingFiles)
        print("Available Files in the folder:")
        pprint(dirList)
        print("Exiting...")
        sys.exit(1)


def getCSVWriter():
    outputFileName = "subscriber list"

    p = os.path.join(os.getcwd(), "output")
    if not os.path.exists(p):
        os.mkdir(p)
        print("Directory created: ", p)
    else:
        print("Output directory exists: ", p)

    outFile = open(os.path.join(p, outputFileName + ".csv"), "w", newline="")
    outputWriter = csv.writer(outFile)

    return outputWriter


def writeCSVData(data, writer):
    for row in data:
        writer.writerow(row)


