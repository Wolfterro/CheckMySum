# CheckMySum
## A simple checksum viewer made in Python!

### Description:

###### This is a simple program made in Python that's capable of computing some of the most common hash algorithms available for the Python's 'hashlib' library.

###### The program will require you to choose an algorithm (md5, sha1, sha224, sha256, sha384, sha512) and the files that you'll want to check. Here are the possible options:

    Usage: ./CheckMySum.exe [-a/--algorithm] ALGORITHM [-f/--files] FILES ...
    -------------------------------------------------------------------------

    '-h', '--help'        Show the help message and exit
    
    '-a', '--algorithm'   Defines the hash algorithm to be used
    '-f', '--files'       Select the files to be checked
    '-v', '--version'     Show the programs version and exit

###### I've made this program to be used on Windows but it can run just fine on other operating systems (like GNU/Linux, BSD and OSX), as long as you have Python 2. 

### Requirements:

#### Compiling:
- Python 2.7
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows only)

##### To compile the program on Windows, just execute the file 'build.bat'.
##### To compile the program on Linux, just execute the file 'build.sh'.
##### **PS**: PyInstaller must be recognized as an internal command on Windows CMD or in the shell if you're using GNU/Linux or other UNIX-like operating system. 

#### Executing directly:

##### You can execute the program directly if you don't want to compile it or in case you don't have PyInstaller:

    python src/Main.py [-a/--algorithm] ALGORITHM [-f/--files] FILES ...

### Download:

##### **PS**: Binary files doesn't require Python to be installed!
#### ***Binary (Windows):*** https://github.com/Wolfterro/CheckMySum/releases/tag/v1.0.0-Windows
#### ***Código-fonte:*** https://github.com/Wolfterro/CheckMySum/archive/master.zip
