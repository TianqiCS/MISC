import requests
from bs4 import BeautifulSoup
import sqlite3
import time
connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def init_table():
    global connection, cursor
    cursor.execute("CREATE TABLE listings (cid INTEGER, prefix TEXT, num INTEGER, title TEXT, detail TEXT, PRIMARY KEY (cid));")
    connection.commit()
    return

def store_data(data, cid, desc):
    global connection, cursor
    prefix = data[0]
    num = int(data[1])
    title = " ".join(data[3:])
    cursor.execute("INSERT INTO listings (cid, prefix, num, title, detail) VALUES (?, ?, ?, ?, ?)", (cid, prefix, num, title, desc))
    connection.commit()
    return

def scrap(target):
    cid = int(target.split("catoid=28&coid=")[1])
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "http://calendar.ualberta.ca/content.php?catoid=28&navoid=7156"
    }
    session = requests.Session()
    url = "http://calendar.ualberta.ca/preview_course_nopop.php?catoid=28&coid="+str(cid)
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text)
    temp = bsObj.find("h1", {"id": "course_preview_title"})
    if temp:
        print("get page cid = %d" % cid)
        root = bsObj.find("h1", {"id": "course_preview_title"}).parent
        desc = "★"+root.get_text().split("★")[1]
        title = root.find("h1", {}).get_text()
        segments = title.split(" ")
        store_data(segments, cid, desc)
        time.sleep(3)
    else:
        print("Error in page cid = %d" % cid)
    print("Done!")

def main():
    connect("123.db")
    init_table()
    urls = open("url.txt", "r").read().splitlines()
    i = urls[:20]
    for a in i:
        scrap(a)

main()