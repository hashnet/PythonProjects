import re

string = """23423423423"""

while True:
    print()
    print("Please insert the regex pattern [Press enter to exist]")
    pattern = input("Pattern: ")
    if pattern == '':
        break

    try:
        regex = re.compile(pattern)
    except Exception as err:
        print("Incorrecrt Pattern: ", err)
        continue

    print("String: ", string)
    print("Entered Pattern: ", pattern)

    mo = regex.search(string)
    if mo is None:
        print("No match found.")
        continue

    print("Match found.")
    print("Complete match: ", mo.group())
    print("List of groups: ", mo.groups())
    print("Groupwise match: ")
    for i in range(1, len(mo.groups())+1):
        print("Group[{}]: {}".format(i, mo.group(i)))

