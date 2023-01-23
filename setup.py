from cx_Freeze import setup, Executable
import sys

# Include the name of all folder or files in your project folder that are nessesary for the project excluding your main flask file.
# If there are multiple files, you can add them into a folder and then specify the folder name.


exe = Executable("main.py", icon=r"C:\Users\Debjeet's PC\Desktop\web_scraper\static\assests\favicon.ico") # <-- HERE


includefiles = [ 'templates', 'static', 'util.py']
includes = [ 'jinja2' , 'jinja2.ext']
excludes = ['Tkinter']

setup(
 name='Unsplash Scrapper',
 version = '0.1',
 description = 'Sample Flask App',
 options = {'build_exe':   {'excludes':excludes,'include_files':includefiles, 'includes':includes}},
 executables = [exe]
)