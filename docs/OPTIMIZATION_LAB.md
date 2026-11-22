

# Optimization-Lab v0.1

A research and engineering project for multi-objective optimization.

## 1. Project Overview

Optimization-Lab is a Python project for learning,

implementing, testing, and evaluating multi-objective

optimization algorithms.

Current version: 0.1.0

## 2. Environment

- Windows 11

- Python 3.13

- Python virtual environment (.venv)

- Editable Python package installation

## 3. Project Structure

src/optimization\_lab/

- problems/: Optimization test problems

- algorithms/: Optimization algorithms (future work)

- evaluation/: Performance indicators (future work)

- \_\_main\_\_.py: Unified demonstration entry point

tests/

- Unit tests for Problem, ZDT1, and ZDT2

experiments/

- Experimental scripts

verify\_project.bat

- One-command Python project verification

## 4. Implemented Features

- Abstract Problem base class

- ZDT1 benchmark problem

- ZDT2 benchmark problem

- Unified evaluate(x) interface

- Python unit tests

- Python module entry point

- Automated verification script

## 5. Installation

Create a virtual environment:

&#x20;   py -3.13 -m venv .venv

Activate it in Windows CMD:

&#x20;   .venv\\Scripts\\activate

Install the project:

&#x20;   python -m pip install -e .

## 6. Run the Project

&#x20;   python -m optimization\_lab

## 7. Run Unit Tests

&#x20;   python -m unittest discover -s tests -v

## 8. Automated Verification

On Windows:

&#x20;   verify\_project.bat

The script checks:

1\. Python environment

2\. Python unit tests

3\. Optimization-Lab entry point

## 9. Mathematical Problems

ZDT1:

&#x20;   f1 = x1

&#x20;   g = 1 + 9 \* sum(x2,...,xn) / (n-1)

&#x20;   f2 = g \* (1 - sqrt(f1/g))

ZDT2:

&#x20;   f1 = x1

&#x20;   g = 1 + 9 \* sum(x2,...,xn) / (n-1)

&#x20;   f2 = g \* (1 - (f1/g)^2)

## 10. Future Work

- Integrate NSGA-II

- Implement IGD and HV indicators

- Add reproducible multi-seed experiments

- Add experiment result analysis

- Explore improved multi-objective algorithms

