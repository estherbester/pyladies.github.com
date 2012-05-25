from sys import argv

filename = argv[1]


f = open(filename, 'r')
lines = f.readlines()
f.close()

newlines = []
no_more = False
for line in lines:
    if no_more == False and line[0:4] == "----":
        newlines.append(line)
        newlines.append("\n:tags: Archive\n:category: Blog\n")
        no_more = True
    else:
        newlines.append(line)

f = open(filename, 'w')
f.writelines(newlines)
f.close()