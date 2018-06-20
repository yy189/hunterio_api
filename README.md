# hunterio_api

To use, add hunter.io API key to api_keys.txt, set LIMIT, CB_PATH(input file path) and NUM in settings.py. Input file must contain
column 'Orgnization name' and 'Website'. E.g. MoviePass, https://www.moviepass.com/

!!!!!! To save your requests, don't delete the file "emails_searched_by_domain.csv" !!!!!!

To save me requests, I have only implemented the (Domain Search)[https://hunter.io/api/docs#domain-search] function, to use other
functions like Email Finder and Email Verifier, you need to implement them by your own.
