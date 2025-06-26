# pyapplications
Django project to manage multiple Job applications

Currently, jobs can only be added through the **admin** interface. The application prioritizes ease-of-use and UX over technology, complexity or correctness. Each **job** has events (also called steps), the three main events are CREATED, APPLIED and DENIED. The dashboard shows the jobs sorted from the most recent event to the oldest event (Recent events first). To show the list in its expected format, each job must have at least. There's another object in database called Wished, these are intented to grow your career. These are jobs you wish you could do or work in the future. You can add any technology or tools inside the Notes description. Theres also plans to include a collection of Job Boards into the application, so whenever you feel like searching for a job you can immediately navigate through your options.

![HomeScreen](docs/images/home.PNG)

## Overview
- **Django's app name:** `mysite`
- **Django's project name:** `pyapplications`
- **Default URL:** `localhost/mysite`
- **Default database:** SQLite3 (no need to install, it's included in Python3)

## Installation
To run application in your computer:
- Install [Python](https://www.python.org/) 
- Install Django framework with `pip install Django`
- Clone this project into your machine by using [Git](https://git-scm.com/downloads) (if you have a Mac🍏 it's already installed)
- Open a console or terminal and type in the following: `python manage.py runserver 9000`
## Usage
To view the homescren go to address: `localhost:9000/mysite`
## Managing records in database
To insert/manage records into database go to `localhost:9000/admin` or click the [Admin] button. Use the default user `admin` and password 1 through 6.
