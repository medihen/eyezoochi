##
# tomari003:
# 全ての入力に肯定的な相槌を返す人工無脳。
# 相槌は登録された語句からランダムで選択して出力する。
#
# responder.py
# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードをコピーして編集。

from random import choice

class Responder:
    """
    AIの応答を制御する思考エンジンの基底クラス。
    継承して使わなければならない。

    メソッド:
    response(str) -- ユーザの入力

    プロパティ：
    name -- Responderオブジェクトの名前
    """

    def __init__(self, name, dictionary):
        """文字列を受け取り、自身のnameに設定する。"""
        self._name = name
        self._dictionary = dictionary

    def response(self, text):
        """文字列を受け取り、思考した結果を返す。"""
        pass

    @property
    def name(self):
        """思考エンジンの名前"""
        return self._name


class RandomResponder(Responder):
    """
    AIの応答を制御する思考エンジンクラス。
    登録された文字列からランダムなものを返す。

    クラス変数:
    RESPONSES -- 応答する文字列のリスト
    """

    def __init__(self, name, dictionary):
        """
        文字列nameを受け取り、オブジェクトの名前に設定する。
        'dics/random.txt'ファイルから応答文字列のリストを読み込む。
        """
        super().__init__(name, dictionary)

        """
        下のファイル操作と同じものがDictionaryクラスにあるので、
        削除しても動くように変更
        """

#        with open('dics/random.txt', mode='r', encoding='utf-8') as f:
#            self._responses = [x for x in f.read().splitlines() if x]

        self._responses = self._dictionary.random

    def response(self, _):
        """ユーザからの入力は受け取るが、使用せずにランダムな応答を返す"""
        return choice(self._responses)
