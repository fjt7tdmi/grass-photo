# grass-photo
Scripts to show GitHub contribution graph (grass) on Google Nest Hub via Google Photos

# Usage of scripts

## Make grass image file
Install required python modules.
```
pip install -r requirements.txt
```
Then, run make-photo.py.
```
python make-photo.py -u <GITHUB_USER_ID>
```

## Upload grass image file
Prepare your OAuth 2.0 keys of Google Photos API.
Then, run upload-photo.py.
```
python upload-photo.py -c --refresh-token <GOOGLE_API_REFRESH_TOKEN> --client-id <GOOGLE_API_CLIENT_ID> --client-secret <GOOGLE_API_CLIENT_SECRET>
```

A new Google Photo album will be created. The default album name is "GitHub grass".
Grass images will be saved in the newly created album.

IT'S YOUR RESPONSIBILITY TO KEEP YOUR OAUTH KEYS SECRET.
WE WILL NOT TAKE RESPONSIBILITY FOR ANY LOSS OR DAMAGE.

# Automation of scripts

This repository includes GitHub Actions workflow files.
You can automate the script execution by the following steps.

1. Fork this repository.
  - I strongly recommend to make your GitHub repository *private* to avoid security issues.
2. Set the following GitHub secrets.
  - GITHUB_USER_ID
  - GOOGLE_API_CLIENT_ID
  - GOOGLE_API_CLIENT_SECRET
  - GOOGLE_API_REFRESH_TOKEN
3. Edit .github/workflows/upload-photo.yml to enable a scheduled trigger.

```
on:
  push:
    branches:
      - master
  schedule:
      - cron:  '15 0 * * *'
```

Old GitHub contribution graphs (grasses) are not removed automatically because Google does not provide any API to remove image.
Take care of your Google Drive capacity.

# Configure Google Nest Hub

Setup your Google Nest Hub to show the created Google Photos album.
The default album name is "GitHub grass".
