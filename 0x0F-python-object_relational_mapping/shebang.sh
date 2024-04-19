#!/usr/bin/bash

#append the Shebang to all .py files in a directory
append_shebang() {
	local file="$1"
	if [[ ! -f "$file" ]]; then
		return 1
	fi
	if [[ ! "$file" =~ \.py$ ]]; then
		return 1
	fi
	if grep -q '^#!/usr/bin/python3' "$file"; then
		return 1
	fi
	cat format > "$file"
}

for file in $(find . -type f);do
	append_shebang "$file"
done
echo "*****"
