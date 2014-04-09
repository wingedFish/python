#encoding utf-8
import wx

app = wx.App()
win = wx.Frame(None,title="essay",size=(700,800))

panel = wx.Panel(win)

openButton = wx.Button(panel,label="open")
saveButton = wx.Button(panel,label="save")
fileName = wx.TextCtrl(panel)
contents = wx.TextCtrl(panel)

hbox = wx.BoxSizer()
hbox.Add(fileName,proportion=1,flag = wx.LEFT,border=5)
hbox.Add(openButton,proportion=0,flag = wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag = wx.LEFT,border=5)


vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag = wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM,border=5)

panel.SetSizer(vbox)

win.Show()
app.MainLoop()