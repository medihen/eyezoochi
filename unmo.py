##
# tomari003:
# 全ての入力に肯定的な相槌を返す人工無脳。
# 相槌は登録された語句からランダムで選択して出力する。
#
# Unmo.py
# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードをコピーして編集。

from random import choice
from responder import RandomResponder
from dictionary import Dictionary

class Unmo:
    """
    人工無脳コアクラス

    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答(Responder)クラスの名前
    """

    def __init__(self, name):
        """
        文字列を受け取り、コアインスタンスの名前に設定する。
        Responder(Random)インスタンスを生成し、保持する。
        Dictionaryインスタンスを作成し、保持する。
        """
        self._dictionary = Dictionary()

        self._name = name
        self._responder = RandomResponder('Random', self._dictionary)

    def dialogue(self, text):
        """
        ユーザからの入力を受け取り、Responderに処理させた結果を返す。
        """
        return self._responder.response(text)

    @property
    def name(self):
        """人工無脳インスタンスの名前"""
        return self._name

    @property
    def responder_name(self):
        """保持しているResponderの名前"""
        return self._responder.name
