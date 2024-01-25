import os
import re

# Changing a directory to "/home/newdir"
working_dir = r"C:\Users\ROBLEE\OneDrive - DNV\Documents-ARHL407909\My Documents\62443\62443-3-3"
working_dir = r"C:\Users\ROBLEE\OneDrive - DNV\Documents-ARHL407909\My Projects\7. NextGen EA\62443-3-3"
working_dir = r'C:\tmp\Golden SCL for SCT'
#file_in = "ServerDyn.iid"



def regular(line):
    # https://www.tutorialspoint.com/python/python_reg_expressions.htm
    line = re.sub(r'^\s*', "", line) # Remove spaces on beginning of the line   
    line = re.sub(r'^\d+\s+', "<H1>", line) # Heading 1
    line = re.sub(r'^\d+\.\d+\s+', "<H2>", line) # Heading 2
    line = re.sub(r'^\d+\.\d+\.\d+\s+', "<H3>", line) # Heading 3
    line = re.sub(r'^\d+\.\d+\.\d+\.\d+\s+', "<H4>", line) # Heading 4
    return line

def sclline(line):
    # https://www.pythontutorial.net/python-regex/python-regex-backreferences/
    line2 = re.sub(r'(.*\<SCL.*revision=".").*(>)', r'\1 release="4"\2',line) # Insert release=4 at the end for <SCL 
    line2 = re.sub(r'(.*\<IED name=.*)(owner=".*">)', r'\1originalSclRelease="4" \2',line2) # insert originalSclRelease="4" before owner for eacht <IED name=
    if line2 != line:
        print(line)
        print(line2)
    return line2

def amain():
    s = 'Python Python is awesome'

    new_s = re.sub(r'(\w+)\s+', r'a\1dss', s)

    print(new_s)

def main():

    os.chdir(working_dir)
    print(f'Working directory: {os.getcwd()}')
    
    #get all files in working directory
    files = [f for f in os.listdir() if os.path.isfile(f)]
 
    for file_in in files:
    
        with open(file_in, mode="r", encoding='utf-8') as fp: #encoding='utf-16' or 'ansi'
            Lines = fp.readlines()
            for count in range(len(Lines)):

                # Modify line with regular expression
                Lines[count] = sclline(Lines[count])

                #print(Lines[count])
            
        file_out = fr'..\Golden SCL for SCT Ed2.1\{file_in}x'
        with open(file_out, "w+", encoding='utf-8') as fp:
            fp.writelines(Lines)
            print(f"File written: {file_out} to {working_dir}")

if __name__=="__main__":
    main()
    print("End")    

