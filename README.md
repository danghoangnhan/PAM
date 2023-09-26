# PAM 

The PAM is a  tool designed to conduct experiments based on the Perceptual Assimilation Model (PAM). This application allows researchers and linguists to create and administer PAM experiments for the study of speech sound perception and categorization.

## Installation

### Prerequisites

- FFmpeg
- Conda (for creating and managing virtual environments)

### Setup
   ```bash
   pip install virtualenv        # if your system didn't install before

   # cd to the project directory
   virtualenv venv               # create virtualenviroment venv

   # Activate venv
   venv\Scripts\activate         # Windows
   source venv/bin/activate      # Mac and Linux

   # handle package
   pip install -r requirements.txt     # Import using package from requirements.txt
   pip freeze > requirements.txt       # Export using package to requirements.txt 
   pip list                            # list all packages install in this virtualenv

   # exit venv
   deactivate
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

## Citation

```
@misc{PAMTest,
    author={Tu-Hung Jen},
    title={PAM Test Application},
    year={2023},
    url={https://github.com/danghoangnhan/PAM},
}
```
