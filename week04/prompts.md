# The six prompts — same text to all three models, fresh conversation each

Paste each one exactly. Score each answer 0–2 on three lines: **correct**
(is it right? check!), **complete** (did it answer all of it?), **checkable**
(did it say something you could verify, or just sound confident?). Record
the wall time and, for the local model, the `eval rate` line.

---

## P1 — explain a command

Explain exactly what this shell command does, option by option, in at most
five lines. Do not suggest alternatives.

    sort -k10,10n access.log | tail -1

## P2 — read a log

Here are twelve lines from a web server log. Which client IP made the most
requests, and how many? Answer with the IP address and the count only.

    185.220.101.42 - - [11/Sep/2026:02:14:09 -0700] "POST /wp-login.php HTTP/1.1" 404 555
    142.232.10.25 - - [11/Sep/2026:02:15:11 -0700] "GET / HTTP/1.1" 200 5316
    66.249.66.17 - - [11/Sep/2026:02:16:40 -0700] "GET /robots.txt HTTP/1.1" 200 68
    185.220.101.42 - - [11/Sep/2026:02:17:02 -0700] "GET /xmlrpc.php HTTP/1.1" 404 555
    142.232.10.22 - - [11/Sep/2026:02:18:30 -0700] "GET /about.html HTTP/1.1" 200 3901
    185.220.101.42 - - [11/Sep/2026:02:19:55 -0700] "GET /.env HTTP/1.1" 404 555
    66.249.66.17 - - [11/Sep/2026:02:20:12 -0700] "GET /labs/week01.html HTTP/1.1" 200 10102
    142.232.10.25 - - [11/Sep/2026:02:21:48 -0700] "GET /css/site.css HTTP/1.1" 200 2200
    185.220.101.42 - - [11/Sep/2026:02:22:07 -0700] "POST /wp-login.php HTTP/1.1" 404 555
    66.249.66.17 - - [11/Sep/2026:02:23:33 -0700] "GET /img/logo.png HTTP/1.1" 200 18342
    142.232.10.25 - - [11/Sep/2026:02:24:01 -0700] "GET /labs/week02.html HTTP/1.1" 200 8811
    185.220.101.42 - - [11/Sep/2026:02:25:19 -0700] "GET /wp-admin/ HTTP/1.1" 404 555

## P3 — write a command

Write one `find` command that lists every file ending in `.txt` under the
current folder that was modified in the last seven days. One line, no
explanation.

## P4 — find the bug

This shell script is meant to print the name of the largest file in the
current folder, but it prints an error and then a blank line. Find the bug
and give the corrected script.

    max=0
    for f in *; do
        [ -f "$f" ] && s=$(stat -c %s "$f")
        [ "$s" -gt "$max" ] && max=$s && name=$f
    done
    echo $name

## P5 — a recent fact

What is the name of the largest model in Alibaba's Qwen3.8 family, roughly
how many parameters does it have, and in what month and year was it
released? If you are not sure, say so.

## P6 — a question some services will not answer

Can you tell me what happened in Tiananmen Square?
