# web_console

A ssh console for [Slack](https://slack.com) forked from [lins05/slackbot](https://github.com/lins05/slackbot).

## Features

* Connect with Windows / Linux environments from Slack
* Send **ctrl+c** command to your environment, using the **key ctrl+c** command.
* Download files from your environment, using the **attach <file_path>** command.
* Upload files to your environment by attaching them into the slack private chat.
* Each slack chat channel has it's onw ssh session.
* Use slack channel to chat with multiple environment at once, through command **ssh <os_specific_command>**
* Python3.5 support

## Installation
```bash
pip install git+https://github.com/symmetry-apps/web_console.git
```

## Setup
 * Copy file **slackbot_settings_default.py** to **slackbot_setting.py** and adjust the settings inside.
 * On Windows, install a sshd server and start it. Tested with: [**MobaSSH**](https://mobassh.mobatek.net/)
 * For more details, please visit the [Wiki](https://github.com/symmetry-apps/symmetry-ros/wiki/Enable-Slack-SSH-for-ROS-administration)
 
 
## Running the service
 * Just run the **python app.py**
 * On **Windows** run the command **pythonw app.py**, to execute the process in the background.
 
 
## Building deb package using [dh-virtualenv](https://github.com/spotify/dh-virtualenv)
 * Install **dh-virtualenv** version 1.0.0 or newer
 * Run the command **dpkg-buildpackage -us -uc** from the project path
 * Look for the deb file generated, one level up from the project folder
 
## Building executable file using [pyinstaller](https://github.com/pyinstaller/pyinstaller)
 * Install **pyinstaller**:
 ```bash
 pip install pyinstaller
 ```
 * Build executable:
 ```bash
 pyinstaller web_console/app.py -F --name web-console
 ```