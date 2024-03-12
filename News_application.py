import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


def open_link(url):
    webbrowser.open(url)


class NewsApp:
    def __init__(self):
        # fetch data using requests library
        self.a = None
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&apiKey=4c13bce5e9694dfe8536d0997bd8b849').json()
        # initial GUI load
        self.load_gui()

        # load 1st news items
        self.load_news(0)

    def load_gui(self):
        self.a = Tk()
        self.a.geometry('400x600')
        self.a.resizable(0, 0)
        self.a.config(bg='#CB3E69')
        self.a.title("What's Happening")
        self.a.iconbitmap('flatworldmap_118410.ico')

    def clear(self):
        """deletes all the current widgets stored in container using pack geometry manager. pack_slave() function
        returns a list of all the child widgets in the container"""
        for i in self.a.pack_slaves():
            i.destroy()

    def load_news(self, index):
        # clear the screen for the new news item
        self.clear()

        # Image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw = urlopen(img_url).read()  # this opens the image fro the url and reads it and store it in the form of
            # binary digit
            im = Image.open(io.BytesIO(raw)).resize((400, 250))
            pic = ImageTk.PhotoImage(im)
        except:
            img_url = ('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQYAAADACAMAAADRLT0TAAAATlBMVEX///+ysrLLy8uvr6/5'
                       '+fm4uLj8/PzExMTn5+fBwcG7u7vX19f19fXj4+Pc3NyXl5fR0dGmpqbKysrr6+uSkpLv7'
                       '++enp6Li4uioqKAgIAhIPmjAAAEJUlEQVR4nO3ci3KjIBQGYBBUEFE0Mem+/4vuORhNvOylM7sl1f'
                       '+baVI1yXBOEBBshQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeGOmrMpL6kIk1ysllQqpi5FYpiRTLnVBkjJjFigPQ+qipJTLSZW6KAk1ak6D8qkLk0zxzAJJXZpkwmsaTt'
                       'tK1ovKIKVOXaA0ymUaVJa6QElcVpXhpJ2mles0lKmLlICfR05q/s2kLtSXKx4jJ2VN7adR1PnGUO5RBfKCNuqzjqH0FPh4bdlP50XiYn21x5XlNGiaN891xT2PnNa1QZ1qDGXnsPtxWy63z+Fl5GR5u6hO'
                       'OYZ6Rj32FPq5rWzqwn2Zl2mGsTF4vcg6zRiqeM45UdQ8K+1fLy/OMoZyi2mGZnfP8dXyVewxs8XFZn6KTnMZc7ystNvMHN2wmmaoVo0F56FOXcj/z65nW6i/XO06wRjKbOacis2k5AnGUKv6H0Pep'
                       'ObwnWaziVj5/Z1HVqzjjcMEt0mDzFOX9L8K24BlOWwmZw++eLNpC8eQ93YeefGm34tY7efmuGOozQJNjLd0m6FE3H/YMdReuPFb36slh1288btfOl9ob3vM6cgBVTuxjrMs+2k45jzUbssgpdWi3'
                       'k3QQVuHnUFSDDbfT8JR51/2hk6/dcwhFNIQba8j/5SGY15ul5/Lw1FvAiqC+gR53NF03YTs74TmkL0lAAAAAAAAfIYp87+eRPzlC5vxMrsp/kGBkrCt86r7w4v6Mf6i/VWYYVysuWphv+Uav2n5kd'
                       'eiCs+TaLXQvBKhRWFiyDU/6TyL0wlzGvTjoI8LuNoLN6ah1VoGfunAazeFLgwf/QZVRMbvmUJ316qTFEgp82stcttVd4pB3qqrE67tYphTGiraS4mTH/ZK331G7ywfaSjopVYUneIPcYo+y3T5/f2n'
                       'ZLppyS1QhN0gWkenQCmqnCpKR4FQ7FTTy8VJ4fkcumvNVagVA9endrwLrNWiopfaEN/d3ChH9BPefz1rToO4uNBeOBDhpeBWs+5EvJmHHuw49/5IA0cad3mX3YXjILPppIgHP0LT+B/CVdRo0lH//vf'
                       'CjCcFNQlSBt8ZwYE+0jB0ouN2gn5fpiH2LKWrb6Uz97F1DIs03PoQgosJ4jQ0758Gf+NH29cf9HRb1AZKQ891va2faYhPgW98a4eMDtZ3rv1UYxZpiOu9w3dKg8hv/lJdKYLsYlvDXd6cBsrMPRhFQY'
                       'Q2/rlAcXWkppbA5J0wV9/kdzqvcmPV3GGGmxHDvfEffTwp4onxDdIgfBVv3dClHTy17gX3g4I7T811v48NgXDjWkzo+57/wU2ouHqYKhP81pD7evyrCn6340pSVtSqDC8/AAAAAAAAAAAAAAAAAA'
                       'AAAAAAAAAAAAAAAAAAAAAAAAAAb+cnJPojNOxxqCEAAAAASUVORK5CYII=')
            raw = urlopen(img_url).read()  # this opens the image fro the url and reads it and store it in the form of
            # binary digit
            im = Image.open(io.BytesIO(raw)).resize((400, 250))
            pic = ImageTk.PhotoImage(im)

        img_lable = Label(self.a, image=pic)
        img_lable.pack()

        # Heading
        heading = Label(self.a, text=self.data['articles'][index]['title'], bg='#CB3E69', fg='#FFC300', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('Arial Bold', 15))

        # Details
        details = Label(self.a, text=self.data['articles'][index]['description'], bg='#CB3E69', fg='white',
                        wraplength=350,
                        justify='center')
        details.pack(pady=(5, 20))
        details.config(font=('verdana', 10))

        # Button creation
        frame = Frame(self.a, bg='#CB3E69')
        frame.pack(expand=True, fill=BOTH)
        if index != 0:
            pre = Button(frame, text='Prev', width=16, height=3, bg='light yellow',
                         command=lambda: self.load_news(index - 1))
            pre.pack(side=LEFT, padx=(20, 0))

        show = Button(frame, text='Show More', width=16, height=3, bg='pink',
                      command=lambda: open_link(self.data['articles'][index]['url']))
        show.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            nex = Button(frame, text='Next', width=16, height=3, bg='light green',
                         command=lambda: self.load_news(index + 1))
            nex.pack(side=LEFT)

        self.a.mainloop()


onj = NewsApp()
