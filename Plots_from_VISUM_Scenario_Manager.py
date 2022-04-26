from os.path import split, join
from glob import glob
import os

Visum.Messages.Clear()
pathname, filename = split(CurrentScriptFile.Path)  # pathname points to location of this script file
numscenario = Visum.ScenarioManagement.CurrentProject.Scenarios.Count

layoutfiles = glob(os.path.join(pathname, '*.gpa'))

# layoutfile = join(pathname,"Flow Zoom Out-Rev 3.gpa")

Totalmsg = Visum.MessageFileName

setofscn = set()
listofscn = list()
m, n = 0, 0 # counter for total no of plots generated and the no. of scenarios for which plot was not generated

for i in range(numscenario):
    Activescn = Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).AttValue("Active")
    if Activescn:
        scnname = Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).AttValue("Description")
        listofscn.append(scnname)
        setofscn.add(scnname)

if len(listofscn) != len(setofscn):
    Visum.Ask(16384, "", "", "", "","Please remove duplicates in the description of active scenarios and run the script again")
elif len(listofscn) == 0:
    Visum.Ask(16384, "", "", "", "","None of the scenarios are set as active ")
else:
    for i in range(numscenario):
        Activescn = Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).AttValue("Active")
        Calculated = Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).AttValue("CalculationState")
        scnname = Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).AttValue("Description")
        if Activescn:
            if Calculated == "CALCULATED":
                Visum.ScenarioManagement.CurrentProject.Scenarios.ItemByKey(i + 1).LoadResults()
                Visum.Sleep(1000)

                for j in layoutfiles:
                    Visum.Net.GraphicParameters.Open(j)
                    Visum.Graphic.WaitForIdle()
                    layoutfile = (os.path.splitext(os.path.basename(j)))[0]
                    filename = join(pathname, scnname + "-" + layoutfile + ".jpg")
                    Visum.Log(16384, filename)
                    Visum.Net.LegendParameters.LegendGeneralParameters.SetAttValue("TitleText", scnname)

                    # the margin of print area
                    printArea = Visum.Net.PrintParameters.PrintArea
                    t = printArea.AttValue("TOPMARGIN")
                    b = printArea.AttValue("BOTTOMMARGIN")
                    l = printArea.AttValue("LEFTMARGIN")
                    r = printArea.AttValue("RIGHTMARGIN")

                    # print graphics at path of script
                    Visum.Graphic.ExportNetworkImageFile(filename, l, b, r, t, 4000, 200, 100)
                    m = m + 1
            else:
                Visum.Log(16384, "Plot for Scenario: " + scnname + " cannot be generated since the scenario is not calculated| " + Calculated)
                n = n + 1

    uncalculated = "\n Plots for were not generated for " + str(n) + " uncalculated scenarios" if n > 0 else ""
    Visum.Ask(16384, "", "", "", "", "Total " + str(m) + " plots were generated for " + str(len(listofscn)) + " active scenarios" + uncalculated)

    
    
  

