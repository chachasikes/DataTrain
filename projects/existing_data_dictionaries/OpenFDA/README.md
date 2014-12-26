

## Open FDA
This modern online data resource has the best quality documentation for the data in the Open FDA fields.
* Open FDA https://open.fda.gov/api/reference/

### Notes
"Query syntax

Queries to the openFDA API are made up of parameters joined by an ampersand &. Each parameter is followed by an equals sign = and an argument.

Searches have a special syntax: search=field:term. Note that there is only one equals sign = and there is a colon : between the field to search, and the term to search for.

Here are a few syntax patterns that may help if you’re new to this API.

Pattern Description
search=field:term Search within a specific field for a term.
search=field:term+AND+field:term  Search for records that match two terms.
search=field:term+field:term  Search for records that match either of two terms.
search=field:term&count=field.exact Search for matching records, then count within that set the number of records that match the unique values of a field."


"Field-by-field reference"


recalling_firm
string
The firm that initiates a recall or, in the case of an FDA requested recall or FDA mandated recall, the firm that has primary responsibility for the manufacture and (or) marketing of the product to be recalled.


https://open.fda.gov/food/enforcement/reference/

Enforcement Report
"results": [
  {
    "reason_for_recall": "Cass-Clay Creamery is voluntarily recalling a number of ice cream products because they may contain undeclared soy (lecithin).",
    "status": "Ongoing",
    "distribution_pattern": "ND, AZ, MN, SD, KS",
    "product_quantity": "81 containers",
    "recall_initiation_date": "20120720",
    "state": "ND",
    "event_id": "62644",
    "product_type": "Food",
    "product_description": "Cass-Clay   , Swiss Chip, 3 Gallon(11.34 L).",
    "country": "US",
    "city": "Fargo",
    "recalling_firm": "Cass Clay Creamery AMPI Fargo Division",
    "report_date": "20120905",
    "voluntary_mandated": "Voluntary: Firm Initiated",
    "classification": "Class II",
    "code_info": "all products that has a plant code of \"38-25\".",
    "openfda": {},
    "initial_firm_notification": "Two or more of the following: Email, Fax, Letter, Press Release, Telephone, Visit"
  }
