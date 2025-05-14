import os

from bot.core.agents import generate_random_user_agent, is_user_agent_valid, get_telegram_custom_params
from bot.utils import logger
from bot.config import settings
from bot.utils.file_manager import load_from_json, save_to_json, update_ua_json_data


class Accounts:
    def __init__(self):
        self.workdir = "sessions/"
        self.api_id = settings.API_ID
        self.api_hash = settings.API_HASH

    @staticmethod
    def get_available_accounts(sessions: list):

        accounts_from_json = load_from_json('sessions/accounts.json')

        if not accounts_from_json:
            raise ValueError("Can't run script | Please, add account/s in sessions/accounts.json")

        available_accounts = []
        for session in sessions:
            is_session_added = False
            for saved_account in accounts_from_json:
                if saved_account['session_name'] == session:
                    if not is_user_agent_valid(saved_account['user_agent']):
                        tg_params = get_telegram_custom_params(saved_account['user_agent'])
                        saved_account['user_agent'] = saved_account['user_agent'] + tg_params if tg_params else (
                            generate_random_user_agent(device_type='android', browser_type='chrome'))
                        update_ua_json_data(f'sessions/accounts.json', dict_=saved_account)
                        logger.success(f'{saved_account["session_name"]} | Successfully updated User-Agent data')
                    available_accounts.append(saved_account)
                    is_session_added = True
                    break
            if not is_session_added:
                logger.warning(f'{session}.session does not exist in sessions/accounts.json')
                ans = input(f"Add {session} to accounts.json? (y/N): ")
                if 'y' in ans.lower():
                    raw_proxy = input("Input the proxy in the format type://user:pass:ip:port (press Enter to use without proxy): ")
                    user_agent = generate_random_user_agent(device_type='android', browser_type='chrome')
                    new_account = {
                         "session_name": session,
                         "user_agent": user_agent,
                         "proxy": raw_proxy
                    }
                    save_to_json(f'sessions/accounts.json', dict_=new_account)
                    available_accounts.append(new_account)
                    logger.success(f'Account {session} added successfully')

        return available_accounts

    def pars_sessions(self):
        sessions = []
        for file in os.listdir(self.workdir):
            if file.endswith(".session"):
                sessions.append(file.replace(".session", ""))

        logger.info(f"Searched sessions: {len(sessions)}.")
        return sessions

    async def get_accounts(self):
        sessions = self.pars_sessions()
        available_accounts = self.get_available_accounts(sessions)

        if not available_accounts:
            raise ValueError("Available accounts not found! Please add accounts in 'sessions' folder")
        else:
            logger.success(f"Available accounts: {len(available_accounts)}.")

        return available_accounts
