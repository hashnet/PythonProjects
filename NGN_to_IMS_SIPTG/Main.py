import pprint

import FileHandle
import Merge
import TrunkGroup
import SubTrunkGroup
import Route

folder = r"/Users/maidul/PythonProjects/NGN_to_IMS_SIPTG/NGN DB for SIP Trunk"

FileHandle.checkFolder(folder)

FileHandle.checkFiles()

writer = FileHandle.getCSVWriter()

max = 10
tg = TrunkGroup.processData()
for row in tg[:max]: print(row)

subtg = SubTrunkGroup.processData()
for row in subtg[:max]: print(row)

rt = Route.processData()
for row in rt[:max]: print(row)

data = Merge.mergeOnIndex(tg, "Trunk group number", subtg, "Trunk group number")
for row in data[:max]: print(row)



FileHandle.writeCSVData(rt, writer)
