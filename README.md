Export your bookmarks from your browser as an HTML file. Save this file to the directory where this repo is stored in.

Add your Notion integration token and database ID in the notion.py file. Follow [this link](https://developers.notion.com/docs/getting-started) to get them.

Run the notion.py file to export all bookmarks to your database of choice. This script assumes that your database has 2 columns, one called Name (for storing the page title) and another called Link. The Name Column has type `text`, while the Link Column has type `url`. You should change these as per your needs.

