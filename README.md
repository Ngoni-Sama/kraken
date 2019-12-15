<img src="./images/logo.png">

# KRAKEN

The SMS-INTERNET Bridge using RaspberryPi

## Note

A Nice documentation will be provide as soon as possible !

# Requirements

- Python (3.x is recommended)
- Gammu (A shell script will be provide to make things more easy).

## How to install

```
$ cd path/project
$ virtualenv -p python3 kraken
$ source kraken/bin/activate
$ pip install -r dev_requirements.txt
```

## How to use it 
### To start the Bulk SMS Server
```
$ python run.py
```

### To send a direct SMS message
```
cd app/util/krk
python send.py -p 6******* -m "This is a test message, for fun"
```

### To start SMS-BOT

```
# In your first terminal, you need to start the Consummer
cd app/util/krk
python receive.py

# In your second terminal, you need to start teh bot itself
cd app/util/krk
python sms_bot.py
```

### Others

- To refresh the connection with the Huawei module
```
cd app/util/krk
python refresh_connection.py
```

- To list sms received and saved in mongo
```
cd app/util/krk
python list_sms_bot.py
```

- To clean sms received (in the SIM card and mongo)
```
cd app/util/krk
python empty.py
```

- To run the tests:

```
$ pytest tests
```

## Author

- Sanix-darker