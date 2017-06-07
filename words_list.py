fo = open("foo.txt", "r")
fo2 = open("foo.txt", "w")
fo3 = open("fe.txt", "w")
fo4 = open("foofinal.txt", "w")
for line in fo:
    fo2.write(line.replace(" 	", ","))

fo.close()
fo2 = open("foo.txt.temp", "r")
for line in fo2:
    fo3.write(line.replace("\n", ","))
fo2.close()
fo3 = open("fe.txt", "r")
for line in fo3:
    fo4.write(line.replace("    ", ""))
fo3.close()
fo4.close()
