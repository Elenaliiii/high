import cv2
import tkinter as tk
from tkinter import filedialog

# تابع برای اعمال الگوریتم افزایش کیفیت و ریز کردن تصویر
def enhance_and_resize(input_image_path, output_image_path, scale_factor):
    # خواندن تصویر از مسیر ورودی
    input_image = cv2.imread(input_image_path)

    # اعمال الگوریتم افزایش کیفیت (بیلاترال فیلتر به عنوان نمونه)
    enhanced_image = cv2.bilateralFilter(input_image, 9, 75, 75)

    # تغییر اندازه تصویر به اندازه مورد نظر با توجه به ضریب اندازه‌گیری
    resized_image = cv2.resize(enhanced_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # ذخیره تصویر ریز شده
    cv2.imwrite(output_image_path, resized_image)
    print("تصویر با کیفیت بالا و اندازه کوچکتر ذخیره شد.")

# تابع برای انتخاب تصویر و اجرای الگوریتم
def select_image_and_process():
    file_path = filedialog.askopenfilename()
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        scale_factor = float(input("لطفاً ضریب اندازه‌گیری را وارد کنید (بزرگتر از 1 برای بزرگ‌تر کردن و کمتر از 1 برای کوچک‌تر کردن): "))
        enhance_and_resize(file_path, output_path, scale_factor)

# ایجاد پنجره
root = tk.Tk()
root.title("انتخاب تصویر، افزایش کیفیت و تغییر اندازه")

# ایجاد دکمه انتخاب تصویر و اجرای الگوریتم
select_button = tk.Button(root, text="انتخاب تصویر و اجرای الگوریتم", command=select_image_and_process)
select_button.pack(pady=20)

# شروع پنجره
root.mainloop()
