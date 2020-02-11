import pyautogui
import datetime
import time
import tkinter as tk


# TODO User set haystack location
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.ref = open('C:\\Users\\Christopher\\Documents\\ShareX\\Screenshots\\2020-02\\tray.png')
        self.ref_path = 'C:\\Users\\Christopher\\Documents\\ShareX\\Screenshots\\2020-02\\tray.png'
        self.hatches = 0
        self.state = 0

    def create_widgets(self):

        # Frame for Start/Stopping #

        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(side='top')

        self.start = tk.Button(self.controls_frame)
        self.start["text"] = "Start counter"
        self.start["command"] = self.run_egg_counter
        self.start.pack(side="left")

        self.stop = tk.Button(self.controls_frame)
        self.stop['text'] = "Stop counter"
        self.stop['command'] = self.stop_egg_counter
        self.stop.pack(side='left')

        # Frame for manually adding hatches #

        self.add_hatch_frame = tk.Frame(self)
        self.add_hatch_frame.pack(side='top')

        self.add_hatch = tk.Button(self.add_hatch_frame)
        self.add_hatch["text"] = "Add one"
        self.add_hatch["command"] = self.add_one_hatch
        self.add_hatch.pack(side="left")
        
        self.add_x_hatch_btn = tk.Button(self.add_hatch_frame)
        self.add_x_hatch_btn["text"] = "Add 10"
        self.add_x_hatch_btn["command"] = lambda arg1=10 : self.add_x_hatch(arg1)
        self.add_x_hatch_btn.pack(side="left")

        ##

        self.hatch_label = tk.Label(self)
        self.hatch_label['text'] = "Hatches: 0"
        self.hatch_label.pack(side="top")

        self.coord_frame = tk.Frame(self)
        self.coord_frame.pack(side="top")

        self.test = tk.Frame(self.coord_frame)
        self.test.pack(side="left")

        self.right = tk.Frame(self.coord_frame)
        self.right.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom", anchor='e')

        self.set_haystack_btn = tk.Button(self)
        self.set_haystack_btn['text'] = 'Set'
        self.set_haystack_btn['command'] = self.set_haystack
        self.set_haystack_btn.pack(side='bottom')

        self.cursor_location = tk.Label(self)
        self.cursor_location['text'] = "X: {0} Y: {1}".format(pyautogui.position()[0], pyautogui.position()[1])
        self.cursor_location.pack(side="bottom")

        # Frame for coordinate input #
        self.upper_left = tk.Entry(self.right)
        self.upper_left.pack(side="top")
        
        self.upper_label = tk.Label(self.test)
        self.upper_label['text'] = "Upper left (x,y): "
        self.upper_label.pack(side="top")

        self.bottom_label = tk.Label(self.test)
        self.bottom_label['text'] = "Bottom right (x,y): "
        self.bottom_label.pack(side="bottom")

        self.bottom_right = tk.Entry(self.right)
        self.bottom_right.pack(side="bottom")

    def run_egg_counter(self):
        if(self.state == 0):
            print("Starting at: " + datetime.datetime.now())
            print("Hatches: " + str(self.hatches))
            self.state = 1
            self.check_for_egg()
        else:
            print("Counter is already running!")

    def stop_egg_counter(self):
        self.state = 0
        print("Counter has stopped.")

    def check_for_egg(self):
        if (self.state == 1):

            x = time.time()
            haystack = pyautogui.screenshot(region=(700,500,400,400));
            egg = pyautogui.locate('C:\\Users\\Christopher\\Documents\\ShareX\\Screenshots\\2020-02\\tray.png', haystack, confidence=.9)
            y = time.time()
            print(y-x)

            if(egg is not None):
                self.hatches += 1
                self.hatch_label['text'] = "Hatches: {0}".format(self.hatches)
                print("Hatches: {0} Last hatch: {1}".format(self.hatches, datetime.datetime.now()))
                app.after(8000, self.check_for_egg)
            else:
                app.after(2000, self.check_for_egg)

    def update_mouse_location(self):
        if(pyautogui.position()[0] < 0 or pyautogui.position()[1] < 0):
            self.cursor_location['fg'] = 'red'
        else:
            self.cursor_location['fg'] = 'black'
        self.cursor_location['text'] = "X: {0} Y: {1}".format(pyautogui.position()[0], pyautogui.position()[1])
        app.after(150, self.update_mouse_location)

    def add_one_hatch(self):
        self.hatches += 1
        self.hatch_label['text'] = "Hatches: {0}".format(self.hatches)

    def add_x_hatch(self, x):
        self.hatches += x
        self.hatch_label['text'] = "Hatches: {0}".format(self.hatches)

    def set_haystack(self):
        x1, y1 = eval(self.upper_left['text'])
        print(x1)

root = tk.Tk()
app = Application(master=root)

app.after(200, app.update_mouse_location)
app.mainloop()