# README

This repository contains programs made for the course Introduction to Modeling at CIC, IPN, Mexico.

The languages used are c++ and python.
For the C++ programs, SDL2 library was used.


## Installation of SDL2
`` sudo apt-get update
sudo apt-get install libsdl2-dev
sudo apt-get install libsdl2-image-dev ``

## To compile c++ code
`` g++ <myCode.cpp> -w -lSDL2 -o <myProgram> ``


The folder `analysis_and_design_algorithms` contains the final project of that course.
The project consisted of implement three operations over large graphs (downloaded from [here] (http://networkrepository.com/TWITTER-Real-Graph-Partial.php) and [here] (http://networkrepository.com/inf-roadNet-PA.php)).
The operations were:

* Display the k-hop neighborhood of a given node u.
* Find and display a path of length k, that has node u as one of the endpoints.
* Display a subgraph containing an independent set of size k that includes node u. Display the nodes in the independent set with a different color.

There are c++ files and python files.
The c++ files are meant to read and apply the search algorithms.
On the other hand, the display was made using the python scripts through pandas and networkx.

The folder `disertation` contains the programs for the MSc disertation.
