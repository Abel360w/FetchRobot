# FetchRobot The Ultimate Video Downloader By [Abel360w](https://github.com/Abel360w)

**---(Disclaimer Always Give Credit To Me If You Use This Code Or Any Of Its Content)---💙**
 
YouTube Download Bot🚀🎬⬇️

This Telegram bot allows you to download videos from YouTube and other supported websites, including FaceBook!

# Usage

[https://t.me/FetchRobot](https://t.me/FetchRobot)

Join Telegram Channel https://t.me/Anonxc for updates.

Send link directly to the bot. Any
Websites [supported by yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) will work too.

# Limitations That You Can Set (For Your Personal Bot)

Due to limitations on servers and bandwidth, there are some restrictions on this free service.

* Each user is limited to 10 free downloads per 24-hour period
* Maximum of three subscriptions allowed for YouTube channels.
* One File Download Will require at least 1 download token.

If you need more downloads, you can buy download tokens.

# Features

1. fast download and upload.
2. ads free
3. support progress bar
4. audio conversion
5. playlist download
6. payment support: afdian, buy me a coffee, Telegram Payment and Tron(TRX)
7. different video resolutions
8. sending as file or streaming as video
9. celery worker distribution - faster than before.
10. subscriptions to YouTube Channels
11. cache mechanism - download once for the same video.
12. instagram posts and reel download not available

## Normal download Demo

<p align="center"><img src="assets/demo.gif?raw=true" width="200"/></p>

# How to deploy?

This bot can be deployed on any platform that supports Python.

If you are having trouble deploying, you can fork the project to your personal account and deploy it from there.

# DEPLOY TO HEROKU

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?)

# DEPLOY TO KOYEB

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Abel360w/FetchRobot&branch=main&name=ytdlbotx)

# DEPLOY TO Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

 # Set The Required And necessary  environment variables:

* WORKERS: workers count for celery
* PYRO_WORKERS: number of workers for pyrogram, default is 100
* APP_ID: **REQUIRED**, get it from https://core.telegram.org/
* APP_HASH: **REQUIRED**
* TOKEN: **REQUIRED**
* REDIS: **REQUIRED if you need VIP mode and cache** ⚠️ Don't publish your redis server on the internet. ⚠️
* EXPIRE: token expire time, default: 1 day
* ENABLE_VIP: enable VIP mode
* OWNER: owner username
* AUTHORIZED_USER: only authorized users can use the bot
* REQUIRED_MEMBERSHIP: group or channel username, user must join this group to use the bot
* ENABLE_CELERY: celery mode, default: disable
* BROKER: celery broker, should be redis://redis:6379/0
* MYSQL_HOST:MySQL host
* MYSQL_USER: MySQL username
* MYSQL_PASS: MySQL password
* AUDIO_FORMAT: default audio format
* ARCHIVE_ID: forward all downloads to this group/channel
* IPv6 = os.getenv("IPv6", False)
* ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)
* PROVIDER_TOKEN: stripe token on Telegram payment
* PLAYLIST_SUPPORT: download playlist support
* M3U8_SUPPORT: download m3u8 files support
* ENABLE_ARIA2: enable aria2c download
* FREE_DOWNLOAD: free download count per day
* TOKEN_PRICE: token price per 1 USD
* GOOGLE_API_KEY: YouTube API key, required for YouTube video subscription.
* RCLONE_PATH: rclone path to upload files to cloud storage
* TMPFILE_PATH: tmpfile path(file download path)
* TRONGRID_KEY: TronGrid key, better use your own key to avoid rate limit
* TRON_MNEMONIC: Tron mnemonic, the default one is on nile testnet.
* PREMIUM_USER: premium user ID, it can help you to download files larger than 2 GiB

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Command To Setup In Botfather

```
start - Let's start
about - What's this bot?
ping - Bot running status
help - Help
ytdl - Download video in group
settings - Set your preference
buy - Buy token
direct - Download file directly
sub - Subscribe to YouTube Channel
unsub - Unsubscribe from YouTube Channel
sub_count - Check subscription status, owner only.
uncache - Delete cache for this link, owner only.
purge - Delete all tasks, owner only.
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Donation

Found this bot useful? You can donate to support the development of this bot.

## Donation Platforms

* [Buy me a coffee](https://www.buymeacoffee.com/abel360w) 😀

## Cryptocurrency 🧐

**Donate Me Via TRX**

My Public Address to Receive TRX TKFjNFYmnMaRBpsLkNdjpDkKUgMnCq2ChP

Pay me via Trust Wallet: https://link.trustwallet.com/send?coin=195&address=TKFjNFYmnMaRBpsLkNdjpDkKUgMnCq2ChP

                                               or scan this Qr Code
<p align="center"><img src="assets/trx.jpg?raw=true" width="200"/></p>

![](assets/tron.png)

# License

Apache License 2.0

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Run natively on your machine

<details> <summary>...</summary>

To deploy this bot, follow these steps:

1. Install bot dependencies
   * Install Python 3.10 or a later version, FFmpeg.
   * (optional)Aria2 and add it to the PATH.

2. Clone the code from the repository and cd into it.
   * ```Bash
     git clone https://github.com/tgbot-collection/ytdlbot
     ```
   * ```Bash
     cd ytdlbot/
     ```
3. Creating a virtual environment and installing required modules in Python.
   * ```Python
     python -m venv venv
     ```
   * ```Bash
     source venv/bin/activate   # Linux
     #or
     .\venv\Scripts\activate   # Windows
     ```
   * ```Python
     pip install --upgrade pip
     ```
   * ```Python
     pip install -r requirements.txt
     ```
4. Set the environment variables `TOKEN`, `APP_ID`, `APP_HASH`, and any others that you may need.
   * Change values in ytdlbot/config.py or
   * Use export APP_ID=111 APP_HASH=111 TOKEN=123
5. Finally, run the bot with
   * ```Python
     python ytdl_bot.py
     ```

## Docker

One line command to run the bot

```shell
docker run -e APP_ID=111 -e APP_HASH=111 -e TOKEN=370FXI bennythink/ytdlbot
```

# Complete deployment guide for docker-compose

* contains every functionality
* compatible with amd64 and arm64

## 1. get docker-compose.yml

Download `docker-compose.yml` file to a directory

## 2. create data directory

```shell
mkdir data
mkdir env
```

## 3. configuration

### 3.1. set environment variables

```shell
vim env/ytdl.env
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 3.2 Set up init data

If you only need basic functionality, you can skip this step.

### 3.2.1 Create MySQL db

Required for VIP(Download token), settings, YouTube subscription.

```shell
docker-compose up -d
docker-compose exec mysql bash

mysql -u root -p

> create database ytdl;
```

### 3.2.2 Setup flower db in `ytdlbot/ytdlbot/data`

Required if you enable celery and want to monitor the workers.

```shell
{} ~ python3
Python 3.9.9 (main, Nov 21 2021, 03:22:47)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dbm;dbm.open("flower","n");exit()
```

## 3.3 Tidy docker-compose.yml

In `flower` service section, you may want to change your basic authentication username password and publish port.

You can also limit CPU and RAM usage by adding a `deploy` key, use `--compatibility` when deploying.

```docker
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 1500M
```

## 4. run

### 4.1. standalone mode

If you only want to run the mode without any celery worker and VIP mode, you can just start `ytdl` service

```shell
docker-compose up -d ytdl
```

### 4.2 VIP mode

You'll have to start MySQL and redis to support VIP mode, subscription and settings.

```
docker-compose up -d mysql redis ytdl
```

### 4.3 Celery worker mode

Firstly, set `ENABLE_CELERY` to true. And then, on one machine:

```shell
docker-compose up -d
```

On the other machine:

```shell
docker-compose -f worker.yml up -d
```

**⚠️ You should not publish Redis directly on the internet. ⚠️**

### 4.4 4 GiB Support

1. Subscribe to Telegram Premium
2. Setup user id `PREMIUM_USER` in `ytdl.env`
3. Create session file by running `python premium.py`
4. Copy the session file `premium.session` to `data` directory
5. `docker-compose up -d premium`

## kubernetes

refer guide here [kubernetes](k8s.md)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## The End.........
