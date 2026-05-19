
# Frontend Instructions

## Stack

- Vue 3
- TypeScript
- ESLint
- Prettier

## Architecture

- Composition API を使用する
- script setup を優先する
- TypeScript の型を明示する
- コンポーネントを小さく保つ
- API 通信は composables に切り出す

推奨構成:

```txt
/web
├─ src
│  ├─ components
│  ├─ pages
│  ├─ composables
│  ├─ services
│  ├─ types
│  └─ assets
```