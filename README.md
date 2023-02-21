# mysqlに一定期間ごとにデータを挿入するシステム

# 動作環境
- python3.10<=

# 動かし方
python3.10以上を入れる

`.env.sample`を`.env`に名前を変更する

.envの中身に各データを入れる

`python -m pip install -r requirements.txt`
と実行

`python main.py`
を実行

デフォルトでは1分に設定してる。

間隔を変えるなら、`time.sleep(60)`の`60`の値を変更してください。(秒数指定)

数値の範囲を変更するには`random.randint(1, 200)`を変更してください。デフォルトは`1~200`