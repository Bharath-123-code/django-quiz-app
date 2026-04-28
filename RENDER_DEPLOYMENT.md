# Render Deployment Guide

## What I've Fixed

I've created an automatic database population system that will populate questions when deploying to Render.

### New Files Created:
1. **`quiz/management/commands/populate_questions.py`** - Django management command that auto-populates 80 questions
2. **`render.yaml`** - Render configuration file that runs migrations and populates questions on deploy
3. **`Procfile`** - Backup configuration for Render

## Steps to Deploy or Fix Existing Deployment

### Option 1: Fresh Deploy (Recommended)
If you haven't deployed yet or want to redeploy:

1. Make sure all files are committed to GitHub:
   ```bash
   git add -A
   git commit -m "Add automatic database population for Render deployment"
   git push
   ```

2. Go to Render dashboard and either:
   - Create a new Web Service, OR
   - Trigger a redeploy of existing service (deploy button)

3. The build will automatically:
   - Run migrations
   - Populate all 80 questions into the database
   - Start the server

### Option 2: Fix Existing Deployment

If your app is already deployed but missing questions:

1. Commit and push the new files:
   ```bash
   git add -A
   git commit -m "Add automatic database population for Render deployment"
   git push
   ```

2. In Render Dashboard:
   - Go to your service
   - Click "Manual Deploy" or "Redeploy latest commit"
   - Wait for build to complete (2-3 minutes)

3. The new build will populate questions automatically

### Option 3: Manual Population (If Still Not Working)

If questions still don't appear after redeploy:

1. In Render Dashboard, go to your service
2. Click "Shell" tab
3. Run this command:
   ```bash
   python manage.py populate_questions
   ```
4. Check your app - questions should now display

## Verify It Works

After deployment:
1. Visit your Render app URL
2. Enter your name and click "Start Quiz"
3. You should see "Question 1 of 15" with a question and 4 options
4. Navigate through questions using Next/Previous buttons
5. Submit to see results and leaderboard

## How It Works

The management command:
- ✅ Checks if questions already exist (prevents duplicates on redeplooy)
- ✅ Creates 80 unique questions from the database
- ✅ Runs automatically during build process
- ✅ Can also be triggered manually from Render shell

Questions selected per quiz: 15 random unique questions
Total questions available: 80
