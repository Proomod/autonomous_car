# Autonomous car

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is a simple lane follower bot realized with raspberrypi 4 

## Getting Started <a name = "getting_started"></a>

Hook up the wires to your motor connect a camera and you are good to train the model


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

OpenCV 
Tensorflowlite for running a model
opencv 

```
pip install opencv-contrib-python

```

create a tflite

### Installing

first you need to collect data using Datacollection module
```
python dataCollectionMain.py
```

train the collected data in google colab



run main program to see the result

```
python carmain.py
```
<!--  -->
<!-- And repeat -->
<!--  -->
<!-- ``` -->
<!-- until finished -->
<!-- ``` -->
![Img](../main/image1.jpg)

## Usage <a name = "usage"></a>

Add notes about how to use the system.
