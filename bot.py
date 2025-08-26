from telebot import TeleBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def banks():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url='https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
        time.sleep(3)

        all_banks_info = []
        for i in range(1, 18):
            bank_name = driver.find_element(By.CSS_SELECTOR, f'body > div.px-4.md\\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\\[375px\\].gap-4.reg\\:flex-row-reverse.reg\\:gap-6.md\\:max-w-\\[unset\\].md\\:w-736.reg\\:w-\\[928px\\].lg\\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\\:absolute.before\\:inset-0.before\\:pointer-events-none.before\\:bottom-auto.before\\:h-16.before\\:border.before\\:rounded-xl.before\\:border-N40.before\\:outline.before\\:outline-\\[0\\.375rem\\].before\\:outline-white.before\\:z-10.after\\:z-10.after\\:absolute.after\\:inset-0.after\\:top-\\[4\\.375rem\\].after\\:border.after\\:border-N40.after\\:rounded-xl.after\\:pointer-events-none.after\\:shadow-\\[0px_4px_0px_8px_white\\] > div.grow.flex.flex-col.h-full.max-w-\\[45%\\].md\\:max-w-none.w-\\[45%\\].md\\:w-\\[40%\\].reg\\:w-\\[50%\\].lg\\:w-\\[46%\\] > div.w-full.grow.rounded-tl-xl > div:nth-child({i}) > span > a')
            rate_arq = driver.find_element(By.CSS_SELECTOR, f'body > div.px-4.md\\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\\[375px\\].gap-4.reg\\:flex-row-reverse.reg\\:gap-6.md\\:max-w-\\[unset\\].md\\:w-736.reg\\:w-\\[928px\\].lg\\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\\:absolute.before\\:inset-0.before\\:pointer-events-none.before\\:bottom-auto.before\\:h-16.before\\:border.before\\:rounded-xl.before\\:border-N40.before\\:outline.before\\:outline-\\[0\\.375rem\\].before\\:outline-white.before\\:z-10.after\\:z-10.after\\:absolute.after\\:inset-0.after\\:top-\\[4\\.375rem\\].after\\:border.after\\:border-N40.after\\:rounded-xl.after\\:pointer-events-none.after\\:shadow-\\[0px_4px_0px_8px_white\\] > div.w-\\[55%\\].grow.-mb-1.md\\:w-\\[60%\\].reg\\:w-\\[50%\\].relative.lg\\:w-\\[54%\\].bg-N30 > div > div.w-full.grow.bg-white > div:nth-child({i}) > div:nth-child(2) > div.w-1\\/2.hover\\:text-O60.mx-auto.w-1\\/2.false > div > div')
            rate_vaj = driver.find_element(By.CSS_SELECTOR, f'body > div.px-4.md\\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\\[375px\\].gap-4.reg\\:flex-row-reverse.reg\\:gap-6.md\\:max-w-\\[unset\\].md\\:w-736.reg\\:w-\\[928px\\].lg\\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\\:absolute.before\\:inset-0.before\\:pointer-events-none.before\\:bottom-auto.before\\:h-16.before\\:border.before\\:rounded-xl.before\\:border-N40.before\\:outline.before\\:outline-\\[0\\.375rem\\].before\\:outline-white.before\\:z-10.after\\:z-10.after\\:absolute.after\\:inset-0.after\\:top-\\[4\\.375rem\\].after\\:border.after\\:border-N40.after\\:rounded-xl.after\\:pointer-events-none.after\\:shadow-\\[0px_4px_0px_8px_white\\] > div.w-\\[55\\%\\].grow.-mb-1.md\\:w-\\[60\\%\\].reg\\:w-\\[50\\%\\].relative.lg\\:w-\\[54\\%\\].bg-N30 > div > div.w-full.grow.bg-white > div:nth-child({i}) > div:nth-child(2) > div:nth-child(2) > div > div')
            all_banks_info.append(f'Բանկ: {bank_name.text},   Առք։ {rate_arq.text},   Վաճ․։ {rate_vaj.text}')
            print(f"Parsing bank {i}")
        with open('banks_info.txt', 'w', encoding='utf-8') as file:
            
            for bank_info in all_banks_info:
                file.write(bank_info + '\n')

        with open('banks_info.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as ex:
        print(ex.__class__.__name__, ex)

    finally:
        driver.close()
        driver.quit()

x = banks()
# with open ('banks_info.txt', 'r', encoding='utf-8') as file1:
#      x = file1.read()
# x = banks()
TOKEN = '8214661534:AAH-V03iM1Vq5uTDuEnA4PGbnUtjG5FeAv0'
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def run_bot(message):
    bot.send_message(message.chat.id, 'Hello Team :)')

@bot.message_handler()
def chat(message):
    if message.text == 'USD':
        bot.reply_to(message, f'{x}')



bot.polling()











