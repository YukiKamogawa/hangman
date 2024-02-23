# ランダム関数でランダムに取得した文字列データを用いたハングマン
import random

def hangman():
    wrong = 0                 # プレイヤーの不正解数
    stages = ["",
              "______       ",
              ".     |      ",
              ".     O      ",
              ".    /|\     ",
              ".    / \     "
              ]
    
    """
    ランダムで文字列を取得して問題を出すように改良した箇所
    """
    word = ["cat", "dog", "elephant"] # ランダムに取得するよ用の文字列
    word = random.choice(word)        # word のリストからランダムに文字列を取得する

    rletters = list(word)     # 答えなければいけない残りの文字を記憶するために使用
    board = ["_"] * len(word) # プレイヤーに見せるヒントを記憶する。
    win = False               # プレイヤーが勝利したかどうかの状態を記憶する。
    print("ハングマンへようこそ!")

    # stagesのリストに格納されているリストの数にプレイヤーの不正解数が到達したら、プレイヤーの負け（それまではループする）
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:            # 正解したら（rletters のリストの中に char の値が含まれていたら）
            cind = rletters.index(char) # rletters のリストの中の char のインデックスを取得
            board[cind] = char          # board のリストの該当番号に 正解した文字を割り当てる（更新する）
            rletters[cind] = "$"        # 正解文字が設定文字列内に複数ある場合の挙動を考慮し、 rletters のリストの該当番号を "$" で置き換える
        else:
            wrong += 1                  # 不正解数を増やす
        print(" ".join(board))          # ""(なし)でリスト内の値を結合する(board 内に格納されている値を結合する）
        e = wrong + 1                   # wrong(不正回数)までだとスライスで不正回数の前までしか取得されないので +1 する
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))