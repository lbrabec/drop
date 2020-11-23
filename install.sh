#!/usr/bin/env bash

DROPDIR=$(realpath `dirname $0`)
DESKTOPPATH="$HOME/.local/share/applications/Drop.desktop"
EXECPATH="$DROPDIR/drop.py"
ICONPATH="$DROPDIR/static/drop.svg"

cat <<EOF > $DESKTOPPATH
#!/usr/bin/env xdg-open
[Desktop Entry]
Type=Application
Name=Drop
Comment=Drop files from phone to computer
Exec=$EXECPATH
Icon=$ICONPATH
Terminal=false
EOF
