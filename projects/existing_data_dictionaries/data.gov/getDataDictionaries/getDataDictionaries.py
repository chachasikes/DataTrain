#!/usr/bin/python
import sys, os, urllib2, json, urllib, requests, datetime, csv

# http://catalog.data.gov/api/3/action/package_search?q=dataDictionary:*&rows=1000&start=2

# Read file and parse JSON based on dot syntax
def process_file(file_list):
    csv_data = [['id','title','data_dictionary','notes','tags','metadata_created','metadata_modified','maintainer','state','resource_formats','data_urls']]
    
            


    for file_path in file_list:
        print "Processing: " + file_path
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/data/" + file_path, 'r')
        json_object = json.load(f)
        results = json_object['result']['results']

        for result in results:
            data = {}
            data['id'] = result['id'].encode('utf-8')
            data['title'] = result['title'].encode('utf-8')
            data['notes'] = result['notes'].encode('utf-8')
            data['metadata_created'] = result['metadata_created']
            data['metadata_modified'] = result['metadata_modified']
            data['maintainer'] = result['maintainer']
            data['state'] = result['state']
            resources = result['resources']
                    # id: "1e68f387-5f1c-46c0-a0d1-46044ffef5bf",
                    # metadata_created: "2014-02-26T00:48:24.897497",
                    # metadata_modified: "2015-01-16T18:05:17.138759",
                    # data['url'] = result['url']
                    # data['format'] = result['format']


            
            
            data['data_dictionary'] = ''
            extras = result['extras']
            for extra in extras:
                if extra['key'] == 'dataDictionary':
                    data['data_dictionary'] = extra["value"]
                if extra['key'] == 'describedBy':
                    data['data_dictionary'] = extra["value"]

            tags = result['tags']
            tag_array = []
            for tag in tags:
                tag_array.append(tag['display_name'].encode('utf-8'))

            resource_formats_array = []
            data_urls = []
            for resource in resources:
                resource_formats_array.append(resource['format'].encode('utf-8'))
                data_urls.append(resource['url'])
            csv_data.append([data['id'],data['title'], data['data_dictionary'], data['notes'], tag_array, data['metadata_created'], data['metadata_modified'],data['maintainer'],data['state'],resource_formats_array])

    
    
        f.close()
    saveCSV(csv_data)
    return "done"


def saveCSV(csv_data):
    
    csv_file_name =  "output/csv/" + datetime.date.today().strftime("%Y-%B-%d") + ".csv"
    csv_writer = csv.writer(open(csv_file_name, 'wb'))

    for row in csv_data:
        csv_writer.writerow(row)

# Main program. Read system arguments, read file, make output file.
def main():
    # Create list of files.
    file_list = []


    input_folder = "data"

    current_directory = os.path.dirname(os.path.realpath(__file__)) + '/'

    files = os.listdir(current_directory + input_folder)

    for file in files:
        if file.endswith(".json"):
            file_list.append(file)



    




    
        
        else:
            "File supplied not JSON"

    

    process_file(file_list)





main()

print "Done."

sys.exit()
