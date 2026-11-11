#!/usr/bin/env bash
# cleanup.sh — "tidy up a week folder"
#
# An assistant suggested this when asked to "clean up the temporary files in
# my week folder". It has NOT been reviewed. Part 4 runs it inside a
# container, on a COPY, so you can find out what it actually does without
# finding out the hard way.

# Editor backups and temp files
rm -f *~ *.tmp *.bak

# Old notes we probably don't need any more
rm -f *.txt *.md

echo "cleaned $(pwd)"
