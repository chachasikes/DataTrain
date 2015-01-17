# Notes on Data Dictionaries and Best Practices


## Definition Data Dictionary
From Wikipedia: http://en.wikipedia.org/wiki/Data_dictionary
A data dictionary, or metadata repository, as defined in the IBM Dictionary of Computing, is a "centralized repository of information about data such as meaning, relationships to other data, origin, usage, and format."[1] The term can have one of several closely related meanings pertaining to databases and database management systems (DBMS):

A document describing a database or collection of databases
An integral component of a DBMS that is required to determine its structure
A piece of middleware that extends or supplants the native data dictionary of a DBMS

#### Notes from Oracle
* https://docs.oracle.com/html/A96524_01/c05dicti.htm
----
"One of the most important parts of an Oracle database is its data dictionary, which is a read-only set of tables that provides information about the database. A data dictionary contains:
 •  The definitions of all schema objects in the database (tables, views, indexes, clusters, synonyms, sequences, procedures, functions, packages, triggers, and so on) 
 •  How much space has been allocated for, and is currently used by, the schema objects 
 •  Default values for columns 
 •  Integrity constraint information 
 •  The names of Oracle users 
 •  Privileges and roles each user has been granted 
 •  Auditing information, such as who has accessed or updated various schema objects 
a • Other general database information 
The data dictionary is structured in tables and views, just like other database data. All the data dictionary tables and views for a given database are stored in that database's SYSTEM tablespace.
Not only is the data dictionary central to every Oracle database, it is an important tool for all users, from end users to application designers and database administrators. Use SQL statements to access the data dictionary. Because the data dictionary is read-only, you can issue only queries (SELECT statements) against it's tables and views.
"

#### MODERNIZATION ideas 
* change to read-write & comment (social, collaboratively edited, stack overflow like)
* sample values
* distinct values with counts
* conversations about the data can influence the very nature of the data and formatting (example: requesting data improvements, like parsing out dates when not normally available, but are critical to actually making the data useful.)



#### Notes on managing Data Dictionaries
* http://library.ahima.org/xpedio/groups/public/documents/ahima/bok1_049331.hcsp?dDocName=bok1_049331
"Common Data Inconsistencies
In many organizations data are stored in different databases and may be of inconsistent quality. Issues such as variable naming conventions, definitions, field length, and element values can all lead to misuse or misinterpretation of data in reporting. The following examples illustrate common data inconsistencies.

Inconsistent naming conventions. The date of the patient's admission is referred to differently in different systems: "Date of Admission" in the patient management module within the EHR, "Admit Date" in the fetal monitoring system, and "Admission Date" in the cardiology database. The unique patient identifier is referred to as a "Medical Record Number" in the patient management system, "Patient Record Identifier" in the operating room system, "A number" (a moniker leftover from a legacy system from 25 years ago), and "Enterprise Master Patient Identifier" in the catheterization lab system.

Inconsistent definitions. The patient access module defines date of admission as the date on which an inpatient or day surgery visit occurs; the trauma registry system defines it as the date on which the trauma patient enters the operating room. Pediatric age is defined as age less than or equal to 13 in the EHR module, while the pediatric disease registry defines pediatric age as below the age of 18. In the bed board system, a nursing unit may be defined as 5W or 5 West. Within the scheduling system, unique locations are defined as short procedure unit or SPU, x-ray, or radiology.

Varying field length for same data element. The field length for a patient's last name is 50 characters in the patient management module and 25 characters in the cancer registry system. The medical record number in the patient management system is 16 characters long, while the cancer registry system maintains a 13-character length for the medical record number.

Varied element values. The patient's gender is captured as M, F, or U in the patient access module, while the gender is captured as Male, Female, or Other in the peripheral vascular lab database.

Inconsistencies in data definitions can lead to innaccurate data use and health data reporting and can potentially affect the quality of care."

"The Benefits of a Data Dictionary

A data dictionary promotes data integrity by supporting the adoption and use of consistent data elements and terminology within health IT systems. By adopting a data dictionary, organizations can improve the reliability, dependability, and trustworthiness of data use.

An established data dictionary can provide organizations and enterprises many benefits, including:

Improved data quality
Improved trust in data integrity
Improved documentation and control
Reduced data redundancy
Reuse of data
Consistency in data use
Easier data analysis
Improved decision making based on better data
Simpler programming
Enforcement of standards1
A data dictionary promotes clearer understanding of data elements; helps users find information; promotes more efficient use and reuse of information; and promotes better data management.

Note

Department of Health and Human Services. "Health Information Technology: Initial Set of Standards, Implementation Specifications, and Certification Criteria for Electronic Health Record Technology." Federal Register, July 28, 2010. http://federalregister.gov/a/2010-17210."

### Best practicies in creating a data dictionary
http://www.utexas.edu/cola/orgs/redcap/Best-Practices.php

### Best Practices for Data Dictionary Definitions and Usage
 Version 1.1 2006-11-14 
http://www.pnamp.org/sites/default/files/best_practices_for_data_dictionary_definitions_and_usage_version_1.1_2006-11-14.pdf


"According to the International Standards Organization (ISO)2
 “The increased use of data processing and
electronic data interchange heavily relies on accurate, reliable, controllable, and verifiable data
recorded in databases. One of the prerequisites for a correct and proper use and interpretation of data is
that both users and owners of data have a common understanding of the meaning and descriptive
characteristics (e.g., representation) of that data. To guarantee this shared view, a number of basic
attributes has to be defined.”



### Useful "TABLE II - DIVERGENCE IN TERMINOLOGY USED TO DESCRIBE DATA-DICTIONARY ELEMENTS"
