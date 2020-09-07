import os, shutil
from glob import glob
os.chdir("A:\Anime\Ghost in the Shell Stand Alone Complex (2020)\Season 3")
location = os.getcwd()

def getSelfFolder(path):
    path = path.split("\\")#split by folder structure
    return path[-1]

def run():
    print("Starting............")

    print("Gathering files.....")
    #result = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], "*"))]
    for count, filename in enumerate(os.listdir(os.getcwd())):
        src = os.getcwd() + "\\" + filename#define original filename
        #print(src)
        if os.path.isfile:
            workname = filename.split(" ")#change it into what we want
            maldname = ""

            #---------------------------------------------------->>>>
            # OPTION 1 ----- Adding an E for abosolute number episode ordering
            # This part adds the episode indicator on the number in the name of the file
            # Python starts list numbering at zero, so "[Judas] ANIME TITLE - 100" could be workname[4], or workname[-1]
            
            workname[7] = "S03E" + (str(1+count) if 1+count>=10 else "0" + str(1+count))

            for w in workname:
                maldname = maldname + w + " "
            
            #----------------------------------------------------<<<<
            
            #---------------------------------------------------->>>>
            # OPTION 2 ----- Manual labeling of all episodes in a season
            
            #maldname = "Mr.Robot S03E" + (str(1+count) if 1+count>=10 else "0" + str(1+count))+ ".srt"
            
            #----------------------------------------------------<<<<
            
            dst = os.getcwd() + "\\" + maldname#define new filename
            print(workname)
            os.rename(src, dst) 

    #print("Adding characters...")
    #for f in result

print("Working directory: " + location)

while True:
    parsed = input().split(" ")
    if parsed[0] == "cd":
        os.chdir(parsed[1])
        print(os.getcwd())
    elif parsed[0] == "cwd":
        print(os.getcwd())
    elif parsed[0] == "ls":
        f = os.listdir(os.getcwd())
        files = []
        folders = []
        for j in f:#for files in list
            if os.path.isfile(j):
                files.append(j)
            else:
                folders.append(j)
        #folders first
        for h in folders:
            print("[" + h + "]")
        for h in files:
            print(h)
    elif parsed[0] == "run":
        run()
        break
    elif parsed[0] == "exit":
        break

print("Done")    
#else:
#    print("Goodbye")