import tkinter as tk
import subprocess
import os
from tkinter import Label, Frame, Scrollbar, Canvas, Button, filedialog
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2
from operations import *

class ImageProcessingApp(tk.Tk):
    operations_info = [
        ("Convert to Grayscale", "Converts image to grayscale. This is commonly achieved using Python libraries like OpenCV or PIL (Python Imaging Library).", convert_to_grayscale),
        ("Detect Edges", "Detects edges in the image using algorithms Canny. Python such as OpenCV provide functions for edge detection.", detect_edges),
        ("Enhance Image", "Enhances the contrast of the image using techniques like histogram equalization or contrast stretching. Python libraries like OpenCV or scikit-image offer functions for image enhancement.", enhance_image),
        ("Smooth Image", "Applies a filter to the image, commonly achieved using Python libraries like OpenCV, Pillow (PIL), or scikit-image.", smooth_image),
        ("Adjust Contrast", "Adjusts the contrast of the image. This operation can be performed using Python libraries like OpenCV or scikit-image.", adjust_contrast),
        ("Denoise Image", "Reduces noise in the image. Algorithms such as Gaussian blur or median filtering are commonly used, and Python libraries like OpenCV provide functions for denoising.", denoise_image),
        ("Deblur Image", "Deblurs the image using Gaussian blur. Python libraries like OpenCV provide functions for image deblurring.", deblur_image),
        ("Contrast Stretching", "Enhances the contrast of the image using contrast stretching. Libraries like OpenCV or scikit-image offer functions for contrast stretching.", contrast_stretching),
        ("Histogram Equalization", "Enhances the contrast of the image using histogram equalization. Libraries like OpenCV or scikit-image offer functions for histogram equalization.", histogram_equalization),
        ("Sharpen Image", "Applies a sharpening filter to the image to enhance the edges. Python libraries like OpenCV, Pillow (PIL), or scikit-image provide functions for image sharpening.", sharpen_image),
        ("Deblur Image Enhanced", "Deblurs the image using a combination of Gaussian blur and image blending. Python libraries like OpenCV provide functions for image deblurring and blending.", deblur_image_enhanced),
        ("Sharpen Image Enhanced", "Enhances the sharpness of the image using a more aggressive sharpening filter. Python libraries like OpenCV, Pillow (PIL), or scikit-image provide functions for image sharpening.", sharpen_image_enhanced)
    ]

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Pixel Harbour")
        self.geometry("600x400")
        self.configure(bg='#f0f0f0')

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (InitialScreen, ImageProcessingPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(InitialScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class InitialScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#f0f0f0')

        label = tk.Label(self, text="Welcome to Pixel Harbour", font=("Bell MT", 32, "bold"), bg='#f0f0f0')
        label.pack(pady=10)
        label.place(relx=0.5, rely=0.4, anchor="center")

        button = tk.Button(self, text="Let's Go", font=("Cambria", 18,), command=lambda: controller.show_frame(ImageProcessingPage), padx=1, pady=1)
        button.pack(pady=10)
        button.place(relx=0.5, rely=0.6, anchor="center")

class ImageProcessingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#f0f0f0')

        label = tk.Label(self, text="List of Image Operations\n", bg='#f0f0f0', font=('Bell MT', 20, 'bold'))
        label.pack(pady=10)

        frame = Frame(self, bg='#f0f0f0')
        frame.pack(fill='both', expand=True)

        canvas = Canvas(frame, bg='#f0f0f0')
        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        operation_frame = Frame(canvas, bg='#f0f0f0')
        operation_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=operation_frame, anchor="nw")

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def on_touchscroll(event):
            if event.num == 5 or event.delta == -120:
                canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                canvas.yview_scroll(-1, "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)
        canvas.bind_all("<Button-4>", on_touchscroll)
        canvas.bind_all("<Button-5>", on_touchscroll)

        for index, (operation, description, func) in enumerate(controller.operations_info, start=1):
            operation_label = Label(operation_frame, text=f"{index}. {operation}", font=('Bell MT', 12, 'bold'), bg='#f0f0f0')
            operation_label.grid(row=index, column=0, pady=5, padx=10, sticky="w")

            def perform_operation(op=func):
                file_path = filedialog.askopenfilename()
                if file_path:
                    image = op(file_path)
                    save_path = filedialog.asksaveasfilename(defaultextension=".png")
                    if save_path:
                        image.save(save_path)

            button = tk.Button(operation_frame, text="Perform Operation", command=perform_operation)
            button.grid(row=index, column=1, pady=5, padx=10, sticky="e")

            info_label = Label(operation_frame, text=description, font=('Cambria', 10), bg='#f0f0f0', wraplength=500, justify='left')
            info_label.grid(row=index, column=2, pady=3, padx=30, sticky="w")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    app = ImageProcessingApp()
    app.mainloop()
