[![](https://img.shields.io/maintenance/yes/2024)](https://github.com/jcivitel/)
[![Static Badge](https://img.shields.io/badge/GitHub-jcivitell-green?logo=github)](https://github.com/jcivitel/py_wifi_qr)
[![GitHub Repo stars](https://img.shields.io/github/stars/jcivitel/py_wifi_qr)](https://github.com/jcivitel/py_wifi_qr)
[![GitHub License](https://img.shields.io/github/license/jcivitel/py_wifi_qr)](https://github.com/jcivitel/py_wifi_qr)

# What is the goal of the project? #
A QR code offers a quick and user-friendly way to connect devices to a network. Simply scanning the code eliminates the need to manually enter the SSID and password, saving time and minimizing errors. The use of encrypted information in the QR code improves security, while automated configurations simplify setup.

### How to install the project? ###
1. First clone the repository to a local directory on your computer.
```console
git clone https://github.com/jcivitel/py_wifi_qr.git
```

2. Open a Command Prompt (CMD) and execute the following command in the directory:
```python
python -m venv venv
```

3. In this step, you need to install the required python packages to provide the script with all it dependencies:
```python
. venv/bin/activate
pip install -r reqirements.txt
```

4. After installing the required packages, you can run the script with your `<SSID>` and password as `<KEY>`:
```python
python main.py <SSID> <KEY>
```

5. The script generates a QR code, which is opened directly with your standard image program.
<img src="docs/Test-WiFi.png" width= 220>

---

## Contributors
[![Contributors Display](https://badges.pufler.dev/contributors/jcivitel/garrysmod?size=50&padding=5&bots=false)](https://github.com/jcivitel/py_wifi_qr/graphs/contributors)
