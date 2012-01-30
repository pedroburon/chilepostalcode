Chile Postal Code
=================

Small script to get the zip code of an address in Chile, made for Google App Engine

Examples
--------

    GET http://chilepostalcode.appspot.com/?street=providencia&commune=providencia&number=229
    
    Content-Type: application/json
    
    {"postalcode": null, "commune": "", "street": "providencia", "number": "", "error": "Error"}


    GET http://chilepostalcode.appspot.com/?street=providencia&commune=providencia&number=229&callback=do_something
    
    Content-Type: text/javascript
    
    do_something({"postalcode": "7500768", "commune": "providencia", "street": "providencia", "number": "229"})


