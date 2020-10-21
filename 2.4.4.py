with open ("D:\Programming\\filein.txt") as filein, open("d:\Programming\\fileout.txt", 'w') as fileout:
#    fileout.writelines(filein.readlines().__reversed__())
    fileout.writelines(reversed(filein.readlines()))
