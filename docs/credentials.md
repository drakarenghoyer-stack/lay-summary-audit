# Credentials — read before any command

Three API keys were exposed in this project, each a different way. All revoked.
All avoidable.

- **In a photo.** `cat .env` prints the whole key; a photo of the terminal
  published it.
- **In the prefix.** Typing `ANTHROPIC_API_KEY=sk-ant-` and pasting the key on
  top produces a duplicated value that does not work, and exposes the value
  during editing.
- **In a verification command.** Searching a tree for the secret's own pattern
  prints the secret. `grep -rn "sk-ant" .` reads .env and puts the key on the
  screen. The command written to check for exposure was itself the exposure.
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

## The structural fix: keep the key out of the project tree

The rules above are each a patch for one vector, and a fifth vector will exist.
The key now lives in `~/.zshrc` as an exported variable, and the project holds
no `.env` with a value in it. The Anthropic client reads the environment
directly. Nothing inside the repository can leak what the repository does not
contain, so grep, cat, a photograph and an accidental commit all find nothing.

Set it without the value ever reaching the screen or the history:

    read -s "k?key: " && echo "export ANTHROPIC_API_KEY=\"$k\"" >> ~/.zshrc && unset k

Verify by length and occurrence count, never by printing:

    echo ${#ANTHROPIC_API_KEY}
    grep -o "sk-ant" <<< "$ANTHROPIC_API_KEY" | wc -l

## The general rule

Verify prefix and length, never content. If a command needs the credential
value as text, the command is wrong: the value goes somewhere you do not
control.

## Shell history is permanent

zsh keeps up to 1000 commands per session and flushes to `~/.zsh_sessions/`.
Everything typed is there, including what was later deleted from the file.
