# chromedriver-installer
Installs / Update last chromedriver version to your system

It will checkout on http://chromedriver.chromium.org for latest release version, download it on to your system, copy it onto /opt/chromedriver and make a sym link to /usr/bin

It's also suitable for update, as will delete the actual version on system. So you can setup an auto-update on crontab basis

## Requirements
- python3.2
- Linux distribution (Tested with > MX Linux 18.03, Ubuntu 20.04, WSL2 (Windows Subsystem for Linux))

## Install

1.Clone this repo:
```
git clone https://github.com/DaWy/chromedriver-installer.git
```

2.Install Python requests package
```
pip install requests
```

## Usage
```
sudo python3 app.py
```

## Crontab Autoupdate

Just update crontab, add a line for this script. For example:

```
0 0 * * *   root    python /root/scripts/chromedriver-installer/app.py
```

This will update the Chromedriver every day at 00:00

