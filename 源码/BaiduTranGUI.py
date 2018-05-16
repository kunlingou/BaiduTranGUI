__author__ = 'gkl'


from tkinter import *
import hashlib
import requests
import json


class TranslateGUI:
    def __init__(self):
        # 创建窗口
        self.root = Tk()
        # 标题
        self.root.title('百度翻译')
        # 窗口大小 小写的x
        self.root.geometry("600x300")
        # 窗口位置
        self.root.geometry("+600+300")

        self.entry = Entry(self.root, width=35)
        self.result = Text(self.root)
        self.result_button1 = Button(self.root, text='英译中', command=self.find1)
        self.result_button2 = Button(self.root, text='中译英', command=self.find2)
        self.clear = Button(self.root, text='清空', command=self.clear)
        # self.find(select_num)
        # self.result = Label(self.root, text="开发者感谢名单\nfuyunbiyi\nfyby尚未出现的女朋友\nhttp://www.programup.com网站")

        # btn = Button(self.root, text='Click me', command=self.hello)
        # # 注意这个地方，不要写成hello(),如果是hello()的话，
        # # 会在mainloop中调用hello函数，
        # # 而不是单击button按钮时出发事件
        # btn.pack(expand=YES, fill=BOTH)  # 将按钮pack，充满整个窗体(只有pack的组件实例才能显示)
    def clear(self):
        for _ in range(100):
            self.result.delete(1.0)

    def find1(self):
        self.result.insert(1.0, Translate(self.entry.get(), 1).getresult() + '\n')

    def find2(self):
        self.result.insert(1.0, Translate(self.entry.get(), 2).getresult() + '\n')

    def gui_arrang(self):
        self.entry.grid(rowspan=3, row=0, column=0, sticky=N + S)
        self.result_button1.grid(row=0, column=1, sticky=N + S)
        self.result_button2.grid(row=1, column=1, sticky=N + S)
        self.clear.grid(row=2, column=1, sticky=N + E + W + S)
        self.result.grid(rowspan=3, row=0, column=2)
        # self.entry.pack(expand=YES, side='left', fill='both')
        # self.result_button1.pack(expand=YES, side='top', fill='both')
        # self.result_button2.pack(expand=YES, side='bottom', fill='both')
        # self.result.pack(expand=YES, side='right', fill='both')


class Translate:
    def __init__(self, info0, select_num):
        # select_num = int(input("请输入功能选项（1：英->中 2：中->英）： "))
        select_num = select_num
        from_info = 'en'
        to_info = 'zh'
        if select_num == 1:
            from_info = 'en'
            to_info = 'zh'
        if select_num == 2:
            from_info = 'zh'
            to_info = 'en'
        # info = input("请输入你要翻译的内容: ")
        info = info0
        # print(info)

        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

        strl = '20180415000146450' + info + '1162729917' + 'GY9U3Xe5RGxl8HfdTzTT'

        sign = hashlib.md5(strl.encode()).hexdigest()
        # print(sign)

        json_info = {
            'q': info,
            'from': from_info.encode('utf-8'),
            'to': to_info,
            'appid': '20180415000146450',
            'salt': '1162729917',
            'sign': sign
        }

        result = requests.post(url, data=json_info).content
        # print(result0.url)
        print(result)
        try:
            result = json.loads(result.decode())['trans_result']
            self.result = result[0]['dst']
            print('翻译结果： ', result)
        except Exception as e:
            if json.loads(result.decode())['error_code'] == '58000':
                self.result = json.loads(result.decode())['data']['client_ip'] + "未注册，请联系管理员！"
            print(e)

    def getresult(self):
        return self.result


def main():
    fl = TranslateGUI()
    fl.gui_arrang()
    mainloop()
    pass

if __name__ == "__main__":
    main()