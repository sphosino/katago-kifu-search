---
title: "開発記録"
---

# ログ一覧
[katago-kifu-search(github)](https://github.com/hosinobu/katago-kifu-search)  
以下に最新の勉強ログを表示します：

{% for post in site.posts %}
  * [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
