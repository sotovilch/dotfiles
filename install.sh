#!/usr/bin/env bash

DOTFILES_ROOT=$(pwd -P)

set -e

echo ""

info() {
	echo -e "\r  [ \033[00;34m..\033[0m ] $1"
}

user() {
	echo -e "\r  [ \033[0;33m??\033[0m ] $1"
}

success() {
	echo -e "\r\033[2K  [ \033[00;32mOK\033[0m ] $1"
}

fail() {
	echo -e "\r\033[2K  [\033[0;31mFAIL\033[0m] $1"
	echo ''
	exit
}

link_file() {
	local src=$1 dst=$2

	local overwrite= backup= skip=
	local action=

	if [ -f "$dst" -o -d "$dst" -o -L "$dst" ]; then

		if [ "$overwrite_all" == "false" ] && [ "$backup_all" == "false" ] && [ "$skip_all" == "false" ]; then

			local currentSrc="$(readlink $dst)"

			if [ "$currentSrc" == "$src" ]; then

				skip=true

			else

				user "File already exists: $dst ($(basename "$src")), what do you want to do?\n\
        [s]kip, [S]kip all, [o]verwrite, [O]verwrite all, [b]ackup, [B]ackup all?"
				read -n 1 action </dev/tty

				case "$action" in
				o)
					overwrite=true
					;;
				O)
					overwrite_all=true
					;;
				b)
					backup=true
					;;
				B)
					backup_all=true
					;;
				s)
					skip=true
					;;
				S)
					skip_all=true
					;;
				*) ;;
				esac

			fi

		fi

		overwrite=${overwrite:-$overwrite_all}
		backup=${backup:-$backup_all}
		skip=${skip:-$skip_all}

		if [ "$overwrite" == "true" ]; then
			rm -rf "$dst"
			success "removed $dst"
		fi

		if [ "$backup" == "true" ]; then
			mv "$dst" "${dst}.backup"
			success "moved $dst to ${dst}.backup"
		fi

		if [ "$skip" == "true" ]; then
			success "skipped $src"
		fi
	fi

	if [ "$skip" != "true" ]; then # "false" or empty
		ln -s "$1" "$2"
		success "linked $1 to $2"
	fi
}

install_dotfiles() {
	info 'installing dotfiles'

	local overwrite_all=false backup_all=false skip_all=false

	find -H "$DOTFILES_ROOT" -maxdepth 4 -name 'links.prop' -not -path '*.git*' | while read linkfile; do
		cat "$linkfile" | while read line; do
			if [ "$line" != "" ]; then
				local src dst dir
				src=$(eval echo "$line" | cut -d '=' -f 1)
				dst=$(eval echo "$line" | cut -d '=' -f 2)
				dir=$(dirname "$dst")

				mkdir -p "$dir"
				link_file "$src" "$dst"
			fi

		done
	done
}

install_dotfiles

echo ""
echo "  All installed!"
