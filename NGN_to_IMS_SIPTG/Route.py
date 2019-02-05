import csv


def processData():
    minRTNum = 600
    maxRTNum = 10000
    blackListedRT = [
        # TGs to be blacklisted in int form,
        # 601,
        # 602,
    ]

    rKeys = [
        "Route No.",
        "Route Name",
        "Subroute Sel.Mode",
        "Per of Dir Subroutes",
        "Percentage 2",
        "Percentage 3",
        "Percentage 4",
        "1st sub-route",
        "2nd sub-route",
        "3rd sub-route",
        "4th sub-route",
    ]
    pKey = rKeys[0]
    fileName = "Bam-tbl_Route.csv"
    with open(fileName, "r") as fileObj:
        data = list(csv.reader(fileObj))
        data = [list(map(lambda s: s.replace("'0", "0"), row)) for row in data]

        headers = data[4]
        print("Available headers in file: ", fileName)
        print(headers)
        print("Required headers: ")
        print(rKeys)

        data = data[5:]
        data = [[row[headers.index(k)] for k in rKeys] for row in data]

        # filter data
        data = list(filter(lambda row: minRTNum <= int(row[rKeys.index(pKey)]) <= maxRTNum, data))
        data = list(filter(lambda row: int(row[rKeys.index(pKey)]) not in blackListedRT, data))
        data = sorted(data, key=lambda row: int(row[rKeys.index(pKey)]))
        # additional filter data
        # data = list(filter(lambda row: row[rKeys.index("Circuit type")] == "SIP", data))

        # insert header
        data.insert(0, rKeys)
        print("1(Header) +", str(len(data) - 1), "lines of data collected.")
        return data
