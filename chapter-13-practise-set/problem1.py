# create two virtual envs . install some packages in first one. How will you create similar configuration in second one

# pip install virtual env
# virtualenv env1
# virtualenv env2
# .\env1\Scripts\activate.bat
# pip install pandas==1.5.2
# pip freeze > requirements.txt
# deactivate
# .\env2\Scripts\activate.bat
# pip install -r .\requirements.txt