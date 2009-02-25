#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Thu Apr  5 14:04:33 2007

import wx
import wx.lib.filebrowsebutton
import diffpy.pdfgui.gui.pdfguiglobals as pdfguiglobals
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.tooltips import preferencespanel as toolTips
from diffpy.pdfgui.control.controlerrors import ControlFileError

class PreferencesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PreferencesPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizerPanelName_staticbox = wx.StaticBox(self, -1, "")
        self.labelPanelName = wx.StaticText(self, -1, "Preferences")
        self.atomeyeFileBrowser = wx.lib.filebrowsebutton.FileBrowseButton(self, -1)
        self.structureDirCheckBox = wx.CheckBox(self, -1, "Remember path to structure files")
        self.dataDirCheckBox = wx.CheckBox(self, -1, "Remember path to data sets")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.okButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: PreferencesPanel.__set_properties
        self.labelPanelName.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade
        self.setToolTips(toolTips)

    def __do_layout(self):
        # begin wxGlade: PreferencesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerPanelName = wx.StaticBoxSizer(self.sizerPanelName_staticbox, wx.HORIZONTAL)
        sizerPanelName.Add(self.labelPanelName, 1, wx.LEFT|wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizerPanelName, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        sizer_2.Add(self.atomeyeFileBrowser, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 5)
        sizer_1.Add(self.structureDirCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(self.dataDirCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add((0, 0), 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(self.static_line_1, 0, wx.LEFT|wx.RIGHT|wx.EXPAND|wx.ALIGN_BOTTOM, 5)
        sizer_3.Add((0, 0), 1, wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.okButton, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add((10, 1), 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.cancelButton, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""
        import os.path
        self.atomeyeFileBrowser.SetLabel("AtomEye path:")
        self.atomeyeFileBrowser.startDirectory = os.path.abspath('.')
        return

    def onCancel(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Cancel the changes. Go back to the last panel."""
        selections = self.treeCtrlMain.GetSelections()
        if selections:
            node = selections[0]
            entrytype = self.treeCtrlMain.GetNodeType(node)
        else:
            entrytype = None
        self.mainFrame.setMode("fitting")
        self.mainFrame.switchRightPanel(entrytype)
        return 

    def onOK(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Record all of the preferences and return to fitting mode."""
        import os.path

        # Atomeye Path
        path = self.atomeyeFileBrowser.GetValue()
        if not self.cP.has_section("ATOMEYEPATH"):
            self.cP.add_section("ATOMEYEPATH")
        self.cP.set("ATOMEYEPATH", "path", path)

        # Structures path
        remember = str(self.structureDirCheckBox.GetValue())
        if not self.cP.has_section("PHASE"):
            self.cP.add_section("PHASE")
        self.cP.set("PHASE", "remember", remember)

        # Data set path
        remember = str(self.dataDirCheckBox.GetValue())
        if not self.cP.has_section("DATASET"):
            self.cP.add_section("DATASET")
        self.cP.set("DATASET", "remember", remember)

        # Get out of here
        self.onCancel(event)
        return

    def refresh(self):
        """Refresh the panel."""
        path = ""

        # Atomeye Path
        if self.cP.has_option("ATOMEYEPATH", "path"):
            path = self.cP.get("ATOMEYEPATH", "path")
        self.atomeyeFileBrowser.SetValue(path)

        # Structures path
        remember = "False"
        if self.cP.has_option("PHASE", "remember"):
            remember = self.cP.get("PHASE", "remember")
        if remember == "True":
            self.structureDirCheckBox.SetValue(1)
        else:
            self.structureDirCheckBox.SetValue(0)

        # Data set path
        remember = "False"
        if self.cP.has_option("DATASET", "remember"):
            remember = self.cP.get("DATASET", "remember")
        if remember == "True":
            self.dataDirCheckBox.SetValue(1)
        else:
            self.dataDirCheckBox.SetValue(0)

        return

# end of class PreferencesPanel


