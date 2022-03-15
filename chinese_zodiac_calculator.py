# coding=utf-8
import wx

# 自定义窗口
class CZ_cal(wx.Frame):
    def __init__(self):
        super().__init__(None, title='生肖计算器', size=(275, 200)) # 设置窗口标题、大小

        # 添加控件
        self.panel = wx.Panel(parent=self)
        self.SetMaxSize((275,200))
        self.SetMinSize((275,200))
        self.Centre()
        self.panel.SetBackgroundColour('#c21f30')
        self.icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        caption = wx.StaticText(self.panel, label='输入公元前年份需加上负号，没有公元0年。')
        text_type = wx.StaticText(self.panel, label='年份：')
        self.text_box = wx.TextCtrl(self.panel)
        button = wx.Button(self.panel, label='计算')
        self.Bind(wx.EVT_BUTTON, self.on_cal, button)
        result_type = wx.StaticText(self.panel, label='生肖：')
        self.result = wx.StaticText(self.panel, label='')
        
        # 布局管理
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer()

        vbox.Add(caption, proportion=1, flag=wx.ALIGN_LEFT | wx.EXPAND | wx.ALL, border=10)
        vbox.Add(text_type, proportion=1, flag=wx.ALIGN_LEFT | wx.EXPAND | wx.LEFT, border=10)
        hbox.Add(self.text_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(button, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(hbox, proportion=1, flag=wx.ALIGN_LEFT)
        vbox.Add(result_type, proportion=1, flag=wx.ALIGN_LEFT | wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(self.result, proportion=1, flag=wx.ALIGN_LEFT | wx.EXPAND | wx.ALL, border=10)
        
        self.panel.SetSizer(vbox)

    # 计算生肖    
    def on_cal(self, event):
        # 检查并解决异常
        try:
            year = int(self.text_box.GetValue())
            
            ad = (year - 1) % 12 # 计算公元年份的表达式
            bc = (year - 1) % 10 # 计算公元前年份生肖的表达式
            z = ['鸡', '狗', '猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴'] # 所有生肖

            # 判断年份为公元后、公元前还是0并输出结果
            if year >= 1:
                self.result.SetLabelText(z[ad])
            elif year == 0:
                self.result.SetLabelText('没有公元0年。')
            else:
                self.result.SetLabelText(z[bc + 1])
        except ValueError as e:
            self.result.SetLabelText('请输入整数。')
        finally:
            f = '这个变量只是为了释放资源而已。'

app = wx.App() # 创建应用程序对象
frm = CZ_cal() # 创建窗口对象
frm.Show() # 显示窗口
app.MainLoop() # 进入主事件循环
