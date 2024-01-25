import tkinter as tk

# Create the main window.
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

# Create input labels and entry fields for weight and height.
weight_label = tk.Label(window, text="Weight [kg]:")
weight_label.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
weight_entry = tk.Entry(window)
weight_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

height_label = tk.Label(window, text="Height [m]:")
height_label.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
height_entry = tk.Entry(window)
height_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Start the main loop.
window.mainloop()
