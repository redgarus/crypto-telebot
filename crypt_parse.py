from bs4 import BeautifulSoup
import requests


def parse(vallet):
	url = f"https://yobit.net/ru/trade/TP1/{vallet}"
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')

	trades = soup.select('.scrolling > .viewport > .overview > .trade_history_table > #microhistory_table > tr')
	val_trades = []
	last_trade = trades[0]
	time = last_trade.select('.first')[0].text
	new_time = ["", "", ""]
	num = 0
	for i in time:
		if i == ":":
			num += 1
		else:
			new_time[num] += i
	new_time[0] = str(int(new_time[0]) + 1)
	form = ""

	for i in new_time:
		if i != new_time[-1]: form += f"{i}:"
		else: form += i

	# -------

	last_trade_succes = {
		"VALLET": vallet,
		f"DATA_{vallet}": {
			'TIME': form,
			'PRICE': last_trade.select('td')[2].text,
			'TP1': last_trade.select('td')[3].text,
			'TYPE': last_trade.select('td')[1].text
			}
	}

	return last_trade_succes