from cx_Freeze import setup, Executable
import sys



# Define the list of files to include
include_files = [('static', '')]  # ('source_path', 'destination_path')
packages=['numpy','pyglet']  
includes= []

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'packages': packages,  
        'includes':includes,  
        'include_files': include_files,  # Include the static folder
    }
}

setup(
    name="QuizzApp",
    version="1.0",
    description="Your Application Description",
    executables=[Executable("main.py", base=base)],
    options=options
)
