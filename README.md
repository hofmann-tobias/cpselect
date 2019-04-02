_Project in Alpha status_
# phg-cpselect
Does what cpselect does in MATLAB.

## Prerequisites
You will need to have the following packages installed:
* matplotlib
* Pillow

## Installing and import

Install the package from pip test repo

`pip install -i https://test.pypi.org/simple/ phg-cpselect-adal02`  

and import it with

`from phg_cpselect.cpselect import cpselect`

## Using phg-cpselect
Just call function `cpselect`. The function takes two inputs, two strings with the path to your pictures.

`controlpointlist = cpselect("path/to/image1", "path/to/image2")`

It will return a list object, which contains a dictionary for each control point.

    [
        {
        'idp': 1,
        'img1x': 1060.4614978873824,
        'img1y': 1152.554044351164,
        'img2x': 136.567465687222,
        'img2y': 1095.033125293419,
        }
        {
        'idp': 2,
        'img1x': 1681.815230178675,
        'img1y': 727.6577421225597,
        'img2x': 1378.2481704454449,
        'img2y': 101.68856148684131,
        }
    ]
