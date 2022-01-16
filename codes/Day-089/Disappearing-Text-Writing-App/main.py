from tkinter import *


destroy_timer = None
user_stop_writting_timer = None
time_counter = 10


def show_widget(widget):
    widget.pack(pady=(12, 0))


def hide_widget(widget):
    widget.pack_forget()


def is_visible(widget):
    try:
        widget.pack_info()
        return True
    except Exception:
        return False


def destroy_text():
    print("destroy_text")
    text.delete("1.0", "end")


def destroy_timer_start():
    print("destroy_timer_start")
    global time_counter, destroy_timer
    if time_counter == 10:
        show_widget(timer_lbl)
    timer_lbl.config(text=f"Text will be disappeare in {time_counter} seconds")
    time_counter -= 1
    if time_counter == 0:
        window.after_cancel(destroy_timer)
        destroy_text()
        hide_widget(timer_lbl)
    else:
        destroy_timer = window.after(1000, func=destroy_timer_start)


def on_key_press(event):
    print("on_key_press")
    global time_counter, user_stop_writting_timer, destroy_timer
    if time_counter < 10:
        hide_widget(timer_lbl)
    if destroy_timer:
        window.after_cancel(destroy_timer)
        time_counter = 10
    if user_stop_writting_timer:
        window.after_cancel(user_stop_writting_timer)
    user_stop_writting_timer = window.after(3000, func=destroy_timer_start)


# ---------------------------- MAIN WINDOW UI ------------------------------- #
if __name__ == "__main__":
    window = Tk()

    window.title('Disappearing Text Writing App')
    window.config(padx=26, pady=26)

    title_lbl = Label(
        window, text="Disappearing Text Writing App", fg='red',  font=('arial', 24, 'bold'))
    title_lbl.pack(pady=(0, 12))
    text = Text(window)
    text.insert(INSERT, "Type here...")
    text.pack()
    text.bind("<Key>", on_key_press)
    timer_lbl = Label(
        window, text=f"Text will be disappeare in 10 seconds", fg='red',  font=('arial', 12, 'normal'))
    window.mainloop()
