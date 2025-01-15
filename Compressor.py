# import os
# from tkinter import Tk, Label, Button, filedialog, Canvas, Frame, messagebox
# from PIL import Image, ImageOps, ImageTk
# import time

# def compress_image(input_path, output_path, quality=85):
#     """Compress the image to reduce file size while maintaining quality."""
#     try:
#         img = Image.open(input_path)
#         img = ImageOps.exif_transpose(img)  # Handle orientation from EXIF data
#         img.save(output_path, optimize=True, quality=quality)
#         return output_path
#     except Exception as e:
#         messagebox.showerror("Error", f"Error compressing image: {e}")
#         return None

# class ImageCompressorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Compressor")
#         self.root.geometry("900x600")
#         self.root.configure(bg="#FFFF33")
#         # self.root.resizable(true, true)

#         # Sidebar
#         self.sidebar = Frame(self.root, bg="#3c4053", width=250)
#         self.sidebar.pack(fill="y", side="left")

#         self.sidebar_title = Label(
#             self.sidebar, text="Menu", bg="#3c4053", fg="white", font=("Arial", 30, "bold")
#         )
#         self.sidebar_title.pack(pady=20)

#         self.upload_button = Button(
#             self.sidebar, text="     Upload Images                ", font=("Arial", 14), bg="#FF5665", fg="white", relief="flat",
#             command=self.upload_images 
#         )
#         self.upload_button.pack(pady=10, ipadx=20, ipady=10)

#         self.save_button = Button(
#             self.sidebar, text="Compress and Save As All ", font=("Arial", 14), bg="#FF5665", fg="white", relief="flat",
#              command=self.compress_and_save_all
#         )
#         self.save_button.pack(pady=10, ipadx=20, ipady=10)

#         self.status_label = Label(
#             self.sidebar, text="", font=("Arial", 12), bg="#3c4053", fg="green"
#         )
#         self.status_label.pack(pady=20)

#         # Developer Info and Version
#         self.dev_info_label = Label(
#             self.sidebar, text="Developer: Md. Mehedi Hasan\nDaffodil International University", font=("Arial", 12), bg="#3c4053", fg="white"
#         )
#         self.dev_info_label.pack(pady=10)

#         self.version_label = Label(
#             self.sidebar, text="\n\n\n\nVersion: 1.0.0", font=("Arial", 10), bg="#3c4053", fg="white"
#         )
#         self.version_label.pack(pady=10)

#         # Clock
#         self.clock_label = Label(
#             self.sidebar, text="Look on the Time", font=("Arial", 12), bg="#3c4053", fg="white"
#         )
#         self.clock_label.pack(pady=20)
#         self.update_clock()

#         # Main area
#         self.main_area = Frame(self.root, bg="#2a2d3e")
#         self.main_area.pack(fill="both", expand=True, padx=20, pady=20)

#         self.title_label = Label(
#             self.main_area, text="Mehedi Image Compressor", font=("Arial", 24, "bold"), bg="#2a2d3e", fg="white"
#         )
#         self.title_label.pack(pady=10)

#         self.preview_area = Canvas(self.main_area, width=500, height=300, bg="#99CCFF", relief="flat")
#         self.preview_area.pack(pady=20)

#     def upload_images(self):
#         self.image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
#         if self.image_paths:
#             self.display_image(self.image_paths[0])
#             self.save_button.config(state="normal")
#             self.status_label.config(text=f"{len(self.image_paths)} images selected.")

#     def display_image(self, image_path):
#         try:
#             img = Image.open(image_path)
#             img.thumbnail((500, 300))
#             self.tk_img = ImageTk.PhotoImage(img)
#             self.preview_area.create_image(250, 150, image=self.tk_img)
#         except Exception as e:
#             messagebox.showerror("Error", f"Error displaying image: {e}")

#     def compress_and_save_all(self):
#         if not self.image_paths:
#             return

#         self.output_dir = filedialog.askdirectory(title="Select Output Directory")
#         if not self.output_dir:
#             return

#         os.makedirs(self.output_dir, exist_ok=True)
#         compressed_count = 0

#         for image_path in self.image_paths:
#             try:
#                 base_name = os.path.basename(image_path)
#                 output_path = os.path.join(self.output_dir, f"compressed_{base_name}")
#                 compress_image(image_path, output_path)
#                 compressed_count += 1
#             except Exception as e:
#                 messagebox.showerror("Error", f"Error compressing {image_path}: {e}")

#         self.status_label.config(text=f"Successfully compressed {compressed_count} images.")
#         messagebox.showinfo("Success", f"Compressed {compressed_count} images and saved to {self.output_dir}.")

#     def update_clock(self):
#         current_time = time.strftime("%H:%M:%S")
#         self.clock_label.config(text=f"Current Time: {current_time}")
#         self.root.after(1000, self.update_clock)  # Update every second

# if __name__ == "__main__":
#     root = Tk()
#     app = ImageCompressorApp(root)
#     root.mainloop()


import os
from tkinter import Tk, Label, Button, filedialog, Canvas, Frame, messagebox
from PIL import Image, ImageOps, ImageTk
import time

def compress_image(input_path, output_path, quality=85):
    """Compress the image to reduce file size while maintaining quality."""
    try:
        print(f"Compressing: {input_path} to {output_path}")  # Debug: Check paths
        img = Image.open(input_path)
        img = ImageOps.exif_transpose(img)  # Handle orientation from EXIF data
        img.save(output_path, optimize=True, quality=quality)
        return output_path
    except Exception as e:
        messagebox.showerror("ত্রুটি", f"চিত্র সংকুচিত করার সময় ত্রুটি: {e}")
        return None

class ImageCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("চিত্র সংকুচক")
        self.root.geometry("900x600")
        self.root.configure(bg="#FFFF33")

        # Sidebar
        self.sidebar = Frame(self.root, bg="#3c4053", width=250)
        self.sidebar.pack(fill="y", side="left")

        self.sidebar_title = Label(
            self.sidebar, text="মেনু", bg="#3c4053", fg="white", font=("Arial", 30, "bold")
        )
        self.sidebar_title.pack(pady=20)

        self.upload_button = Button(
            self.sidebar, text="     ইমেজ আপলোড করুন                ", font=("Arial", 14), bg="#FF5665", fg="white", relief="flat",
            command=self.upload_images 
        )
        self.upload_button.pack(pady=10, ipadx=20, ipady=10)

        self.save_button = Button(
            self.sidebar, text="ইমেজ সংরক্ষণ করুন", font=("Arial", 14), bg="#FF5665", fg="white", relief="flat",
             command=self.compress_and_save_all
        )
        self.save_button.pack(pady=10, ipadx=20, ipady=10)

        self.status_label = Label(
            self.sidebar, text="", font=("Arial", 12), bg="#3c4053", fg="green"
        )
        self.status_label.pack(pady=20)

        # Developer Info and Version
        self.dev_info_label = Label(
            self.sidebar, text="ডেভেলপার: মোঃ মেহেদী হাসান\nড্যাফোডিল ইন্টারন্যাশনাল ইউনিভার্সিটি", font=("Arial", 12), bg="#3c4053", fg="white"
        )
        self.dev_info_label.pack(pady=10)

        self.version_label = Label(
            self.sidebar, text="\n\n\n\nসংস্করণ: 1.0.0", font=("Arial", 10), bg="#3c4053", fg="white"
        )
        self.version_label.pack(pady=10)

        # Clock
        self.clock_label = Label(
            self.sidebar, text="সময় দেখুন", font=("Arial", 12), bg="#3c4053", fg="white"
        )
        self.clock_label.pack(pady=20)
        self.update_clock()

        # Main area
        self.main_area = Frame(self.root, bg="#2a2d3e")
        self.main_area.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = Label(
            self.main_area, text="বেশী ডাটা নিই অল্প ডাটা দিই ", font=("Arial", 15, "bold"), bg="#2a2d3e", fg="white"
        )
        self.title_label.pack(pady=10)

        self.preview_area = Canvas(self.main_area, width=500, height=300, bg="#99CCFF", relief="flat")
        self.preview_area.pack(pady=20)

    def upload_images(self):
        self.image_paths = filedialog.askopenfilenames(filetypes=[("চিত্র ফাইল", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.image_paths:
            self.display_image(self.image_paths[0])
            self.save_button.config(state="normal")
            self.status_label.config(text=f"{len(self.image_paths)} চিত্র নির্বাচন করা হয়েছে।")

    def display_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((500, 300))
            self.tk_img = ImageTk.PhotoImage(img)
            self.preview_area.create_image(250, 150, image=self.tk_img)
        except Exception as e:
            messagebox.showerror("ত্রুটি", f"চিত্র প্রদর্শন করার সময় ত্রুটি: {e}")

    def compress_and_save_all(self):
        if not self.image_paths:
            return

        self.output_dir = filedialog.askdirectory(title="আউটপুট ডিরেক্টরি নির্বাচন করুন")
        if not self.output_dir:
            return

        os.makedirs(self.output_dir, exist_ok=True)
        compressed_count = 0

        for image_path in self.image_paths:
            # Check if the file extension is supported
            if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                messagebox.showerror("ত্রুটি", f"{image_path} এই ফাইলটি সাপোর্টেড ইমেজ ফরম্যাট নয়।")
                continue

            try:
                base_name = os.path.basename(image_path)
                output_path = os.path.join(self.output_dir, f"compressed_{base_name}")
                compress_image(image_path, output_path)
                compressed_count += 1
            except Exception as e:
                messagebox.showerror("ত্রুটি", f"{image_path} সংকুচিত করার সময় ত্রুটি: {e}")

        self.status_label.config(text=f"সফলভাবে {compressed_count} চিত্র সংকুচিত করা হয়েছে।")
        messagebox.showinfo("সাফল্য", f"{compressed_count} চিত্র সংকুচিত এবং {self.output_dir} তে সংরক্ষণ করা হয়েছে।")

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=f"বর্তমান সময়: {current_time}")
        self.root.after(1000, self.update_clock)  # Update every second

if __name__ == "__main__":
    root = Tk()
    app = ImageCompressorApp(root)
    root.mainloop()

