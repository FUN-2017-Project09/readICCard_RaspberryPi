# readICCard_RaspberryPi
ラズベリーパイ側のソースリポジトリ  
ICCardReadSystem.sh を実行して始める

## ファイル構成
### cli.py
ICカードを読み取る時に必要なファイル
### GUI-useServer.py
アプリケーションのメインとなるファイル  
ここでGUIの表示とICカードの読み取り・条件判定を行う
### GUI.py
GUI-useServer.pyの旧版  
サーバと接続する前に作成していたもの
### history.py
ICカード内に記録されている使用履歴を表示するプログラム
### ICCardReadSystem.sh
GUI-useServer.pyを再起動するために作ったシェルスクリプト
### readBIN.py
利用履歴と改札入出場履歴の履歴を20件バイナリで取り出すプログラム
### readCard.py
ICカードから読み取ったデータを出力するプログラム
### readICCard.py
ICカードの情報にアクセスするメソッドを実装したプログラム  
これを利用してGUI-useServer.pyでICカードのデータを活用している  
readBIN.pyとreadIDm.pyをインポートして利用している
使い方はプログラム中に記載
### readIDm.py
IDmを読み取るプログラム  
getIDmというメソッドを独自に実装
### test.py
readICCard.pyの使用例を記載（動作テストで使用した）  
  
## 小話
### 大元のプログラム
これらプログラムはnfcpyを改造したものである。  
プロジェクトのリポジトリにフォークしてきているので参照されたし
### Raspberry Pi上でのICカード読み取り環境構築方法
29年度の最終報告書の付録または[このリポジトリのWiki](https://github.com/FUN-2017-Project09/readICCard_RaspberryPi/wiki)に記載
### gitの活用
最初にgitやGitHubの講習会をしないとgitを使う文化にはならない。 
こまめにコミットやPushする癖をつけないと複数の端末で同じソースを扱う時に辛い
### 残された改善点
ICカードの読み取りでは、連続で読み取りを行う時にうまく挙動せず、再起動することで対応とした
オプションをつけると連続で読み取ることが可能だが、今期では機能の抽出ができなかった  
あとissueに改善項目が1つだけある
### フィードバック
- レシートに印刷日時を入れたい
- 利用した人の署名欄を追加したい
- 画面上のメニューバーを消したい
- モバイルSuicaにも対応してほしい
