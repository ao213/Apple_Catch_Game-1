# Apple_Catch_Game

## For ao213

## 簡易アーキテクチャ図

![MVCアーキテクチャもどき](https://user-images.githubusercontent.com/36401898/126044596-227056a4-fe08-409d-afc1-2a0a0c5a2062.png)

## TODO(レビュー事項)

- TODO: 自力でコード書けるレベルになっててすごい！あとはオブジェクト指向とかを上手く使えるとBetterなんだけど、これは難しいから少しずつ本を読んでいくといいと思う(俺も出来てない)
- TODO: PEP8を調べて、準拠した書き方に変える
- TODO: docstringを書く(PEP8)
- TODO: 定数は全て大文字のスネークケース(PEP8)
- TODO: クラス名はパスカルケース(PEP8)
- TODO: クラスメソッドとインスタンスメソッドの違いを理解して書く
- TODO: 単一メソッドに役割を分離する
- TODO: 例えば、draw_appleなのに、当たり判定もしてるし、りんごも移動させてるし、凝縮させすぎ
- TODO: 変数の名前に気をつける。bottom_top　とか矛盾してるからね
- TODO: settingsは出来るだけ定数だけおきたい。グローバル変数みたいな使い方は管理がしづらい
- TODO: スペルミスがチラホラあるので、エディターのスペルミスチェック機能をちゃんと使おう
- TODO: 現時点で必要のない実装はしない。(YAGNIの原則)
- TODO: オブジェクト指向を学び直すといいかも。
- TODO: モジュール間の通信が多く、結合度が強い。デザインパターン等を学ぶと良いかも
- TODO: テストを書く前提でコードを考えると凝縮度が高いコードを書けると思う。テストを学ぶといいかも
- TODO: リストみたいな複数存在するものは複数形のsを丁寧に使ってあげると分かりやすいかも。esになる英単語もあります
- TODO: 今回はできてないけど、testsにテストコードを書いていく。(python unittestで検索)
- TODO: pythonの型宣言も行うように意識するといいかも。今回はやってないけど
- TODO: リファクタリングしていく上で、画面表示が綺麗になりました。やったね
- TODO: 自力でコード書けるレベルになっててすごい！あとはオブジェクト指向とかを上手く使えるとBetterなんだけど、これは難しいから少しずつ本を読んでいくといいと思う(俺も出来てない)
- TODO: Pythonにはアクセサ(@property)であるらしいので、セッターゲッターはそれを使うように実装する
- TODO: PlayerクラスとAppleクラスは似た実装が多いので、似た部分の実装を上に１個クラスで作って、継承させてもいいかもしれない

## 注意点

GitHub Copilot使って書いたので、ところどころおかしいところあるかも？
基本的にdocstringの型指定はcopilotが勝手にやったことなのでキャストしてるところもあります。
あとロジックはそれほど精査してません。
