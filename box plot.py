import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def create_box_plot():
    np.random.seed(0)

    data1 = np.random.normal(100, 10, 100)
    data2 = np.random.normal(80, 5, 100)

    fig, ax = plt.subplots()
    box_plot_data = [data1, data2]
    box_colors = ['blue', 'green']
    box = ax.boxplot(box_plot_data, patch_artist=True, labels=['Data 1', 'Data 2'])

    for patch, color in zip(box['boxes'], box_colors):
        patch.set_facecolor(color)
    ax.set_title('Box Plot with Colors')
    ax.set_xlabel('Data')
    ax.set_ylabel('Value')

    plt.show()
    
root = tk.Tk()
root.title("Box Plot with Colors")
button = ttk.Button(root, text="Generate Box Plot", command=create_box_plot)
button.pack(padx=20, pady=10)
root.mainloop()
