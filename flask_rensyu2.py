#s24010
#flaskの練習
#「こんにちは世界」と書かれたHTML文を表示するプログラム

#事前にflaskモジュールをインストールすると使える
#render_templateはhtmlファイルを扱う際必要
from flask import Flask, render_template

#Flaskライブラリをインスタンス化し、app変数に割り当て
#その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
@app.route('/')
def index():
    #template/indexをあらかじめ作成しておく
    return render_template("index.html")


if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5000,debug=True)
