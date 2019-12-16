# cpselect
Does not exactly the same as cpselect does in MATLAB, but similiar.

## Prerequisites
You will need to have the following packages installed:
* matplotlib (tested with 3.0.1)
* Pillow (tested with 5.3.0)
* PyQt5 (tested with 5.11.3)


## Installing and import

Install the package using pip

`pip install cpselect`

and import it with

`from cpselect.cpselect import cpselect`

## Using cpselect
Just call function `cpselect`. The function takes two inputs, two strings with the path to your pictures.

`controlpointlist = cpselect("path/to/image1", "path/to/image2")`

It will return a list object, which contains a dictionary for each control point.

    [
        {
        'point_id': 1,
        'img1_x': 1060.4614978873824,
        'img1_y': 1152.554044351164,
        'img2_x': 136.567465687222,
        'img2_y': 1095.033125293419,
        }
        {
        'point_id': 2,
        'img1_x': 1681.815230178675,
        'img1_y': 727.6577421225597,
        'img2_x': 1378.2481704454449,
        'img2_y': 101.68856148684131,
        }
    ]
