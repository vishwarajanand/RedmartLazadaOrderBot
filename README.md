# RedmartLazadaOrderBot

[Redmart orders on Lazada](https://cart.lazada.sg/cart) are slotted - one order per day and that too limited no of slots per delivery location. See lazada-redmart delivery impacted notice as mentioned on [this website](https://pages.lazada.sg/wow/i/sg/redmart/covid19updates):


In order to survive, I attempted to make an automation so that I could secure a delivery slot for my Redmart orders on Lazada.

> Chrome automation is a set of technologies used to achieve any particular website interaction using programmatic tools.

Few of those tools are selenium (skipping helium which I am yet to try but is apparently easier) and chrome webdrivers.

## How to run

1. Install [chromedriver dependency](http://chromedriver.storage.googleapis.com/index.html) - download chromedriver, unzip, move to /usr/local/bin (Mac OS / Linux)

2. Install selenium: `pip install selenium`

3. Use `venv`:

```
vishwarajan-mbp:chrome_automation vishwarajanand$ virtualenv venv

# to open editor
(venv) vishwarajan-mbp:chrome_automation vishwarajanand$ code .

# to run
vishwarajan-mbp:chrome_automation vishwarajanand$ source venv/bin/activate
(venv) vishwarajan-mbp:chrome_automation vishwarajanand$ python web_bot.py
```

## Demo


