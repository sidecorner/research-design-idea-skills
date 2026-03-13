# Reddit UI/UX リサーチスキル

r/UI_Design と r/UXDesign から高評価なアプリUI/UX事例を調査し、Markdownレポートとして出力する。

---

## 入力形式

ユーザーは以下のように指示する：
- 「2024年のUI/UXトレンドをRedditで調べてレポートにして」
- 「r/UI_Design から高評価のアプリをまとめて」
- 年号のみ（例：「2024」）

年号が指定された場合、その年の投稿を対象にする。指定がない場合は直近1年を対象にする。

---

## 実行ステップ

### Step 1: Reddit 投稿を検索して収集する

⚠️ **重要:** Redditは直接アクセス（`web_fetch`）できない場合が多い。以下の戦略を順番に試すこと。

#### 戦略A：Googleキャッシュ経由の検索（推奨・まず試す）

`web_search` で以下のようなクエリを実行する（年号を適宜置き換える）：

```
reddit r/UI_Design best app UI design [年号] upvotes comments
reddit r/UXDesign highly rated app UX [年号]
reddit.com/r/UI_Design [年号] app design top posts
reddit r/UXDesign [年号] award winning app interface
site:reddit.com r/UI_Design [年号] app
site:reddit.com r/UXDesign [年号] mobile UI
```

- 各サブレディットで **最低3クエリ** 実行し、合計20件以上の候補URLを収集する
- 検索結果のスニペットからupvote数・コメント数が読み取れる場合は記録する
- 受賞・特集された投稿（"Award", "Featured", "Best of" など）を優先する

#### 戦略B：Reddit投稿ページの取得を試みる

検索結果に `reddit.com/r/UI_Design/comments/...` 形式のURLが含まれる場合、`web_fetch` で取得を試みる。

- 取得できた場合：タイトル・upvote数・コメント内容・画像URLを抽出する
- 取得できない場合（403やブロックエラー）：検索結果のスニペット情報のみ使用する

#### 戦略C：外部キュレーションサイトの活用（A/Bで不足する場合）

以下のサイトも補助的に検索・取得する：
```
reddit UI design [年号] roundup OR "best of" OR highlights
r/UI_Design r/UXDesign [年号] annual summary top posts
```

- Mobbin、Dribbble、Awwwards などのデザイン系サイトで「Reddit話題作」として紹介されている事例も対象とする
- ただし情報源はReddit投稿を優先し、補助として使う

### Step 2: 各投稿・アプリ情報を抽出する

収集できた情報から以下を整理する：

- **アプリ名**（投稿タイトルやコメントから判断。不明な場合は「タイトルそのまま」）
- **アプリの概要**（何をするアプリか。1〜2文）
- **upvote数**（取得できた場合のみ。不明の場合「取得不可」と記載）
- **コメント数**（取得できた場合のみ）
- **投稿URL**（reddit.com の直リンク）
- **UI/UXの特徴・評価ポイント**（コメントや投稿文から抽出）
- **画像URL**（スクリーンショットが添付されている場合）

### Step 3: 上位10件を選定する

以下の優先順位でランキングする：
1. upvote数（高いほど優先）
2. 受賞・特集されているか
3. コメントの活発さ

上位10件を最終レポートの対象とする。

### Step 4: 各アプリの画像を取得する（可能な場合）

`image_search` ツールを使い、アプリ名で画像検索してスクリーンショットを補完する：

```
[アプリ名] app screenshot UI
[アプリ名] app design interface
```

Reddit投稿に直接画像がある場合はそちらを優先する。

### Step 5: Markdownレポートを生成して保存する

以下のフォーマットでMarkdownファイルを作成し、プロジェクトディレクトリ内の `reports/` フォルダに保存する。

**ファイル名形式：** `ui-ux-report-[調査年]-[調査実行日YYYYMMDD].md`

例：`ui-ux-report-2024-20260313.md`

---

## 出力フォーマット

```markdown
# Reddit UI/UX 高評価アプリ調査レポート

**調査対象年:** [年号]
**調査日:** [YYYY年MM月DD日]
**調査元:** r/UI_Design, r/UXDesign
**選定基準:** upvote数・受賞/特集実績

---

## 調査サマリー

- 収集した投稿数: XX件
- 最終選定: 10件
- upvote数合計（選定分）: XX,XXX

---

## 高評価 UI/UX アプリ TOP 10

### 1. [アプリ名]

| 項目 | 内容 |
|------|------|
| **アプリ概要** | [何をするアプリか1〜2文] |
| **upvote数** | [数値] |
| **コメント数** | [数値] |
| **Reddit投稿** | [URL] |
| **受賞・特集** | [あれば記載、なければ「-」] |

**UI/UXの特徴・評価ポイント:**
- [特徴1]
- [特徴2]
- [特徴3]

![スクリーンショット]([画像URL])

---

### 2. [アプリ名]
... (以下同様に10件まで)

---

## まとめ・トレンド考察

[調査年のUI/UXトレンドを3〜5文でまとめる]
```

---

## 注意事項

- Reddit APIではなく `web_search` + `web_fetch` を使って情報収集する
- upvote数が取得できない場合は「不明」と記載し、コメント数や受賞情報で補う
- アプリ名が不明な場合は投稿タイトルをそのまま使う
- 画像が取得できない場合はその項目を省略する（エラーにしない）
- レポートは **日本語** で作成する（アプリ名・URL・技術用語は英語のまま）
- 年号の指定がない場合は「直近1年」と明記する
