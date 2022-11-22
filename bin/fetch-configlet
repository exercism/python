#!/usr/bin/env bash

# This file is a copy of the
# https://github.com/exercism/configlet/blob/main/scripts/fetch-configlet file.
# Please submit bugfixes/improvements to the above file to ensure that all tracks benefit from the changes.

set -eo pipefail

readonly LATEST='https://api.github.com/repos/exercism/configlet/releases/latest'

case "$(uname)" in
  Darwin*)   os='mac'     ;;
  Linux*)    os='linux'   ;;
  Windows*)  os='windows' ;;
  MINGW*)    os='windows' ;;
  MSYS_NT-*) os='windows' ;;
  *)         os='linux'   ;;
esac

case "${os}" in
  windows*) ext='zip' ;;
  *)        ext='tgz' ;;
esac

case "$(uname -m)" in
  *64*)  arch='64bit' ;;
  *686*) arch='32bit' ;;
  *386*) arch='32bit' ;;
  *)     arch='64bit' ;;
esac

curlopts=(
  --silent
  --show-error
  --fail
  --location
  --retry 3
)

if [[ -n "${GITHUB_TOKEN}" ]]; then
  curlopts+=(--header "authorization: Bearer ${GITHUB_TOKEN}")
fi

suffix="${os}-${arch}.${ext}"

get_download_url() {
  curl "${curlopts[@]}" --header 'Accept: application/vnd.github.v3+json' "${LATEST}" |
    grep "\"browser_download_url\": \".*/download/.*/configlet.*${suffix}\"$" |
    cut -d'"' -f4
}

main() {
  if [[ -d ./bin ]]; then
    output_dir="./bin"
  elif [[ $PWD == */bin ]]; then
    output_dir="$PWD"
  else
    echo "Error: no ./bin directory found. This script should be ran from a repo root." >&2
    return 1
  fi

  download_url="$(get_download_url)"
  output_path="${output_dir}/latest-configlet.${ext}"
  curl "${curlopts[@]}" --output "${output_path}" "${download_url}"

  case "${ext}" in
    *zip) unzip "${output_path}" -d "${output_dir}"   ;;
    *)    tar xzf "${output_path}" -C "${output_dir}" ;;
  esac

  rm -f "${output_path}"
}

main
