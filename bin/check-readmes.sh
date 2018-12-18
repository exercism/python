#!/bin/bash

get_timestamp()
{
    path="$1"
    git log -n1 --pretty=format:%ct -- "$path"
}

ret=0
for exercise in $(ls -d exercises/*/); do
    meta_dir="${exercise}.meta"
    if [ -d "$meta_dir" ]; then
        meta_timestamp="$(get_timestamp "$meta_dir")"
        readme_timestamp="$(get_timestamp "${exercise}README.md")"
        if [ "$meta_timestamp" -gt "$readme_timestamp" ]; then
            ret=1
            echo "$(basename "$exercise"): .meta/ contents newer than README. Please regenerate it with configlet."
        fi
    fi
done

exit $ret
