import os
for root,directories,filenames in os.walk(r'E:\Videos\favor'):
    #print(root)
    for filename in filenames:
        if filename.split('.')[1]=='jpg':
            print(filename)
            os.startfile(root+os.sep+filename)
            input()
