Setup Management System
-----------------------

Step 01: Setup the MySQL Database

		Source: "source/0-resources/0-database/hecms.sql"
		
		Method: Setup MySQL Engine

Setup 02: Host the files on server
		
		Source: "source/2-hecms-management-system"



Setup Monitoring System
-----------------------

Step 01: Install Anaconda

Step 02: Install dependencies from environment 
		
		Source: "source/0-resources/1-requirements/hecms-monitoring-system-requirements.yml"

		Command: Type on CMD "conda env create -f environment.yml"


Setp 03: Turn on database (if it is hosted on localhost, turn on xampp/any)

Setp 04: Navigate to the project folder: "source/1-hecms-monitoring-system"

Step 04: Type on CMD "activate tensorflow_gpu" to activate the environment. 

Step 05: Type "python main.py"