#! /usr/bin/env bash

function bluer_ai_env_backup() {
    local task=$1

    if [ "$task" == "list" ]; then
        bluer_objects_ls $abcli_path_env_backup
        return
    fi

    mkdir -pv $abcli_path_env_backup

    pushd $abcli_path_git >/dev/null
    local repo_name
    for repo_name in $(ls -d */); do
        repo_name=$(basename $repo_name)

        [[ -f $repo_name/.env ]] &&
            cp -v \
                $repo_name/.env \
                $abcli_path_env_backup/$repo_name.env
    done
    popd >/dev/null

    cp -v \
        "$HOME/Library/Application Support/Code/User/settings.json" \
        $abcli_path_env_backup/vscode-settings.json

    local thing
    for thing in ssh aws kaggle; do
        cp -rv \
            ~/.$thing \
            $abcli_path_env_backup/.$thing
    done

    cp -v \
        $ABCLI_PATH_IGNORE/*.pem \
        $abcli_path_env_backup

    bluer_ai_log "ℹ️ make sure $abcli_path_env_backup is synced with Google Drive."
}
