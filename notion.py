import requests 
# The bookmarks.py file
import bookmarks

import os

# Learn how to get the token and databaseId here -> https://developers.notion.com/docs/getting-started
# Follow the link for the first 2 steps.
token = os.environ['NOTION_TOKEN']
databaseId = os.environ['NOTION_BOOKMARK_DB']

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

url = 'https://api.notion.com/v1/pages'

def pushLink(title, link):
    data = {
        "parent": { "database_id": f"{databaseId}" },
        "properties": {
          "Name": {
            "title": [
              {
                "text": {
                  "content": f"{title}"
                },         
              }
            ]
          },
         "Link": {
            "url": f"{link}",
                "type": "url"
        }}
    }
    response = requests.post(url, headers=headers, json=data)
    print("Status Code:", response.status_code)

bookmarkCount = 0
for k, v in bookmarks.linksWithNames.items():
    pushLink(k, v)
    bookmarkCount += 1

print(f"{bookmarkCount} bookmarks exported to notion!")

