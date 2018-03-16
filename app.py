from Tkinter import *
parent_widget = Tk()

group = LabelFrame(parent_widget, text="Load file:")
group.pack(side=TOP)

text_box = Entry(group)
text_box.pack(side=LEFT)

button_widget = Button(group, text="Submit")
button_widget.pack(side=LEFT)

group = LabelFrame(parent_widget, text="Action")
group.pack(side=LEFT)

button_widget = Button(group, text="List countries with most attacks")
button_widget.pack(fill=X)

button_widget = Button(group, text="Visualize countries with most attacks")
button_widget.pack(fill=X)

button_widget = Button(group, text="List countries with highest casualties")
button_widget.pack(fill=X)

button_widget = Button(group, text="List countries with events between specified dates")
button_widget.pack(fill=X)

button_widget = Button(group, text="Locate countries with events between specified dates")
button_widget.pack(fill=X)

group = LabelFrame(parent_widget, text="Visualize")
group.pack(side=LEFT)

button_widget = Button(group, text="Show word cloud")
button_widget.pack(fill=X)

button_widget = Button(group, text="Show world map")
button_widget.pack(fill=X)

group = LabelFrame(parent_widget, text="Visualize")
group.pack(side=LEFT)

mainloop()