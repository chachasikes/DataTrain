#!/usr/bin/python
import sys, os

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def process_file(file_path, limit):
    # Total number lines
    


    f = open(file_path, 'r')
    lines = f.readlines()
    line_count = file_len(file_path)
    print "Total number lines: " + str(line_count)

    count = 0
    text = ''
    for line in lines:
        if count < int(limit):
            text = text + line
            count = count + 1

    print "Saved new file with " + str(limit) + " rows at: "
    f.close()

    return text

def save_sample(text, output_file_name):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    print current_directory + "/" + output_file_name
    fout = open("output/" + output_file_name,"w")
    fout.seek(0)
    fout.write(text)
    fout.truncate()
    fout.close()

def main():
    # Create list of files.
    file_list = []
    
    if len(sys.argv) > 1:
        input_path = str(sys.argv[1])

        if input_path.endswith(".csv"):
            file_list.append(file)

            if sys.argv[2]:
                output_file_name = str(sys.argv[2])
            else:
                "No output file name given"  

            if len(sys.argv) > 3:
                limit = str(sys.argv[3])
            else:
                limit = 100
            
            csv_sample = process_file(input_path,limit)
            save_sample(csv_sample, output_file_name)

        else:
            "File supplied not CSV"

    else: 
        print "No file given"

main()
