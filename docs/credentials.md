# Credentials — read before any command

Three API keys were exposed in this project, each a different way. All revoked.
All avoidable.

- **In a photo.** `cat .env` prints the whole key; a photo of the terminal
  published it.
- **In the prefix.** Typing `ANTHROPIC_API_KEY=sk-ant-` and pasting the key on
  top produces a duplicated value that does not work, and exposes the value
  during editing.
- **In shell history.** Passing a key as an argument to `ssh` or `sed` writes
  the value into zsh history, which survives closing the window, goes into any
  export, and syncs to the cloud with it.

## Never

    cat .env
    ssh host "sed -i 's|KEY=.*|KEY=value|' file"
    export KEY=value
    photograph a screen with a credential value visible

## Always

    cut -c1-26 .env        verify the prefix, not the content
    ssh in and edit .env at the destination with nano
    .env in .gitignore BEFORE the key exists
    grep -c "sk-ant" before exporting, syncing or committing any log

## The general rule

Verify prefix and length, never content. If a command needs the credential
value as text, the command is wrong: the value goes somewhere you do not
control.

## Shell history is permanent

zsh keeps up to 1000 commands per session and flushes to `~/.zsh_sessions/`.
Everything typed is there, including what was later deleted from the file.
