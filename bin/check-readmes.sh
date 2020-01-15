#!/bin/bash

SPEC="${1:-spec}"

get_timestamp()
{
    path="$1"
    git log -n1 --pretty=format:%ct -- "$path"
}

ret=0
for exercise in $(ls -d exercises/*/); do
    exercise="${exercise%/}"
    slug="$(basename "$exercise")"
    meta_dir="${exercise}/.meta"
    hints_file="${meta_dir}/hints.md"
    readme="${exercise}/README.md"
    if [ -f "$hints_file" ]; then
        bin/configlet generate -p "$SPEC" -o "${slug}" .
        if ! git diff --quiet "${readme}"; then
            echo "$slug: README is out-of-date. Please regenerate README with configlet."
        else
            echo "$slug ok"
        fi
        git checkout -- "${readme}"
    fi
done

exit $ret
