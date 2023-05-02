# Heart rate detection with CMOS preprocessor based on neural network

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting-started)
  + [Prerequisites](#prerequisites)
+ [Installing the requirements](#installing)
+ [Running the code](#running-the-code)
+ [Todo](#todo)
+ [License](#license)

## About

Heart rate detection with neural network-based CMOS preprocessor. It involves developing a heart rate detection model using TinyML techniques on the PhysioNet dataset and parsing it on a CMOS preprocessor written in Spice.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Python libraries that you need to use this software:

+ WFDB
+ Tensorflow

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

In order to run the code, you will only need to prepare two files, multiplication coefficients grid and model file.

**prepare_dataset_pipeline.py**

```
$ python prepare_dataset.py -h
usage: prepare_dataset.py [-h] --ds-dir DS_DIR --output-file OUTPUT_FILE --sample-length SAMPLE_LENGTH --sample-freq SAMPLE_FREQ [--download]

options:
  -h, --help            show this help message and exit
  --ds-dir DS_DIR       Directory with ECG data from physionet (default: None)
  --output-file OUTPUT_FILE
                        File in which the dataset will be saved (default: None)
  --sample-length SAMPLE_LENGTH
                        The length of a sample's window (default: None)
  --sample-freq SAMPLE_FREQ
                        Number of sampled points from a window (default: None)
  --download            Whether to download database or not (default: False)
```

**parse_model.py**

Now, in order to run the code you can call the parse_model.py directly.

```
$ python parse_model.py -h
usage: parse_model.py [-h] --model MODEL --grid GRID

options:
  -h, --help     show this help message and exit
  --model MODEL  Path to file, that contains TensorFlow model (default: None)
  --grid GRID    Path to file, that contains weight grid (default: None)
```

## Authors

+ **Piotr Baryczkowski** - *ANN to CMOS preprocessor parser implementation* - [Piotr45](https://github.com/Piotr45)
+ **Sebastian Szczepaniak** - *Implementation of dataset pipeline and training ANN* - [D3nz13](https://github.com/D3nz13)

See also the list of [contributors](https://github.com/Piotr45/cmos-preprocessor/graphs/contributors) who participated in this project.

## TODO

- [ ] clean parser code

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
