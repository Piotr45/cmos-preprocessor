# Heart rate detection with CMOS preprocessor based on neural network

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting-started)
  + [Prerequisites](#prerequisites)
+ [Installing the requirements](#installing)
+ [Running the code](#running-the-code)
+ [License](#license)

## About

Heart rate detection with neural network-based CMOS preprocessor. It involves developing a heart rate detection model using TinyML techniques on the PhysioNet dataset and parsing it on a CMOS preprocessor written in Spice.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Python libraries that you need to use this software:

+ WFDB
+ Tensorflow
+ PyTorch

CMOS simulation tools, that are required:

+ Eldo
+ EZwave

### Installing

A step by step series of examples that tell you how to get a development env running.
All the installation steps are being handled by the [requirements](requirements.txt). You can use venv by typing:

```
$ python -m venv venv
```

Activate venv and install requierments.

```
$ pip install -r requirements.txt
``` 

## Running the code

TODO

## Authors

+ **Piotr Baryczkowski** - *ANN to CMOS preprocessor parser implementation* - [Piotr45](https://github.com/Piotr45)
+ **Sebastian Szczepaniak** - *Implementation of dataset pipeline and training ANN* - [D3nz13](https://github.com/D3nz13)

See also the list of [contributors](https://github.com/Piotr45/cmos-preprocessor/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
