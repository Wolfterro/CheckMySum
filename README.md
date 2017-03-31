# CheckMySum
## A simple checksum viewer made in Python!

### Description:

###### This is a simple program made in Python that's capable of computing some of the most common hash algorithms available for the Python's 'hashlib' library.

###### The program will require you to choose an algorithm (md5, sha1, sha224, sha256, sha384, sha512) and the files that you'll want to check. Here are the possible options:

    Usage: CheckMySum.exe [-a/--algorithm] ALGORITHM [-f/--files] FILES ... [-u/--upper] [-g/--generate GENERATE]
    -------------------------------------------------------------------------------------------------------------

    '-h', '--help'          Show the help message and exit
    '-v', '--version'       Show the programs version and exit
    
    '-a', '--algorithm'     Defines the hash algorithm to be used
    '-f', '--files'         Select the files to be checked
    '-u', '--upper'         Display the hash value in uppercase letters
    '-g', '--generate'      Generate a checksum file for the files checked

###### You can generate a hash file with the results computed by the program, just use the '-g' or '--generate' option and input a filename for the hash file to be created.

###### You can display the hash in uppercase letters by using the '-u' or '--upper' option. By default the hash will be displayed in downcase letters.

###### I've made this program to be used on Windows but it can run just fine on other operating systems (like GNU/Linux, BSD and OSX), as long as you have Python 2. 

## [Check the CHANGELOG.txt for more informations!](https://raw.github.com/Wolfterro/CheckMySum/master/CHANGELOG.txt)

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

    python2 src/Main.py [-a/--algorithm] ALGORITHM [-f/--files] FILES ... [-u/--upper] [-g/--generate GENERATE]

### Download:

##### **PS**: Binary files doesn't require Python to be installed!
#### ***Binary (Windows):*** https://github.com/Wolfterro/CheckMySum/releases/tag/v1.0.1-Windows
#### ***Source code:*** https://github.com/Wolfterro/CheckMySum/archive/master.zip
