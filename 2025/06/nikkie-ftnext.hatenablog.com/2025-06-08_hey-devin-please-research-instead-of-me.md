<!-- metadata -->

- **title**: ふーん Devinやるじゃん - nikkie-ftnextの日記
- **source**: https://nikkie-ftnext.hatenablog.com/entry/hey-devin-please-research-instead-of-me
- **author**: nikkie-ftnext.hatenablog.com
- **published**: 2025-06-08T13:16:21Z
- **fetched**: 2025-06-08T17:14:14.383340Z
- **tags**: codex, ai
- **image**: https://ogimage.blog.st-hatena.com/8599973812319890363/6802418398466646461/1749388581

## 要約

**Devin**を*ジュニアエンジニア*として扱い、面倒な**環境構築**タスクを丸投げしたところ、必要な依存関係とセットアップ手順を丁寧に調べてスクリプト化まで行ってくれた。おかげでテスト作成やデッドコード削除といった本質的な作業に集中でき、**調査代行**の効果を実感。今後も積極的に活用したいと締めくくられている。

## 本文

### はじめに

[七尾百合子](https://millionlive-theaterdays.idolmaster-official.jp/idol/yuriko/)さん、お誕生日 _83日目_ おめでとうございます！ nikkieです。

Devinは*ジュニアエンジニア*と言われますが、手取り足取りお世話しなくてもいいんだなと思った事象の紹介です[1](#fn:1)

### 目次

### これまでのnikkieとDevin

自律型のコーディングエージェントDevinは、**ジュニアエンジニアとして扱う**のがよいとされています。

> TLDR: Treat Devin like a junior engineer. Assign Devin tasks a junior engineer or intern could figure out if provided with sufficient, clear instructions. Remember to instruct Devin with the level of detail that you would give to a human coworker. ([When to Use Devin](https://docs.devin.ai/essential-guidelines/when-to-use-devin))

実際、コードの変更箇所を**丁寧に指示**してきました。

上の記事とは別の例[2](#fn:2)

任せた作業が円滑に進むよう依頼者側で丁寧に指示するものと*思い込んでいた*のですが、「実は丸投げしてDevinの好きにやらせてみてもいいのかもしれない」とこのひと月くらい考えています。

### めちゃくちゃ気が乗らねェ開発TODO

メンテナしているSpeechRecognitionにプルリク[エス](https://d.hatena.ne.jp/keyword/%A5%A8%A5%B9)トが届きました。

これは私が気づけていなかった修正で、ありがたい限りです。  
変更箇所にテストはないのですが、実質ドキュメントの修正なのでマージしました。

ただこの作業の中で**デッドコードに気づきます**

```
if not hasattr(self, 'vosk_model'):
    if not os.path.exists("model"):
-        return "Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder."
+        return "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder."
        exit(1)

```

「早期returnの後の`sys.exit(1)`、到達しないコード（＝デッドコード）だぞ...」

ミノ駆動本の教えによれば、デッドコードは発見次第即削除です（[改訂新版](https://gihyo.jp/book/2025/978-4-297-14622-1) 10.1）。  
しかしながらこの箇所（`recognize_vosk`メソッド）には、テストがありません。  
まずテストを書き、壊していないことを確認しながらデッドコードを削除した方がよいと判断しました。  
デッドコードの他にも修正点が見えていたというのもあります。

さて、テストを書くのは全然気が乗るのですが（[リファクタリング](https://d.hatena.ne.jp/keyword/%A5%EA%A5%D5%A5%A1%A5%AF%A5%BF%A5%EA%A5%F3%A5%B0)し放題のボーナスタイムになりますからね！）、`recognize_vosk`を動かすようにするための**環境構築が面倒**くさくてかないませんでした。  
ここではそもそもテストがないので、（モックでなく）実物を使ったテストを1つ用意しようとしています。

Voskというのは[音声認識](https://d.hatena.ne.jp/keyword/%B2%BB%C0%BC%C7%A7%BC%B1)のツールのようなのですが、私には初見です。  
SpeechRecognitionにはVosk設定のためのドキュメントがありますが、自分が手を動かすというのが苦痛でした。  
私の有限の時間は、もっと強く興味を惹かれることに使いたい！

### Devinに環境構築方法の調査を依頼

ただメンテナとしてやらなければなりません[3](#fn:3)。  
気が乗らない中、私はふと想います、「Devin、お前、できるか？」

ジュニアエンジニアのDevinに、私が丁寧に指示できない領域を依頼しました。  
この時点では「できたら儲けもの」（たぶんできないからそのときは腹をくくってやろう）と考えていました。

```
調査をお願いします。
プルリクエストは作らず、このチャットに調査結果を記載してください

## 調査内容
以下のrecognize_voskを動かせる状態にしてください
https://github.com/Uberi/speech_recognition/blob/0747dccaf42b01cab720ecda25eb2e5741bef9e4/speech_recognition/__init__.py#L1249-L1265

```

これを**Devinが達成した**んです！（抜粋して紹介）

```
# SpeechRecognition ライブラリの recognize_vosk 機能を動作させる方法

## 調査結果

SpeechRecognition ライブラリの `recognize_vosk` 関数を動作させるために必要な手順を調査しました。以下に詳細をまとめます。

### 必要な依存関係

1. **vosk パッケージのインストール**:

2. **Vosk モデルのダウンロードと配置**:

### セットアップ手順

1. **モデルの配置**:

2. **コードの実装**:

### 動作確認

テスト用のスクリプトを作成して実行したところ、正常に動作することを確認しました：

### 注意点

### まとめ

SpeechRecognition ライブラリの `recognize_vosk` 関数を動作させるには、vosk パッケージのインストールとモデルの適切な配置が必要です。これらの手順を実行することで、オフラインでの音声認識が可能になります。

```

望外の結果に私は驚きました。  
自分がめちゃめちゃ気が乗らないがやらなければならなかったことを、**Devinが代わりにやってくれた**ことに感動しました（ありがとう〜、最高です！）

[リポジトリ](https://d.hatena.ne.jp/keyword/%A5%EA%A5%DD%A5%B8%A5%C8%A5%EA)に置く[スクリプト](https://d.hatena.ne.jp/keyword/%A5%B9%A5%AF%A5%EA%A5%D7%A5%C8)化も続けて依頼しました

```
調査ありがとうございます、素晴らしいと思います

「モデルの配置」手順を再現するPythonスクリプトを作って、このチャットに出力してください

```

私の方でPEP 723対応をして、コミットしました

環境構築できたので、テストを用意して、デッドコード削除などの[リファクタリング](https://d.hatena.ne.jp/keyword/%A5%EA%A5%D5%A5%A1%A5%AF%A5%BF%A5%EA%A5%F3%A5%B0)を実施しています🙌

ちなみにDevinの実装から以下の記事に書いた学びがありました

### 終わりに

ジュニアエンジニアとしてDevinに丁寧にタスクを指示してきましたが、私の気が乗らないタスクをダメ元でDevinに「調査して」とお願いしたところ、見事に達成してくれた事例を紹介しました。

今回の環境構築、過程は私にとってどうでもよくて、環境構築の再現可能な手順が自分の手を動かさずに知れるのが理想だったんですよね。  
**過程は完全にDevinにお任せして、結論をレポートしてもらう**という方法を見出しました。

実はこの方法は1回限りとせずに、たまに試しています。  
LLMまわりで興味ある技術が尽きないのですが、私が手を動かす部分が[ボトルネック](https://d.hatena.ne.jp/keyword/%A5%DC%A5%C8%A5%EB%A5%CD%A5%C3%A5%AF)になるんですよね。  
そんなときは（本当は私がやれたらいいのですが、次から次へと出てくる状況で関心の賞味期限も短いので）**Devinにお願いして調査代行**してもらっています。  
Devinが採用した過程からも学びがあるんですよね〜

Devinはたまに[ポンコツ](https://d.hatena.ne.jp/keyword/%A5%DD%A5%F3%A5%B3%A5%C4)なこともしますが私を幸せにもしたので、『アイの歌声を聴かせて』のシオンさんぽいですね

### P.S. Devin as 妹

妹**口調**にしています。  
こ、これはKnowledgeの設定の素振りであって、[くぁwせdrftgyふじこlp](https://ja.wikipedia.org/wiki/%E3%81%8F%E3%81%81w%E3%81%9Bdrftgy%E3%81%B5%E3%81%98%E3%81%93lp)（言い訳しどろもどろ）
