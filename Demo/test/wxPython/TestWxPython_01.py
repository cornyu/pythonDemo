import wx #导入wxPython库


class Panel(wx.Panel):

    def __init__(self,parent):

        wx.Panel.__init__(self,parent=parent, id=-1)

        pass

class Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, parent = None, title = u'量化软件', size=(1000,600), style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)

        self.DispPanel= Panel(self)

        pass

class App(wx.App):

    def OnInit(self):

        self.frame = Frame()

        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

if __name__ == '__main__':

    app = App()

    app.MainLoop()