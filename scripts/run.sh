#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p target/classes target/test-classes
# The module entry point also works if a JDK has no javac launcher on PATH.
java com.sun.tools.javac.Main --release 17 -encoding UTF-8 -d target/classes src/daa/*.java
java com.sun.tools.javac.Main --release 17 -encoding UTF-8 -cp target/classes -d target/test-classes tests/daa/*.java
if [[ "${1:-demo}" == "test" ]]; then
    java -cp target/classes:target/test-classes daa.AlgorithmTests
else
    java -cp target/classes daa.Main "$@"
fi
