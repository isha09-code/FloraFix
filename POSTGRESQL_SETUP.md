<<<<<<< HEAD
# PostgreSQL Database Setup on Render - Complete Guide

## Step-by-Step Instructions

### Step 1: Go to Render Dashboard
1. Visit https://render.com and log in to your account
2. You should see the main dashboard with your services

### Step 2: Create PostgreSQL Database Service
1. Click the **"New +"** button in the top-right corner
2. Select **"PostgreSQL"** from the dropdown menu

### Step 3: Configure Your Database

Fill in the following details:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | `florafix-db` | Use a descriptive name |
| **Database** | `florafix_db` | Auto-filled or customize |
| **User** | `postgres` | Default or create custom |
| **Region** | *Same as your Web Service* | Must match for better performance |
| **PostgreSQL Version** | 15 or 16 | Recommended: 15+ |
| **Plan** | Free | Free tier available |

### Step 4: Review & Create
- Review all settings
- Click **"Create Database"**
- Render will initialize and deploy the database (takes 2-3 minutes)

### Step 5: Get Connection Details
Once deployed, you'll see your database dashboard with connection info:

**Connection Details you'll need:**
```
External Database URL: postgresql://user:password@host:5432/database_name
Database Host: xyz.c.db.onrender.com
Database Port: 5432
Database Name: florafix_db
Username: postgres
Password: [shown in dashboard]
```

### Step 6: Add to Web Service Environment Variables

Go back to your **Web Service** and add these environment variables:

```
DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
ALLOWED_HOSTS=your-service-name.onrender.com
USE_POSTGRESQL=True
DB_NAME=florafix_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=xyz.c.db.onrender.com
DB_PORT=5432
```

**Or use the Internal Database URL:**
```
DATABASE_URL=postgresql://user:password@host:5432/database_name
```

### Step 7: Update Settings.py (Already Done ✅)

Your `settings.py` already has the logic to read these environment variables:

```python
if config('USE_POSTGRESQL', default=False, cast=bool):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }
```

### Step 8: Run Migrations

After connecting, run migrations:

**Option A: Via Render Shell**
1. Go to Web Service dashboard
2. Click "Shell" tab
3. Run:
```bash
cd backend
python manage.py migrate
```

**Option B: Add to Build Command**
Update your build command in `render.yaml`:
```yaml
buildCommand: "cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput"
```

### Step 9: Verify Connection

In Render shell, test the connection:
```bash
cd backend
python manage.py dbshell
```

Should show PostgreSQL prompt:
```
florafix_db=>
```

Type `\q` to exit.

---

## Rendering.yaml Configuration Example

```yaml
services:
  - type: web
    name: florafix
    runtime: python
    buildCommand: "cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput"
    startCommand: "gunicorn -w 4 -b 0.0.0.0:8000 backend.kisan_chikitsa.wsgi:application"
    envVars:
      - key: DEBUG
        value: false
      - key: SECRET_KEY
        sync: false
      - key: USE_POSTGRESQL
        value: true
      - key: DB_HOST
        fromService:
          name: florafix-db
          property: host
      - key: DB_NAME
        fromService:
          name: florafix-db
          property: database
      - key: DB_USER
        fromService:
          name: florafix-db
          property: user
      - key: DB_PASSWORD
        fromService:
          name: florafix-db
          property: password
  
  - type: pserv
    name: florafix-db
    plan: free
    ipAllowList: []
```

---

## Free Tier Limitations

| Feature | Free Tier | Pro Tier |
|---------|-----------|---------|
| Storage | 1 GB | Unlimited |
| CPU | Shared | Dedicated |
| Backup | 7 days | 30 days |
| Connection Pooling | Limited | Yes |
| High Availability | No | Yes |
| Idle Shutdown | Yes (after 15 min) | No |

**Note:** Free tier PostgreSQL instances are spun down after 15 minutes of inactivity. Your web service will wake it up on first request.

---

## Troubleshooting

### Connection Refused
- ✅ Check database is running (should say "Available" in dashboard)
- ✅ Verify IP allowlist (empty = allow all)
- ✅ Check credentials in environment variables

### Migrations Failed
- ✅ Run `python manage.py migrate` in shell
- ✅ Check logs in Render dashboard
- ✅ Ensure psycopg2-binary is in requirements.txt

### Static Files Not Working
- ✅ Run `python manage.py collectstatic --noinput`
- ✅ Check WhiteNoise middleware is installed
- ✅ Verify STATIC_ROOT and STATICFILES_DIRS

### Database Won't Connect
```bash
# Test connection in shell
python -c "import psycopg2; psycopg2.connect('postgresql://user:pwd@host:5432/db')"
```

---

## Next Steps

1. ✅ Create PostgreSQL database on Render
2. ✅ Copy connection credentials
3. ✅ Add to environment variables
4. ✅ Deploy web service
5. ✅ Run migrations
6. ✅ Test the application
7. ✅ Monitor logs for errors

Once everything is working, your FloraFix app will be live and storing data in PostgreSQL!

---

## Quick Reference Links

- Render Dashboard: https://dashboard.render.com
- Render PostgreSQL Docs: https://render.com/docs/databases
- Django PostgreSQL Setup: https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes
=======
# PostgreSQL Database Setup on Render - Complete Guide

## Step-by-Step Instructions

### Step 1: Go to Render Dashboard
1. Visit https://render.com and log in to your account
2. You should see the main dashboard with your services

### Step 2: Create PostgreSQL Database Service
1. Click the **"New +"** button in the top-right corner
2. Select **"PostgreSQL"** from the dropdown menu

### Step 3: Configure Your Database

Fill in the following details:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | `florafix-db` | Use a descriptive name |
| **Database** | `florafix_db` | Auto-filled or customize |
| **User** | `postgres` | Default or create custom |
| **Region** | *Same as your Web Service* | Must match for better performance |
| **PostgreSQL Version** | 15 or 16 | Recommended: 15+ |
| **Plan** | Free | Free tier available |

### Step 4: Review & Create
- Review all settings
- Click **"Create Database"**
- Render will initialize and deploy the database (takes 2-3 minutes)

### Step 5: Get Connection Details
Once deployed, you'll see your database dashboard with connection info:

**Connection Details you'll need:**
```
External Database URL: postgresql://user:password@host:5432/database_name
Database Host: xyz.c.db.onrender.com
Database Port: 5432
Database Name: florafix_db
Username: postgres
Password: [shown in dashboard]
```

### Step 6: Add to Web Service Environment Variables

Go back to your **Web Service** and add these environment variables:

```
DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
ALLOWED_HOSTS=your-service-name.onrender.com
USE_POSTGRESQL=True
DB_NAME=florafix_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=xyz.c.db.onrender.com
DB_PORT=5432
```

**Or use the Internal Database URL:**
```
DATABASE_URL=postgresql://user:password@host:5432/database_name
```

### Step 7: Update Settings.py (Already Done ✅)

Your `settings.py` already has the logic to read these environment variables:

```python
if config('USE_POSTGRESQL', default=False, cast=bool):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }
```

### Step 8: Run Migrations

After connecting, run migrations:

**Option A: Via Render Shell**
1. Go to Web Service dashboard
2. Click "Shell" tab
3. Run:
```bash
cd backend
python manage.py migrate
```

**Option B: Add to Build Command**
Update your build command in `render.yaml`:
```yaml
buildCommand: "cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput"
```

### Step 9: Verify Connection

In Render shell, test the connection:
```bash
cd backend
python manage.py dbshell
```

Should show PostgreSQL prompt:
```
florafix_db=>
```

Type `\q` to exit.

---

## Rendering.yaml Configuration Example

```yaml
services:
  - type: web
    name: florafix
    runtime: python
    buildCommand: "cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput"
    startCommand: "gunicorn -w 4 -b 0.0.0.0:8000 backend.kisan_chikitsa.wsgi:application"
    envVars:
      - key: DEBUG
        value: false
      - key: SECRET_KEY
        sync: false
      - key: USE_POSTGRESQL
        value: true
      - key: DB_HOST
        fromService:
          name: florafix-db
          property: host
      - key: DB_NAME
        fromService:
          name: florafix-db
          property: database
      - key: DB_USER
        fromService:
          name: florafix-db
          property: user
      - key: DB_PASSWORD
        fromService:
          name: florafix-db
          property: password
  
  - type: pserv
    name: florafix-db
    plan: free
    ipAllowList: []
```

---

## Free Tier Limitations

| Feature | Free Tier | Pro Tier |
|---------|-----------|---------|
| Storage | 1 GB | Unlimited |
| CPU | Shared | Dedicated |
| Backup | 7 days | 30 days |
| Connection Pooling | Limited | Yes |
| High Availability | No | Yes |
| Idle Shutdown | Yes (after 15 min) | No |

**Note:** Free tier PostgreSQL instances are spun down after 15 minutes of inactivity. Your web service will wake it up on first request.

---

## Troubleshooting

### Connection Refused
- ✅ Check database is running (should say "Available" in dashboard)
- ✅ Verify IP allowlist (empty = allow all)
- ✅ Check credentials in environment variables

### Migrations Failed
- ✅ Run `python manage.py migrate` in shell
- ✅ Check logs in Render dashboard
- ✅ Ensure psycopg2-binary is in requirements.txt

### Static Files Not Working
- ✅ Run `python manage.py collectstatic --noinput`
- ✅ Check WhiteNoise middleware is installed
- ✅ Verify STATIC_ROOT and STATICFILES_DIRS

### Database Won't Connect
```bash
# Test connection in shell
python -c "import psycopg2; psycopg2.connect('postgresql://user:pwd@host:5432/db')"
```

---

## Next Steps

1. ✅ Create PostgreSQL database on Render
2. ✅ Copy connection credentials
3. ✅ Add to environment variables
4. ✅ Deploy web service
5. ✅ Run migrations
6. ✅ Test the application
7. ✅ Monitor logs for errors

Once everything is working, your FloraFix app will be live and storing data in PostgreSQL!

---

## Quick Reference Links

- Render Dashboard: https://dashboard.render.com
- Render PostgreSQL Docs: https://render.com/docs/databases
- Django PostgreSQL Setup: https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes
>>>>>>> 35e0a5b36eb1bbb2244e40b494c2a14f57220f06
