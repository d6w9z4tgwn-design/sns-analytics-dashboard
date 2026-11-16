# SNS Analytics Dashboard

SNS投稿のCSVをもとに、インプレッション・エンゲージメント・反応率をひと目で把握できるオフラインHTMLレポートを作成します。APIキーや外部サービスを必要とせず、エクスポート済みデータを安全に分析できます。

## 主な機能

- インプレッション、いいね、コメント、シェアからエンゲージメント率を算出
- サマリーカードと投稿別ランキングで成果を素早く確認
- レスポンシブな単一HTMLファイルとして共有可能
- 負数や必須列の不足を検出し、誤った集計を防止

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py samples/example.csv report.html` を実行し、生成された `report.html` をブラウザで開きます。CSVには `impressions`、`likes`、`comments`、`shares` 列が必要です。投稿本文を表示したい場合は `post` 列も含めてください。

Python 3.10+ 推奨。ライブSNS APIとの連携は行いません。
