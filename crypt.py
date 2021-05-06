import telebot, json, sqlite3, telebot.types as types
from crypt_parse import parse
from time import sleep


def read_json(name):
	with open(name, 'r') as file: 
		data = json.load(file)
		file.close()
	return data

def write_json(name, new_data, index: int):
	with open(name, 'r') as file:
		data_do = json.load(file)
		file.close()

	data_do[index] = new_data

	with open(name, "w", encoding="utf-8") as file:
		json.dump(data_do, file, ensure_ascii=False)
		file.close()


CHAT_ID = 929084625 #
client = telebot.TeleBot(read_json("settings.json")["TOKEN"])


@client.message_handler(commands=["start"])
def start(message):
	while True:
		parsing1 = parse("RUR")
		parsing2 = parse("BTC")
		parsing3 = parse("ETH")
		

		if read_json("config.json")[0] != parsing1:
			if parsing1['DATA_RUR']["TYPE"] == "BUY":
				emoji = "✅ Покупка"
			else:
				emoji = "❌ Продажа"
			form = f"{emoji} по цене (в рублях){parsing1['DATA_RUR']['PRICE']}.\n TP1: {parsing1['DATA_RUR']['TP1']}.\n В {parsing1['DATA_RUR']['TIME']}!"
			client.send_message(message.chat.id, form)
			write_json("config.json", parsing1, 0)
		

		if read_json("config.json")[1] != parsing2:
			if parsing2['DATA_BTC']["TYPE"] == "BUY":
				emoji = "✅ Покупка"
			else:
				emoji = "❌ Продажа"
			form = f"{emoji} по цене (в биткоинах){parsing2['DATA_BTC']['PRICE']}.\n TP1: {parsing2['DATA_BTC']['TP1']}.\n В {parsing2['DATA_BTC']['TIME']}!"
			client.send_message(message.chat.id, form)
			write_json("config.json", parsing2, 1)

		
		if read_json("config.json")[2] != parsing3:
			if parsing3['DATA_ETH']["TYPE"] == "BUY":
				emoji = "✅ Покупка"
			else:
				emoji = "❌ Продажа"
			form = f"{emoji} по цене (в эфириум){parsing3['DATA_ETH']['PRICE']}.\n TP1: {parsing3['DATA_ETH']['TP1']}.\n В {parsing3['DATA_ETH']['TIME']}!"
			client.send_message(message.chat.id, form)
			write_json("config.json", parsing3, 2)
		sleep(10)


client.polling()