import yt_dlp
from pathlib import Path
import os
def intro():
    print("=" * 40)
    print("         Instagram Downloader         ")
    print("=" * 40)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_post(post_url, download_path=None):    
    if download_path is None:
        download_path = Path("Downloaded Posts")
        download_path.mkdir(exist_ok=True)
    ydl_opts = {
        'outtmpl': str(download_path / '%(uploader)s_%(id)s.%(ext)s'),
        'writeinfojson': False,
        'ignoreerrors': True,
        'format': 'best',
    }
    print(f"Downloading: {post_url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([post_url])
        print("Successfully downloaded!")
    except Exception as e:
        print(f"Error downloading: {str(e)}")

def main():
    while True:
        clear_screen()
        intro()
        post_url = input("Enter Instagram post URL: ").strip()
        
        if not post_url:
            print("Error: No URL provided.")
        elif "instagram.com" not in post_url:
            print("Error: Please provide a valid Instagram URL.")
        else:
            clear_screen()
            intro()
            download_post(post_url)

        x = input("\nDo you want to download another post? (y/n): ").strip().lower()
        if x != 'y':
            print("Exiting Instagram Downloader. Goodbye!")
            break

if __name__ == "__main__":
    main()
