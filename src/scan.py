"""Module that contains the scan function for scanning a document from an image. Primarily uses the cv2 library for image processing.
"""

from numpy import array, ndarray
from cv2 import warpPerspective, findHomography

def arrange_clockwise_from_upper_left(points: list[list[int]]) -> list[list[int]]:
    """
    Assuming the origin [0,0] is at the upperleft corner,
    arranges list of points [x, y] in the following arrangement:
        upper left -> upper right -> lower right -> lower left

    Args:
        points (list[list[int]]): List of coordinates [x, y]
    """

    assert len(points) == 4, \
        f"Must have exactly 4 points to arrange clockwise from upper left (has  {len(points)})"

    assert all(len(point) == 2 for point in points), \
        f"Each point must have exactly 2 coordinates"

    # Assuming an origin [0,0] at upper left corner,
    # the lowest  distance from origin is upper-leftmost point, and
    # the largest distance from origin is lower-rightmost point
    distance_sorted_points = sorted(points, key=sum)
    upper_left, lower_right = distance_sorted_points[::3]

    # For remaining points, the upper-right is the point with highest value of x
    lower_left, upper_right = [point for point in sorted(points)
                               if point not in [upper_left, lower_right]]

    # Clockwise arrangement, starting at upper left point
    return [upper_left, upper_right, lower_right, lower_left]

def canonical_points(points: list[list[int]]) -> list[list[int]]:
    """Determine the canonical points of a 4-sided polygon from list of points.

    Args:
        points (list[list[int]]): Estimated corners [x, y] of the polygon.
    """

    points = arrange_clockwise_from_upper_left(points)
    upper_left, upper_right, lower_right, lower_left = points

    # Determine the minimum and maximum points in the x and y directions by averaging between two possible extremes
    left = round((upper_left[0] + lower_left[0]) // 2)
    right = round((upper_right[0] + lower_right[0]) // 2)

    top = round((upper_left[1] + upper_right[1]) // 2)
    bottom = round((lower_left[1] + lower_right[1]) // 2)

    # Setup the canonical points in clockwise arrangement, starting upper left
    canonical_points = [[left, top], [right, top],
                        [right, bottom], [left, bottom]]

    return canonical_points

def scan(source: ndarray, source_points: list[list[int]]) -> ndarray:
    """Returns the portion of a source image that is bounded by the source_points.

    Args:
        source (ndarray): Numpy matrix with three channels, representing the colored image to be scanned
        source_points (list[list[int]]): Coordinates [x, y] of the corners of the portion of the source image in the source image
    """

    target_points = canonical_points(source_points)
    
    # Apply a homography matrix to the source image
    undistort = findHomography(array(source_points), array(target_points), 0)
    target = warpPerspective(source.copy(), undistort[0], source.shape[1::-1])
    
    # Crop image to the bounding box of the document
    left, top = target_points[0]
    right, bottom = target_points[2]
    target = target[top:bottom, left:right]
     
    return target
