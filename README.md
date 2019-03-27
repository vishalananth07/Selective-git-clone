# Selective Git Clone
A python script which clones a github repository's structure from root of repository or from a particular folder  

## Running the Script
Run the script with
```
python3 cloneSelective.py -u <Github_Repository_URL> [-p Folder_Path] [-s] [-b Branch_Name] [-d]
```
* -u : Specify the URL of repository to clone from  
* -p : Specify required file/folder to selectively clone, If the option is not specified the entire repository is cloned
* -b : Specify the branch to clone, If the option is not specified the master branch is chosen
* -d : Clones only the file/folder mentioned in -p directly without creating the parent directories or other files
* -s : Clone the specified file/folder but create empty directories/files for other things in the repository for future use

### Clone a folder
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree -p FormulaTree/ -d
```
### Clone a file
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree -p FormulaTree/Formula.cpp -d
```
### Clone full repository
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree
```
### Clone a different branch
```
python3 cloneSelective.py -u https://github.com/anishbadhri/Formula_Tree -b alternate -d
```
## Requirements
* Requests

## Ubuntu specific instructions
```
git clone https://github.com/vishalananth07/Selective-git-clone
pip install -r "requirements.txt"
python3 cloneSelective.py -u <Github_Repository_URL> [-p FolderPath] [-s] [-b]
```