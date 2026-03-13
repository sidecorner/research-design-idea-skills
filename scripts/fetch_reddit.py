import json, sys, urllib.request

def fetch_reddit(subreddit: str, limit: int = 15):
    url = f"https://old.reddit.com/r/{subreddit}/.json?limit={limit}"
    # User-Agent を設定しないと 403 Forbidden になる
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    for p in data["data"]["children"]:
        d = p["data"]
        print(f"- [{d['score']}pts] {d['title']}")
        print(f"  https://old.reddit.com{d['permalink']}")

if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else "UI_Design"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    fetch_reddit(subreddit, limit)