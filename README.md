# __SuperLeet CTF__ site made with _Django_

## Installation

1. Clone the repo: `https://github.com/Ayush21298/SuperLeet-CTF.git`
2. `cd` to the _Django_ project directory: `cd SuperLeet-CTF/webapp-django/`
3. Install _requirements_: `pip3 install -r requirements.txt`
4. Run the server: `python3 manage.py runserver`


# Project Description

There are 3 [`apps`](https://docs.djangoproject.com/en/1.11/ref/applications/) in this _Django_ `project`.
- _`questionnaire`_: This app will handle the part of the contest consisting of questions (normal or MCQ-type).
- _`jeopardyctf`_: This app will handle the _jeopardy style CTF_ contests.
- _`accounts`_: This app concerns with user profiles.
- _`allauth`_: This is the app we're using for authentication, with social logins.

We're using [_`django-allauth`_](https://www.intenct.nl/projects/django-allauth/) for authentication. _GitHub_, _Google_, and _Facebook_ has been added as '_social login_' providers.
To explore it, visit the routes:
- `http://127.0.0.1:8000/accounts/signup/`
- `http://127.0.0.1:8000/accounts/login/`
- `http://127.0.0.1:8000/accounts/logout/`

### _`addquestions`_ command

There is an `addquestions` command, which adds question from an input `JSON` file to the _database_. This will hopefully make adding new questions a robust process.

Below is an example run of the `addquestions` command.
```
λ python manage.py addquestions
Successfully added questions to DB from 'questionnaire/questions/questions.json'
```

By default is assumes the input `JSON` file is `questionnaire/questions/questions.json`.

## Milestones

- [x] Add `django-allauth` to project.
- [x] Add _social logins_ to the project.
- [x] Create core functionalities for the `questionnaire` app.
- [x] Create scoring system for `questionnaire`.
- [x] Complete `questionnaire` by making `routes`, `views` and `templates`.
- [x] Make `models` and basic backbone for _jeopardy-style challenges_.
- [ ] Add time based contests system.
- [ ] Make Challenge and Quizzes inaccessible out of challenge during ongoing time
- [ ] Checking mechanism for contests
- [ ] Score saving for User and Contest
- [ ] Leaderboard
