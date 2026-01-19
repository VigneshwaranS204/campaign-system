# How to Deploy for Free (Streamlit Community Cloud)

The best way to host this application for free is **Streamlit Community Cloud**. It connects directly to your GitHub repository.

## Prerequisites
1. **GitHub Account**: You need a GitHub account.
2. **Project on GitHub**: The project must be uploaded to a public repository (See `SHARING_GUIDE.md` for steps).

## Step-by-Step Deployment Guide

### 1. Upload Code to GitHub
Follow the "Option 1" steps in `SHARING_GUIDE.md` to push your code to GitHub.
**Crucial:** Ensure `requirements.txt` is in the root or `ai_marketing_intelligence` folder.

### 2. Sign Up for Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/).
2. Click **Sign up with GitHub**.
3. Authorize Streamlit to access your repositories.

### 3. Deploy the App
1. Click **New app** (top right corner).
2. **Repository**: Select your `ai-marketing-intelligence` repository.
3. **Branch**: Select `main`.
4. **Main file path**: Enter the path to your app file:
   ```
   ai_marketing_intelligence/dashboard/app.py
   ```
   *(Note: Adjust this if you changed the folder structure. It must point to `app.py`).*
5. Click **Deploy!** 🚀

### 4. Watch it Build
- You will see a "Manage app" terminal on the right.
- It will install the libraries from `requirements.txt`.
- Once finished, your app will open in a new tab!

### 5. Share the Link
- You will get a unique URL (e.g., `https://ai-marketing-intelligence-yourname.streamlit.app`).
- You can share this link with anyone, and they can use the dashboard from their phone or laptop.

## Troubleshooting

- **"ModuleNotFoundError"**: This means a library is missing from `requirements.txt`. Check the logs to see which one.
- **"FileNotFoundError"**: Ensure `campaign_data.csv` was uploaded to GitHub inside the `data` folder.
