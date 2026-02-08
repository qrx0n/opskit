# Description

xss_punisher - is a web-application penetration tool. 
That performs quick scan for XSS Vulnerability, by trying to inject JS Code (payload).
-----

# Preview

![preview](/imgs/preview.png)

# Usage & Instalation

Instalation
---
`git clone https://github.com/PR0PH3CY0x1/xss_punisher.git`

`cd xss_punisher/xss_punisher`

Setup
---

`pip3 install -r requirments.txt`

`python3 scanner.py -h`

Usage
---

Try flag '-h' or '--help' to see the help message.

You have to set `target` and `payload`:
----

`python3 scanner.py -t URL -p "JS_CODE"`

# Tests
Software tested on Windows, Termux, Linux.
