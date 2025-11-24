# AI Deep Learning Platform - Setup Guide

## Overview

This is a Flask-based web application with Firebase authentication for the AI Deep Learning platform.

### Project Structure

```
ai-deep-learning/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Login page
│   └── dashboard.html         # Student dashboard
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md                  # This file
```

---

## 🚀 DEPLOYMENT ON PYTHONYWHERE

### Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com
2. Sign up for a free account
3. Verify your email

---

### Step 2: Upload Files to PythonAnywhere

1. Log in to PythonAnywhere
2. Go to **Files** tab
3. Navigate to `/home/your-username/`
4. Create a new folder: `ai-deep-learning`
5. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `templates/index.html`
   - `templates/dashboard.html`

**Folder structure on PythonAnywhere:**
```
/home/your-username/ai-deep-learning/
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    └── dashboard.html
```

---

### Step 3: Create Web App

1. Go to **Web** tab
2. Click **"Add a new web app"**
3. Choose **"Python 3.10"** (or latest)
4. Choose **"Flask"**
5. For source code path, enter: `/home/your-username/ai-deep-learning`
6. For WSGI file, it will auto-generate

---

### Step 4: Update WSGI File

PythonAnywhere auto-generates a WSGI file. Update it:

1. Go to **Web** tab
2. Click on the WSGI file link (something like `/var/www/your_username_pythonanywhere_com_wsgi.py`)
3. Replace the content with:

```python
import sys
path = '/home/your-username/ai-deep-learning'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

4. Save the file

---

### Step 5: Install Dependencies

1. Go to **Consoles** tab
2. Click **"Start a new Console"** → **"Bash"**
3. Run these commands:

```bash
cd /home/your-username/ai-deep-learning
pip install -r requirements.txt
```

---

### Step 6: Reload Web App

1. Go back to **Web** tab
2. Click the **"Reload"** button next to your web app
3. Wait 10-20 seconds for it to reload

---

### Step 7: Test Your App

1. Click on your web app URL (will be like: `https://your-username.pythonanywhere.com`)
2. You should see the **Login page**!
3. Try logging in with Firebase authentication

---

## ✅ FIREBASE CONFIGURATION

Your Firebase config is already embedded in `templates/index.html` and `templates/dashboard.html`:

```javascript
const firebaseConfig = {
    apiKey: "AIzaSyDuQ1EFMk2VglBcHGyAF1TZRI91TqLoEBM",
    authDomain: "deepacademy-96e3c.firebaseapp.com",
    projectId: "deepacademy-96e3c",
    storageBucket: "deepacademy-96e3c.firebasestorage.app",
    messagingSenderId: "801289797734",
    appId: "1:801289797734:web:448ad230fbe35e2615eda7"
};
```

**Important:** If you regenerate your Firebase project, update this config in both HTML files.

---

## 🔧 NEXT STEPS

### 1. Add Your Logo

Replace the logo URL in `templates/index.html`:

```html
<!-- OLD (placeholder) -->
<img src="https://via.placeholder.com/200x80?text=AI+Deep+Learning" alt="AI Deep Learning Logo" class="logo">

<!-- NEW (your logo) -->
<img src="static/images/logo.png" alt="AI Deep Learning Logo" class="logo">
```

Then upload your logo to `/home/your-username/ai-deep-learning/static/images/logo.png`

### 2. Connect to Django Backend

Currently, the dashboard is a placeholder. To connect to your Django backend:

1. Uncomment the API calls in `templates/dashboard.html`
2. Create corresponding Django API endpoints
3. Verify Firebase tokens in Django

### 3. Add PostgreSQL Database

Later, you'll connect to PostgreSQL for:
- Student profiles
- Course enrollments
- Progress tracking
- Quiz scores

---

## 📝 TROUBLESHOOTING

### Issue: "No module named 'flask'"

**Solution:** Run pip install in a Bash console:
```bash
pip install Flask==3.0.0
```

### Issue: "Permission denied" when uploading files

**Solution:** Make sure you're uploading to `/home/your-username/` directory

### Issue: Blank page or 500 error

**Solution:** Check the error log:
1. Go to **Web** tab
2. Scroll down to **Log files**
3. Click **"Error log"**
4. Look for error messages

### Issue: Firebase auth not working

**Solution:** 
1. Check browser console for errors (F12)
2. Make sure Firebase config is correct
3. Check that HTTPS is enabled

---

## 🎯 CURRENT STATUS

- ✅ Login page with Firebase auth
- ✅ Google login
- ✅ Email/Password login
- ✅ Sign up functionality
- ✅ Dashboard (placeholder)
- ⏳ Connect to Django backend
- ⏳ PostgreSQL database
- ⏳ Course content
- ⏳ Progress tracking

---

## 📞 SUPPORT

For Firebase issues: https://firebase.google.com/support
For PythonAnywhere issues: https://www.pythonanywhere.com/help/

---

## 🔒 SECURITY NOTES

1. **Change the SECRET_KEY** in `app.py` before production
2. **Keep Firebase config secure** - never share with untrusted users
3. **Use HTTPS** - PythonAnywhere provides this by default
4. **Add CORS headers** when connecting to backend APIs
5. **Validate tokens** on the backend before returning user data

---

## 📚 NEXT MODULE: Django Backend

After testing on PythonAnywhere, we'll create:
1. Django REST API
2. PostgreSQL database models
3. Student authentication & authorization
4. Course management
5. Progress tracking
6. Quiz system
7. Reporting & analytics

---

**Ready to deploy?** Follow the steps above! 🚀
