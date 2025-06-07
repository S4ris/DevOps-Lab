#!/bin/bash

#Update system
sudo apt update

#Instal python and pip
sudo apt install -y python3 python3-pip

#Create folder for app
mkdir -p /home/vagrant/app

#Copy serwer files into VM
cp /vagrant/app/server.py /home/vagrant/app/

#Run the application
nohup python3 /home/vagrant/app/server.py