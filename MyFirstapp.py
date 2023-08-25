import os 
import subprocess
#import requests 
from pathlib import Path
#import nbformat
# GitHub username and access token (replace with your own values)
USERNAME = "moueiden"

# Retrieve the access token from the environment variable
personal_access_token= os.getenv("GITHUB_ACCESS_TOKEN")
api_base_url = "https://api.github.com" 
# Ask the user to enter the name of the directory
directory_name = input("Enter the name of the directory where the folders will be created: ")
# Create the directory on your desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
target_directory = os.path.join(desktop_path, directory_name)
os.makedirs(target_directory, exist_ok=True)

os.makedirs(os.path.join(target_directory, "data/cleaned"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "data/raw"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "docs"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "models"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "notebooks"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "reports"), exist_ok=True)
os.makedirs(os.path.join(target_directory, "src"), exist_ok=True)

# remplir le fichier readmit
readme_path = os.path.join(target_directory, "README.md")
if not os.path.exists(readme_path):
    with open(readme_path, "w") as readme_file:
        readme_file.write("# Mon Projet d'Analyse de Données\n\nRemplissez ici la description de votre projet.")
# Créez un objet NotebookNode
notebook_content = nbformat.v4.new_notebook()

# Ajoutez une cellule de code au notebook
cell_code = nbformat.v4.new_code_cell("print('repertoire contenant tous les notebooks rédigés.')")
notebook_content.cells.append(cell_code)
main_notebook_path = os.path.join(target_directory, "notebooks/main.ipynb")
if not os.path.exists(main_notebook_path):
    with open(main_notebook_path, "w") as main_notebook_file:
        nbformat.write(notebook_content,main_notebook_file)

requirement_path = os.path.join(target_directory, "requirement.txt")
if not os.path.exists(requirement_path):
    with open(requirement_path, "w") as requirement_file:
        requirement_file.write("#  fichier contenant la liste des dépendances du projets.")

utils_path = os.path.join(target_directory, "src/utils.py")
if not os.path.exists(utils_path):
    with open(utils_path, "w") as utils_file:
        utils_file.write("#  repertoire contenant tout code python utile.")

# Faire un initial commit
subprocess.run(["git", "init"], cwd=target_directory)
subprocess.run(["git", "add", "."], cwd=target_directory)
subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=target_directory)

# Function to create a new repository on GitHub
# Create a dictionary to store the data for your new repository                                   
data = {                                                                                          
    "name": directory_name,                                                                  
    "description": "This is my new repository",                                                   
    "private": False                                                                              
}                                                                                                 
  
# Send a POST request to the API endpoint to create a new repository                              
                                                                                               
repo_url = f"https://{personal_access_token}@ghttps://github.com/moueiden/{data['name']}.git"
#repo_url = "https://" + personal_access_token + "@https://github.com/moueiden/tp_depot_branch"
subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=target_directory)

subprocess.run(["git", "push", "-u", "origin", "master"], cwd=target_directory)