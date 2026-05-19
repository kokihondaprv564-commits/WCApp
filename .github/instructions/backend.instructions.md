# Backend Instructions

## Stack

- Python
- FastAPI
- uv

## Architecture

- ルーティングとビジネスロジックを分離する
- スキーマは Pydantic で定義する
- API ごとに router を分割する
- 型ヒントを必須とする

推奨構成:

```txt
/api
├─ app
│  ├─ main.py
│  ├─ routers
│  ├─ schemas
│  ├─ services
│  ├─ repositories
│  └─ data
```