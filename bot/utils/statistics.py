from tabulate import tabulate
from typing import List, Optional
from loguru import logger

from src.utils.config import Config, WalletInfo


def print_wallets_stats(config: Config):
    """
    Выводит статистику по всем кошелькам в виде таблицы
    """
    try:
        # Сортируем кошельки по индексу
        sorted_wallets = sorted(config.WALLETS.wallets, key=lambda x: x.account_index)

        # Подготавливаем данные для таблицы
        table_data = []
        total_balance = 0
        total_transactions = 0

        for wallet in sorted_wallets:
            # Маскируем приватный ключ (последние 5 символов)
            masked_key = "•" * 3 + wallet.private_key[-5:]

            total_balance += wallet.balance
            total_transactions += wallet.transactions

            row = [
                str(wallet.account_index),  # Просто номер без ведущего нуля
                wallet.address,  # Полный адрес
                masked_key,
                f"{wallet.balance:.4f} MON",
                f"{wallet.transactions:,}",  # Форматируем число с разделителями
            ]
            table_data.append(row)

        # Если есть данные - выводим таблицу и статистику
        if table_data:
            # Создаем заголовки для таблицы
            headers = [
                "№ Account",
                "Wallet Address",
                "Private Key",
                "Balance (MON)",
                "Total Txs",
            ]

            # Формируем таблицу с улучшенным форматированием
            table = tabulate(
                table_data,
                headers=headers,
                tablefmt="double_grid",  # Более красивые границы
                stralign="center",  # Центрирование строк
                numalign="center",  # Центрирование чисел
            )

            # Считаем средние значения
            wallets_count = len(sorted_wallets)
            avg_balance = total_balance / wallets_count
            avg_transactions = total_transactions / wallets_count

            # Выводим таблицу и статистику
            logger.info(
                f"\n{'='*50}\n"
                f"         Wallets Statistics ({wallets_count} wallets)\n"
                f"{'='*50}\n"
                f"{table}\n"
                f"{'='*50}\n"
                f"{'='*50}"
            )

            logger.info(f"Average balance: {avg_balance:.4f} MON")
            logger.info(f"Average transactions: {avg_transactions:.1f}")
            logger.info(f"Total balance: {total_balance:.4f} MON")
            logger.info(f"Total transactions: {total_transactions:,}")
        else:
            logger.info("\nNo wallet statistics available")

    except Exception as e:
        logger.error(f"Error while printing statistics: {e}")
