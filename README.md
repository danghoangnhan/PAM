# QuizzApp

QuizzApp is a Python application for conducting quizzes or tests with audio questions.

## Installation

### Prerequisites

- Python 3.8 or higher
- Conda (for creating and managing virtual environments)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/danghoangnhan/QuizzApp.git
   cd QuizzApp
   ```
2. Create a Conda environment from the env.yml file:

   ```bash
   conda env create -f environment.yml
   ```
3. Activate the Conda environment:

   ```bash
   conda activate quizzapp

   ```

## Usage

To run the QuizzApp, use the following command:

```bash
python main.py
```

## Build Executable

You can build an executable for QuizzApp using cx_Freeze. Run the following command:

```bash
python setup.py build
```

This will create an executable in the build directory.
