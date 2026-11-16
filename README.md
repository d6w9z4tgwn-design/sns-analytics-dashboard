# sns-analytics-dashboard

CSVから投稿の反応率を集計し、サマリーカード・ランキング・一覧を含む見やすいHTMLレポートを作成。API連携なし。

Generate an offline HTML engagement dashboard from CSV. No live API.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py samples/example.csv report.html`

Python 3.10+ recommended. AI-generated development assistance was used.
