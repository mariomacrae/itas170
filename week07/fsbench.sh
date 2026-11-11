#!/usr/bin/env bash
# fsbench.sh — time the same file workload in one place, append the result.
#
#   bash fsbench.sh LABEL DIRECTORY [FILES]
#
#   bash fsbench.sh ext4  ~                          # the Linux filesystem
#   bash fsbench.sh ntfs  /mnt/c/Users/$USER/bench   # Windows, over 9P (WSL)
#   bash fsbench.sh usb   /media/$USER/STICK/bench   # a FAT32 stick (Ubuntu)
#   bash fsbench.sh tmpfds /tmp/bench                 # RAM, as a control
#
# Five tests, each timed once, appended as rows to results.csv in the
# folder you ran it FROM (not the one you tested):
#
#   machine,label,fs,test,files,seconds
#
# Run it three times per place and take the median — one run is an
# anecdote. The workload is the shape of real developer work: many small
# files (create, read, delete), a git repository, and one big file.

set -u
if [ $# -lt 2 ]; then
    echo "usage: bash fsbench.sh LABEL DIRECTORY [FILES]" >&2
    exit 2
fi
label="$1"; base="$2"; N="${3:-2000}"
out="$PWD/results.csv"
machine="$(hostname)"
now() { date +%s%N; }
secs() { awk -v a="$1" -v b="$2" 'BEGIN { printf "%.2f", (b - a) / 1e9 }'; }
row() { echo "$machine,$label,$fs,$1,$N,$2" >> "$out"; printf '  %-9s %7s s\n' "$1" "$2"; }

mkdir -p "$base" || { echo "cannot create $base" >&2; exit 1; }
fs="$(df --output=fstype "$base" | tail -1 | tr -d ' ')"
d="$base/fsbench-$$"
rm -rf "$d"; mkdir -p "$d"; cd "$d" || exit 1
[ -f "$out" ] || echo "machine,label,fs,test,files,seconds" > "$out"
echo "== $label  $base  ($fs, $N files) =="

t0=$(now)
for i in $(seq 1 "$N"); do 
    f="dir$((i % 20))"; mkdir -p "$f"; printf 'line %s\n' "$i" > "$f/file$i.txt"
done
t1=$(now); row create "$(secs "$t0" "$t1")"

t0=$(now)
find . -type f -name '*.txt' -exec cat {} + > /dev/null
t1=$(now); row read "$(secs "$t0" "$t1")"

t0=$(now)
git init -q . && git add -A && \
    git -c user.name=bench -c user.email=bench@example.ca commit -qm init && \
    git status > /dev/null
t1=$(now); row git "$(secs "$t0" "$t1")"

t0=$(now)
dd if=/dev/zero of=big.bin bs=1M count=200 status=none && sync
t1=$(now); row big200MB "$(secs "$t0" "$t1")"

t0=$(now)
cd "$base" && rm -rf "$d"
t1=$(now); row delete "$(secs "$t0" "$t1")"
echo "  rows appended to $out"
