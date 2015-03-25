#!/bin/bash 

#Run all tests including skipped ones.
for file in $(find . -name *_test.py);
do
  dirname=$(dirname $file)
  basename=$(basename $file)

  pushd $dirname  > /dev/null
  example_file=$(grep -o '^from.*import.*' $basename |cut -f2 -d' ' | tail -1)
  if [[ -z $example_file ]] || [ __future__ == $example_file ] \
    || [ "unittest" == "$example_file" ]
  then
    example_file=$(echo $basename |cut -f1 -d'_')
  fi

  if [ -f ${example_file}.py ]
  then
    cp ${example_file}.py ${example_file}.py.orig
  fi

  cp example.py ${example_file}.py
  sed '/@unittest.skip/d' $(basename $file) | python
  rm ${example_file}.py

  if [ -f ${example_file}.py.orig ];
  then
    cp ${example_file}.py.orig ${example_file}.py
    rm ${example_file}.py.orig
  fi
  popd > /dev/null
done
