# neurodata
We're doing cool stuff with data!

## Installation
Using `conda`, create a new environment with python 3.10 using the following commands:
```
conda env create -f environment.yml
```

After this, you should simply be able to run the main Python program:
```
python main.py
```

## Creating a requirements.txt file
To create an `environment.yml` file that contains all of the packages installed in your virtual environment, run the following command:

```
conda env export > environment.yml
```

You should run this command every time you install a new package in your virtual environment.
