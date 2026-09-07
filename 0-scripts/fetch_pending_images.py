#!/usr/bin/env python3
"""
Downloads images the Tampermonkey script couldn't fetch client-side
(HackerRank's CDN 403s some cross-origin/hotlink requests from the browser,
and Manifest V3 extensions can no longer reliably override Referer to get
around that). This runs server-side in GitHub Actions instead, where a
plain Python request has no such header restriction.

Reads every JSON manifest under .pending-images/*.json, each a list of:
    {"url": "<image url>", "path": "<repo-relative destination path>"}

Each url is downloaded and written to path. A manifest file is deleted once
every entry in it succeeds. If some entries still fail (e.g. the CDN is
briefly down), those entries are kept and retried on the next push.
"""
import json
import os
import time
import urllib.error
import urllib.request

MANIFEST_DIR = ".pending-images"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; hackerrank-solutions-sync/1.0)",
    "Referer": "https://www.hackerrank.com/",
}


def download(url, dest_path, retries=3):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(dest_path, "wb") as f:
                f.write(data)
            print(f"  ok: {url} -> {dest_path} ({len(data)} bytes)")
            return True
        except urllib.error.HTTPError as e:
            print(f"  attempt {attempt}/{retries} failed ({e.code}): {url}")
        except Exception as e:
            print(f"  attempt {attempt}/{retries} failed ({e}): {url}")
        if attempt < retries:
            time.sleep(2 * attempt)
    return False


def main():
    if not os.path.isdir(MANIFEST_DIR):
        print("No .pending-images directory, nothing to do.")
        return

    manifest_files = sorted(
        os.path.join(MANIFEST_DIR, f)
        for f in os.listdir(MANIFEST_DIR)
        if f.endswith(".json")
    )
    if not manifest_files:
        print("No pending image manifests, nothing to do.")
        return

    print(f"Found {len(manifest_files)} pending manifest(s).")
    for mpath in manifest_files:
        with open(mpath) as f:
            entries = json.load(f)

        remaining = []
        for entry in entries:
            url = entry.get("url")
            path = entry.get("path")
            if not url or not path:
                continue
            print(f"Fetching {url}")
            if not download(url, path):
                remaining.append(entry)

        if remaining:
            print(f"  {len(remaining)} entr(y/ies) still pending in {mpath}; will retry next run.")
            with open(mpath, "w") as f:
                json.dump(remaining, f, indent=2)
        else:
            os.remove(mpath)
            print(f"  all images fetched, removed {mpath}")


if __name__ == "__main__":
    main()
