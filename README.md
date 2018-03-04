# web_console

A ssh console for [Slack](https://slack.com) forked from [lins05/slackbot](https://github.com/lins05/slackbot).

## Features

* Connect with Windows / Linux environments from Slack
* Send **ctrl+c** command to your environment, using the **key ctrl+c** command.
* Download files from your environment, using the **attach <<file-path>>** command.
* Upload files to your environment by attaching them into the slack private chat.
* Each slack chat channel has it's onw ssh session.
* Use slack channel to chat with multiple environment at once, through command **ssh <<os specific command>>**
* Python3 support

## Installation
```
pip install git+https://github.com/symmetry-apps/web_console.git
```
