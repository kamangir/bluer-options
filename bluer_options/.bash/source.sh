#! /usr/bin/env bash

function bluer_ai_source_caller_suffix_path() {
    local suffix=$1

    local path=$(dirname "$(realpath "${BASH_SOURCE[1]}")")
    path=$path$suffix

    if [[ ! -d "$path" ]]; then
        bluer_ai_log_error "bluer_ai_source_caller_suffix_path: $path: path not found."
        return 1
    fi

    pushd $path >/dev/null

    local filename
    for filename in *.sh; do
        source $filename
    done

    popd >/dev/null
}
