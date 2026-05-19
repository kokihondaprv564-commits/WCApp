# WCApp

2026 FIFA ワールドカップ観戦向けの選手名鑑アプリ

このリポジトリは `api/`（FastAPI）と `web/`（Vue 3 + Vite）を含みます。

クイックスタート:

バックエンド:

```zsh
cd api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8080
```

フロントエンド:

```zsh
cd web
npm install
npm run dev
```
