# Implementation of MS Smooth Streaming on a django-enabled webservice #

OVERVIEW:  
Simple webservice to enable content delivery through different streaming endpoints using the Smooth Streaming protocol.

![Output sample](https://github.com/roopekj/Viihde/raw/master/viihde.gif)

HOW TO RUN:
* add **data.json** to the root directory with the variables
    * **key**
        * secret key that is used for creating hashes within the service.
    * **api-url**
        * URL (+port) that django should query with inputs in order to find the Manifest-file required for smooth streaming
        * Format used in the queries is _{api-url}/streams/?q={user-input}_
    * **dep-url**
        * URL (+port) that the user's browser should query for dependencies (namely *hasplayer.js* and *Elisa.svg*).
        * This is due to django being run outside of debug-mode (as it should for security reasons) and the fact that django cannot provide any way to distribute larger files in a way that would scale
        * Format used in the queries is _{dep-url}/dependencies/{filename}.{extension}_
    * **allowed-host**
        * The hostname that django responds to (mainly used to avoid CSRF-attacks etc.)
        
In the root-directory run python3 manage.py runserver hostname:port.   
Full documentation for sections where applicable can be found at https://docs.djangoproject.com/en/3.0/.

Credit:
* https://github.com/Orange-OpenSource/hasplayer.js
* https://www.djangoproject.com/