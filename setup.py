import cx_Freeze
import logging

# Configure error logging settings
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Create a file handler for error logging
error_log_handler = logging.FileHandler('error.log')
error_log_handler.setLevel(logging.ERROR)

# Create a formatter for the log messages (customize as needed)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_log_handler.setFormatter(formatter)

# Add the error log handler to the root logger
root_logger = logging.getLogger()
root_logger.addHandler(error_log_handler)

# Define the list of files to include
include_files = [('static', 'static')]  # ('source_path', 'destination_path')

# Continue with your cx_Freeze setup script
executables = [cx_Freeze.Executable("main.py", base=None)]

options = {
    'build_exe': {
        'packages': [],  # Add your packages here
        'includes': [],  # Add your includes here
        'include_files': include_files,  # Include the static folder
    }
}

cx_Freeze.setup(
    name="QuizzApp",
    version="1.0",
    description="Your Application Description",
    executables=executables,
    options=options
)
