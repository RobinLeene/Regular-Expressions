import os
import re

# Changing a directory to "/home/newdir"
working_dir = r'C:\tmp\Golden SCL for SCT'

def scl_line(line):
    # https://www.pythontutorial.net/python-regex/python-regex-backreferences/
    line2 = re.sub(r'(.*\<SCL.*revision=".".*)(>)', r'\1 release="4"\2',line) # Insert release=4 at the end for <SCL 
    line2 = re.sub(r'(.*\<IED name=.*)(owner=".*">)', r'\1originalSclRelease="4" \2',line2) # insert originalSclRelease="4" before owner for eacht <IED name=
    if line2 != line:
        print(f'Original Line: {line}')
        print(f'New Line: {line2}')
    return line2

def main():

    os.chdir(working_dir)
    print(f'Working directory: {os.getcwd()}')
    
    #get all files in working directory no subdirectory
    files = [f for f in os.listdir() if os.path.isfile(f)]
 
    for file_in in files:
        
        print(f'\n======= File: {file_in} ========')
        
        # change lines from file
        with open(file_in, mode="r", encoding='utf-8') as fp: #posible encoding like 'utf-16' or 'ansi'
            Lines = fp.readlines()
            for count in range(len(Lines)):
                Lines[count] = scl_line(Lines[count]) # Modify line with regular expression
                
        # Write all and updated lines to new file (file_out)    
        file_out = fr'..\Golden SCL for SCT Ed2.1\{file_in}' # f = formatted string literals r = raw string' default unicode
        with open(file_out, "w+", encoding='utf-8') as fp:
            fp.writelines(Lines) # Write all new lines to new file
            print(f"File written: {file_out} to {working_dir}")
    print("\nEnd")           

if __name__=="__main__":
    main()
