# Worst Fix Ever: Funniest Commit Message
[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/maezageryan-del/worst-fix-ever-commit-message/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/maezageryan-del/worst-fix-ever-commit-message/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

One commit message for a bug fix that made everything worse. Entry for the
[make.fun bounty](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722).

## The entry

> fix: the 500 error by returning 200 instead — the page still fails, but successfully

84 characters. The repair does not fix the failure — it lies about it. The page still
fails; it just fails successfully now. No deletion, no login joke, no revert: the fix
is a lie about the symptom, which is a fresh angle in this field.

## How it works

`main.py` writes exactly that one line to `/output/entry.txt`
(`MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
