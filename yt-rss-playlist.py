base_rss = "https://www.youtube.com/feeds/videos.xml?playlist_id="
playlist_url = str(input("Enter YouTube playlist URL: "))
playlist_id = playlist_url.split("list=")[1]
print(f"RSS Feed URL: {base_rss+playlist_id}")