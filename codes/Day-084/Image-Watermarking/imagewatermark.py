from tkinter import *
from tkinter import messagebox, filedialog, colorchooser
from PIL import Image, ImageFont, ImageDraw


RED = "#b71c1c"

POSITION_OPTIONS = [
    "Top-Left",
    "Top-Right",
    "Center",
    "Bottom-Left",
    "Bottom-Right"
]


class ImageWatermark(Tk):
    def __init__(self):
        super(ImageWatermark, self).__init__()
        self.title('Image Watermark')
        self.config(padx=46, pady=46)

        self.font_family = "arial"
        self.font_size = 10
        self.font_color = (255, 255, 255)
        self.select_font_color = ((0, 0, 0), '#000000')
        self.image_paths = []
        self.destination_path = "/"
        self.canvas = Canvas(width=800, height=600, highlightthickness=0)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.grid(row=8, column=0, columnspan=3)
        self.image_on_canvas = self.canvas.create_image(
            400, 300, image=self.logo_img)

        # UPLOAD IMAGES BUTTON
        self.upload_images_btn = Button(
            text="Browse", command=self.upload_images)
        self.upload_images_btn.grid(row=1, column=1, sticky="W")

        # ADD WATERMARK LABEL
        self.add_text_label = Label(text="Watermark Text: ")
        self.add_text_label.grid(row=2, column=0, sticky="E")

        # ADD WATERMARK USER INPUT
        self.add_text_input = Entry(width=40)
        self.add_text_input.insert(0, "Md.Ghulam Azad Ansari")
        self.add_text_input.grid(row=2, column=1, columnspan=2, sticky="W")

        # SELECT FONT SIZE LABEL
        self.select_font_size_label = Label(
            text="Select Watermark Font Size: ")
        self.select_font_size_label.grid(row=3, column=0, sticky="E")

        # SELECT FONT SIZE SLIDER
        self.select_font_size_slider = Scale(
            from_=10, to=72, orient=HORIZONTAL)
        self.select_font_size_slider.grid(
            row=3, column=1, columnspan=2, sticky="W")

        # SELECT FONT COLOR LABEL
        self.select_font_color_label = Label(
            text="Select Watermark Font Color: ")
        self.select_font_color_label.grid(row=4, column=0, sticky="E")

        # SELECT FONT COLOR BUTTON
        self.select_font_color_btn = Button(
            text="Choose Color", command=self.choose_color)
        self.select_font_color_btn.grid(
            row=4, column=1, columnspan=2, sticky="W")

        # SELECT WATERMARK POSITION LABEL
        self.add_position_label = Label(text="Select Position of Watermark: ")
        self.add_position_label.grid(row=5, column=0, sticky="E")

        # SELECT WATERMARK POSITION DROPDOWN
        self.position_options = StringVar(self)
        self.position_options.set(POSITION_OPTIONS[0])
        self.add_position_options = OptionMenu(
            self, self.position_options, *POSITION_OPTIONS)
        self.add_position_options.grid(
            row=5, column=1, columnspan=2, sticky="W")

        # DESTINATION FOLDER BUTTON
        self.destination_folder_btn = Button(
            text="Destination Folder", command=self.destination_folder)
        self.destination_folder_btn.grid(row=6, column=0, sticky="E")

        # DESTINATION FOLDER LABEL
        self.destination_folder_lbl = Label(text="Destination Folder")
        self.destination_folder_lbl.grid(row=6, column=1, sticky="W")

        # SAVE WATERMARK
        self.save_btn = Button(text="Save Watermark",
                               command=self.save_watermark)
        self.save_btn.grid(row=7, column=0, columnspan=3)

    def destination_folder(self):
        self.destination_path = filedialog.askdirectory(initialdir="/")
        self.destination_folder_lbl.config(
            text=self.destination_path, fg=RED)

    def upload_images(self):
        self.image_paths = filedialog.askopenfilenames(
            initialdir="/", title="Select Image File/s", filetypes=[("image", ".png"), ])
        self.images = [PhotoImage(file=image) for image in self.image_paths]

        if len(self.images) > 0:
            messagebox.showinfo(
                title="Image Watermark", message=f"{len(self.images)} images uploaded.")
            self.canvas.itemconfig(self.image_on_canvas, image=self.images[0])
        else:
            messagebox.showerror(
                title="Error", message="No images uploaded.")

    def choose_color(self):
        self.select_font_color = colorchooser.askcolor(title="Choose Color")

    def save_watermark(self):
        try:
            watermark_text = self.add_text_input.get()
            self.font_size = self.select_font_size_slider.get()
            self.font_color = self.select_font_color[1]
            position = self.position_options.get()

            # ADD WATERMARK TO THE IMAGE AND SAVE IMAGE
            if len(self.image_paths) > 0:
                for image in self.image_paths:
                    with Image.open(image) as img:
                        image_draw = ImageDraw.Draw(img)
                        font = ImageFont.truetype(
                            self.font_family, self.font_size)
                        # GET WATERMARK POSITION
                        watermark_position = self.get_watermark_position(
                            position, img, image_draw, watermark_text, font)
                        # WRITE TEXT ON IMAGE
                        image_draw.text(
                            watermark_position, watermark_text, self.font_color, font=font)

                        # SAVE FILE AS A COPY OF THE ORIGINAL FILE
                        image_name = image.split("/")[-1]
                        img.save(f"{self.destination_path}/copy-{image_name}")
                messagebox.showinfo(
                    title="Image Watermark", message="Image saved.")
            else:
                messagebox.showerror(
                    title="Error", message="Please upload images.")
        except Exception:
            messagebox.showerror(
                title="Error", message="Something happen.\nPlease try again")

    def get_watermark_position(self, position, img, image_draw, watermark_text, font):
        # SET POSITION OF THE WATERMARK TEXT
        text_width, text_height = image_draw.textsize(
            watermark_text, font)
        margin = 25
        if position == "Top-Left":
            return (margin, margin)
        elif position == "Top-Right":
            return (
                img.size[0] - (text_width + margin), margin)
        elif position == "Center":
            return (
                img.size[0] / 2 - text_width / 2, img.size[1] / 2 - text_height / 2)
        elif position == "Bottom-Left":
            return (
                25, img.size[1] - (25 + self.font_size))
        else:
            return (
                img.size[0] - (text_width + margin), img.size[1] - (text_height + margin))
