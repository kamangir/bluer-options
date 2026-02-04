#! /usr/bin/env bash

function bluer_ai_watch() {
    local options=$1
    local do_clear=$(bluer_ai_option_int "$options" clear 1)
    local count=$(bluer_ai_option "$options" count -1)
    local error=$(bluer_ai_option "$options" error none)

    local loop_count=0
    while true; do
        [[ "$do_clear" == 1 ]] && clear

        bluer_ai_eval "$@"
        local status="$?"
        [[ "$error" == until ]] && [[ $status -ne 0 ]] && return 1
        [[ "$error" == while ]] && [[ $status -eq 0 ]] && return 1

        loop_count=$((loop_count + 1))
        if [[ "$count" != -1 ]] &&
            [[ "$loop_count" -ge "$count" ]]; then
            break
        fi

        bluer_ai_sleep ,$options

        [[ "$do_clear" == 0 ]] && bluer_ai_hr
    done
}
