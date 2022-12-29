# neurodata
We're doing cool stuff with data!

## Installation
Using `conda`, create a new environment with python 3.10 using the following commands from the Anaconda Powershell Prompt:
```
conda create --name neurodata
```

Export the environment to environment.yml file using:
```
conda env export > environment.yml
```
Activate the environment:
```
conda activate neurodata
```

conda env create -f environment.yml
```
Locate the environment file in the desktop. Usually, it would be in the same folder as Anaconda/Miniconda. Open the file using Notepad and edit it with the dependencies provided in `environmentnew.yml` file in our repository.
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
