# Selective Git Clone
A python script which clones a github repository's structure from root of repository or from a particular folder  

## Running the Script
Run the script with
```
python3 cloneSelective.py -u <Github_Repository_URL> [-p FolderPath] [-s]
```
* -u : Specify the URL of repository to clone from  
* -p : Specify required folder to clone and not any other folder  
* -s : Specify if files need not be downloaded and only structure is needed

### Clone a folder
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree -p FormulaTree/ 
```
### Clone a file
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree -p FormulaTree/Formula.cpp
```
### Clone full repository
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree
```
## Requirements
* Requests

## Ubuntu specific instructions
```
git clone https://github.com/vishalananth07/Selective-git-clone
pip install -r "requirements.txt"
python3 cloneSelective.py -u <Github_Repository_URL> [-p FolderPath] [-s]
```

## Constraints and Requirements:
* Script can only pull from master branch
* Folder names must end with a / while File names should not incase -p is specified
