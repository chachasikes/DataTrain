#!/usr/bin/python
import sys, os
import random

# Get length of file.
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Read file and return cropped file, or random sample.
def process_file(file_path, limit, is_random):
    # Total number lines
    f = open(file_path, 'r')
    lines = f.readlines()
    line_count = file_len(file_path)
    print "Total number lines: " + str(line_count)

    count = 0
    text = ''
    print bool(is_random)
    if bool(is_random):
        sample = random.sample(lines, int(limit))
        for line in sample:
                if count < int(limit):
                    if count == 0:
                        text = lines[0]
                    else:
                        text = text + line
                    count = count + 1
    else:
        for line in lines:
            if count < int(limit):
                text = text + line
                count = count + 1

    print "Saved new file with " + str(limit) + " rows at: "
    f.close()
    return text

# Save sample as file.
def save_sample(text, output_file_name):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    print current_directory + "/" + output_file_name
    fout = open("output/" + output_file_name,"w")
    fout.seek(0)
    fout.write(text)
    fout.truncate()
    fout.close()

# Main program. Read system arguments, read file, make output file.
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


            if len(sys.argv) > 4:
                random = str(sys.argv[4])
            else:
                random = false

            csv_sample = process_file(input_path,limit,random)
            save_sample(csv_sample, output_file_name)

        else:
            "File supplied not CSV"

    else: 
        print "No file given"

main()
