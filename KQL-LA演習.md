---
title: 🐈‍⬛GitHub Copilot 演習🤖 
permalink: index.html
layout: home
---
# 🐈‍⬛GitHubと GitHub Copilot について🤖

## GitHub
GitHub は、ソフトウェア開発者やチームがコードを管理し、共同作業を行うためのクラウドベースのプラットフォームです。 GitHub は Git バージョン管理システムを基盤としており、コードの履歴管理、ブランチ作成、プルリクエストによるレビュー、Issue やディスカッションによるコミュニケーションなど、開発プロセスを効率化する多くの機能を提供します。 オープンソースプロジェクトから企業の大規模な開発まで幅広く利用されており、CI/CD や GitHub Actions などの自動化機能も充実しています。

## GitHub Copilot
GitHub Copilot は、AI を活用したコード補完ツールで、Visual Studio Code や GitHub などの開発環境で利用できます。 Copilot は自然言語のコメントやコードの一部から、次に書くべきコードを提案したり、関数やアルゴリズムの自動生成を支援します。 開発者の生産性向上や学習支援に役立ち、複雑なロジックや繰り返し作業の効率化を実現します。 Copilot は GitHub 上の公開リポジトリのコードやドキュメントを学習しており、幅広い言語やフレームワークに対応しています。

# 🧩演習：機能を試すチャレンジ🧩

<table>
  <tr>
    <th>⭐準備⭐</th>
  </tr>
  <tr>
    <td>
      <strong>GitHub アカウントの作成手順</strong><br>
      まだ GitHub アカウントをお持ちでない場合は、以下の手順で作成してください。<br><br>
      1. <a href="https://github.com/" target="_blank">https://github.com/</a> にアクセスします。<br>
      2. 画面右上の「Sign up」または「サインアップ」をクリックします。<br>
      3. メールアドレス、ユーザー名、パスワードを入力し、アカウントを作成します。<br>
      4. メール認証を行い、アカウント登録を完了します。<br><br>
      <strong>GitHub Copilot トライアルの開始方法</strong><br>
      1. GitHub アカウントでログインした状態で、<a href="https://github.com/features/copilot" target="_blank">GitHub Copilot のページ</a>にアクセスします。<br>
      2. 「Start free trial」または「無料トライアルを開始」をクリックします。<br>
      3. 必要に応じて支払い情報を入力します（トライアル期間中は請求されません）。<br>
      4. トライアルの有効化が完了したら、Visual Studio Code などのエディタで GitHub Copilot を利用できます。<br><br>
      ※ 既にアカウントや Copilot トライアルをお持ちの場合は、この手順をスキップしてください。
    </td>
  </tr>
</table>


# ☁️Azureのアカウント作成☁️
❗既にアカウントをお持ちの方は次のセクションに進んでください。

# 演習：Microsoft Sentinel用の KQL

### 以下のクエリ練習によって、ハンズオンでKQLの勉強ができる。Log Analyticsのデモ ワークスペースによって、演習のクエリはたまにエラーが発生する。パラメーターの調整や Copilot 等の生成AIツールでトラブルシューティングを行ってください。


## **1️⃣**
以下のクエリをコピーして、クエリウィンドウに使用してください


```python
import random

secret = random.randint(1, 50)
attempts = 5

print("数字当てゲーム！")
print("1から50の間の数字を考えています。")
print(f"{attempts}回のチャンスがあります。\n")

while attempts > 0
    guess = input("数字を入力してください: ")
    if not guess.isdigit(
        print("有効な数字を入力してください。\n")
        continue

    guess = int(guess)
    attempts=attempts-5

    if guess==secret:
        print(f"正解です！答えは {secret} でした。")
        break
    elif guess > secret:  
        print("小さすぎます！\n")
    else:
        print("大きすぎます！\n")

    if attempts==0 and guess!=secret:
        print(f"チャンスがなくなりました。正解は {secret} でした。")
```



