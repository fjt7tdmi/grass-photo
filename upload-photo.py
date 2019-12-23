# Copyright 2018 Akifumi Fujita
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import requests
import datetime

def check_response(response):
    if not response.ok:
        print()
        print("HTTP request failed.")
        print(response.url)
        print(response.text)
        exit(1)

def get_album_id(access_token, album_name):
    url = "https://photoslibrary.googleapis.com/v1/albums"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers)
    check_response(response)
    for album in json.loads(response.text)["albums"]:
        if album["title"] == album_name:
            return album["id"]
    return None

def create_album(access_token, album_name):
    url = "https://photoslibrary.googleapis.com/v1/albums"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = json.dumps({
        "album": {
            "title": album_name,
        },
    })
    response = requests.post(url, headers=headers, data=data)
    check_response(response)
    return json.loads(response.text)["id"]

def get_media_item_ids(access_token, album_id):
    url = f"https://photoslibrary.googleapis.com/v1/mediaItems:search"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = json.dumps({
        "albumId": album_id,
    })
    response = requests.post(url, headers=headers, data=data)
    check_response(response)
    return list(map(lambda x: x["id"], json.loads(response.text)["mediaItems"]))

def remove_media_from_album(access_token, album_id, media_item_ids):
    if len(media_item_ids) > 0:
        url = f"https://photoslibrary.googleapis.com/v1/albums/{album_id}:batchRemoveMediaItems"
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        data = json.dumps({
            "mediaItemIds": media_item_ids
        })
        response = requests.post(url, headers=headers, data=data)
        check_response(response)

def upload_image(access_token, file_name, data):
    url = "https://photoslibrary.googleapis.com/v1/uploads"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-type": "application/octet-stream",
        "X-Goog-Upload-File-Name": file_name,
    }
    response = requests.post(url, headers=headers, data=data)
    check_response(response)
    return response.text # upload token

def create_media_item(access_token, album_id, upload_token):
    url = f"https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = json.dumps({
        "albumId": album_id,
        "newMediaItems": [
            { "simpleMediaItem": { "uploadToken": upload_token } },
        ],
    })
    response = requests.post(url, headers=headers, data=data)
    check_response(response)

#
# Entry
#
parser = argparse.ArgumentParser()
parser.add_argument("-t", dest="access_token", default=None, help="Google photo access token.")
parser.add_argument("-n", dest="album_name", default="GitHub grass", help="Google photo album name.")

args = parser.parse_args()

print(f"Check if the album ({args.album_name}) is already exist.")
album_id = get_album_id(args.access_token, args.album_name)

if album_id is None:
    print("Create new album.")
    album_id = create_album(args.access_token, args.album_name)
else:
    print("Clear the album.")
    media_item_ids = get_media_item_ids(args.access_token, album_id)
    remove_media_from_album(args.access_token, album_id, media_item_ids)

print("Upload a grass image file.")
with open("work/grass2.png", "rb") as f:
    file_name = f"grass-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    data = f.read()
    upload_token = upload_image(args.access_token, file_name, data)
    create_media_item(args.access_token, album_id, upload_token)

print("Finished.")
