# Data License

This project uses data from two sources, each with their own licensing terms:

## World Happiness Report 2018

**Source**: United Nations Sustainable Development Solutions Network  
**License**: Open Access  
**URL**: https://www.kaggle.com/datasets/unsdsn/world-happiness

The World Happiness Report data is publicly available and free to use for research and educational purposes. Please cite appropriately:

> Helliwell, J., Layard, R., & Sachs, J. (2018). World Happiness Report 2018. New York: Sustainable Development Solutions Network.

## Gapminder Global Development Data

**Source**: Gapminder Foundation  
**License**: CC BY 4.0 (Creative Commons Attribution 4.0 International)  
**URL**: https://www.kaggle.com/datasets/albertovidalrod/gapminder-dataset

This data is licensed under CC BY 4.0, which allows you to:
- Share - copy and redistribute the material in any medium or format
- Adapt - remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

**Attribution**: 
> Gapminder Foundation. (2018). Gapminder Global Development Data. www.gapminder.org. Licensed under CC BY 4.0.

## Derived Data

All processed and merged datasets created as part of this project (`data/processed/*`) inherit the licensing terms of their source data. When using these derived datasets, please provide attribution to both original sources.
```

6. Press **Ctrl + S** to save

---

## Step 3: Upload Data to Box

Now you need to upload your data folder to Box:

1. Go to https://uofi.app.box.com
2. Log in with your Illinois credentials
3. Create a new folder called `IS477-Project-Data`
4. Upload your entire `data` folder:
   - Click **Upload** → **Folder**
   - Select your `IS-477/data` folder
   - Wait for upload to complete (should take 1-2 minutes)

---

## Step 4: Create Shareable Box Link

1. In Box, right-click on the `IS477-Project-Data` folder
2. Click **Share**
3. Click **Create Shared Link**
4. Set permissions to: **People with the link**
5. Copy the shareable link
6. Keep this link handy - we'll add it to README.md

---

## Step 5: Update README.md with Box Link

1. Open `README.md` in VS Code
2. Find the section that says `**Download Link**: [Box Folder - IS477 Project Data](#)`
3. Replace the `#` with your actual Box link
4. It should look like: `**Download Link**: [Box Folder - IS477 Project Data](https://uofi.box.com/s/your-actual-link-here)`
5. Press **Ctrl + S** to save

---

## Step 6: Update .gitignore (Already Created)

Open `.gitignore` and verify it has this content:
```
# Data files (will be on Box)
data/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
