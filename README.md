## Config app
```
pip install -r requirements.txt
```

## Start app
```
ENV=(test or prod) python main.py
```

## Fake SMTP server for testing:
```
python -m smtpd -n -c DebuggingServer localhost:2500
```