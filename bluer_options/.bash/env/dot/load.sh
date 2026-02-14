#! /usr/bin/env bash

function bluer_ai_env_dot_load() {
    local options=$1
    local plugin_name=$(bluer_ai_option "$options" plugin abcli)
    local suffix=$(bluer_ai_option "$options" suffix)
    local filename=$(bluer_ai_option "$options" filename .env)

    local path=$(dirname "$(realpath "${BASH_SOURCE[1]}")")$suffix

    if [[ ! -f "$path/$filename" ]]; then
        local use_ssm=$(bluer_ai_option_int "$options" ssm 0)
        if [[ "$use_ssm" == 1 ]]; then
            local module_name=$(bluer_ai_get_module_name_from_plugin $plugin_name)
            bluer_ai_ssm_get path=$path/$module_name
        else
            bluer_ai_log_warning "@env: dot: load: $path/$filename: file not found."
        fi
        return
    fi

    pushd $path >/dev/null

    local line
    local count=0
    for line in $(dotenv \
        --file $filename \
        list \
        --format shell); do

        export "$line"
        ((count++))
    done

    popd >/dev/null

    bluer_ai_log "@env: dot: load: $count var(s): $path/$filename"
}
