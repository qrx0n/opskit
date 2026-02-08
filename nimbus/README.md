# 🔍 Nimbus

**Nimbus** - an ethical hacking tool, made for reverse DNS lookup;

---

## ⚙️ Installation

1. `git clone https://github.com/pyc4che/nimbus.git && cd nimbus` - install Github Repo;
2. `python3 -m venv .venv` (optional), `pip install -r requirements.txt` - Python setup.

## 📑 Usage

`python3 -m nimbus 'target_ip' -c/--config 'config' -a/--all`

1. `target_ip` - ip to check;
2. `-a/--all` - find all corresponding websites, on this server;
3. `-c/--config` - config file path, like `example.ini` (in `configs` directory)

## 🖼️ Demonstration

![preview](/imgs/preview.png)

---

### ❗ I used [ViewDNS](https://viewdns.info/) API service, for reverse lookup actions
