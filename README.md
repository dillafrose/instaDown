# Instagram Post Downloader

A simple Python script to download Instagram posts using `yt-dlp`. This tool allows you to download individual Instagram posts by providing the post URL.

## Features

- Download Instagram posts by URL
- Save posts with original filenames
- Simple command-line interface
- Progress tracking during downloads
- Automatic folder creation for downloads

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Internet connection

## Installation

1. Clone this repository or download the source code:

   ```bash
   git clone https://github.com/yourusername/instadown.git
   cd instadown
   ```

2. Install the required package:
   ```bash
   pip install yt-dlp
   ```

## Usage

### Basic Usage

Run the script and follow the prompts:

```bash
python instaDown.py
```

### Direct Download

You can also download a post directly by providing the URL as a command-line argument:

```bash
python instaDown.py "https://www.instagram.com/p/EXAMPLE_POST_URL/"
```

### Output

- Downloaded files are saved in the `Downloaded Posts` directory by default
- Each file is named using the format: `[username]_[post_id].ext`
- The script will create the output directory if it doesn't exist

## How It Works

The script uses `yt-dlp` to handle the downloading of Instagram posts. It automatically:

1. Validates the Instagram URL
2. Creates a download directory if it doesn't exist
3. Downloads the highest quality version of the post
4. Saves it with a descriptive filename

## Troubleshooting

### Common Issues

1. **URL Format**

   - Make sure to use the full Instagram post URL
   - Example: `https://www.instagram.com/p/ABC123xyz/`

2. **Download Errors**

   - Check your internet connection
   - Verify the post is public and accessible
   - Make sure you're not being rate-limited by Instagram

3. **Dependencies**
   - If you get a `ModuleNotFoundError`, make sure to install the requirements:
     ```bash
     pip install yt-dlp
     ```

## Security Note

- The script only requires read access to the Instagram post
- No login or personal information is needed
- All downloads are saved locally on your machine

## Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Simple and lightweight solution for Instagram downloads
