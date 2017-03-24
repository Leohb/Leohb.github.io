import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.font
import idlelib.tooltip
import datetime
import weather_report


class WeatherReportGUI(tk.Frame):
    '''This class is used to query weather report'''

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg='sky blue')
        self.pack()
        self.initUI()
        self.weather_dict = {}
        self.weather_history = {}
        self.weather_dict = weather_report.convert_txt_to_dict('weather_info.txt', self.weather_dict)

    def initUI(self):
        '''This function is used to create widgets'''
        # font
        self.font = tk.font.Font(family='Times', size=12)
        self.bg = 'sky blue'
        # create widgets
        self.history_icon = tk.PhotoImage(file='history.png')
        self.history = tk.Button(self, image=self.history_icon, command=self.print_history, bg=self.bg)
        idlelib.tooltip.ToolTip(self.history, '查询历史记录')
        self.history.grid(row=0, column=0, sticky=tk.W+tk.N+tk.S+tk.E)

        self.label = tk.Label(self, text='城市', anchor=tk.E, font=self.font, bg=self.bg)
        self.label.grid(row=0, column=1, sticky=tk.E)
        self.entry = tk.Entry(self, font=self.font)
        self.entry.grid(row=0, column=2, sticky=tk.W)
        self.entry.focus_set()
        self.entry.bind('<Return>', self.query_weather)

        self.help_icon = tk.PhotoImage(file='help.png')
        self.help = tk.Button(self, image=self.help_icon, command=self.help, bg=self.bg)
        idlelib.tooltip.ToolTip(self.help, '帮助')
        self.help.grid(row=0, column=3, sticky=tk.W+tk.N+tk.S+tk.E)

        self.quit_icon = tk.PhotoImage(file='quit.png')
        self.quit = tk.Button(self, image=self.quit_icon, command=self.quit, bg=self.bg)
        idlelib.tooltip.ToolTip(self.quit, '退出')
        self.quit.grid(row=0, column=4, sticky=tk.W+tk.N+tk.S+tk.E)

        self.scrolledtext = tk.scrolledtext.ScrolledText(self, font=self.font, height=10, state=tk.DISABLED)
        self.scrolledtext.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    def write_scrolledtext(self, message):
        '''This function outputs message to the scrolledtext widgets'''
        self.scrolledtext.config(state=tk.NORMAL)
        self.scrolledtext.delete(1.0, tk.END)
        self.scrolledtext.insert(tk.INSERT, message)
        self.scrolledtext.config(state=tk.DISABLED)

    def query_weather(self, event):
        '''This function displays the weather of the city'''
        city = self.entry.get()
        city = city.strip()
        self.entry.delete(0, tk.END)

        if city in self.weather_dict:
            weather = self.weather_dict[city]
            if not weather:
                self.write_scrolledtext('没有查到{0}}的天气'.format(city))
            else:
                self.write_scrolledtext('{0}: {1}'.format(city, weather))
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.weather_history[city] = [now, weather]
        else:
            self.write_scrolledtext('没有查到这个城市。')

    def print_history(self):
        '''This function prints the query history if it is not empty'''
        length = len(self.weather_history)
        history = ''
        if length != 0:
            for index, key in enumerate(self.weather_history, start=1):
                history += '{0} {1} {2} {3}\n'.format(index, key, self.weather_history[key][0], self.weather_history[key][1])
            self.write_scrolledtext(history)
        else:
            self.write_scrolledtext('您还没有查询记录。')

    def help(self):
        '''This function shows help in a info messagebox'''
        user_guide = '''
        这是一个查询城市天气的程序。
        \t* 请输入城市或者地区的中文名称
        \t\t例子1：上海
        \t\t例子2：浦东新区
        \t* 点击History，查看历史记录
        \t* 点击Quit，退出程序
        \t* 点击Help，查看帮助
        '''
        tk.messagebox.showinfo('帮助', user_guide)

    def quit(self):
        '''This function shows a quit messagebox'''
        if tk.messagebox.askyesno('退出', '确定退出程序吗?'):
            root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title('天气查询')
    app = WeatherReportGUI(root)
    app.mainloop()
