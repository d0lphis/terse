#!/bin/sh

# USAGE: run this script in container started from ide_img.sh, to install extensions for apps mounted from /usr/wks/por/



printf '\nCopy app shortcuts to desktop.\n'
cp /apps/* /home/pharo/Desktop/.

install_chrome_extension () {
  preferences_dir_path="/opt/google/chrome/extensions"
  pref_file_path="$preferences_dir_path/$1.json"
  upd_url="https://clients2.google.com/service/update2/crx"
  mkdir -p "preferences_dir_path"
  echo "{" > "$pref_file_path"
  echo " \"external_update_url\": \"$upd_url\"" >> "$pref_file_path"
  echo "}" >> "$pref_file_path"
  echo Added \""$pref_file_path"\" ["$2"]
}

printf '\nInstall Chrome extensions...\n'
install_chrome_extension "fmkadmapgofadopljbjfkapdkoienihi" "react dev tools"
install_chrome_extension "lkcagbfjnkomcinoddgooolagloogehp" "IBM Equal Access Accessibility Checker"

printf '\nAll installed Chrome extensions:\n'
for i in $(find /home/pharo/.config/google-chrome/Default/Extensions -name 'manifest.json'); do
  n=$(grep -hIr \"name $i | cut -f4 -d '"' | sort)
  u="https://chrome/google.com/extensions/details/"
  ue=$(basename $(dirname $(dirname $i)))
  printf "%~30s%s\n" "$n" "$u$ue"
done



printf '\nInstall Visual Studio extensions...\n'
#rm -rf /home/pharo/.config/Code /home/pharo/.vscode/extensions
vscodeBin=/usr/wks/por/visual-studio-code/code
su pharo -c "$vscodeBin" --install-extension ryu1kn.partial-diff"
su pharo -c "$vscodeBin" --install-extension valentjn.vscode-ltex"
su pharo -c "$vscodeBin" --install-extension Tobias-Faller.vt100-syntax-highlighting"
su pharo -c "$vscodeBin" --install-extension eamodio.gitlens"
su pharo -c "$vscodeBin" --install-extension ms-vscode.csharp"
su pharo -c "$vscodeBin" --install-extension firsttris.vscode-jest-runner"
printf '\nAll installed VSCode extensions:\n'
su pharo -c "$vscodeBin --list-extensions"
