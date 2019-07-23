#!/bin/bash

get_timestamp()
{
    path="$1"
    git log -n1 --pretty=format:%ct -- "$path"
}

ret=0

bin/generate_tests.py
if ! git diff --quiet; then
    ret=1
    echo "Generated tests do not match current templates. Please run bin/generate_test.py to resolve."
fi

for exercise in $(ls -d exercises/*/); do
    meta_dir="${exercise}.meta"
    hints_file="${meta_dir}/HINTS.md"
    if [ -f "$hints_file" ]; then
        hints_timestamp="$(get_timestamp "$hints_file")"
        readme_timestamp="$(get_timestamp "${exercise}README.md")"
        if [ "$hints_timestamp" -gt "$readme_timestamp" ]; then
            ret=1
            echo "$(basename "$exercise"): .meta/HINTS.md contents newer than README. Please regenerate README with configlet."
        fi
    fi
done

exit $ret
