#! /usr/bin/env bash

function bluer_options() {
    local task=$1

    bluer_ai_generic_task \
        plugin=bluer_options,task=$task \
        "${@:2}"
}

function bluer_options_action_git_before_push() {
    [[ "$(bluer_ai_git get_branch)" != "main" ]] &&
        return 0

    bluer_options pypi build
}

python3 -m bluer_options version \
    --show_icon 1

function bluer_options_source_dependencies() {
    local path=$1

    source $path/options.sh
    source $path/source.sh

    source $path/assert.sh
    source $path/bool.sh
    source $path/browse.sh
    source $path/code.sh
    source $path/env.sh
    source $path/eval.sh
    source $path/generic_task.sh
    source $path/help.sh
    source $path/install.sh
    source $path/list.sh
    source $path/logging.sh
    source $path/open.sh
    source $path/pause.sh
    source $path/plugins.sh
    source $path/pylint.sh
    source $path/pytest.sh
    source $path/repeat.sh
    source $path/seed.sh
    source $path/sleep.sh
    source $path/string.sh
    source $path/terminal.sh
    source $path/test.sh
    source $path/wait.sh
    source $path/watch.sh

    source $path/alias.sh
}

bluer_options_source_dependencies $(dirname "$(realpath "${BASH_SOURCE[0]}")")
