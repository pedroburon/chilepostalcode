Chile Postal Code
=================

Small script to get the zip code of an address in Chile, made for Google App Engine

Examples
--------

you can get a json response:


    GET http://chilepostalcode.appspot.com/?street=providencia&commune=providencia&number=229
    
    Content-Type: application/json
    
    {"postalcode": "7500768", "commune": "", "street": "providencia", "number": ""}

or a javascript response (with callback param):

    GET http://chilepostalcode.appspot.com/?street=providencia&commune=providencia&number=229&callback=do_something
    
    Content-Type: text/javascript
    
    do_something({"postalcode": "7500768", "commune": "providencia", "street": "providencia", "number": "229"})

if we can't get the postalcode:

    GET http://chilepostalcode.appspot.com/?street=providencia&commune=new+york&number=229&callback=do_something
    
    Content-Type: text/javascript
    
    do_something({"postalcode": null, "commune": "new+york", "street": "providencia", "number": "229", "error": "Error"})


