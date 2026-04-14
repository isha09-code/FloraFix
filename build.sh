<<<<<<< HEAD
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r backend/requirements.txt

cd backend
python manage.py collectstatic --no-input
python manage.py migrate
=======
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r backend/requirements.txt

cd backend
python manage.py collectstatic --no-input
python manage.py migrate
>>>>>>> 35e0a5b36eb1bbb2244e40b494c2a14f57220f06
