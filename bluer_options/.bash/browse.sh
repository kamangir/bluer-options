#! /usr/bin/env bash

function bluer_ai_browse() {
    local url=$1

    local description=$2
    [[ ! -z "$description" ]] &&
        bluer_ai_log "$description"

    [[ -z "$url" ]] && return 0

    bluer_ai_log "🔗 $url"
    if [ "$abcli_is_mac" == true ]; then
        open "$url"
    elif [ "$abcli_is_ec2" == true ]; then
        firefox "$url"
    elif [ "$abcli_is_rpi" == true ]; then
        DISPLAY=:0 chromium-browser -kiosk --no-sandbox "$url"
    else
        bluer_ai_log_warning "@browse: $url: skipped."
    fi
}
