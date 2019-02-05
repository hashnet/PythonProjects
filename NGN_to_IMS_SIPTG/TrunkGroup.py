import csv


def processData():
    minTGNum = 600
    maxTGNum = 10000
    blackListedTG = [
        # TGs to be blacklisted in int form,
        # 601,
        # 602,
    ]

    rKeys = [
        "Trunk group number",
        "Call-in authority",
        "Call-out authority",
        "Trunk group name",
        "Call source code",
        "Circuit type",
        "Default caller number",
        "Idle circuits for weak call restriction",
        "Idle circuits for forced call restriction",
    ]
    pKey = rKeys[0]
    fileName = "Bam-tbl_TrunkGroup.csv"
    with open(fileName, "r") as fileObj:
        data = list(csv.reader(fileObj))
        data = [list(map(lambda s: s.replace("'0", "0"), row)) for row in data]

        headers = data[4]
        print("Available headers in file: ", fileName)
        print(headers)
        print("Required headers: ")
        print(rKeys)

        data = data[5:]
        # temp = []
        # for row in data:
        #     d = {headers[i]: row[i] for i in range(0, len(row))}
        #     nd = {k: d[k] for k in rKeys}
        #     temp.append(nd)
        # data = temp
        ###### data = [{k: {headers[i]: row[i] for i in range(0, len(row))}[k] for k in rKeys} for row in data]

        # data = list(filter(lambda d: minTGNum <= int(d[pKey]) <= maxTGNum, data))
        # data = list(filter(lambda d: int(d[pKey]) not in blackListedTG, data))
        # data = list(filter(lambda d: d["Circuit type"] == "SIP", data))
        #
        # data = sorted(data, key=lambda d: int(d[pKey]))
        data = [[row[headers.index(k)] for k in rKeys] for row in data]

        # filter data
        data = list(filter(lambda row: minTGNum <= int(row[rKeys.index(pKey)]) <= maxTGNum, data))
        data = list(filter(lambda row: int(row[rKeys.index(pKey)]) not in blackListedTG, data))
        data = sorted(data, key=lambda row: int(row[rKeys.index(pKey)]))
        # additional filter data
        data = list(filter(lambda row: row[rKeys.index("Circuit type")] == "SIP", data))

        # insert header
        data.insert(0, rKeys)
        print("1(Header) +", str(len(data) - 1), "lines of data collected.")
        return data
