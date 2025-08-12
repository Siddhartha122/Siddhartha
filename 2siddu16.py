import tkinter as tk

def display_text():
    entered_text = entry.get()
    label_output.config(text=entered_text)

# Create main window
root = tk.Tk()
root.title("Text Input App")
root.geometry("300x150")

# Entry widget (Text Field)
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button to display text
button = tk.Button(root, text="Display Text", command=display_text)
button.pack()

# Label to show typed text
label_output = tk.Label(root, text="", font=("Arial", 12))
label_output.pack(pady=10)

# Run the app
root.mainloop()
