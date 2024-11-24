from PIL import Image
import os

# تغییر اندازه تصویر
def resize_image(image, size):
    return image.resize(size)

# ایجاد 9 تصویر 100x100 خالی
def create_empty_images(count, size):
    return [Image.new("RGB", size) for _ in range(count)]

# فرآیند استخراج و قرار دادن پیکسل‌ها در تصاویر 100x100
def process_image(image, grid_size, small_image_size):
    width, height = image.size
    small_images = create_empty_images(grid_size[0] * grid_size[1], small_image_size)

    step = 3  # گام حرکت ماتریس 3x3

    # پیمایش 9 تصویر 100x100
    for k in range(grid_size[0] * grid_size[1]):
        small_image = small_images[k]
        pixels = small_image.load()

        # انتخاب نقطه شروع (x و y) برای هر تصویر 100x100
        start_x = (k % grid_size[0]) * small_image_size[0]
        start_y = (k // grid_size[1]) * small_image_size[1]

        small_pixel_index = 0
        for i in range(0, small_image_size[0]):
            for j in range(0, small_image_size[1]):
                # محاسبه موقعیت ماتریس 3x3 در تصویر اصلی
                x = start_x + i
                y = start_y + j

                if x < width and y < height:
                    # انتخاب پیکسل از تصویر اصلی
                    pixel = image.getpixel((x, y))
                    pixels[i, j] = pixel
                    small_pixel_index += 1

    return small_images

# ذخیره تصاویر کوچک
def save_images(small_images, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, img in enumerate(small_images):
        # مسیر ذخیره هر تصویر
        img.save(f"{output_dir}/small_image_{i + 1}.png")

def main():
    # مسیر تصویر ورودی
    input_image_path = "input.jpg"
    output_image_size = (900, 900)
    grid_size = (3, 3)  # ماتریس 3x3
    small_image_size = (100, 100)  # اندازه تصاویر کوچک
    output_dir = "output_images"  # مسیر ذخیره تصاویر

    # باز کردن تصویر و تغییر اندازه آن
    image = Image.open(input_image_path)
    resized_image = resize_image(image, output_image_size)
    
    # پردازش تصویر و ایجاد 9 تصویر کوچک
    small_images = process_image(resized_image, grid_size, small_image_size)

    # ذخیره تصاویر کوچک در فولدر
    save_images(small_images, output_dir)

    # نمایش تصویر اصلی
    resized_image.show()

    print(f"9 تا تصویر کوچک در پوشه {output_dir} ذخیره شد.")

if __name__ == "__main__":
    main()
