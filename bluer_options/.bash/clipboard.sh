#! /usr/bin/env bash

function bluer_ai_copy_to_clipboard() {
    local thing=$1

    if [ "$abcli_is_mac" == true ]; then
        echo $thing | pbcopy
    elif [ "$abcli_is_ubuntu" == true ]; then
        echo $thing | xclip -sel clip
    else
        bluer_ai_log_warning "cannot copy to clipboard."
        return 1
    fi
}
