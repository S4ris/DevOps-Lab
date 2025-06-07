# 🧪 DevOps Lab

An educational DevOps project designed to build a fully automated development environment using Vagrant, Ubuntu, and Python.

## 📌 Project Goal

- Learn the basics of **Vagrant**
- Automate the creation of virtual machines
- Use **shell provisioning** to configure environments
- Launch a simple **Python HTTP server**
- Build a solid foundation and portfolio as a Junior DevOps Engineer

---

## 🔧 Technologies Used

- **Vagrant** – infrastructure as code for local environments
- **VirtualBox** – virtual machine provider
- **Ubuntu (Jammy 22.04)** – guest OS
- **Python 3** – simple HTTP server

---

## 🚀 Getting Started

### Prerequisites

- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

### Run the Project

```bash
vagrant up

Then open your browser and go to:
http://localhost:8080

You should see: 
Hello from your DevOps Lab machine!

⚙️ Project Structure:
DevOps-Lab/
├── app/
│   └── server.py        # Python HTTP server
├── provision.sh         # Shell provisioning script
├── Vagrantfile          # VM configuration
├── .gitignore
├── LICENSE
└── README.md

🧠 What I Learned
1. How to automate virtual environment setup with Vagrant
2. Basics of provisioning with shell scripts
3. How to expose ports from a guest VM to the host
4. How to run Python services in a virtual machine

📄 License
This project is licensed under the MIT License.