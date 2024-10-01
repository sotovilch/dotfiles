FONT_NAME="FiraCode"
ZIP_NAME="$FONT_NAME.zip"
URL="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/$ZIP_NAME"
USER_FONT_DIR="$HOME/.local/share/fonts"
NERD_FONT_SUBDIR="$FONT_NAME"

info() {
	echo -e "\r  [ \033[00;34m..\033[0m ] $1"
}

success() {
	echo -e "\r\033[2K  [ \033[00;32mOK\033[0m ] $1"
}

fail() {
	echo -e "\r\033[2K  [\033[0;31mFAIL\033[0m] $1"
	echo ''
	exit
}

info "Download Nerd Font"

if [[ $(command -v curl) ]]; then
	curl -OL "$URL"
elif [[ $(command -v wget) ]]; then
	wget "$URL"
else
	fail "We cannont find curl or wget. Please install one of them."
	exit
fi
success "Downloaded $ZIP_NAME"

mkdir -p "$USER_FONT_DIR"
success "Created fonts directory: $USER_FONT_DIR"

info "Extracting font."
unzip "$ZIP_NAME" -d "$USER_FONT_DIR/$NERD_FONT_SUBDIR"
rm "$ZIP_NAME"

fc-cache -fv
success "Updated font cache."

echo ""
echo "  All installed!"
