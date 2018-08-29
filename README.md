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
 * Download the correct distribution from the [Releases](https://github.com/symmetry-apps/web_console/releases) section.
   * For **linux debian distro**, download [web-console_0.1.5_amd64.deb](https://github.com/symmetry-apps/web_console/releases/download/0.1.5/web-console_0.1.5_amd64.deb)
   * For **linux**, manual installation, download [web-console-0.1.5.zip](https://github.com/symmetry-apps/web_console/releases/download/0.1.5/web-console-0.1.1.zip)
   * For **windows** automatic install, download [WebConsoleInstaller.msi](https://github.com/symmetry-apps/web_console/releases/download/0.1.5/WebConsoleInstaller.msi)

## Setup
 * Edit the file **config.ini** to adjust the settings inside.
 * On **windows**, the msi package contains [**MobaSSH**](https://mobassh.mobatek.net/) as the ssh server.
 * For more details, please visit the [Wiki](https://github.com/symmetry-apps/symmetry-ros/wiki/Enable-Slack-SSH-for-ROS-administration)
 
 
## Running the service
 * On **linux** after running the **postinst** script, the service **web-console** is configured to run at startup
 * On **windows** the web-console is run at startup. To adjust the **MobaSSH** settings, run the app from the Start Menu -> Web Console
 
## Dubugging and logging
 * On **linux**, look for the **web-console.log** file, under **/var/log/symmetry-apps/** folder.
