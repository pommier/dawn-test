source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def check_no_traces(conOb):
    mouseClick(conOb, 15, 9, 0, Button.Button1)
    snooze(1)
    test.verify(not object.exists(":Configure Graph Settings.Traces_TabItem"), "Traces tab not there")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))

def main():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    vals = dawn_constants;
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 12, 8, 0, Button.Button1)
    
    #open 4 traces
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "1/0"), 10, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "2/0"), 6, 2, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "3/0"), 10, 10, 0, Button.Button1)
    
    #check plot
    conOb = waitForObject(":Configure Settings..._ToolItem")
    
    check_plotted_trace_name_yval(conOb,"Column_1",vals.METALMIX_1_MAX,vals.METALMIX_1_MIN)
    
    nameList = ["Column_1","Column_2","Column_3","Column_4"]
    check_plotted_traces_names(conOb, nameList)
    
    #Change to derivative and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    
    check_plotted_trace_name_yval(conOb,"Column_1'",vals.METALMIX_1_DMAX,vals.METALMIX_1_DMIN)
    
    nameListDer = ["Column_1'","Column_2'","Column_3'","Column_4'"]
    check_plotted_traces_names(conOb, nameListDer)
    #uncheck, test no traces
    clickButton(waitForObject(":Derivative.Display f'(Data)_Button"))
    check_no_traces(conOb)
    
    #check data
    clickButton(waitForObject(":Derivative.Display Data_Button"))
    check_plotted_trace_name_yval(conOb,"Column_1",vals.METALMIX_1_MAX,vals.METALMIX_1_MIN)
    check_plotted_traces_names(conOb, nameList)
    
    #uncheck, test no traces
    clickButton(waitForObject(":Derivative.Display Data_Button"))
    check_no_traces(conOb)
    
    #check 1st der
    clickButton(waitForObject(":Derivative.Display f'(Data)_Button"))
    check_plotted_trace_name_yval(conOb,"Column_1'",vals.METALMIX_1_DMAX,vals.METALMIX_1_DMIN)
    check_plotted_traces_names(conOb, nameListDer)
    
    #uncheck, test no traces
    clickButton(waitForObject(":Derivative.Display f'(Data)_Button"))
    check_no_traces(conOb)
    
    #check 2nd der
    clickButton(waitForObject(":Derivative.Display f''(Data)_Button"))
    nameListDer2 = ["Column_1''","Column_2''","Column_3''","Column_4''"]
    check_plotted_trace_name_yval(conOb,"Column_1''","200.0",vals.METALMIX_0_DMIN)
    check_plotted_traces_names(conOb, nameListDer2)
    
    #uncheck, test no traces
    clickButton(waitForObject(":Derivative.Display f''(Data)_Button"))
    check_no_traces(conOb)
    
    closeOrDetachFromDAWN()


    