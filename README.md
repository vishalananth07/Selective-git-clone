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

## Constraints and Requirements
* Script can only pull from master branch
* Folder names must end with a / while File names should not incase -p is specified
