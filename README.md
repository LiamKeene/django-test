# Django Test

## Setup
There are no external requirements other than Django

1. Pull from github
```bash
$ git clone https://github.com/LiamKeene/django-test.git .
```

2. Create database
```bash
$ ./manage.py migrate
```

3. Install fixtures
```bash
$ ./manage.py loaddata enrolment/fixtures
```

4. Start the server
```bash
$ ./manage.py runserver
```

## The Test
There are five simple exercises to complete (take a quick look at each to work out time you think you need);

1. `enrolment/models.py` - create a simple model and migration
2. `enrolment/forms.py` - create a simple form for the above model
3. `enrolment/models.py` - database queries
4. `enrolment/models.py` - general Python knowledge
5. `enrolment/static/plan_selection.js` - user interactions

You are free to use google, SO, etc.

The exercises are not intended to be difficult, which should leave you time to think about the problem and come up with an elegant solution.  There are also opportunities to demonstrate deeper knowledge in some of these problems.

Comments in your code and tests would also be highly regarded.

Please commit your changes (good communication in commit messages is also something we like to see) and push them to github on a new branch.
