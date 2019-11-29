
def fileread_str(f, n=None):
    '''reads a string of n chars from file or entire file '''
    fileref = open(f,"r")
    chars = fileref.read(n)  
    fileref.close()
    return chars    

def filelines2(f, n=None):
    '''Returns a list of strings, each representing a single line of the file. 
    If n is not provided then all lines of the file are returned. If n is provided then n 
    characters are read but n is rounded up so that an entire line is returned'''
    
    fileref = open(f,"r")
    lines = fileref.readlines(n) #returns a list of strings
    fileref.close()
    return lines

def fileread_list(f, n=None):
    '''Returns a list of strings, each representing a single line of the file. 
    If n is not provided then all lines of the file are returned. If n is provided then n 
    characters are read but n is rounded up so that an entire line is returned'''
    
    with open(f,"r") as fileref:
        lines = fileref.readlines(n) #returns a list of strings
    return lines

def filewrite(f):
    with open(f,'w') as outfile:
        for number in range(1,10):
            sq = number * number
            outfile.write(str(sq) + "\n")

    
# afile = 'files/school_prompt2.txt'
# print("Char count {} in {} lines".format(len(filestr(afile)), len(filelines(afile))))
# print(filestr(afile, 40))
# 
# filewrite("files/testwrite.txt")
# infile = filelines("files/testwrite.txt")
# print(infile)

# afile = 'files/studentdata.txt'
# lines = filelines(afile)
# for line in lines:
#     scores = line.split()
#     if len(scores) > 6:
#         print(scores[0])


afile = 'files/travel_plans.txt'
lines = fileread_list(afile)
destination = []
for line in lines:
    if ':' in line:
        destination.append(line)
print(destination)

