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
Prepare your OAuth 2.0 access key of Google Photo API.
Then, run upload-photo.py.
```
python upload-photo.py -a <your-access-key>
```

IT'S YOUR RESPONSIBILITY TO KEEP YOUR OAUTH KEYS SECRET.
WE WILL NOT TAKE RESPONSIBILITY FOR ANY LOSS OR DAMAGE.
