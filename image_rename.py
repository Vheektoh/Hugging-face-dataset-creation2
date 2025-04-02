import os

def rename_images(folder_path):
    # Get a list of all image files in the folder
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Sort images to maintain order
    images.sort()
    
    # Loop through images and rename them
    for index, image in enumerate(images, start=1):
        ext = os.path.splitext(image)[1]
        new_name = f"image_{index}{ext}"
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {image} -> {new_name}")
    
    print("Renaming complete!")

# Provide the path to your image folder
folder_path = "/Users/macbok/Downloads/Telegram Desktop"  # Change this to your actual folder path
rename_images(folder_path)

