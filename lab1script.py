# Question 1: What is your GitHub URL?
# Answer: https://github.com/maraf-dev
# Question 2: What version is the requests library installed on the system? Is there none at all? Or is it already installed?
# Answer: version 2.25.1
# Question 3: Is requests installed? If so, what version is the requests library installed in the virtualenv?
# Answer: version 2.27.1
# Question 4: What is the difference between the virtual environment and the not virtual environment python?
# Answer: The virtual environment is a copy of the python environment that is isolated from the system python environment. This allows for the installation of packages without affecting the system python environment. This is useful for when you want to install packages for a specific project without affecting the system python environment.




from pip._vendor import requests
print("Version of Requests Library:  " + requests.__version__)
