import os
from PIL import Image

def gather_images(folder_path):
    image_files = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff')):
            image_files.append(os.path.join(folder_path, file))
    return image_files

def create_tiff(image_files, result_file):
    images = [Image.open(file) for file in image_files]
    if images:
        images[0].save(result_file, save_all=True, append_images=images[1:])
        return os.path.abspath(result_file)

def main():
    folder_path = input("Enter the folder with full path: ")
    result_file = "resultfile.tiff"
    image_files = gather_images(folder_path)
    tiff_path = create_tiff(image_files, result_file)
    if tiff_path:
        print("TIFF file saved as:", tiff_path)

if __name__ == "__main__":
    main()
