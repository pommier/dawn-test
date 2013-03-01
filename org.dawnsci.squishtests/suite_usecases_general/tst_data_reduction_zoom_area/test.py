source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    openExternalFile("9758.nxs")

    # Select image and zoom
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 6, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Keep aspect ratio_ToolItem"), 12, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Zoom Profile"))
    
    snooze(1)
    proxy  = waitForObject(":9758.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(2) # While zoom...
    
    system = getPlottingSystem("9758.nxs")
    test.verify(system.getRegions().size()==1)
    test.passes("One trace plotted") 
    
    clickTab(waitForObject(":Data_CTabItem_2"), 28, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Data reduction..._ToolItem"), 9, 11, 0, Button.Button1)
    
    clickButton(waitForObject(":Overwrite file if it exists._Button"))
    snooze(1) 
    clickButton(waitForObject(":Finish_Button", 10000))
    
    # Show plotted image
    snooze(1) 
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 7, 11, 0, Button.Button1)
    snooze(3) 
    system = getPlottingSystem("9758_Zoom_Profile_reduction.h5")
    test.verify(system.getRegions().size()==0)
    test.verify(system.getTraces().size()==1)
    test.passes("Something plotted from data reduction") 

    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
 