# grass-photo
Scripts to show GitHub contribution graph (grass) on Google Nest Hub

# Usage of scripts

## Make grass image file
Install required python modules.
```
pip install -r requirements.txt
```
Then, run make-photo.py.
```
python make-photo.py <your-github-id>
```

## Upload grass image file
Prepare your OAuth 2.0 access key of Google Photo. (KEEP THE ACCESS KEY SECRET!)
Then, run upload-photo.py.
```
python upload-photo.py -a <your-access-key>
```

## Setup your Nest Hub

T.B.D.

# Automation
This repository includes scripts to make and upload image files automatically using GitHub Actions.
You can automate making and uploading images by forking this repository.
For automation, you need to save your OAuth 2.0 access key of Google Photo to GitHub secrets.

IT'S YOUR RESPONSIBILITY TO KEEP YOUR OAUTH KEYS SECRET.
WE STRONGLY RECOMMEND TO USE GITHUB PRIVATE REPOSITORY FOR THE AUTOMATION.
WE WILL NOT TAKE RESPONSIBILITY FOR ANY LOSS OR DAMAGE.

## GitHub secrets
You need to set the following GitHub secrets.

| GitHub secret name | Description |
| GITHUB_USER_ID | Your GitHub id. This ID is used to access to GitHub and make a grass image. |
