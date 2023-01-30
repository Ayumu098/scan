# Document Scanner

## Description

This is a simple document scanner built in `Python 3.11`. The user selects the four corners of a document in a distorted image and applies perspective transformation to output a top-down perspective of the document. 

## Prerequisites

Clone the GitHub repository using git
```
git clone https://github.com/Ayumu098/scan.git
```

Enter the project folder
```
cd scan
```

Install the Python dependencies in `requirements.txt`
```
pip install -r requirements.txt
```

## Usage

Run the Python file `scan-gui.py` with arguments `--input=FILEPATH_INPUT` and `--output=FILEPATH_OUTPUT`, where `FILEPATH_INPUT` is the file location of the image to scan and `FILEPATH_OUTPUT` is the file location where the scanned imaged will be saved. If the arguments are not used, the filepaths are both set to the src directory with names `input.png` and `output.png` respectively. Make sure to not include whitespaces in the filepaths.
```
python src/scan-gui.py --input=src\input.png --output=src\output.png
```

This opens a `matplotlib` screen with two subplots. The left plot is for the original image and the right plot is a preview of the scanned image. Using the polygon selector, select the four corners of the document in the left plot. Make sure that the first point and the last are connected to form a 4-sided polygon; Else, the program will fail to run. Once the polygon is formed, the right plot will show the scanned image after some delay. Adjust the four points accordingly. If the scanned image is satisfactory, close the window. The scanned image will be saved to the provided output location.

Alternatively, the `scan` function in `scanner.py` can be directly used.