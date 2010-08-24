"""
    timer.py

    This module controls all the timers and plays a wav file 
    after countdown.
"""

import wx

class Timer(wx.Timer):
    def __init__(self, track, hours, minutes, timer_id):
        wx.Timer.__init__(self)
        # instance of main GUI - for setting the timer label 
        # every 1 minute
        self.track = track
        self.hours = hours
        self.minutes = minutes
        self.timer_id = timer_id
        
        self.Bind(wx.EVT_TIMER, self.do, self)
        
    def do(self, event):
        self.track.set_label(self.hours, self.minutes, self.timer_id)
        self.minutes -= 1
        
        if self.minutes < 0:
            self.hours -= 1
            self.minutes = 59  
            
        if self.hours <= 0 and self.minutes <= 0:
            sound = wx.Sound("/media/Storage/Music/everything.wav")
            
            # play sound asynchronously, if SOUND_SYNC is used instead, the
            # whole GUI will freeze until it is done playing
            sound.Play(wx.SOUND_ASYNC)     
            self.track.set_label(self.hours, self.minutes, self.timer_id)
            self.Stop()
    
