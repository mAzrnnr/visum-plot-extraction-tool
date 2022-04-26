# VISUM-Scenario_Manager-Plot_Extraction_tool
Python Script for bulk extraction of plots from VISUM Scenarios


Created by
----------------------------
- Created by: Aadil Nawaz 
- Revision 0: 28th June 2021

Scope for improvement
---------------------------
- Remove need to install glob module
- Check with Python 3.9 requirements


Description
----------------------------
- Tool to generate plots from active scenarios in the Scenario Manager
- Can generate plots from multiple GPA files
- Modifies Title of Legend based on "description" of scenario in Edit Project window

Requirements:
---------------------------------
- Works on VISUM 2021.01-05 or later (post specific PTV updates that allow Legend modification)
- Works for both Python 2 and Python 3 
- Requires glob module which can be installed by command pip install glob2 in command prompt.


Procedure to run
-----------------------------
- Copy relevant GPA files in the working folder containing the python script
- In Edit Project window of VISUM, select the scenarios for which plots needs to be generated and make them active
- Run the script from the Scripts menu


Checks undertaken by script:
-----------------------------
- Throws warning in case of missing GPA files.
- Throws warning when there are duplicates in description of active scenarios
- Informs about total no. of plots generated and no. of active scenarios
- Informs total no. of uncalculated scenarios for which plots could not be generated 
