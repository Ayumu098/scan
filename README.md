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

Run the Python file `scan-gui.py` with arguments `--input=FILEPATH_INPUT` and `--output=FILEPATH_OUTPUT`, where `FILEPATH_INPUT` is the file location of the image to scan and `FILEPATH_OUTPUT` is the file location where the scanned imaged will be saved. If the arguments are not used, the filepaths are both set to the current directory with names `input.png` and `output.png` respectively. Make sure to not include whitespaces in the filepaths.
```
python src/scan-gui.py --input=input.png --output=output.png
```

This opens a `matplotlib` screen. Drag the four points to the corners of the document in the image. Once the points cover the entire document, close the window. The scanned image will be saved to the output location.

Alternatively, the `scan` function in `scanner.py` can be directly used.