#!/bin/bash



echo -e "\n\n\n\n\n\n>>>STEP 1. Source library..."
cd `dirname $0`
_exec_path=`pwd`
export SCRIPT_LIB_PATH=$_exec_path/../lib
cd -
. $_exec_path/../lib/commonlib.sh
. $_exec_path/../test/testlib.sh
if [ $? -eq 0 ]; then
	echo -e "\n   >Source library succeeded."
else
	echo -e "\n   >Source library failed, exiting..."
	exit
fi

echo -e "\n\n\n\n\n\n>>>STEP 2. Initialize variables..."
Files1=(
	test_data/dat/,tst,will,655
	test_data/dat/,lnc,root,655
	test_data/dat/dao/,isk,user1,666
	test_data/dat/bwa/,si,user2,755
	test_data/dat/emk/,sa,user3,777
	test_data/dat/dao/ckp/,mine,user4,761
	test_data/dat/bwa/ckp/ion/,io,user5,750
	test_data/dat/bwa/ckp/ion/sof/,cik,user6,650
	test_data/dat/bwa/ckp/wam/osk/dak/,ain,user7,667
)
Files2=(
	test_data/zdat/,ztst,will,655
	test_data/zdat/,zlnc,root,655
	test_data/zdat/zdao/,zisk,user1,666
	test_data/zdat/zbwa/,zsi,user2,755
	test_data/zdat/zdatdata/zemk/,zsa,user3,777
	test_data/zdat/zdao/zckp/,zmine,user4,761
	test_data/zdat/zbwa/zckp/zion/,zio,user5,750
	test_data/zdat/zbwa/zckp/zion/zsof/,zcik,user6,650
	test_data/zdat/zbwa/zckp/zwam/zosk/zdak/,zain,user7,667
)

Tags=(
	Au,Gold,Metals
	Ag,Silver,Metals
	Cu,Copper,Metals
	C,Carbon,Non-metals
	N,Nitrogen,Non-metals
	# He,Helium,Inert gasses
	# Ne,Neon,Inert gasses
	# Ar,Argon,Inert gasses
	# Kr,Krypton,Inert gasses
	# Xe,Xenon,Inert gasses
	# Rn,Radon,Inert gasses
	# Og,Oganesson,Inert gasses
	Re,Red,Colors
	Or,Orange,Colors
	Ye,Yellow,Colors
	Gr,Green,Colors
	Bl,Blue,Colors
	Tr,Triangle,Shapes
	Ci,Circle,Shapes
	Sq,Square,Shapes
)

Actions=(CREATE ADD DELETE UPDATE QUERY)
for ((i=0; i < ${#Actions[@]}; i++)); do
	act_name=${Actions[i]}
	declare -r ${act_name}=$i
done
# echo ${Actions[$CREATE]}

_db_host=localhost
_db_port=3306
_db_user=root
_db_pwd=
_db_base=tag_base
# _sys_admin=lsfadmin
# _sec_admin=secadmin
# _aud_admin=audadmin
# _tr_group=tr_group
# _tr_user=tr_user
# _tr_user_log=tr_user_log
_log_time=`date "+%Y-%m-%d %H:%M:%S"`
_page_size=20

export DB_CONN="mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e "

echo -e "\n   >Intialize vars finished."

# ConcatWS WHERE TAG_NAME=\'Sn\' TAG_VAL=\'Tin\' _tag_type=\'Metals\'
# _tag_name=Sn
# _tag_value=Tin
# _tag_type=Metals
# GetTags "" "" "" "" TAG_NAME=\'Sn\' TAG_VAL=\'Tin\'
# GetTags "" "" TAG_ID HEX TAG_NAME=\'Sn\' TAG_VAL=\'Tin\' TAG_TYPE=\'Metals\'
# read


echo -e "\n\n\n\n\n\n>>>STEP 3. Initialize test data..."
InitialData "${Files1[*]}"
InitialData "${Files2[*]}"
echo -e "\n   >Intialize test data finished."



echo -e "\n\n\n\n\n\n>>>STEP 4. Initialize database..."
CreateDB $_db_base $_db_user $_db_pwd
InitialTags "${Tags[*]}"
InitialFiles "$_exec_path/test_data/dat/" "${Tags[*]}"
InitialFiles "$_exec_path/test_data/zdat/"
echo -e "\n   >Intialize database finished."



echo -e "\n\n\n\n\n\n>>>STEP 5. Start unit test..."
###################################################################
echo -e "\n\n\n>CASE 1.1: create a tag(name and value not duplicated, no tag type specified)."
_tag_name=F
_tag_value=Fluorine

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value
GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_value\'

_tag_record=`GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_value\'`
echo $_tag_record | grep $_tag_name | grep $_tag_value > /dev/null
Verify $? 0
###################################################################
echo -e "\n\n\n>CASE 1.2: create a tag(name and value not duplicated)."
_tag_name=N
_tag_value=Nitrogen
_tag_type=Non-metals

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type
GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_value\'

_tag_record=`GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_value\'`
echo $_tag_record | grep $_tag_name | grep $_tag_value > /dev/null
Verify $? 0
###################################################################
echo -e "\n\n\n>CASE 1.3: create a tag(name and value duplicated)."
_tag_name=Sn
_tag_value=Tin
_tag_type=Metals

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type > /dev/null
Verify $? 1
###################################################################
echo -e "\n\n\n>CASE 2.1: delete a tag."
_tag_name=Pu
_tag_value=Purple
_tag_type=Colors

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type

$SCRIPT_LIB_PATH/delete_tag.sh $_tag_name $_tag_value

_tag_record=`GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_value\'`
echo $_tag_record | grep $_tag_name | grep $_tag_value
Verify $? 1
###################################################################
echo -e "\n\n\n>CASE 3.1: update a tag(name and value not duplicated)."
_tag_name=O
_tag_value=Oxygen
_tag_type=Non-metals
_tag_new_value=Oxygen_mod

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type

$SCRIPT_LIB_PATH/update_tag.sh $_tag_name $_tag_value $_tag_new_value
GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_new_value\'

_tag_record=`GetTags "" "" TAG_NAME=\'$_tag_name\' TAG_VAL=\'$_tag_new_value\'`
echo $_tag_record | grep $_tag_name | grep $_tag_new_value > /dev/null
Verify $? 0
###################################################################
echo -e "\n\n\n>CASE 3.2: update a tag(name and value duplicated)."
_tag_name=Fe
_tag_value=Iron
_tag_type=Metals
_tag_new_value=Iron_mod

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_value $_tag_type

$SCRIPT_LIB_PATH/add_tag.sh $_tag_name $_tag_new_value $_tag_type

$SCRIPT_LIB_PATH/update_tag.sh $_tag_name $_tag_new_value $_tag_value > /dev/null
Verify $? 1
###################################################################
echo -e "\n\n\n>CASE 4.1: add a tag for a file."
_file_id=`GetFile "" "$_exec_path/test_data/dat/dao/ckp/1.mine" FILE_ID`
# echo $_file_id
_tag_name=F
_tag_value=Fluorine

GetFile $_file_id
_old_file_tags=`GetFile $_file_id "" FILE_TAGS`

$SCRIPT_LIB_PATH/add_file_tag.sh $_file_id $_tag_name $_tag_value

GetFile $_file_id

_new_file_tags=`GetFile $_file_id "" FILE_TAGS`
echo "Original file tags hex id: "$_old_file_tags
echo "Final file tags hex id: "$_new_file_tags
_tag_hex_id=`GetTagHexID $_tag_name $_tag_value`
echo "Added tag hex id: "$_tag_hex_id
echo $_new_file_tags | grep $_tag_hex_id > /dev/null
Verify $? 0
###################################################################
echo -e "\n\n\n>CASE 5.1: delete a tag for a file."
_file_id=`GetFile "" "$_exec_path/test_data/dat/bwa/ckp/wam/osk/dak/1.ain" FILE_ID`
# echo $_file_id
_tag_name=Re
_tag_value=Red


$SCRIPT_LIB_PATH/add_file_tag.sh $_file_id $_tag_name $_tag_value
GetFile $_file_id
_old_file_tags=`GetFile $_file_id "" FILE_TAGS`

$SCRIPT_LIB_PATH/delete_file_tag.sh $_file_id $_tag_name $_tag_value
GetFile $_file_id

_new_file_tags=`GetFile $_file_id "" FILE_TAGS`
echo $_new_file_tags
echo "Original file tags hex id: "$_old_file_tags
echo "Final file tags hex id: "$_new_file_tags
_tag_hex_id=`GetTagHexID $_tag_name $_tag_value`
echo "Deleted tag hex id: "$_tag_hex_id
echo $_new_file_tags | grep $_tag_hex_id > /dev/null
Verify $? 1
###################################################################
echo -e "\n\n\n>CASE 6.1: update a tag for a file."
_file_id=`GetFile "" "$_exec_path/test_data/zdat/zdao/zckp/1.zmine" FILE_ID`
# echo $_file_id
_tag_name=F
_tag_value=Fluorine
_tag_new_name=Re
_tag_new_value=Red

$SCRIPT_LIB_PATH/add_file_tag.sh $_file_id $_tag_name $_tag_value
GetFile $_file_id
_old_file_tags=`GetFile $_file_id "" FILE_TAGS`

$SCRIPT_LIB_PATH/update_file_tag.sh $_file_id $_tag_name $_tag_value $_tag_new_name $_tag_new_value
GetFile $_file_id

_new_file_tags=`GetFile $_file_id "" FILE_TAGS`
echo "Original file tags hex id: "$_old_file_tags
echo "Final file tags hex id: "$_new_file_tags
_tag_hex_id=`GetTagHexID $_tag_new_name $_tag_new_value`
echo "Updated tag hex id: "$_tag_hex_id
echo $_new_file_tags | grep $_tag_hex_id > /dev/null
Verify $? 0
###################################################################
echo -e "\n\n\n>CASE 7.1: query file tag action log."
_file_id=`GetFile "" "$_exec_path/test_data/dat/bwa/ckp/wam/osk/dak/3.ain" FILE_ID`
# echo $_file_id
_tag_name=N
_tag_value=Nitrogen
_tag_new_name=N_modified
_tag_new_value=Nitrogen_modified

GetLog

$SCRIPT_LIB_PATH/update_file_tag.sh $_file_id $_tag_name $_tag_value $_tag_new_name $_tag_new_value
$SCRIPT_LIB_PATH/delete_file_tag.sh $_file_id $_tag_new_name $_tag_new_value
$SCRIPT_LIB_PATH/add_file_tag.sh $_file_id $_tag_new_name $_tag_new_name
$SCRIPT_LIB_PATH/update_file_tag.sh $_file_id $_tag_new_name $_tag_new_value $_tag_name $_tag_value
$SCRIPT_LIB_PATH/delete_file_tag.sh $_file_id $_tag_new_name $_tag_new_name

GetLog

_record=`GetLog $_file_id`
echo $_record | grep UPDATE | grep DELETE > /dev/null
Verify $? 0
###################################################################