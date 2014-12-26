

Objective:
* Create clearly articulated data schema for the application and data storage.
* Document fields, especially the unique ones.
* Make data schema valid & formatted for automated testing and easy user-data validation.

Notes:
* http://jsonschema.net
* http://json-schema.org/implementations.html
* https://github.com/lbovet/docson


# Localization
* efficient mongodb storage for mulitlingual databases:
http://stackoverflow.com/questions/7528733/what-is-an-efficient-mongodb-schema-design-for-a-multilingual-e-commerce-site


{ "_id" : ObjectId("4e9bfb4b4403871c0f080000"), 
"name" : "some internal name", 
"sku" : "10001", 
"company" : { /* reference to another collection */ }, "price" : 99.99,
"attributes": { 
  "description": { "en": "english desc", "de": "deutsche Beschreibung" },
  "another_field": { "en": "something", "de": "etwas"}, 
  "non_i18n_field": { "*": xxx } 
 }
}

* http://en.wikipedia.org/wiki/Language_localisation


# Writing technically
* http://www.writingassist.com/resources/articles/think-globally-write-locally/
* "controlled english" : http://www.slideshare.net/Enlaso/localization-technical-writing-and-translation
* framemaker
* translator workbench
* "global readiness" writing: http://techwhirl.com/writing-global-readiness-technical-writers-need-know/


Questions:
* use en_us instead of en?

