2015/1/15
これは、WEbStorageのテスト用ディレクトリです。

pageA〜pageCを遷移する情報と各ページの滞在時間をlocalStorageに保存しておき、
セットされた値に応じてインプレッションが変わるデモの作成を目指します。

更新履歴
20150/1/15 新規作成
とりあえず、ページを用意した。
デバッグがchromeがやりやすいが、safariしか入っていないため、chromeを入れてstorageが利用できているかを確認するのが次。

2015/02/02 タイムスタンプの取得を実装した。
次回、ローカルストレージに格納した値をもとに、インプレッションを変更する。

2015/02/08 遷移情報と滞在時間によって、色が変わる機能を追加。
滞在時間が、NaNが入ってエラーになるバグがある。。。

2015/02/14 バグfixして完成。
