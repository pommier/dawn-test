source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

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
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Check data has plotted by looking at graph settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"Column_1",vals.METALMIX_0_MAX,vals.METALMIX_0_MIN)
    
    #Change to derivative and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    test.verify(widget.getSelection(), "Check Default Selection")
    

    check_plotted_trace_name_yval(conOb, "Column_1'",vals.METALMIX_0_DMAX,vals.METALMIX_0_DMIN)
    
    mouseClick(waitForObject(":Derivative_CTabCloseBox"), 11, 4, 0, Button.Button1)
    
    check_plotted_trace_name_yval(conOb,"Column_1",vals.METALMIX_0_MAX,vals.METALMIX_0_MIN)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 10, 4, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Derivative' in dedicated view"))
    
    check_plotted_trace_name_yval(conOb,"Column_1'",vals.METALMIX_0_DMAX,vals.METALMIX_0_DMIN)
    
    for child in children:
        if "MoKedge_1_15.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table_2", "4/0"), 10, 7, 0, Button.Button1)
    
    conOb2 = waitForObject(":Configure Settings..._ToolItem_2")
    check_plotted_trace_name_yval(conOb2,"ln(I0/It)'","0.06","-0.02")
    
    mouseClick(waitForObject(":Derivative_CTabItem"), 10, 4, 0, Button.Button1)
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    mouseClick(widget, 5, 5, 0, Button.Button1)
    test.verify(widget.getSelection()==0, "Check click Selection")
    
    
    widget = waitForObject(":Derivative.Display Data_Button")
    mouseClick(widget, 5, 5, 0, Button.Button1)
    test.verify(widget.getSelection()==1, "Check click Selection")
    
    check_plotted_trace_name_yval(conOb2,"ln(I0/It)","-1.5","-3.0")

    clickTab(waitForObject(":metalmix.mca_CTabItem"), 64, 5, 0, Button.Button1)
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    test.verify(widget.getSelection(), "Check default Selection")
    
    check_plotted_trace_name_yval(conOb,"Column_1'",vals.METALMIX_0_DMAX,vals.METALMIX_0_DMIN)


    closeOrDetachFromDAWN()