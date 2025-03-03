---
title: "開発記録"
layout: "default"
---
[katago-kifu-search(github)](https://github.com/hosinobu/katago-kifu-search)  
# ログ一覧

以下に最新のログを表示します：

{% for post in site.posts %}
  * [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}
