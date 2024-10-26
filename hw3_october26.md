## Question 1
Install ```Pipenv```

What's the version of ```pipenv``` you installed?

Use ```--version``` to find out

## Answer 1 

I initially created a folder named hw_deployment. Then, using the Anaconda prompt, I activated the ml-zoomcamp environment by running conda activate ml-zoomcamp. After that, I navigated to my folder by using cd ```hw_deployment```. I installed pipenv in this folder by running ```pip install pipenv```, which helps create a virtual environment. To check the installed version of pipenv, I ran pipenv.__version__, which returned __'2024.2.0'__.

## Question 2
Use ```Pipenv``` to install ```Scikit-Learn``` version ```1.5.2```

What's the first hash for ```scikit-learn``` you get in ```Pipfile.lock```?

Note: you should create an empty folder for homework and do it there.

## Answer 2

After running ```pipenv install scikit-learn==1.5.7```, I successfully generated both the ```Pipfile``` and ```Pipfile.lock``` files. To view the contents of the Pipfile.lock file, I used the command code . in the command line, which opened the project in Visual Studio Code. The first hash for Scikit-learn in the Pipfile.lock is "sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445". 



(Before that, I mistakenly used the command ```pipenv install sklearn==1.5.7```, which caused issues. It took me some time to realize the error. Even though I had a ```Pipfile.lock``` file, it did not include the hash for Scikit-learn, which led to the problem. Once I corrected the package name to scikit-learn, everything worked as expected.)

