---
title: "インクルード問題"
date: 2025-05-05
layout: post
---

hspのインクルードはそのファイル基準ではなく、一番最初に読み込まれたファイル基準だからかなり不便だ。
何かいい方法はないものだろうか。。。


追記：2025/05/06
 - root
    - common（このフォルダ内では全て他ファイルをadditionでインクルード）利用時は依存ファイル(addition)を確認して、呼び出し側からinclude
      - basic_mod1.hsp  
      - basic_mod2.hsp  
      - basic_mod3.hsp (using_basic_mod1)　#addition "basic_mod1.hsp"  
   - project1  
     - main.hsp (basic_mod.hspをインクルードする)  
     - basic_mod.hsp(実際に使用するcommon内ファイルをプロジェクトからの相対位置で纏めて記述）  
     - modules  
       - module1_in_project1  
       - module2_in_project1  
   - project2  
    
   - project3  

このパターンだとbasic_mod.hspのなかに  
#include "../common/basic_mod1.hsp"  
#include "../common/basic_mod3.hsp"  
と順番に記述する。

これで運用していこう
