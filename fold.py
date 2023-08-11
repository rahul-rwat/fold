import os
import shutil
import time as extractspeed
import re 

# Folder paths
source_folders = [r"source_folders"]
                 

image_folder = r"image_folder"
label_folder = r"label_folder"

# Create the destination folders if they don't exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(label_folder, exist_ok=True)

# Counters for image and text files
image_counter = 0
text_counter = 0
 
# Iterate through the source folders
for source_folder in source_folders:
    
    # Create a list of filenames in ascending order
    filenames = sorted(os.listdir(source_folder), key=lambda x: int(re.findall(r'\d+', x)[0]) if re.findall(r'\d+', x) else float('inf'))


    
    # Iterate through the sorted list of filenames
    for filename in filenames:
        source_file = os.path.join(source_folder, filename)
        
        # Skip specific files
        if filename.lower() in ["main.txt", "classes.txt", "main"]:
            continue
        
        # Check if the file is an image
        if filename.lower().endswith(".png"):
            # Generate the new image filename
            image_counter += 1
            new_filename = f"{str(image_counter).zfill(6)}.png"
            destination_file = os.path.join(image_folder, new_filename)
            
            # Rename and move the image file
            shutil.copy(source_file, destination_file)
            print(f"Image file '{filename}' renamed to '{new_filename}' and moved to 'image' folder.")
        
        # Check if the file is a text file
        elif filename.lower().endswith(".txt"):
            # Generate the new text file filename
            text_counter += 1
            new_filename = f"{str(text_counter).zfill(6)}.txt"
            destination_file = os.path.join(label_folder, new_filename)
            
            # Rename and move the text file
            shutil.copy(source_file, destination_file)
            print(f"Text file '{filename}' renamed to '{new_filename}' and moved to 'label' folder.")
        
        
        
        
        
        #extractspeed.sleep(2)
