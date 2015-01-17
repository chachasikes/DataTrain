# Chop CSV
Chop a long CSV file into a shorter one, for quick data sampling.
Example: 98MB many lines into 500 lines. 

* Make sure chmod +x chopCSV.py

### Usage
Run the file giving the input path, file name and number of rows to return

./chopCSV.py full_path_input_file file_name_output_file number_rows

Example:
/chopCSV.py /Folder/datatrain/projects/existing_data_dictionaries/NYC\ -\ Pluto\ Data\ Dictionary/source_files/nyc_pluto_14v2/MN.csv MN_sample.csv 100