from MongdbHandler.MongodbHandler import MongodbHandler
import datetime


class MongodbTradeLock:
    @staticmethod
    def trade_lock(symbol_name: str, strategy: str) -> None:
        """
        交易同步锁, 避免重复交易
        :param symbol_name:
        :param strategy:
        :return:
        """
        mongodb_handler = MongodbHandler()
        document = {"symbol": symbol_name, "strategy": strategy, "time": datetime.datetime.now()}
        mongodb_handler.lock_collection.insert_one(document)

    @staticmethod
    def trade_unlock(symbol_name: str, strategy: str) -> None:
        """
        解除交易同步锁
        :param symbol_name:
        :param strategy:
        :return:
        """
        mongodb_handler = MongodbHandler()
        document = {"symbol": symbol_name, "strategy": strategy}
        mongodb_handler.lock_collection.delete_many(document)

    @staticmethod
    def check_trade_lock_exist(symbol_name: str, strategy: str) -> bool:
        """
        查看交易同步锁是否存在
        :param symbol_name:
        :param strategy:
        :return:
        """
        mongodb_handler = MongodbHandler()
        document = {"symbol": symbol_name, "strategy": strategy}
        count_documents = mongodb_handler.lock_collection.count_documents(document)
        if count_documents > 0:
            return True
        else:
            return False
