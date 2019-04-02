# phg-cpselect
Does what cpselect does in MATLAB.

## Prerequisites
You will need to have the following packages installed:
* matplotlib

## Installing and import
Download phg-cpselect package and import it with

`import phg-cpselect` 

or 

`from phg-cpselect import cpselect`

## Using phg-cpselect
Just call function `cpselect`. The function takes two inputs, two strings with the path to your pictures.

`controlpointlist = cpselect("path/to/image1", "path/to/image2")`

It will return a list object, with a tuple per control point.

`[`  
`(1, 1078.7366076606556, 1166.260376681119, 120.61927314904301, 1090.4764988539393),`  
`(2, 1672.6776752920384, 1390.1304714037171, 1378.2481704454449, 1085.9198724144596),`  
`(3, 1672.6776752920384, 732.2265195658779, 1385.0831101046642, 103.96687470658117),`  
`(4, 1042.186388114109, 599.7319737096464, 116.0626467095633, 103.96687470658117)`  
]`
`
