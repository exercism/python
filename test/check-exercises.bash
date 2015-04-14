#!/bin/bash 
#
# Runs all tests including skipped ones.
#
TEST_FILES=$(find . -name *_test.py)

for file in $TEST_FILES;
do
  EXERCISE_DIR=$(dirname $file)
  TEST_FILE=$(basename $file)
  EXAMPLE_FILE=$(echo $TEST_FILE | sed 's/_test//')

  pushd $EXERCISE_DIR  > /dev/null

  # Protect Resources.
  if [ -f $EXAMPLE_FILE ]
  then
    mv $EXAMPLE_FILE ${EXAMPLE_FILE}.orig
  fi

  # Test.
  cp example.py $EXAMPLE_FILE
  sed '/@unittest.skip/d' $TEST_FILE | python
  
  # Cleanup.
  rm $EXAMPLE_FILE

  if [ -f ${EXAMPLE_FILE}.orig ];
  then
    mv ${EXAMPLE_FILE}.orig ${EXAMPLE_FILE}
  fi
  popd > /dev/null
done
