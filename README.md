# ScienceOps Heartbeat
Automated CI style deployments for ScienceOps models.


## Jenkins
### With Docker
Run your deployment inside of a docker container. This prevents you from polluting your Jenkins server with scientific python/r. Install [docker](https://docs.docker.com/installation/) on your Jenkins server and setup a job to run that's configured with this git repo. We suggest using the following schedule: `H * * * *`
```bash
cd $WORKSPACE

set -ex

docker build -t yhat/heartbeat .
docker run -e 'USERNAME=YOUR_USERNAME' -e 'APIKEY=YOUR_APIKEY' -e 'OPS_ENDPOINT=http://scienceops-hostname/' yhat/heartbeat python hello.py
```
### With `virtualenv`
If you don't want to use docker, `virtualenv` is a good alternative. Bootstrap your Jenkins server and install python, pip, and virtualenv.

```bash
# bootstrap your server
$ sudo apt-get -y update
$ sudo apt-get install -y python-software-properties python-pip
$ sudo pip install virtualenv
```

Once you've done this, setup a job that does the following (see script below):
- creates a virtualenv and activates it
- installs latest yhat client using pip
- runs deployment script
- deactivates virtualenv and removes environment

```bash
# as a part of your jenkins job
$ virtualenv env
$ source env/bin/activate
$ sudo pip install yhat
$ python hello.py
$ deactivate
$ rm -rf env
```

## Cron
If you're not using Jenkins, then Cron is a simple alternative. More details [here](http://help.yhathq.com/v1.0/docs/automating-deployments).
```bash
# bootstrap your server
$ sudo apt-get -y update
$ sudo apt-get install -y python-software-properties python-pip
$ sudo pip install yhat
```

```bash
# grab this repo
$ git clone https://github.com/yhat/scienceops-heartbeat/
# in your crontab
0 * * * * python hello.py
```
