# Wallpaper changer

## Description
A simple software for fetching images automatically from reddit. Main use case is to poll images from `r/wallpaper` and `r/wallpapers`.
The software works only on ubuntu based linux and is tested only on Linux Mint 19.

## Setup

The program need reddit api-key which can be gained using instructions at `https://github.com/reddit-archive/reddit/wiki/OAuth2`

Then copy and rename `keys.example.json` to `keys.secret.json` and setup values accordingly.

## Test

It is recommended to `venv` when dealing with python. Then simply test functionality with the following commands.
```sh
python3 -m venv venv
source venv/bin/activate
python3 main.py
```

If no exceptions arrived at your console, then the system worked without issues. 
If there was valid image, it will be loaded and set as background.

## Running in background

Running as a CRON-task is the simplest way. Simply setup a shellscript and add to cron running.

Idiot-proof guide fro running things hourly.

1) Set CHANGEME in run.example.sh to root of this project as absolute path
2) `cp run.example.sh run-wallpaper-fetch.sh`
3) `chmod +x run-wallpaper-fetch.sh`
4) `sudo cp run-wallpaper-fetch.sh /etc/cron.hourly`
