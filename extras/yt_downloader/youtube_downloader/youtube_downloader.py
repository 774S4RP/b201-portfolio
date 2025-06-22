from pytube import YouTube

url = input("🎬 Paste the YouTube video link: ")

try:
    yt = YouTube(url)
    print("Video Title:", yt.title)

    stream = yt.streams.get_highest_resolution()
    stream.download()

    print("✅ video downloaded successfully!")

except Exception as e:
    print("❌ An error occured:", e)
