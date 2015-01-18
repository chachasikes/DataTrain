#!/usr/bin/python
import sys, os, urllib2, json, urllib, requests,datetime
from bs4 import BeautifulSoup

# Read file and return cropped file, or random sample.
def process_file(file_path, limit, selector, process_only):
    # Total number lines
    f = open(file_path, 'r')
    lines = f.readlines()
    line_count = file_len(file_path)
    print "Total number urls: " + str(line_count)


    count = 0
    text = ''
    csv_object_array = []
    for row in lines:
        if count < int(limit):
            row = row.strip('\n')
            line = row.split(',')

            file_name = str(line[2]) + "_" + str(line[1])
            url = line[0]
            csv_object = processURL(url, file_name, selector, process_only)
            csv_object_array.append(csv_object)
            count = count + 1

    saveCSV(csv_object_array)

    print "Saved new file with " + str(limit) + " rows at: "

    f.close()
    return text


def saveCSV(csv_object_array):
    csv_file_name =  datetime.date.today().strftime("%Y-%B-%d")

    csv_out = open("output/csv/" + csv_file_name + ".csv","w")
    csv_out.seek(0)

    csv = buildCSV(csv_object_array)

    csv_out.write(csv)

    csv_out.truncate()
    csv_out.close()

def buildCSV(csv_list):
    output = ''


    # Build complete attribute list from all csv objects.
    attributes = []

    # @TODO Group by dataset name

    for record in csv_list:
      keys = record.keys()
      attributes_set = set(attributes)
      keys_set = set(keys)

      difference = keys_set - attributes_set

      full_attributes = attributes + list(difference)

    print full_attributes

    rebuilt_csv_list = []

    for item in csv_list:
      csv_object = {}

      for attribute in full_attributes:

        if item[attribute] == "None":
          csv_object[attribute] = "NULL"
        else:
          csv_object[attribute] = item[attribute]

      rebuilt_csv_list.append(csv_object)


    counter = 0
    for record_item in rebuilt_csv_list:

      if counter == 0:      
        for label_attr, label_value in record_item.items():
            output = output + "'" + label_attr + "',"
        output = output + '\n'
      
      for attr, value in record_item.items():
          output = output + "'" + value + "',"

      

      counter = counter + 1
      output = output + '\n'
    return output



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


def processURL(url, file_name, selector,process_only):
    # Loading URL.
    # print "Loading " + url

    results = storeURLResults(url, file_name, selector,process_only)
    output = compressResultsCSV(file_name, results)

    return output

def compressResultsCSV(file_name, results):
    count = 0
    lines = results.split('\n')
    output = ''

    csv_object = {}

    for line in lines:
      l = line.split(',')

      csv_object['File Name'] = file_name

      if count == 0:
        csv_object['Dataset Name'] = l[0]

        if len(l) > 1:
          csv_object['Dataset Description'] = l[1]

      else:
          if len(l) > 1:
              csv_object[l[0].strip(':')] = l[1]
      count = count + 1

    return csv_object

def storeURLResults(url, file_name, selector, process_only):
    # Store results from visit to web page.
    if process_only == True:
      with open("output/processed/" + file_name + ".txt", "wb") as write_file:
          # print "Processing data only."
          with open("output/raw/" + file_name + ".html", 'r') as read_file:
            text = read_file.read()
            content = getFileNameDetails(text,selector)
            content = content + getFileDescriptionDetails(text,selector) + '\n'
            content = content + limitResultsBySelector(text,selector)
            write_file.write(str(content) + "\n")
            return str(content)
    else:
        r = requests.get(url)
        text = r.content

        with open("output/raw/" + file_name + '.html', "wb") as f:
            f.write(text)

        with open("output/processed/" + file_name + ".txt", "wb") as f:
            content = getFileNameDetails(text,selector)
            content = content + getFileDescriptionDetails(text,selector) + '\n'
            content = content + limitResultsBySelector(text,selector)
            f.write(str(content) + "\n")
            return str(content)

def getFileNameDetails(text,selector):
    output = ''
    soup = BeautifulSoup(text)

    # Name
    name_selector = selector[0].split(' ')
    last_selector = name_selector.pop()
    name_selector = ' '.join(name_selector)

    result_name = soup.select(name_selector)

    for r in result_name:
      
      div = r.find_all(last_selector)

      for d in div:
        if d != []:
          value = str(d.string).strip()
    return value + ","


def getFileDescriptionDetails(text,selector):
    output = ''
    soup = BeautifulSoup(text)

    # Name
    name_selector = selector[1].split(' ')
    last_selector = name_selector.pop()
    name_selector = ' '.join(name_selector)

    result_name = soup.select(name_selector)

    for r in result_name:
      div = r.find_all(last_selector)
      
      for d in div:
        value = str(d.string).strip()

    return value

def limitResultsBySelector(text,selector):
    # Find selector in results.
    # Return results from selector.

    #http://www.briancarpio.com/2012/12/02/website-scraping-with-python-and-beautiful-soup/
    soup = BeautifulSoup(text)
    # Content
    result = soup.select(selector[2])
    output = ''
    for r in result:
      div = r.find_all('div')
      d_count = 0
      for d in div:
        value = str(d.string)
        output = output + value.strip()
        if d_count < len(div) - 1:
          output = output + ","
        d_count = d_count + 1
      output = output + "\n"
    return output


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
                selector = selector.split(',')
            else:
                print "No selector given"
                selector = ''

            process = False

            if len(sys.argv) > 4:
                process_only = str(sys.argv[4])
                print process_only
                if process_only == 'process-only':

                  process = True



            url_results = process_file(input_path, limit, selector, process)

        else:
            "File supplied not CSV"

    else:
        print "No file given"



main()

print "Done."

sys.exit()
