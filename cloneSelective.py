from argparse import ArgumentParser
import re
import requests
import os


def getInput():
	parser = ArgumentParser()
	parser.add_argument("-u", "--url",required=True)
	parser.add_argument("-p", "--path")
	parser.add_argument("-s", "--skeleton",action='store_true')
	parser.add_argument("-b", "--branch")
	parser.add_argument("-d", "--direct",action='store_true')
	args = parser.parse_args()

	username = re.split(r'\/',args.url)[3]
	repo = re.split(r'\.',re.split(r'\/',args.url)[4])[0]
	path = args.path
	flag = args.skeleton
	branch = args.branch
	direct = args.direct
	if path == None:
		path = ""
	if branch == None:
		branch = "master"
	return (username,repo,path,flag,branch,direct)

def constructURL(repository_details):
	api_url = "https://api.github.com/repos/"
	api_url = api_url + repository_details[0] + "/"
	api_url = api_url + repository_details[1] + "/"
	api_url = api_url + "contents/"
	return api_url
def saveFile(url,filepath):                
	page = requests.get(url)
	open(filepath, 'wb').write(page.content)
def createStructure(cur_api_url,cur_directory_url,skeletal_flag,branch):
	payload = {"ref" : branch}
	resp = requests.get(cur_api_url,params=payload)
	if resp.status_code<200 or resp.status_code>299:
		print("Error in Request")
		print(resp.url)
		quit()
	data = resp.json()

	if 'name' in data:
		os.system("touch " + cur_directory_url)
		if skeletal_flag == 0:
			saveFile(data['download_url'],cur_directory_url)
		return
	for i in data:
		if i['type'] == 'file':
			os.system("touch " + cur_directory_url + i['name'])
			if not skeletal_flag:
				saveFile(i['download_url'],cur_directory_url + i['name'])
		elif i['type'] == 'dir':
			os.system("mkdir -p " + cur_directory_url + i['name'])
			createStructure(cur_api_url + i['name'] + "/",cur_directory_url + i['name'] + "/",skeletal_flag,branch)

def main():
	repository_details = getInput()
	api_url = constructURL(repository_details)
	folder_directory = repository_details[2]
	skele_flag = repository_details[3]
	branch_name = repository_details[4]
	direct_flag = repository_details[5]
	i = len(folder_directory) - 1
	while i>0:
		if folder_directory[i]=='/':
			break
		i = i - 1
	if not direct_flag:
		if folder_directory == "" or folder_directory[len(folder_directory)-1] == '/':
			os.system("mkdir -p "+repository_details[1] + "/" + folder_directory)
		else:
			os.system("mkdir -p "+repository_details[1] + "/" + folder_directory[0:i])
		createStructure(api_url + folder_directory , repository_details[1] + "/" + folder_directory,skele_flag,branch_name)
	else:
		if folder_directory[-1] == '/':
			os.system("mkdir -p "+repository_details[1])
			createStructure(api_url + folder_directory , repository_details[1] + "/",skele_flag,branch_name)
		else:
			it = len(folder_directory) - 1
			while True:
				if folder_directory[it]=='/':
					it = it + 1
					break
				elif it == 0:
					break
				it = it - 1
			file_name = folder_directory[it:]
			os.system("mkdir -p "+repository_details[1])
			os.system("touch " + repository_details[1]+"/"+file_name)
			createStructure(api_url + folder_directory, repository_details[1] + "/" + file_name,skele_flag,branch_name)

if __name__ == "__main__":
	main()