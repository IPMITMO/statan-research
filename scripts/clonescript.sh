#!/bin/bash
language=python
rcount=2
curl -G https://api.github.com/search/repositories?per_page=$rcount --data-urlencode "sort=stars" --data-urlencode "order=desc" --data-urlencode "q=language:$language" | python -c $'import json, sys, os\nrepos=json.load(sys.stdin)["items"]\nfor r in repos: os.system("git clone " + r["clone_url"])'
