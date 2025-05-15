---
title: "レンダラ移行中のバグ"
date: 2025-05-15
layout: post
---

めっちゃ謎バグが起きて、かなり苦労した。
chatGPTさんのコードコピペで使ってたら大変なことになった。
関係ないオブジェクトのパラが他のオブジェクトに影響して混乱。

以下のコードrenderer.hspより [tag =>v1.9.0]
```hsp
#deffunc set_extra_param int id, int idx, str newval
	split draw_object_params(id), ",", tmp
	tmp(idx) = newval
	s = tmp(0)
	repeat stat - 1 //ここでlength(tmp)-1になっていた。
		s += "," + tmp(cnt+1)
	loop
	draw_object_params(id) = s
	return stat //length(tmp)

```

tmpのlengthじゃあおかしくなるわなｗｗｗｗ

そのオブジェクトのパラ数とは限らんから。

気づかずに喜んでコピペしてしまった。
