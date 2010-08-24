#! /usr/bin/env python

"""
    track.py

    This is the main GUI showing the actual countdown timer and todo 
    textbox labels.
"""

import wx
import settimer
import glob
import os.path

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Setup GUI controls so that its names would be something like the following:
        # txt_todo1 --> txt_todo5, lbl_timer1 --> lbl_timer5 ...
        # It is done this way to eliminate redundancy in code 
        for i in range(1,6):
            setattr(self, "txt_todo%d" % i, wx.TextCtrl(self, -1, ""))
            setattr(self, "lbl_timer%d" % i, wx.StaticText(self, -1, "00:00"))
            setattr(self, "btn_set%d" % i, wx.Button(self, -1, "Set Timer"))
            
            # Add an 'id' attribute to self.btn_set# so the program can keep track of which row  
            # and which specific button was clicked. That way, the program can figure out which
            # lbl_timer# should be set
            setattr(getattr(self, "btn_set%d" % i), "id", i)
            
            # Bind all btn_set# buttons to self.on_set
            self.Bind(wx.EVT_BUTTON, self.on_set, getattr(self, "btn_set%d" % i))
        
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Track Work")
        for x in range(1,6):
            getattr(self, "txt_todo%d" % x).SetMinSize((300, 25))
            getattr(self, "lbl_timer%d" % x).SetMinSize((100, 30))
            getattr(self, "lbl_timer%d" % x).SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
            getattr(self, "btn_set%d" % x).SetMinSize((85, 27))     

    def __do_layout(self):
        flex_sizer = wx.FlexGridSizer(5, 3, 2, 25)

        for y in range(1,6):
            flex_sizer.Add(getattr(self, "txt_todo%d" % y), 0, 0, 0)
            flex_sizer.Add(getattr(self, "lbl_timer%d" % y), 0, 0, 0)
            flex_sizer.Add(getattr(self, "btn_set%d" % y), 0, 0, 0)        
        
        self.SetSizer(flex_sizer)
        flex_sizer.Fit(self)
        self.Layout()

        
    def on_set(self, event): 
        # Grab the id of the button that was clicked
        btn_id = event.GetEventObject().id
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        set_frame = settimer.SetTimerWindow(None, -1, "")
        set_frame.get_out_instance(self, btn_id)
        app.SetTopWindow(set_frame)
        set_frame.Show()
        app.MainLoop()
        event.Skip()
        
    def set_label(self, hours, minutes, id):
        # Set the countdown timer label.
        # This works properly because it knows which specific label to modify.
        # The id was taken from a specific btn_set# button.
        getattr(self, "lbl_timer%d" % id).SetLabel("%02d:%02d" % (hours, minutes))

    def check_wav(self):
        # check if there's a wav file in the same dir as the script. If there is none, 
        # show an error message and return false so the main frame won't show 
        if not glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)),"*.wav")):
            d = wx.messagedialog(none, "you need to have a .wav file beside the script to make "
            "it work", "wav required", wx.ok | wx.icon_error)
            d.showmodal()
            return False
        return True


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    main_frame = MyFrame(None, -1, "")

    if main_frame.check_wav():
        app.SetTopWindow(main_frame)
        main_frame.Show()
        app.MainLoop()
