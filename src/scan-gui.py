"""A GUI application using matplotlib for scanning images using homography.
"""

import argparse
import matplotlib.pyplot as plt
from os.path import isfile
from matplotlib.widgets import PolygonSelector
from scan import scan

def get_file_locations() -> tuple[str]:
    """
    Obtains the file location of the image to be scanned and
    and the file location where the scanned imaged will be saved via cli.

    Returns:
        tuple[str]: the input_filepath and output_filepath from cli in a tuple
    """

    parser = argparse.ArgumentParser(prog='Document Scanner GUI Application')

    parser.add_argument('--input',  default="src\input.jpg",
                        type=str, help="File location of the image to be scanned. Defaults to \"src\input.png\".")

    parser.add_argument('--output', default="src\output.png",
                        type=str, help="File location where the scanned imaged will be saved. Defaults to \"src\output.png\"")

    arguments = parser.parse_args()
    input_filepath, output_filepath = arguments.input, arguments.output

    assert isfile(input_filepath), "Invalid load filepath. Please check the file exists and try again."

    return input_filepath, output_filepath


def main(input_filepath: str, output_filepath: str):
    """Opens a matplotlib window with two subplots (left and right), one for the original image in input_filepath and one for the scanned image. The user can use the matplotlib polygon selector to select the portion of the image to be scanned. The scanned image will be displayed in the scanned image subplot. Exiting the window will save the scanned image to the output_filepath.

    Args:
        input_filepath (str): File location of the image to be scanned.
        output_filepath (str): File location where the scanned imaged will be saved
    """

    # Matplotlib settings
    figure, ax = plt.subplots(1,2, gridspec_kw = {'wspace':0, 'hspace':0})

    for a in ax:
        a.set_xticks([])
        a.set_yticks([])

    plt.tight_layout()

    # Load source image
    image = plt.imread(input_filepath)

    ax[0].imshow(image)
    ax[1].imshow(image)

    def onselect(verts):
        """Displays the scanned image in the right subplot when the user adjusts the selector or finishes making the selector.

        Args:
            verts: List of corners [.x, .y] of the polygon selected by the user.
        """
        scanned_image = scan(image, verts)
        ax[1].imshow(scanned_image)

    selector = PolygonSelector(ax[0], onselect)
    
    # Create a predefined selector in the center of the image 
    center_y, center_x = image.shape[0]//2, image.shape[1]//2
    space_x,  space_y  = max(int(0.2*center_x), 1), max(int(0.2*center_y), 1)
    
    selector.verts = [
        [center_x-space_x, center_y-space_y],
        [center_x+space_x, center_y-space_y],
        [center_x+space_x, center_y+space_y],
        [center_x-space_x, center_y+space_y],
    ]

    plt.show()

    # Save image on successful exit
    plt.imsave(output_filepath, scan(image, selector.verts))

if __name__ == '__main__':
    args = get_file_locations()
    main(*args)
