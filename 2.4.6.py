import os.path
print(os.name)
print(os.getcwd())
print(os.curdir)
endpath = 'main'
os.chdir(("D:\\Programming\\"+endpath))
print(os.getcwd())
os.chdir("D:\\Programming\\")
print(os.getcwd())

listDirs = []
print("---------")
try:
    for root, dirs, files in os.walk('main'):
#        print(dirs, '-', files)
        for i in files:
            if i.endswith(".py"):
                listDirs.append(root)
                break
except TypeError:
    print("wall does not work")
#os.startfile("filein.txt")
#print(os.listdir())
for _ in listDirs:
#    print(_.replace(os.getcwd(), endpath))
    print(_)