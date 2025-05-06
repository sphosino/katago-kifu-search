---
title: "インクルード問題"
date: 2025-05-05
layout: post
---

hspのインクルードはそのファイル基準ではなく、一番最初に読み込まれたファイル基準だからかなり不便だ。
何かいい方法はないものだろうか。。。

追記：
  一応
    root
    common（このフォルダ内のhspファイルは全てadditionで記述）
      basic_mod1.hsp
      basic_mod2.hsp
      basic_mod3.hsp (using_basic_mod1)　#addition "basic_mod1.hsp"
    project1
      main.hsp (basic_mod.hspをインクルードする)
      basic_mod.hsp(実際に使用するcommon内ファイルをプロジェクトからの相対位置で纏めて記述）
      modules
        module1_in_project1
        module2_in_project1
    project2
      ...
    project3
      ...

これが現状の結論！！
