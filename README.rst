===============================
``slack-scheduler-server`` - Flask-REST-API server for creating sechduled slack messages
===============================

Installation
------------

::

    1. Clone the repo localy
    2. Intsall needed python libs using - >> pip install -r requirements.txt
    3. Enter your group's Authentication-Token to the server.py file

Usage
-----

::

    >> python server.py
    >> python tests.py // Will send a test POST request to the server, and after X minutes will fire the slack messaging event