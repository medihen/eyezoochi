##
# tomari003:
# 全ての入力に肯定的な相槌を返す人工無脳。
# 相槌は登録された語句からランダムで選択して出力する。
#
# dictionary.py
# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードをコピーして編集。

class Dictionary:
    """
    思考エンジンのクラス。

    クラス変数:
    DICT_RANDOM -- ランダム辞書のファイル名。

    プロパティ:
    random -- ランダム辞書
    """

    DICT_RANDOM = 'dics/random.txt'

    def __init__(self):
        """
        ファイルからの辞書の読み込みを行う。
        """
        with open(Dictionary.DICT_RANDOM, encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

    @property
    def random(self):
        """
        ランダム辞書
        """
        return self._random
