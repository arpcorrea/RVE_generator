# RVE GENERATOR

## GOAL
This code aims to create a 2D Representative Volumetric Element (RVE) of circular embbeded particles within a continuous midia, ressembling a fibre-matrix composite.

## ASSUMPTIONS
This code uses a random algorithm to place fibres within a continuous domain (matrix).

## LIMITATIONS
Due to the random algorithm, the maximum volumetric fraction of the embbeded particles is limited up to the order of 45% depending on the particle (fibre) radius per RVE dimension.

## USAGE
The parameters of the RVE is found in "RandomRVE.yaml", which is located inside the "deck" folder. In this file, the user can change the RVE dimensions, the target volumetric fraction, the fibres radius and the output folder. 
Once the parameters are set, the user simply needs to run the file named "main.py". Note that, as previously mentioned, convergency can be problematic if the target volumetric fraction is sufficiently high.