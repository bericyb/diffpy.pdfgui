# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 1.0.2 on Tue Nov  2 17:49:01 2021
#

import wx

# begin wxGlade: dependencies
import wx.grid
# end wxGlade
from diffpy.structure import Atom
from diffpy.pdfgui.gui.insertrowsdialog import InsertRowsDialog
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui import tooltips
from diffpy.pdfgui.gui.wxextensions.autowidthlabelsgrid import \
    AutoWidthLabelsGrid
from diffpy.pdfgui.gui.wxextensions.validators import TextValidator, FLOAT_ONLY
from diffpy.pdfgui.gui.wxextensions.textctrlutils import textCtrlAsGridCell
from diffpy.pdfgui.gui.wxextensions import wx12
from diffpy.pdfgui.gui import magpanelutils
from diffpy.pdfgui.gui.advancedmagconfig import AdvancedFrame
from diffpy.pdfgui.gui.magviewerpanel import CanvasFrame
from diffpy.utils.wx import gridutils

import numpy as np
import re

# begin wxGlade: extracode
# end wxGlade


class MagConfigurePanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MagConfigurePanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        sizer_main = wx.BoxSizer(wx.VERTICAL)

        sizerPanelName = wx.BoxSizer(wx.HORIZONTAL)
        sizer_main.Add(sizerPanelName, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.labelPanelName = wx.StaticText(self, wx.ID_ANY, "Magnetic Configuration")
        self.labelPanelName.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizerPanelName.Add(self.labelPanelName, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)

        self.buttonAdvanced = wx.Button(self, wx.ID_ANY, "Advanced")
        sizerPanelName.Add(self.buttonAdvanced, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizerLatticeParameters = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_main.Add(sizerLatticeParameters, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        grid_sizer_3 = wx.FlexGridSizer(1, 6, 0, 0)
        sizerLatticeParameters.Add(grid_sizer_3, 1, wx.ALL | wx.EXPAND, 0)

        labelCorrLength = wx.StaticText(self, wx.ID_ANY, "corr. length")
        grid_sizer_3.Add(labelCorrLength, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.textCtrlCorrLength = wx.TextCtrl(self, wx.ID_ANY, "0.0", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlCorrLength, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 5)

        label_1 = wx.StaticText(self, wx.ID_ANY, "ord. scale")
        grid_sizer_3.Add(label_1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.textCtrlOrdScale = wx.TextCtrl(self, wx.ID_ANY, "1.0", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlOrdScale, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 5)

        labelParaScale = wx.StaticText(self, wx.ID_ANY, "para. scale")
        grid_sizer_3.Add(labelParaScale, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.textCtrlParaScale = wx.TextCtrl(self, wx.ID_ANY, "1.0", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlParaScale, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 5)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_main.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 5)

        grid_sizer_2 = wx.FlexGridSizer(1, 6, 0, 0)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        self.radio1 = wx.RadioBox(self, wx.ID_ANY, "mPDF Type", choices=["Normalized", "Unnormalized"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radio1.SetSelection(0)
        grid_sizer_2.Add(self.radio1, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)

        self.buttonMagviewer = wx.Button(self, wx.ID_ANY, "Mag Viewer")
        grid_sizer_2.Add(self.buttonMagviewer, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        sizerAtoms = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.VERTICAL)
        sizer_main.Add(sizerAtoms, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        sizer_1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizerAtoms.Add(sizer_1, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 0)

        labelIncludedPairs = wx.StaticText(self, wx.ID_ANY, "Included Pairs")
        sizer_1.Add(labelIncludedPairs, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.textCtrlIncludedPairs = wx.TextCtrl(self, wx.ID_ANY, "all-all", style=wx.TE_READONLY)
        self.textCtrlIncludedPairs.SetMinSize((250, 28))
        sizer_1.Add(self.textCtrlIncludedPairs, 0, wx.ALL, 5)

        self.gridAtoms = AutoWidthLabelsGrid(self, wx.ID_ANY, size=(1, 1))
        self.gridAtoms.CreateGrid(0, 4)
        self.gridAtoms.EnableDragRowSize(0)
        self.gridAtoms.SetColLabelValue(0, "elem")
        self.gridAtoms.SetColLabelValue(1, "basis vecs")
        self.gridAtoms.SetColLabelValue(2, "prop. vecs")
        self.gridAtoms.SetColLabelValue(3, "FF key")
        sizerAtoms.Add(self.gridAtoms, 1, wx.EXPAND, 0)

        grid_sizer_2.AddGrowableCol(0)
        grid_sizer_2.AddGrowableCol(1)
        grid_sizer_2.AddGrowableCol(2)
        grid_sizer_2.AddGrowableCol(3)
        grid_sizer_2.AddGrowableCol(4)
        grid_sizer_2.AddGrowableCol(5)

        self.SetSizer(sizer_main)
        sizer_main.Fit(self)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onAdvanced, self.buttonAdvanced)
        self.Bind(wx.EVT_BUTTON, self.onPanel, self.buttonMagviewer)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_CHANGED, self.onCellChange, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.onCellRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_EDITOR_SHOWN, self.onEditorShown, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_LABEL_RIGHT_CLICK, self.onLabelRightClick, self.gridAtoms)
        self.Bind(wx.EVT_RADIOBOX, self.checkNormalized, self.radio1)
        self.Bind(wx.EVT_TEXT, self.applyTextCtrlPanel, self.textCtrlCorrLength)
        self.Bind(wx.EVT_TEXT, self.applyTextCtrlPanel, self.textCtrlOrdScale)
        self.Bind(wx.EVT_TEXT, self.applyTextCtrlPanel, self.textCtrlParaScale)
        # end wxGlade
        self.magviewOpen = False
        self.__customProperties()
        self.firstViewerLaunch = True
        self.Xarr = []
        self.Update()

##########################################################################
    # Misc Methods
    def addPhaseGridRef(self, phaseGridAtoms):
        self.phaseGridAtoms = phaseGridAtoms

    def __customProperties(self):
        """Custom properties for the panel."""
        self.structure = None
        self.constraints = {}
        self.results = None
        self._textctrls = []
        self._row = 0
        self._col = 0
        self._focusedText = None
        self._selectedCells = []

        self.lAtomConstraints = ['elem', 'basis vecs', 'prop. vecs', 'FF key']

        # ff keys in ffkey dictionary
        self.ffkeys = set(['None', 'Am2', 'Am3', 'Am4', 'Am5', 'Am6', 'Am7', 'Ce2', 'Co0',
                           'Co1', 'Co2', 'Co3', 'Co4', 'Cr0', 'Cr1', 'Cr2', 'Cr3', 'Cr4', 'Cu0', 'Cu1', 'Cu2',
                           'Cu3', 'Cu4', 'Dy2', 'Dy3', 'Er2', 'Er3', 'Eu2', 'Eu3', 'Fe0', 'Fe1', 'Fe2', 'Fe3',
                           'Fe4', 'Gd2', 'Gd3', 'Ho2', 'Ho3', 'Mn0', 'Mn1', 'Mn2', 'Mn3', 'Mn4', 'Mo0', 'Mo1',
                           'Nb0', 'Nb1', 'Nd2', 'Nd3', 'Ni0', 'Ni1', 'Ni2', 'Ni3', 'Ni4', 'Np3', 'Np4', 'Np5',
                           'Np6', 'Pd0', 'Pd1', 'Pr3', 'Pu3', 'Pu4', 'Pu5', 'Pu6', 'Rh0', 'Rh1', 'Ru0', 'Ru1',
                           'Sc0', 'Sc1', 'Sc2', 'Sm2', 'Sm3', 'Tb2', 'Tb3', 'Tc0', 'Tc1', 'Ti0', 'Ti1', 'Ti2',
                           'Ti3', 'Tm2', 'Tm3', 'U3', 'U4', 'U5', 'V0', 'V1', 'V2', 'V3', 'V4', 'Y0', 'Yb2',
                           'Yb3', 'Zr0', 'Zr1'])

        # pdffit internal naming
        self.lConstraintsMap = {
            'textCtrlCorrLength': 'lat(1)',
            'textCtrlOrdScale': 'lat(2)',
            'textCtrlParaScale': 'lat(3)',
        }

        #self.lConstraintsMap = {}

        # bind onSetFocus onKillFocus events to text controls

        for tname in self.lConstraintsMap:
            self.__dict__[tname].Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            self.__dict__[tname].Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
            self.__dict__[tname].SetValidator(TextValidator(FLOAT_ONLY))
            self.__dict__[tname].Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        self.textCtrlIncludedPairs.Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
        self.textCtrlIncludedPairs.Bind(
            wx.EVT_KILL_FOCUS, self.onSelectedPairs)
        self.textCtrlIncludedPairs.Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        # define tooltips
        #self.setToolTips(tooltips.magpanel)
        # make sure tooltips exist for all lConstraintsMap controls as
        # this is later assumed in restrictConstrainedParameters code

        """
        for tname in self.lConstraintsMap:
            assert getattr(self, tname).GetToolTip() is not None
        """

        # set 'elem' column to read-only
        attr = wx.grid.GridCellAttr()
        attr.SetReadOnly(True)
        attr.IncRef()
        self.gridAtoms.SetColAttr(0, attr)
        # drop local reference to `attr` as it was constructed here.
        attr.DecRef()

        # catch key events and apply them to the grid
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        return

    # Create the onTextCtrlKey event handler from textCtrlAsGridCell from
    # wxextensions.textctrlutils
    onTextCtrlKey = textCtrlAsGridCell

    def checkNormalized(self, event):
        """Sets the normalization of the structure."""
        if self.radio1.GetStringSelection() == "Normalized":
            self.structure.magStructure.normalized = True
        elif self.radio1.GetStringSelection() == "Unnormalized":
            self.structure.magStructure.normalized = False

    def getNormalized(self):
        """Gets the normalization of the structure."""
        if self.structure.magStructure.normalized == True:
            self.radio1.SetSelection(0)
        else:
            self.radio1.SetSelection(1)

    def _cache(self):
        """Cache the current structure and constraints for future comparison."""
        pass

    def arrayToStr(self, arr):
        """returns basis and kvec numpy arrays in str format
        Ex. [[1 2 3],[4 5 6]] -> (1, 2, 3),(4, 5, 6)"""
        if arr is None or type(arr) != np.ndarray:
            return
        ret = str(arr.astype(float).tolist())[1:-1]
        ret = ret.replace("[", "(")
        ret = ret.replace("]", ")")
        return ret

    __this_is_first_refresh = True

    def refresh(self):
        """Refreshes widgets on the panel."""
        if self.structure.magStructure is None:
            return
        self.getNormalized()
        #magpanelutils.refreshTextCtrls(self)
        self.textCtrlCorrLength.SetValue(str(self.structure.magStructure.corrLength))
        self.textCtrlOrdScale.SetValue(str(self.structure.mpdffit['ordScale']))
        self.textCtrlParaScale.SetValue(str(self.structure.mpdffit['paraScale']))
        pairs = self.structure.getSelectedPairs()
        self.textCtrlIncludedPairs.SetValue(pairs)
        magpanelutils.refreshGrid(self)
        self.gridAtoms.ForceRefresh()
        self.Refresh()
        self.Update()
        #self.restrictConstrainedParameters()

        # wxpython 3.0 on Windows 7 prevents textCtrlA from receiving
        # left-click input focus and can be only focused with a Tab key.
        # This only happens for the first input, the text control behaves
        # normally after receiving focus once.
        # Workaround: do explicit focus here for the first rendering.
        if self.__this_is_first_refresh:
            self.__this_is_first_refresh = False
            #focusowner = self.textCtrlA.FindFocus()
            #wx.CallAfter(self.textCtrlA.SetFocus)
            '''
            if focusowner is not None:
                wx.CallAfter(focusowner.SetFocus)
            '''
        return
    '''
    def restrictConstrainedParameters(self):
        """Set 'read-only' boxes that correspond to constrained parameters."""

        self.setToolTips(tooltips.magpanel)
        #txtbg = self.textCtrlA.DefaultStyle.BackgroundColour

        # First the TextCtrls
        for key, var in self.lConstraintsMap.items():
            textCtrl = getattr(self, key)
            if var in self.constraints:
                textCtrl.SetEditable(False)
                textCtrl.SetBackgroundColour(
                        wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
                tt = textCtrl.GetToolTip()
                tt.SetTip(self.constraints[var].formula)
            else:
                textCtrl.SetEditable(True)
                #textCtrl.SetBackgroundColour(txtbg)
                textCtrl.SetBackgroundColour(wx.WHITE)

        # Now the grid
        rows = self.gridAtoms.GetNumberRows()
        cols = self.gridAtoms.GetNumberCols()
        for i in range(rows):
            for j in range(1, cols):
                var = self.lAtomConstraints[j-1]
                var += '(%i)'%(i+1)
                if var in self.constraints:
                    self.gridAtoms.SetReadOnly(i, j, True)
                    self.gridAtoms.SetCellBackgroundColour(i, j,
                        wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
                else:
                    self.gridAtoms.SetReadOnly(i, j, False)
                    self.gridAtoms.SetCellBackgroundColour(i, j, wx.NullColour)

        return
'''
    def applyTextCtrlPanel(self, event):
        """Update a structure according to a change in a TextCtrl.

        id      --  textctrl id
        value   --  new value
        """
        if self.structure is None:
            return
        textCtrl = event.GetEventObject()
        id = textCtrl.GetId()
        try:
            if id == self.textCtrlCorrLength.GetId():
                value = float(self.textCtrlCorrLength.GetValue())
                self.structure.magStructure.corrLength = value
                self.textCtrlCorrLength.SetValue(value)
            elif id == self.textCtrlOrdScale.GetId():
                value = float(self.textCtrlOrdScale.GetValue())
                self.structure.mpdffit['ordScale'] = value
            elif id == self.textCtrlParaScale.GetId():
                value = float(self.textCtrlParaScale.GetValue())
                self.structure.mpdffit['paraScale'] = value
            return value

        except:
            return None
# self.mpdffit = {"qdamp": 0.0, "ordScale": 1.0, "paraScale": 1.0}
    def applyTextCtrlChange(self, id, value):
        """Update a structure according to a change in a TextCtrl.

        id      --  textctrl id
        value   --  new value
        """
        if self.structure is None:
            return

        try:
            value = float(value)
            if id == self.textCtrlCorrLength.GetId():
                self.structure.magStructure.corrLength = value
            elif id == self.textCtrlOrdScale.GetId():
                self.structure.mpdffit['ordScale'] = value
            elif id == self.textCtrlParaScale.GetId():
                self.structure.mpdffit['paraScale'] = value
            return value

        except:
            return None

    def readCoordinates(self, text):
        """Returns a str of coordinates as a nested numpy array

        crds    --  string of coordinates in format (x,y,z),(x,y,z)...
        """
        try:
            # check if string is valid
            text = text.replace(" ", "")
            text = text.replace("[", "(")
            text = text.replace("{", "(")
            text = text.replace("]", ")")
            text = text.replace("}", ")")
            if text[-1] != ",":
                text = text + ","
            #if not re.match("^(\(\d*\.?\d+\,\d*\.?\d+\,\d*\.?\d+\),)+$", text):
                #return
            text = text[:-1]
            ret = []
            crds = text.split('),')  # split coordinates
            for i, crd in enumerate(crds):
                if crd[0] != '(':  # verify valid coordinate
                    crd = "(" + crd
                if crd[-1] != ')':
                    crd = crd + ")"
                if i == len(crds) - 1:  # remove end parenthesis not removed by split
                    crd = crd[:-1]
                crd = crd[1:]  # remove start parentheses
                crd = crd.split(',')  # split each coordinate
                if len(crd) != 3:
                    return
                arr = []
                for val in crd:
                    print(val)
                    if val.replace('.','',1).isdigit() is True:  # checks validity of input
                        arr.append(float(val))  # add each value to an array
                    else:
                        return
                ret.append(arr)
            return np.array(ret)

        except:
            return

    def applyCellChange(self, i, j, value):
        """Update an atom according to a change in a cell.

        i       --  cell position
        j       --  cell position
        value   --  new value
        """
        if not self.mainFrame or self.structure.magStructure is None:
            return
        if j == 0:
            return

        # ignore the change if the value is not valid
        try:
            i = int(self.gridAtoms.GetRowLabelValue(i)) - 1
            label = self.structure.magnetic_atoms[i][1]
            if j == 1:
                value = self.readCoordinates(value)
                # basis vecs
                self.structure.magStructure.species[label].basisvecs = value
                value = self.arrayToStr(value)
            elif j == 2:
                value = self.readCoordinates(value)
                # prop. vecs
                self.structure.magStructure.species[label].kvecs = value
                value = self.arrayToStr(value)
            elif j == 3:
                value = value if value in self.ffkeys else None
                # FF key
                self.structure.magStructure.species[label].ffparamkey = value

            self.mainFrame.needsSave()
            return value

        except ValueError:
            return

    ##########################################################################
    # Event Handlers

    def onAdvanced(self, event):
        frame = AdvancedFrame(
            title="Advanced", mags=self.structure.magnetic_atoms, struc=self.structure)

    def onPanel(self, event):
        if False:
            raise CustomError("An error occurred")
        if self.magviewOpen is False:
            def split_up_magnetics(cond, mags, struc, row_element):
                X, orig_inx, nonmag, Xelem = [], [], [], []

                for i in range(len(struc)):
                    if str(cond[i]) in mags:
                        X += [struc[i, :]]
                        orig_inx += [i]
                        Xelem += [row_element[i]]
                    else:
                        nonmag += [struc[i, :]]
                return np.array(X), np.array(orig_inx), np.array(nonmag), np.array(Xelem)
            mags = []
            count = 1
            for a in self.structure.magnetic_atoms:
                if a[0] == 1:
                    mags.append(str(count))
                count += 1

            struc = self.structure.xyz_cartn
            elems = list(set(self.structure.element))
            elems.sort() 				# alphabetical list of elements
            # 1 to n+1 indices for each element
            element_inx = np.arange(1, 1+len(elems))
            # element name to associated number
            dmap = dict(zip(elems, element_inx))
            revdmap = dict(zip(element_inx, elems))
            row_element = np.array([dmap[i] for i in self.structure.element])

            X, orig_inx, nonmag, Xelem = split_up_magnetics(
                np.arange(1, 1+len(struc)), mags, struc, row_element)

            if self.firstViewerLaunch is False:  # Checks if changes to Mag Structure have been made
                XarrTmp = self.Xarr
                if X != self.Xarr:
                    toDelete = []
                    for i in range(len(X)):  # Checks for added mag atoms
                        isInArr = False
                        for j in range(len(self.Xarr)):
                            if X[i, 0] == self.Xarr[j, 0] and X[i, 1] == self.Xarr[j, 1] and X[i, 2] == self.Xarr[j, 2]:
                                isInArr = True
                        if isInArr is False:
                            Xtmp = np.array(
                                [X[i, 0], X[i, 1], X[i, 2], 0, 0, 0, 0, 1, 0])
                            XarrTmp = np.append(
                                XarrTmp, [Xtmp], axis=0)
                    self.Xarr = XarrTmp
                    for i in range(len(self.Xarr)):  # Checks for deleted mag atoms
                        isInArr = False
                        for j in range(len(X)):
                            if self.Xarr[i, 0] == X[j, 0] and self.Xarr[i, 1] == X[j, 1] and self.Xarr[i, 2] == X[j, 2]:
                                isInArr = True
                        if isInArr is False:
                            toDelete.append(i)
                    self.Xarr = np.delete(self.Xarr, toDelete, axis=0)
                X = np.array(self.Xarr)

            canvas = CanvasFrame(X, Xelem, revdmap, self, nonmag, basis=self.structure.lattice.stdbase)
            #self.magviewOpen = True

    # TextCtrl Events

    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be compared in onKillFocus later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return

    def onKillFocus(self, event):
        """Check value of TextCtrl and update structure if necessary."""
        """
        if not self.mainFrame:
            return
        textctrl = event.GetEventObject()
        value = textctrl.GetValue()
        if value != self._focusedText:
            self.applyTextCtrlChange(textctrl.GetId(), value)
            magpanelutils.refreshTextCtrls(self)
            self.mainFrame.needsSave()
        self._focusedText = None
        event.Skip()
        """
        return

    def onSelectedPairs(self, event):
        """Check to see if the value of the selected pairs is valid."""
        if not self.mainFrame:
            return
        value = self.textCtrlIncludedPairs.GetValue()
        self.structure.setSelectedPairs(value)
        value = self.structure.getSelectedPairs()
        self.textCtrlIncludedPairs.SetValue(value)
        event.Skip()
        return

    # Grid Events
    def onLabelRightClick(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        if self.structure is not None:
            dx = dy = 0
            if event.GetRow() == -1:
                dy = self.gridAtoms.GetGridCornerLabelWindow().GetSize().y
            if event.GetCol() == -1:
                dx = self.gridAtoms.GetGridCornerLabelWindow().GetSize().x

            # do not popup menu if the whole grid is set to read only
            if len(self.structure) == 0:
                self.popupMenu(self.gridAtoms, event.GetPosition().x-dx,
                               event.GetPosition().y-dy)
        event.Skip()
        return

    def onCellRightClick(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        self._row = event.GetRow()
        self._col = event.GetCol()

        # If the right-clicked node is not part of a group, then make sure that
        # it is the only selected cell.
        append = False
        r = self._row
        c = self._col
        if self.gridAtoms.IsInSelection(r, c):
            append = True
        self.gridAtoms.SelectBlock(r, c, r, c, append)

        self.popupMenu(self.gridAtoms, event.GetPosition().x,
                       event.GetPosition().y)
        event.Skip()
        return

    def onEditorShown(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Capture the focused text when the grid editor is shown."""
        i = event.GetRow()
        j = event.GetCol()
        self._focusedText = self.gridAtoms.GetCellValue(i, j)
        self._selectedCells = gridutils.getSelectedCells(self.gridAtoms)
        return

    def onCellChange(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Update focused and selected text when a cell changes."""
        # NOTE: be careful with refresh(). It calls Grid.AutoSizeColumns, which
        # creates a EVT_GRID_CMD_CELL_CHANGED event, which causes a recursion
        # loop.
        i = event.GetRow()
        j = event.GetCol()

        value = self.gridAtoms.GetCellValue(i, j)
        while (i, j) in self._selectedCells:
            self._selectedCells.remove((i, j))
        # We need the edited cell to be at the front of the list
        self._selectedCells.insert(0, (i, j))
        self.fillCells(value)
        self._focusedText = None
        return

    def fillCells(self, value):
        """Fill cells with a given value.

        value       --  string value to place into cells

        This uses the member variable _selectedCells, a list of (i,j) tuples for
        the selected cells.
        """
        for (i, j) in self._selectedCells:
            if not self.gridAtoms.IsReadOnly(i, j):
                # Get the last valid text from the cell. For the cell that triggered
                # this method, that is the _focusedText, for other cells it is the
                # value returned by GetCellValue
                oldvalue = self._focusedText or self.gridAtoms.GetCellValue(i, j)
                self._focusedText = None
                newvalue = self.applyCellChange(i, j, value)
                if newvalue is None:
                    newvalue = oldvalue
                self.gridAtoms.SetCellValue(i, j, newvalue)

        gridutils.quickResizeColumns(self.gridAtoms, self._selectedCells)
        return

    def onKey(self, event):
        """Catch key events in the panel."""
        key = event.GetKeyCode()

        # Select All
        # Ctrl A
        if event.ControlDown() and key == 65:
            rows = self.gridAtoms.GetNumberRows()
            cols = self.gridAtoms.GetNumberCols()
            self.gridAtoms.SelectBlock(0, 0, rows, cols)

        # context menu key
        elif key == wx.WXK_MENU:
            self.popupMenu(self.gridAtoms,
                           event.GetPosition().x, event.GetPosition().y)

        # Vim-like search for atom selection
        elif key == 47:
            self.onPopupSelect(event)

        # Delete an atom
        # Delete
        elif key == 127:
            selected = self.gridAtoms.GetSelectedRows()
            if selected:
                self.structure.deleteAtoms(selected)
                self.refresh()
                self.mainFrame.needsSave()

        # Ctrl -
        elif event.ControlDown() and key == 45:
            indices = gridutils.getSelectionRows(self.gridAtoms)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()

        # Append an atom
        # Ctrl + or Ctrl =
        elif event.ControlDown() and (key == 61 or key == 43):
            indices = gridutils.getSelectionRows(self.gridAtoms)
            pos = 0
            if indices:
                pos = 1+indices[-1]
            elif self.structure:
                pos = len(self.structure)
            # insert "rows" atoms into the structure
            atoms = [_defaultNewAtom()]
            self.structure.insertAtoms(pos, atoms)
            self.refresh()
            self.mainFrame.needsSave()

        else:
            event.Skip()

        return

    ##########################################################################
    # Grid popup menu and handlers

    def popupMenu(self, window, x, y):
        """Creates the popup menu

        window  --  window, where to popup a menu
        x       --  x coordinate
        y       --  y coordinate
        """
        # only do this part the first time so the events are only bound once
        if not hasattr(self, "insertID"):
            self.insertID = wx12.NewIdRef()
            self.deleteID = wx12.NewIdRef()
            self.selectID = wx12.NewIdRef()
            self.copyID = wx12.NewIdRef()
            self.pasteID = wx12.NewIdRef()
            self.supercellID = wx12.NewIdRef()
            self.spaceGroupID = wx12.NewIdRef()

            self.Bind(wx.EVT_MENU, self.onPopupInsert, id=self.insertID)
            self.Bind(wx.EVT_MENU, self.onPopupDelete, id=self.deleteID)
            self.Bind(wx.EVT_MENU, self.onPopupSelect, id=self.selectID)
            self.Bind(wx.EVT_MENU, self.onPopupCopy, id=self.copyID)
            self.Bind(wx.EVT_MENU, self.onPopupPaste, id=self.pasteID)
            self.Bind(wx.EVT_MENU, self.onPopupSupercell, id=self.supercellID)
            self.Bind(wx.EVT_MENU, self.onPopupSpaceGroup,
                      id=self.spaceGroupID)

        # make a menu
        menu = wx.Menu()

        # add some other items
        menu.Append(self.insertID, "&Insert atoms...")
        menu.Append(self.deleteID, "&Delete atoms")
        menu.AppendSeparator()
        menu.Append(self.selectID, "Select &atoms...")
        menu.Append(self.copyID, "&Copy")
        menu.Append(self.pasteID, "&Paste")
        menu.AppendSeparator()
        menu.Append(self.supercellID, "Create supercell...")
        menu.Append(self.spaceGroupID, "Expand space group...")

        # Disable some items if there are no atoms selected
        indices = gridutils.getSelectionRows(self.gridAtoms)
        if not indices:
            menu.Enable(self.deleteID, False)
            menu.Enable(self.spaceGroupID, False)

        # Disable some items if there is no structure
        if self.structure is None or len(self.structure) == 0:
            menu.Enable(self.deleteID, False)
            menu.Enable(self.supercellID, False)
            menu.Enable(self.spaceGroupID, False)

        # Check for copy/paste
        if not magpanelutils.canCopySelectedCells(self):
            menu.Enable(self.copyID, False)
        if not magpanelutils.canPasteIntoCells(self):
            menu.Enable(self.pasteID, False)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        window.PopupMenu(menu, wx.Point(x, y))
        menu.Destroy()
        return

    def onPopupInsert(self, event):
        """Adds rows to the grid."""
        if self.structure is not None:
            dlg = InsertRowsDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                rows = dlg.spin_ctrl_Rows.GetValue()

                if len(self.structure) == 0:
                    self._row = 0
                elif (dlg.radio_box_where.GetSelection() == 1):  # if selected "below"
                    self._row += 1

                # insert "rows" atoms into the structure
                atoms = [_defaultNewAtom() for i in range(rows)]
                self.structure.insertAtoms(self._row, atoms)
                self.refresh()
                self.mainFrame.needsSave()

                # Highlight the elements of the new rows so that they can be
                # changed by the user.
                self.gridAtoms.SetFocus()
                self.gridAtoms.SelectBlock(
                    self._row, 0, self._row+len(atoms)-1, 0)
                self.gridAtoms.SetGridCursor(self._row, 0)

            dlg.Destroy()
        return

    def onPopupDelete(self, event):
        """Deletes the row under mouse pointer from the grid."""
        if self.structure is not None:
            indices = gridutils.getSelectionRows(self.gridAtoms)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()
        return

    def onPopupSelect(self, event):
        """Limit cell selection to specified atom selection string.
        """
        magpanelutils.showSelectAtomsDialog(self)
        return

    def onPopupCopy(self, event):
        """Copy selected cells."""
        magpanelutils.copySelectedCells(self)
        return

    def onPopupPaste(self, event):
        """Paste previously copied cells."""
        magpanelutils.pasteIntoCells(self)
        return

    def onPopupSupercell(self, event):
        """Create a supercell with the supercell dialog."""
        from diffpy.pdfgui.gui.supercelldialog import SupercellDialog
        if self.structure is not None:
            dlg = SupercellDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                mno = dlg.getMNO()
                self.structure.expandSuperCell(mno)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return

    def onPopupSpaceGroup(self, event):
        """Create a supercell with the supercell dialog."""
        from diffpy.pdfgui.gui.sgstructuredialog import SGStructureDialog
        if self.structure is not None:

            indices = gridutils.getSelectionRows(self.gridAtoms)
            dlg = SGStructureDialog(self)
            dlg.mainFrame = self.mainFrame
            dlg.indices = indices
            dlg.setStructure(self.structure)
            if dlg.ShowModal() == wx.ID_OK:
                spcgrp = dlg.getSpaceGroup()
                offset = dlg.getOffset()
                self.structure.expandAsymmetricUnit(spcgrp, indices, offset)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return

# end of class MagConfigurePanel

# Local helpers --------------------------------------------------------------


def _defaultNewAtom():
    """Create new atom instance with non-zero initial U.
    """
    uii = 0.003
    rv = Atom("C", [0.0, 0.0, 0.0],
              U=[[uii, 0, 0], [0, uii, 0], [0, 0, uii]])
    return rv
