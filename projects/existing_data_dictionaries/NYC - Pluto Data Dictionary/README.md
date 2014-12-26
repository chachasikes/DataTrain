
# Make Machine readable PLUTO Data Dictionary


### Convert the 53 page PLUTO Data Dictionary document into machine-readable format.
* Source: http://www.nyc.gov/html/dcp/pdf/bytes/pluto_datadictionary.pdf, copied into microtasks/sources/pluto_datadictionary.pdf
* See also: http://www.nyc.gov/html/dcp/html/bytes/applbyte.shtml
"Extensive land use and geographic data at the tax lot level in comma–separated values (CSV) file format. The PLUTO files contain more than seventy fields derived from data maintained by city agencies."


## TODO
* Check that this is the most recent version of the file.
* More research to see if this has already been done (ask around.)
* More research to see what issues people have had with the data dictionary.
* Downlaod the PLUTO dataset and investigate data samples.
* Make new git repository for parsing the PLUTO Data Dictionary.

If all is a go:
* Parse the PDF file and render the contents according to the data_dictionary schema /data/schema/data_dictionary/data_dictionary_spec.md



###Examples

### Dataset
id, name, dataUrl, sourceName, sourceURL, type, location, tags, description, comments, dateAdded, dateUpdated, published, contributors, revision
, "PLUTO Data Dictionary", "http://www.nyc.gov/html/dcp/pdf/bytes/pluto_datadictionary.pdf", 

## Fields
id, name, fieldName, dataTypeName, description, comments, renderTypeName, datasetId, datasetName, contentSummary

## Localization
id, type, fieldId, language, fieldName, abbreviation, labelShort, labelLong, description, definition, icon, reference, contact, supplemental



Field Name: BOROUGH (Borough)
Format: Alphanumeric - 2 characters
Data Source: Department of City Planning - based on data from:
Department of Finance - RPAD Master File
Description: The borough that the tax lot is located in.
This field contains a two character borough code.
CODES DECODES
BX Bronx
BK Brooklyn
MN Manhattan
QN Queens
SI Staten Island
NOTE: Two portions of the city, Marble Hill and Rikers Island, are each
legally located in one borough but are serviced by different
boroughs. The BOROUGH codes associated with these areas
are the boroughs they are legally located in.
Specifically, Marble Hill is serviced by the Bronx but is legally
located in Manhattan and has a Manhattan BOROUGH Code.
Rikers Island has a Bronx BOROUGH Code because it is legally
located in the Bronx although it is serviced by Queens.


