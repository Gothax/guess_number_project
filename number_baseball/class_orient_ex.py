from tkinter import *
from random import *
from tkinter.font import *

layout = []
anwer_list = []

class MyApp:
    def __init__(self,Parent):
        Parent.geometry('700x500')
        Parent.title('객체지향이라는걸 해보자')
        #font set
        font_title = Font(family="나눔 고딕", size=20, weight='bold')
        font_menu = Font(family='나눔 고딕', size=10)
        # menu_frame set
        self.menu_frame = Frame(Parent, relief='solid', width=700, height=300)
        self.menu_frame.pack(expand=True, fill='both')
        Label(self.menu_frame, text='인공지능 숫자야구', font=font_title).pack()
        # select_frame set
        select_frame = LabelFrame(self.menu_frame, width=400, height=50, relief='groove', text='<메뉴>'
                                  , labelanchor='n', font=font_menu)
        select_frame.pack()
        # button(select_frame)
        self.cpu_btn = Button(select_frame, text='컴퓨터와 대전', command = self.cpu_click)
        self.cpu_btn.place(anchor='center', x=80, y=15)
        self.ply_btn = Button(select_frame, text='친구들과 대전', command = self.ply_click)
        self.ply_btn.place(anchor='center', x=180, y=15)
        self.set_btn = Button(select_frame, text='설정', command = self.set_click)
        self.set_btn.place(anchor='center', x=260, y=15)
        self.quit_btn = Button(select_frame, text='종료', command = lambda : quit())
        self.quit_btn.place(anchor='center', x=310, y=15)
        #play_frame
        self.play_frame = LabelFrame(Parent, text='<Score Board>', relief='groove', labelanchor='n', width=600, height=200)
        self.play_frame.place(anchor='center', x=350, y=380)
        #info, entry(terminal _t), ok_button
        self.info = Label(Parent, text='선택 대기중...');
        self.info.place(anchor='center', x=350, y=235)
        self._t = Entry(Parent, state='disabled');
        self._t.place(x=260, y=250)
        self._t.bind("<Return>", self.onPressEnter)
        self.ok_btn = Button(Parent, text='확인', command=self.onButtonClick(), state='disabled')
        self.ok_btn.place(x=410, y=246)
    def cpu_click(self):
        print("cpu_clicked 인공지능이랑 붙자!")
        # print('answer list :', answer_list)
        # print('cpu num : ', cpu_num[0])
        self.cpu_btn['state'] = 'disabled';
        self.ply_btn['state'] = 'disabled';
        self.set_btn['state'] = 'disabled'  # 버튼 비활성화
        self.ok_btn['state'] = 'active';
        self._t['state'] = 'normal'  # 입력창 활성화
        self.info['text'] = '당신의 차례 입니다. 추측한 컴퓨터의 숫자를 입력하세요'
        layout.append(Label(self.play_frame, text='<플레이어1>'));
        layout[len(layout) - 1].place(x=50, y=0)
        layout.append(Label(self.play_frame, text='<CPU>'));
        layout[len(layout) - 1].place(x=160, y=0)
        layout.append(Label(self.play_frame, text='회차'));
        layout[len(layout) - 1].place(x=10, y=20)
        layout.append(Label(self.play_frame, text='입력'));
        layout[len(layout) - 1].place(x=50, y=20)
        layout.append(Label(self.play_frame, text='결과'));
        layout[len(layout) - 1].place(x=90, y=20)
        layout.append(Label(self.play_frame, text='입력'));
        layout[len(layout) - 1].place(x=150, y=20)
        layout.append(Label(self.play_frame, text='결과'));
        layout[len(layout) - 1].place(x=190, y=20)

    def ply_click(self):
        print("ply_clicked")

    def set_click(self):
        setting = {'max':3, 'dupl':False, 'zero':False}
        self.cpu_btn['state'] = 'disabled'
        self.ply_btn['state'] = 'disabled'
        self.set_btn['state'] = 'disabled'  # 버튼 비활성화
        #layout-(LabelFrame-SetFrame)-(radiobutton,checkbutton)
        SetFrame = LabelFrame(text='설정', width=400, height=110, labelanchor='n')
        max_num = IntVar();
        dupl = IntVar();
        zero = IntVar()
        layout.append(SetFrame);
        layout[len(layout) - 1].place(anchor='center', x=350, y=150)

        layout.append(Radiobutton(SetFrame, text='3자리', value=3, variable=max_num))
        layout[len(layout) - 1].place(x=90, y=10)
        if setting['max'] == 3:
            layout[len(layout) - 1].select()
        layout.append(Radiobutton(SetFrame, text='4자리', value=4, variable=max_num))
        layout[len(layout) - 1].place(x=90, y=30)
        if setting['max'] == 4:
            layout[len(layout) - 1].select()

        layout.append(Checkbutton(SetFrame, text='중복허용', variable=dupl))
        layout[len(layout) - 1].place(x=190, y=10)
        if setting['dupl']:
            layout[len(layout) - 1].select()

        layout.append(Checkbutton(SetFrame, text='사용 가능한 숫자에 0을 포함', variable=zero))
        layout[len(layout) - 1].place(x=190, y=30)
        if setting['zero']:
            layout[len(layout) - 1].select()
        # layout.append(Button(SetFrame, text='확인', command=lambda: self.ok_set(max_num.get(), dupl.get(), zero.get())))
        layout[len(layout) - 1].place(anchor='center', x=SetFrame['width'] // 2, y=70)

    def onPressEnter(self,event):
        print("enter pressed")
        entryValue = self._t.get()
        print(entryValue)
        self._t.delete(0,END)
    def onButtonClick(self):
        print("button clicked")
        entryValue = self._t.get()
        print(entryValue)
        self._t.delete(0,END)
    # def ok_set(self):
    #     print("setting complete")



root = Tk()
MyApp(root)
root.mainloop()