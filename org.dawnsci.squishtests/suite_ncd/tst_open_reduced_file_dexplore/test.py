source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    
    startOrAttachToDAWN()
    openPerspective("DExplore")
    
    openExternalFile("results_i22-107001_Pilatus2M_120713_183001.nxs")
    
    snooze(2)
    
    system = getPlottingSystem("Dataset Plot")
    #TODO test was trying to use the data node which is a link to original data file
    # rewrite using other data nodes
#    expand(waitForObjectItem(":Tree_Tree_2", "entry1"))
#    snooze(2)
#    expand(waitForObjectItem(":Tree_Tree_2", "Pilatus2M"))
#    snooze(2)
#    doubleClick(waitForObjectItem(":Tree_Tree_2", "data"), 17, 8, 0, Button.Button1)
#    
#    snooze(1)
#    
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    
#    test.verify(shape.at(0) == 1679, "image plotted x")
#    test.verify(shape.at(1) == 1475, "image plotted y")
    
#    expand(waitForObjectItem(":Tree_Tree_2", "Pilatus2M__result"))
#    
#    doubleClick(waitForObjectItem(":Tree_Tree_2", "data_1"), 19, 14, 0, Button.Button1)
#    snooze(1)
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    test.verify(shape.at(0) == 1414, "image plotted x")
#    test.verify(shape.at(1) == 1, "image plotted y")
    
#    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:2"), 0, 0, 0, Button.NoButton)
#    snooze(1)
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    test.verify(shape.at(0) == 6, "image plotted x")
#    test.verify(shape.at(1) == 1414, "image plotted y")
#    
#    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:1"), 0, 0, 0, Button.NoButton)
#    snooze(1)
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    test.verify(shape.at(0) == 7, "image plotted x")
#    test.verify(shape.at(1) == 1414, "image plotted y")
#    
#    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:3"), 0, 0, 0, Button.NoButton)
#    snooze(1)
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    test.verify(shape.at(0) == 1414, "image plotted x")
#    test.verify(shape.at(1) == 1, "image plotted y")
#
#    
#    mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 5, 7, 0, Button.Button1)
#    activateItem(waitForObjectItem(":Pop Up Menu", "1D plot"))
#    snooze(1)
#    shape = system.getTraces().toArray().at(0).getData().getShape()
#    test.verify(shape.length == 1)
#    test.verify(shape.at(0) == 1414, "line plotted x")
#    test.verify(system.getTraces().toArray().at(0).getXData().getName() =="q")
#    
#    mouseClick(waitForObject(":_Twistie"), 2, 3, 0, Button.Button1)
#    setValue(waitForObject(":_Slider"), 1)
#    setValue(waitForObject(":_Slider"), 2)
#    setValue(waitForObject(":_Slider"), 3)
#    setValue(waitForObject(":_Slider"), 4)
#    setValue(waitForObject(":_Slider"), 5)
#    setValue(waitForObject(":_Slider"), 6)
#    setValue(waitForObject(":_Slider_2"), 1)
#    setValue(waitForObject(":_Slider_2"), 2)
#    setValue(waitForObject(":_Slider_2"), 3)
#    setValue(waitForObject(":_Slider_2"), 4)
#    setValue(waitForObject(":_Slider_2"), 5)

    closeOrDetachFromDAWN()