# File Organizer for Labeled Data

The File Organizer for Labeled Data is a Python script designed to help you organize labeled images and their corresponding text labels into separate folders. This can be particularly useful for managing datasets used in machine learning or computer vision projects.

## Features

- Organizes labeled images and text labels from a source folder into separate destination folders.
- Renames files to ensure consistent and sequential naming.
- Handles both image files (PNG format) and text files (TXT format).
- Skips specific files (e.g., "main.txt", "classes.txt", "main").

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Clone this repository to your local machine or download the ZIP file and extract it.
    
    ```bash
    git clone https://github.com/rahul-rwat/fold.git
    ```
    
2. Navigate to the project directory.
    
    ```bash
    cd fold
    
    ```
    
3. Update the `source_folders` list in the `fold.py` script to specify the source folder(s) containing your labeled data.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the script by executing the following command:
    
    ```bash
    python fold.py
    
    ```
    
6. The script will rename and move the image and text files to the appropriate destination folders (`images` and `labels`) within the specified source folder(s).

## Configuration

- `source_folders`: List of source folders containing labeled data.
- `image_folder`: Destination folder for organized image files.
- `label_folder`: Destination folder for organized text label files.

## Notes

- Make sure to have your labeled image files in PNG format and text label files in TXT format.
- Certain files like "main.txt", "classes.txt", and "main" will be skipped during the organization process.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a GitHub issue or pull request in this repository.

---
