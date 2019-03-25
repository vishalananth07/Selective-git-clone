from argparse import ArgumentParser
import re
import requests
import os


def getInput():
	parser = ArgumentParser()
	parser.add_argument("-u", "--url",required=True)
	parser.add_argument("-p", "--path")
	parser.add_argument("-s", "--skeleton",action='store_true')
	args = parser.parse_args()

	username = re.split(r'\/',args.url)[3]
	repo = re.split(r'\.',re.split(r'\/',args.url)[4])[0]
	path = args.path
	flag = args.skeleton
	if path == None:
		path = ""
	return (username,repo,path,flag)

def constructURL(repository_details):
	api_url = "https://api.github.com/repos/"
	api_url = api_url + repository_details[0] + "/"
	api_url = api_url + repository_details[1] + "/"
	api_url = api_url + "contents/"
	return api_url
def saveFile(url,filepath):                
	page = requests.get(url)
	open(filepath, 'wb').write(page.content)
def createStructure(cur_api_url,cur_directory_url,skeletal_flag):
	resp = requests.get(cur_api_url)
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
			createStructure(cur_api_url + i['name'] + "/",cur_directory_url + i['name'] + "/",skeletal_flag)

def main():
	repository_details = getInput()
	api_url = constructURL(repository_details)
	folder_directory = repository_details[2]
	skele_flag = repository_details[3]
	i = len(folder_directory) - 1
	while i>0:
		if folder_directory[i]=='/':
			break
		i = i - 1
	if folder_directory == "" or folder_directory[len(folder_directory)-1] == '/':
		os.system("mkdir -p "+repository_details[1] + "/" + folder_directory)
	else:
		os.system("mkdir -p "+repository_details[1] + "/" + folder_directory[0:i])
	createStructure(api_url + folder_directory , repository_details[1] + "/" + folder_directory,skele_flag)

if __name__ == "__main__":
	main()