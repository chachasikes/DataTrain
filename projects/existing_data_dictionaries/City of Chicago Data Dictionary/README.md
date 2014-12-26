# Project
The City of Chicago has a data dictionary. It's a simple php database.

We can use this open data to seed DataTrain, and explore the possibilities of improving our understanding of governments with social data dictionaries.

## TODO
* Get list of variables (done, in file most_variables.csv) - obtained by searching for the letter A, viewing source, copying the raw html, and splitting it up into a CSV file. This is enough to go on to get started, we can request a full data dump later.
* Using Google Refine or Python, obtain the raw html of a sampling of variables.
* Document the structure of the datasets.
* Document the structure of the field lists.
* Document the structure of the attribute documentation.
* Analyze the data.
* Convert to JSON format using the data_train schema. (raw to begin with, then with an app later, TBD.)


## Notes

## City of Chicago Data Dictionary
Launched October 13, 2014

### Articles
* http://datasmart.ash.harvard.edu/news/article/the-next-phase-of-transparency-327
* http://govfresh.com/2013/10/chicago-launches-first-comprehensive-public-data-dictionary/

### Project links
* http://datadictionary.cityofchicago.org/
* http://datadictionary.cityofchicago.org/table_info.php?table_id=2260
* Example, Budget system dictionary: http://datadictionary.cityofchicago.org/database_info.php?database_id=61
* Source code: https://github.com/chicago/metalicious ("Metalicious")


#### Example data
BOOK_ACTION List of actions for the Budget Book Application based on user role
BOOK_ACTIVE_USER  Last active user of Budget Book
BOOK_ALDERMANIC_PAYRATE data used for creating pay schedule for aldermanic staff published in the Budget Book
BOOK_ANNOTATION Annotations entered into the Budget Book application by OBM staff
BOOK_AUDIT  Audit trail of modifications made in the Budget Book Application by Draft number.
BOOK_CBS_MAPPING  Maps BOOK_DRAFT to BOOK_SECTION to BOOK_PAGE_ELEMENT might be used for book synchronization
BOOK_DRAFT  list of available budget book drafts




"About the City of Chicago Data Dictionary
-- http://datadictionary.cityofchicago.org/about.php
Welcome to the City of Chicago’s Data Dictionary. This website serves as a single, comprehensive database catalog for the City of Chicago and City of Chicago sister agencies. It is a resource for anyone who is interested in understanding what data is held by City agencies and departments, how and if it may be accessed, and in what formats it may be accessed. We invite you to explore the huge volume of data maintained by the City of Chicago."

Terms of Use

Permission is hereby granted, free of charge, to any person obtaining a copy of this data, metadata, schema, and associated documentation files (the "Database"), to deal in the Database without restriction, including without limitation the rights to extract and re-utilize all or a substantial part of the data, and the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Database, and to permit persons to whom the Database is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Database. 

The Database is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the creators, authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Database or the use or other dealings in the Database. 

The listed data fields are not indicative as to whether any information is captured in a particular data field. Further, the listed data fields are not indicative as to whether information captured in a particular data filed is subject to release under the Freedom of Information Act.