import tkinter as tk
from tkinter import ttk
from tkinter import font,messagebox,colorchooser,filedialog
import os

# import calculater
main_application = tk.Tk()
main_application.geometry('2880x1800')
main_application.title("Spad text editor")
main_application.wm_iconbitmap('icons//Spad.ico')


##################################### Main Manu ################################################

# File Iconss
new_icon = tk.PhotoImage(file = "icons/new.png")
open_icon = tk.PhotoImage(file = "icons/open.png")
save_icon = tk.PhotoImage(file = "icons/save.png")
save_as_icon = tk.PhotoImage(file = "icons/save_as.png")
exit_icon = tk.PhotoImage(file = "icons/exit.png")



main_menu = tk.Menu()
filee = tk.Menu(main_menu, tearoff = False)

edit = tk.Menu(main_menu, tearoff = False)
# Edit icons
copy_icon = tk.PhotoImage(file = "icons/copy.png")
paste_icon = tk.PhotoImage(file = "icons/paste.png")
cut_icon = tk.PhotoImage(file = "icons/cut.png")
clear_all_icon = tk.PhotoImage(file = "icons/clear_all.png")
find_icon = tk.PhotoImage(file = "icons/find.png")

view = tk.Menu(main_menu, tearoff = False)

tool_bar_icon = tk.PhotoImage(file = 'icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons/status_bar.png')



colour_theme = tk.Menu(main_menu, tearoff = False)

light_default_icon = tk.PhotoImage(file = 'icons/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')
monokai_icon = tk.PhotoImage(file = 'icons/monokai.png')

red_icon = tk.PhotoImage(file = 'icons/red.png')
night_blue_icon = tk.PhotoImage(file = 'icons/night_blue.png')
theme_choice = tk.StringVar()
color_icon = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2'),
}

main_menu.add_cascade(label = "File",menu = filee)
main_menu.add_cascade(label = "Edit",menu = edit)
main_menu.add_cascade(label = "View",menu = view)
main_menu.add_cascade(label = "Colour Theme",menu = colour_theme)



# ------------------------------ &&&&& End main manu &&&&& ---------------------------------------





##################################### Tool bar ################################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP,fill = tk.X)

# font_box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 30, textvariable = font_family,state = 'readonly')
font_box['values'] = font_tuple
# font_box.current(font_tuple.index('Microsoft Himalaya'))
try:
    # Set the current font to 'Microsoft Himalaya'
    font_box.current(font_tuple.index('Microsoft Himalaya'))
except ValueError:
    # If 'Microsoft Himalaya' is not in the tuple, set a default font
    default_font = 'Arial'  # Replace with your preferred default font
    if default_font in font_tuple:
        font_box.current(font_tuple.index(default_font))
    else:
        # If the default font is also not available, set the first font as default
        font_box.current(0)
        print(f"Default font '{default_font}' is not available. Using the first available font.")
font_box.grid(row = 0,column = 0,padx = 5)

# font_size_box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width = 14,textvariable = size_var,state = 'readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row = 0,column = 1,padx = 5)

# bold_btn
bold_icon = tk.PhotoImage(file = 'icons/bold.png')
bold_btn = ttk.Button(tool_bar,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)

# Italic_btn
Italic_icon = tk.PhotoImage(file = 'icons/italic.png')
italic_btn = ttk.Button(tool_bar,image = Italic_icon)
italic_btn.grid(row = 0 ,column = 3,padx = 5)

# Underline_btn
Underline_icon = tk.PhotoImage(file = 'icons/underline.png')
underline_btn = ttk.Button(tool_bar,image = Underline_icon)
underline_btn.grid(row = 0 ,column = 4,padx = 5)

# font_color_btn
font_color_icon = tk.PhotoImage(file = 'icons/font_color.png')
font_color_btn = ttk.Button(tool_bar,image = font_color_icon)
font_color_btn.grid(row = 0 ,column = 5,padx = 5)

# align_left_btn
align_left_icon = tk.PhotoImage(file = 'icons/align_left.png')
align_left_btn = ttk.Button(tool_bar,image = align_left_icon)
align_left_btn.grid(row = 0 ,column = 6,padx = 5)

# align_center_btn
align_center_icon = tk.PhotoImage(file = 'icons/align_center.png')
align_center_btn = ttk.Button(tool_bar,image = align_center_icon)
align_center_btn.grid(row = 0 ,column = 7,padx = 5)

# align_right_btn
align_right_icon = tk.PhotoImage(file = 'icons/align_right.png')
align_right_btn = ttk.Button(tool_bar,image = align_right_icon)
align_right_btn.grid(row = 0 ,column = 8,padx = 5)
# calculator button
calculator_icon = tk.PhotoImage(file='icons/calculator.png')
calculator_icon = calculator_icon.subsample(2)  # Decrease the size of the icon
calculator_btn = ttk.Button(tool_bar, image=calculator_icon)
calculator_btn.grid(row=0, column=9, padx=2, sticky=tk.E)

# todo_list button
todo_icon = tk.PhotoImage(file='icons/to-do-list.png')
todo_icon = todo_icon.subsample(16)  # Decrease the size of the icon
todo_btn = ttk.Button(tool_bar, image=todo_icon)
todo_btn.grid(row=0, column=10, padx=2, sticky=tk.E)
# ------------------------------ &&&&& Tool bar &&&&& ---------------------------------------



##################################### text editor ################################################

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word',relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

current_font_type = 'Liberation Serif'
current_font_size = '12'

def change_font(main_application):
    global current_font_type
    current_font_type = font_family.get()
    text_editor.configure(font = (current_font_type,current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_type,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)
text_editor.configure(font = ('Liberation Serif',12))

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_type,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font = (current_font_type,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

# italic button functionality
def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_type,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_type,current_font_size,'roman'))

italic_btn.configure(command = change_italic)

# underline button functionality
def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_type,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font = (current_font_type,current_font_size,'normal'))

underline_btn.configure(command = change_underline)

# font_color_chooser
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command = change_font_color)

# left_align_btn_functionality
def left_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command = left_align)

# center_align_btn_functionality
def center_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command = center_align)

# right_align_btn_functionality
def right_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command = right_align)

# calculator button functionality
def calculator():
    os.system('python calculater.py')
calculator_btn.configure(command=calculator)


# todo_list button functionality
def todo_list():
    os.system('python todo.py')

todo_btn.configure(command=todo_list)

# ------------------------------ &&&&& End text manu &&&&& ---------------------------------------




##################################### Status bar ################################################

status_bar = ttk.Label(main_application,text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

def changed(event=None):
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text = f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)

# ------------------------------ &&&&& End Status bar &&&&& ---------------------------------------




##################################### Main Manu functionality ################################################

## variable
url = ''

## new functionality
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

## file commnads
filee.add_command(label = 'New' ,image = new_icon,compound = tk.LEFT,accelerator = "Ctrl+N",command = new_file)

## open functionality

def open_file(evet=None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Select File',filetypes = (('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

filee.add_command(label = 'Open' ,image = open_icon,compound = tk.LEFT,accelerator = "Ctrl+O",command = open_file)

## save file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

filee.add_command(label = 'Save' ,image = save_icon,compound = tk.LEFT,accelerator = "Ctrl+S",command = save_file)

## save as file
def save_as(event = None):
    global url
    try:
        content2 = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content2)
        url.close()
    except:
        return

filee.add_command(label = 'Save as' ,image = save_as_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+S",command = save_as)

# exit functionality

def exit_func(event=None):
    global url, changed
    try:
        if changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

filee.add_command(label = 'Exit' ,image = exit_icon,compound = tk.LEFT,accelerator = "Ctrl+Q",command = exit_func)

############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()

    find_dialogue.geometry('350x150')
    find_dialogue.title('Find')
    find_dialogue.wm_iconbitmap("icons//find.ico")
    find_dialogue.resizable(0,0)



    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=10)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace : ')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## Edit commands
edit.add_command(label = 'Copy' ,image = copy_icon ,compound = tk.LEFT,accelerator = "Ctrl+C",command = lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label = 'Paste' ,image = paste_icon,compound = tk.LEFT,accelerator = "Ctrl+V",command = lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label = 'Cut' ,image = cut_icon,compound = tk.LEFT,accelerator = "Ctrl+X",command = lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label = 'Clear all' ,image = clear_all_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+X",command = lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label = 'Find' ,image = find_icon,compound = tk.LEFT,accelerator = "Ctrl+F",command = find_func)

## view checkbuttons

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_satausbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label = "Tool bar",onvalue = True,offvalue = 0,variable = show_toolbar,image = tool_bar_icon,compound = tk.LEFT,command = hide_toolbar)
view.add_checkbutton(label = "Status bar",onvalue = 1,offvalue = False,variable = show_statusbar,image = status_bar_icon,compound = tk.LEFT,command = hide_satausbar)

## color theme radio buttons

def color_chooser():
    choosed_color = theme_choice.get()
    color_tuple = color_dict.get(choosed_color)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,fg = fg_color)

count = 0
for i in color_dict:
    colour_theme.add_radiobutton(label = i,image = color_icon[count],variable = theme_choice,compound = tk.LEFT,command = color_chooser)
    count += 1


# ------------------------------ &&&&& End main manu functionality &&&&& ---------------------------------------


# short_cut_keys
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_func)


main_application.config(menu = main_menu)
main_application.mainloop()
