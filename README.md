# Sazim FastAPI Assessment Template

[Here](https://github.com/SazimAssessments/sazim-fastapi-assessment-starter) is a starter repository to fork off of. You are open to using it and you are also welcome to change some minor packages (like forms and schema validation) if you are more familiar with other packages

## **Installation**

Ensure you have python version **3.10+** installed in your system. Then run the following commands:

```
python -m venv .venv
```
it will create a virtual environment named **.venv**. You can use any name of your choice.

```
pip install -r requirements.txt
```
this command will install all the packages mentioned in the **requirements.txt** file.

## **Run The Server**

Open up the terminal and run the command:

```
fastapi dev main.py
```

To execute the tests, type the command:

```
pytest
```

## **NOTE**

If you install any new packages, please update the **requirements.txt** file by typing this command:

```
pip freeze > requirements.txt
```



