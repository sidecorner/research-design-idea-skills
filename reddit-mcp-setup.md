# Reddit MCP Server セットアップ手順

## Step 1: Redditアプリを登録

1. https://www.reddit.com/prefs/apps にアクセス
2. **「Create App」** をクリック
3. 以下を入力：
   - **App Name**: 任意（例: "Claude MCP Tool"）
   - **App Type**: `script`（個人用）
   - **Redirect URI**: 空欄でOK
4. 「Create app」をクリック
5. 表示された **Client ID**（上段）と **Client Secret**（secretの横）を控える

---

## Step 2: Claude CodeにMCPサーバーを追加

ターミナルで以下を実行（Client IDなどを置き換えてください）：

```bash
claude mcp add --transport stdio reddit \
  --env REDDIT_CLIENT_ID=あなたのClientID \
  --env REDDIT_CLIENT_SECRET=あなたのClientSecret \
  --env REDDIT_USER_AGENT="ClaudeMCP/1.0 (by あなたのRedditユーザー名)" \
  -- npx -y @hawstein/mcp-server-reddit
```

---

## Step 3: 確認

```bash
claude mcp list
```

`reddit` が表示されればOKです。

---

## 利用可能な主なMCPサーバー

| パッケージ | 特徴 |
|---|---|
| `@hawstein/mcp-server-reddit` | 高評価・投稿/コメント/スレッド取得対応 |
| `GeLi2001/reddit-mcp` | 軽量・読み取り専用 |
| `jordanburke/reddit-mcp-server` | 投稿・コメント作成もできるフル機能版 |

---

## トラブルシューティング

### 2段階認証（2FA）エラーが出る場合
パスワード認証が使用できません。2FAを一時的に無効化するか、アプリ用の専用パスワードを生成してください。

### Windows で "Connection closed" エラーが出る場合
```bash
claude mcp add --transport stdio reddit \
  -- cmd /c npx -y @hawstein/mcp-server-reddit
```

### Client ID / Secret の場所がわからない場合
登録画面で「personal use script」の下に表示されます：
- **Client ID**: アプリ名の下にある短い文字列
- **Client Secret**: 「secret」ラベルの横にある文字列

---

## 参考リンク

- [Reddit Developer Portal](https://www.reddit.com/prefs/apps)
- [Hawstein/mcp-server-reddit（GitHub）](https://github.com/Hawstein/mcp-server-reddit)
- [GeLi2001/reddit-mcp（GitHub）](https://github.com/GeLi2001/reddit-mcp)
- [jordanburke/reddit-mcp-server（GitHub）](https://github.com/jordanburke/reddit-mcp-server)
