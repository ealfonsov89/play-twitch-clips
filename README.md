## Project Description

This project is an OBS script that allows you to play Twitch clips in OBS using VLC as the video player. The script is written in Python and requires the `requests` package to be installed.

## Installation

1. Install Python by downloading it from the official website: https://www.python.org/downloads/
2. Install the `requests` package by running the following command in your terminal: `pip install -r requirements.txt`
3. Download and install VLC from the official website: https://www.videolan.org/vlc/
4. Download the OBS script from the project repository: [GitHub Repository](https://github.com/username/project)
5. Configure the OBS script in OBS by following these steps:
   1. Open OBS and go to `Tools` > `Scripts`
   2. Click the `+` button and select the downloaded script file
   3. Set the Python bin path in OBS Scripts Windows by following these steps:
      1. Go to `File` > `Settings` > `Scripts`
      2. Click the `Python Settings` button
      3. Set the `Python Executable` field to the path of your Python executable
   4. Add a VLC video source to your OBS scene by following these steps:
      1. Right-click in the `Sources` box and select `Add` > `VLC Video Source`
      2. Set the `VLC Source Name` to the name of your VLC video source
6. Configure the script properties by following these steps:
   1. Right-click on the script in the `Scripts` window and select `Properties`
   2. Set the `twitch_channel` property to the name of your Twitch channel
   3. Set the `vlc_source_name` property to the name of your VLC video source
   4. Set the `client_id` property to your Twitch API client ID
   5. Set the `client_secret` property to your Twitch API client secret

## Downloads

- Python: https://www.python.org/downloads/
- VLC: https://www.videolan.org/vlc/