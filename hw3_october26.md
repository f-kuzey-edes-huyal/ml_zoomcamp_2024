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

After running ```pipenv install scikit-learn==1.5.7```, I successfully generated both the ```Pipfile``` and ```Pipfile.lock``` files. To view the contents of the Pipfile.lock file, I used the command code . in the command line, which opened the project in Visual Studio Code. The first hash for Scikit-learn in the Pipfile.lock is __"sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445"__. 



(Before that, I mistakenly used the command ```pipenv install sklearn==1.5.7```, which caused issues. It took me some time to realize the error. Even though I had a ```Pipfile.lock``` file, it did not include the hash for Scikit-learn, which led to the problem. Once I corrected the package name to scikit-learn, everything worked as expected.)

## Models
We've prepared a dictionary vectorizer and a model.

They were trained (roughly) using this code:

```
features = ['job', 'duration', 'poutcome']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = LogisticRegression().fit(X, y)
```

Note: You don't need to train the model. This code is just for your reference.

And then saved with Pickle. Download them:

DictVectorizer
LogisticRegression
With wget:

```
PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```
## Question 3
Let's use these models!

Write a script for loading these models with pickle
Score this client:
```{"job": "management", "duration": 400, "poutcome": "success"}```
What's the probability that this client will get a subscription?

- 0.359
- 0.559
- 0.759
- 0.959
If you're getting errors when unpickling the files, check their checksum:

```$ md5sum model1.bin dv.bin
3d8bb28974e55edefa000fe38fd3ed12  model1.bin
7d37616e00aa80f2152b8b0511fc2dff  dv.bin
```

## Answer 3

__I calculated the probability that the client will subscribe, and it is 0.759.__

## Question 4
Now let's serve this model as a web service

Install ```Flask``` and ```gunicorn``` (or waitress, if you're on Windows)

Write ```Flask``` code for serving the model

Now score this client using requests:
```url = "YOUR_URL"```

```client = {"job": "student", "duration": 280, "poutcome": "failure"}```

```requests.post(url, json=client).json()```

What's the probability that this client will get a subscription?
- 0.335
- 0.535
- 0.735
- 0.935
