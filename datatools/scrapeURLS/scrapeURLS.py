#!/usr/bin/python
import sys, os, urllib2, json, urllib, requests

# Read file and return cropped file, or random sample.
def process_file(file_path, limit, selector):
    # Total number lines
    f = open(file_path, 'r')
    lines = f.readlines()
    line_count = file_len(file_path)
    print "Total number urls: " + str(line_count)

    count = 0
    text = ''
    for line in lines:
        if count < int(limit):
            file_name = "file_" + str(count) + '.html'
            url = line
            processURL(url, file_name, selector)
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

# Get length of file.
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def processURL(url, file_name, selector):
    # Loading URL.
    print "Loading " + url
    
    r = requests.get(url)
    content = r.content
    
    storeURLResults(content, file_name, selector)


def storeURLResults(text, file_name, selector):
    # Store results from visit to web page.
    with open("output/" + file_name, "wb") as f:
        content = limitResultsBySelector(text,selector)
        f.write(content)

def limitResultsBySelector(text,selector):
    # Find selector in results.
    # Return results from selector.

    #http://www.briancarpio.com/2012/12/02/website-scraping-with-python-and-beautiful-soup/
    #soup = BeautifulSoup(urllib2.urlopen('http://www.usamega.com/mega-millions-history.asp?p=1').read())
    return text

    # @TODO write

# Main program. Read system arguments, read file, make output file.
def main():
    # Create list of files.
    file_list = []
    
    if len(sys.argv) > 1:
        input_path = str(sys.argv[1])

        if input_path.endswith(".csv"):
            file_list.append(file)

            if len(sys.argv) > 2:
                limit = str(sys.argv[2])
            else:
                limit = 10

            if len(sys.argv) > 3:
                selector = str(sys.argv[3])
            else:
                print "No selector given"  
                selector = ''

            url_results = process_file(input_path, limit, selector)

        else:
            "File supplied not CSV"

    else: 
        print "No file given"



main()
  
print "Done."

sys.exit()
