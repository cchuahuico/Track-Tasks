"""
    settimer.py

    This is the small GUI that shows up when a user clicks
    the set timer window.
"""

import wx
import timer


class SetTimerWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.txt_hours = wx.TextCtrl(self, -1, "")
        self.lbl_hours = wx.StaticText(self, -1, "HH")
        self.txt_minutes = wx.TextCtrl(self, -1, "")
        self.lbl_minutes = wx.StaticText(self, -1, "MM")
        self.btn_set = wx.Button(self, -1, "Set")
        self.out_instance = None
        self.timer_id = 0
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_set, self.btn_set)

    def __set_properties(self):
        self.SetTitle("Set Timer")
        self.txt_hours.SetMinSize((40, 25))
        self.lbl_hours.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt_minutes.SetMinSize((40, 25))
        self.lbl_minutes.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.btn_set.SetMinSize((50, 27))

    def __do_layout(self):
        flex_sizer = wx.FlexGridSizer(1, 5, 0, 4)
        flex_sizer.Add(self.txt_hours, 0, 0, 0)
        flex_sizer.Add(self.lbl_hours, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        flex_sizer.Add(self.txt_minutes, 0, 0, 0)
        flex_sizer.Add(self.lbl_minutes, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        flex_sizer.Add(self.btn_set, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(flex_sizer)
        flex_sizer.Fit(self)
        flex_sizer.AddGrowableRow(1)
        flex_sizer.AddGrowableCol(3)
        self.Layout()
        
    def get_out_instance(self, out, id):
        # out is an instance of the main GUI window
        self.out_instance = out
        self.timer_id = id

    def on_set(self, event): 
        # If user left hours textbox blank, assume a 0 value
        try:
            hours = int(self.txt_hours.GetValue())
        except ValueError:
            hours = 0
        minutes = int(self.txt_minutes.GetValue())
        
        # set timer label
        self.out_instance.set_label(hours, minutes, self.timer_id)
        t = timer.Timer(self.out_instance, hours, minutes, self.timer_id)
        
        # countdown timer every 1 minute
        t.Start(60000)
        
        # Close the Set Timer frame
        self.Destroy()
        event.Skip()

