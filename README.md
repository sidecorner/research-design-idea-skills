# research-design-idea-skills

Reddit の UI/UX コミュニティから高評価な投稿を収集し、Markdown レポートとして出力する Claude Code スキル集。

---

## スキル一覧

### `/reddit-ui-research`

r/UI_Design と r/UXDesign から高評価な UI/UX 投稿を調査し、TOP 10 をまとめた Markdown レポートを自動生成する。

---

## 使い方

```
/reddit-ui-research [年号]
```

| 呼び出し例 | 説明 |
|------------|------|
| `/reddit-ui-research 2026` | 調査対象年を 2026 と明記してレポート生成 |
| `/reddit-ui-research` | 年号なし。実行時の西暦年を自動使用（例：2026年実行 → 2026） |

---

## 仕組み

```
scripts/fetch_reddit.py
  └─ old.reddit.com の JSON API へアクセス（認証不要）
       ├─ r/UI_Design  25件取得
       └─ r/UXDesign   25件取得
            ↓
       upvote数でランキング → TOP 10 選定
            ↓
       reports/[年]/[YYYYMMDD]/[HHmmss].md に保存
```

### fetch_reddit.py

`scripts/fetch_reddit.py` は Python 3 標準ライブラリのみで動作する Reddit 取得スクリプト。

```bash
python scripts/fetch_reddit.py <subreddit> <limit>

# 例
python scripts/fetch_reddit.py UI_Design 25
python scripts/fetch_reddit.py UXDesign 10
```

出力形式：

```
- [37pts] Landing page feedback
  https://old.reddit.com/r/UI_Design/comments/...
```

---

## レポートの保存先

```
reports/
└─ [調査年 or 直近]/
   └─ [YYYYMMDD]/
      └─ [HHmmss].md
```

例：

```
reports/
├─ 2026/
│  └─ 20260313/
│     └─ 143052.md
└─ 直近/
   └─ 20260313/
      └─ 175605.md
```

---

## 前提条件

- Python 3（標準ライブラリのみ。追加インストール不要）
- `scripts/fetch_reddit.py` がプロジェクトルートに存在すること
- Reddit API 認証は不要（`old.reddit.com` の公開 JSON エンドポイントを使用）

---

## ファイル構成

```
.
├─ README.md
├─ scripts/
│  └─ fetch_reddit.py        # Reddit 取得スクリプト
├─ reports/                  # 生成されたレポート（自動作成）
└─ .claude/
   └─ commands/
      └─ reddit-ui-research.md  # スキル定義
```
