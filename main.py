import tkinter as tk
from tkinter import scrolledtext

timer_ids = []


class DisappearingTextWritingApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Disappearing Text Writing App")
        self.geometry("600x400")

        self.user_input_string = tk.StringVar()
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        # Multiline space for user input
        self.label = tk.Label(
            master=self.main_frame,
            text="Type your text here",
            font=("Times New Roman", 25)
        )
        self.label.grid(
            column=0,
            row=0,
            pady=(10, 10),
            sticky=tk.EW
        )

        self.text_area = scrolledtext.ScrolledText(
            master=self.main_frame,
            wrap=tk.WORD,
            width=50,
            height=14,
            font=("Times New Roman", 15)
        )
        self.text_area.grid(
            column=0,
            row=1,
            pady=(10, 0),
            sticky=tk.EW
        )

    def key_release(self, e):
        timer_id = self.text_area.after(5000, self.remove_input)
        timer_ids.append(timer_id)

    def key_press(self, e):
        for i_d in timer_ids:
            self.text_area.after_cancel(i_d)
            self.after_cancel(i_d)
            self.main_frame.after_cancel(i_d)

    def remove_input(self):
        self.text_area.delete("1.0", tk.END)


if __name__ == "__main__":
    app = DisappearingTextWritingApp()
    app.mainloop()
