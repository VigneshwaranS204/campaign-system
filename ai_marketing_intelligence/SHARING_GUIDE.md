# How to Share This Project

You can share this project in two primary ways: uploading it to GitHub (Recommended) or sharing it as a ZIP file.

## Option 1: Share via GitHub (Professional & Recommended)
This method is best for academic projects as it shows version control skills.

### 1. Initialize Git
*Note: You need to have Git installed. If not, download it from [git-scm.com](https://git-scm.com/downloads).*

Open your terminal in the project folder and run:
```bash
git init
git add .
git commit -m "Initial commit of AI Marketing Intelligence System"
```

### 2. Create a Repository on GitHub
1. Go to [GitHub.com](https://github.com) and log in.
2. Click **New Repository**.
3. Name it `ai-marketing-intelligence`.
4. Do **not** check "Add a README" (we already have one).
5. Click **Create repository**.

### 3. Push to GitHub
Copy the commands shown on GitHub (under "…or push an existing repository from the command line") and run them. They will look like this:
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-marketing-intelligence.git
git push -u origin main
```
*Note: Replace `YOUR_USERNAME` with your actual GitHub username.*

### 4. Share the Link
Send the repository URL to your professor or colleagues.

---

## Option 1.5: Upload via GitHub Website (No Git Required)
If you don't want to install Git, you can upload files manually.

1.  **Create Repository**: Follow steps 1 & 2 in "Option 1" above to create a blank repo.
2.  **Upload Files**:
    -   In your new repository on GitHub, click the **"uploading an existing file"** link (usually under the "Quick setup" box).
    -   Or click **Add file** > **Upload files**.
3.  **Drag & Drop**:
    -   Open your project folder `ai_marketing_intelligence` on your computer.
    -   Select all files and folders (including `data`, `dashboard`, `model`, `requirements.txt`, etc.).
    -   Drag them into the browser window.
4.  **Commit**: Wait for files to upload, then click **Commit changes**.

---

## Option 2: Share via ZIP File
If you cannot use GitHub, you can zip the project.

### 1. Clean Up (Optional)
To make the file smaller, you can delete the `__pycache__` folders and the virtual environment (if inside the folder), but **keep** `requirements.txt`.
You can recreate the environment later.

### 2. Zip the Folder
1. Right-click the `ai_marketing_intelligence` folder.
2. Select **Send to > Compressed (zipped) folder**.
3. Rename the file to `AI_Marketing_Intelligence_Project.zip`.

### 3. How the Receiver Runs It
Tell them to:
1. Unzip the file.
2. Open a terminal in the folder.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run ai_marketing_intelligence/dashboard/app.py`.

---

## Option 3: Share via WhatsApp
This is the quickest way to send the project to friends or group chats.

### 1. Locate the Zip File
I have already created a zip file for you named **`AI_Marketing_Intelligence_Project.zip`** in your project folder (`c:\Users\ADMIN\Desktop\campaign system`).

### 2. Send it
1. Open **WhatsApp Web** or **WhatsApp Desktop**.
2. Open the chat where you want to send the project.
3. Drag and drop the `AI_Marketing_Intelligence_Project.zip` file into the chat.
4. Hit Send!

---

## Checklist Before Sharing
- [ ] **README.md**: Ensure it has your name and project details.
- [ ] **Data**: The synthetic data is included in `data/campaign_data.csv`.
- [ ] **Requirements**: `requirements.txt` is up to date.
