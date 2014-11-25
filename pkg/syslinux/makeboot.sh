#!/bin/bash
# Author: Steven Shiau <steven _at_ nchc org tw>, Ceasar Sun <ceasar _at_ nchc org tw>
# License: GPL
# Description: Program to make USB flash drive (FAT, EXT, BTRFS , XFS or NTFS) bootable by syslinux or extlinux

# 1. Checking if partition table correct (on boundary, bootable)
# 2. cat mbr
# 3. "syslinux -f -i" or "extlinux -i"
#
# Append PATH
export PATH=/sbin:/usr/sbin:/bin:/usr/bin:$PATH

# Settings
ocs_batch_mode="false"

#
prog="$(basename $0)"
path_of_prog="$(LC_ALL=C cd "$(dirname "$0")/../../"; pwd)"

#
[ -z "$SETCOLOR_SUCCESS" ] && SETCOLOR_SUCCESS="echo -en \\033[1;32m"
[ -z "$SETCOLOR_FAILURE" ] && SETCOLOR_FAILURE="echo -en \\033[1;31m"
[ -z "$SETCOLOR_WARNING" ] && SETCOLOR_WARNING="echo -en \\033[1;33m"
[ -z "$SETCOLOR_NORMAL"  ] && SETCOLOR_NORMAL="echo -en \\033[0;39m"
BOOTUP="color"

#
msg_are_u_sure_u_want_to_continue='Are you sure you want to continue?'
msg_you_have_to_enter_yes_or_no="You have to enter 'y', 'yes', 'n' or 'no'. Please enter it again!"
msg_do_you_want_to_make_it_bootable="Do you want to mark it as bootable ?"

#
USAGE() {
   echo "$prog - To make the device bootable with syslinux"
   echo "Usage: $prog [OPTION] partition_device"
   echo "Options:"
   echo "-b, --batch-mode 	batch, unattended mode. Use carefully! DANGEROUS!!!"
   echo "-L, --LABEL STRING 	set device via LABEL if LABEL exists"
   echo "-U, --UUID STRING	set device via UUID"
   echo "Note:"
   echo "  Device assignment priority: Partition name > UUID > LABEL (if not only one NAME-TYPE is assigned)"
   echo "Ex:" 
   echo "To make \"/dev/sdg1\" bootable on GNU/Linux:"
   echo "  $prog /dev/sdg1"
   echo "To make device label \"LABEL_STRING\" bootable on GNU/Linux:"
   echo "  $prog -L LABEL_STRING" 
   echo "To make device with UUID \"UUID_STRING\" bootable on GNU/Linux:"
   echo "  $prog -U UUID_STRING"
}
# Check if root or not
check_if_root() {
   if [ ! "$UID" = "0" ]; then
     echo
     echo "[$LOGNAME] You need to run this script \"`basename $0`\" as root."
     echo
     exit 1
   fi
}
#
to_continue_or_not() {
  local prompt_msg="$1"
  continue_choice=""
  while [ -z "$continue_choice" ]; do
    [ "$BOOTUP" = "color" ] && $SETCOLOR_WARNING
    echo "$prompt_msg"
    [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
    echo -n "[y/n] "
    read continue_choice 
    case "$continue_choice" in
         y|Y|[yY][eE][sS])
            echo "OK! Let's do it!" ;;
         n|N|[nN][oO])
            echo "Program terminated!"
            exit 1
            ;;
         *)
            [ "$BOOTUP" = "color" ] && $SETCOLOR_WARNING
            echo "$msg_you_have_to_enter_yes_or_no!"
            [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
            echo "--------------------------------------------"
            ;;
    esac
  done
} # end of to_continue_or_not
#
get_diskname() {
  local disk=${1#/dev/*}

  if [ -n "$disk" ]; then
    echo "$disk" | sed -e 's/^\([^0-9]*\)[0-9]*$/\1/g' \
                       -e 's/^\(.*[0-9]\{1,\}\)p[0-9]\{1,\}$/\1/g'
  fi
} # end of get_diskname
#
get_part_number() {
  local disk=${1#/dev/*}
  local num=""

  if [ -n "$disk" ]; then
    num=$(echo "$disk" | sed -e 's/^[^0-9]*\([0-9]*\)$/\1/g' \
                             -e 's/^.*[0-9]\{1,\}\(p[0-9]\{1,\}\)$/\1/g')
  fi

  echo $num
} # end of get_part_number
#
check_if_syslinux_runs() {
  local sys_exec="$1"
  local rc
  # Check if the libc6-i386 (debian/ubuntu) files exists, which is required
  # for running 32-bit syslinux
  # E.g. On Debian AMD64 system without installing libc6-i386,
  #      $ ldd syslinux
  #      not a dynamic executable
  #      If libc6-i386 is installed:
  #      $ ldd syslinux
  #      linux-gate.so.1 =>  (0xf77dd000)
  #	    libc.so.6 => /lib32/libc.so.6 (0xf7661000)
  #	    /lib/ld-linux.so.2 (0xf77e0000)
  # It's easier we use "syslinux -h" to test if it runs:
  # $ ls -alFh ./syslinux
  # -rwxrwxr-x 1 steven steven 209K Oct  7 00:32 ./syslinux*
  # $ ./syslinux -h
  # bash: ./syslinux: No such file or directory
  # $ echo $?
  # 127
  # The above is the case which libc6-i386 is not installed, and the
  # return code is 127.
  if [ -z "$sys_exec" ]; then
    [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
    echo "Variable sys_exec was not assigned!"
    [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
    echo "Program terminated!"
    exit 1
  fi
  if [ ! -e "$sys_exec" ]; then
    [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
    echo "File \"$sys_exec\" does not exist!"
    [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
    echo "Program terminated!"
    exit 1
  fi
  $sys_exec -h 2>/dev/null >/dev/null
  rc=$?
  if [ "$rc" -ne 0 ]; then
   if [ "$(LC_ALL=C uname -m)" = "x86_64" ]; then
     [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
     echo "On x86-64 system, you should install libc6-i386 (for Debian/Ubuntu) or glibc.i686 (for Fedora/CentOS/OpenSuSE) package so that the required libraries to run 32-bit program $sys_exec exist."
     [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
     echo "Program terminated!"
     exit 1
   fi
  fi
} # end of check_if_syslinux_runs

#
export LANG=C

#
while [ $# -gt 0 ]; do
 case "$1" in
   -b|--batch) ocs_batch_mode="true"; shift;;
   -L|--LABLE) shift
           if [ -z "$(echo $1 |grep ^-.)" ]; then
             # skip the -xx option, in case 
	     target_part_label=$1
             shift;
           fi
           [ -z "$target_part_label" ] && USAGE && exit 1
           ;;
   -U|--UUID) shift
           if [ -z "$(echo $1 |grep ^-.)" ]; then
             # skip the -xx option, in case 
	     target_part_uuid=$1
             shift;
           fi
           [ -z "$target_part_uuid" ] && USAGE && exit 1
           ;;
   -*)     echo "${0}: ${1}: invalid option" >&2
           USAGE >& 2
           exit 2 ;;
   *)      break ;;
 esac
done

#
check_if_root
target_part="$1"

if ! type parted &>/dev/null; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo 'Program "parted" was not found on this GNU/Linux system. Please install it.'
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  echo "Program terminated!"
  exit 1
fi
if ! type blkid &>/dev/null; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo 'Program "blkid" was not found on this GNU/Linux system. Please install it.'
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  echo "Program terminated!"
  exit 1
fi

if [ -n "$target_part_label" -a -z "$target_part" ] ; then
  target_part_via_label="$(LC_ALL=C blkid | grep -iE "^/dev/[hsu][bd][a-z]+[[:digit:]]+.+LABEL=\"$target_part_label\".*" | grep -oE -w '^/dev/[hsu][bd][a-z]+[[:digit:]]+'| head -n 1)"
fi 

if [ -n "$target_part_uuid" -a -z "$target_part" ] ; then 
  target_part_via_uuid="$(LC_ALL=C blkid | grep -iE "^/dev/[hsu][bd][a-z]+[[:digit:]]+.+UUID=\"$target_part_uuid\".*" | grep -oE -w '^/dev/[hsu][bd][a-z]+[[:digit:]]+'| head -n 1)"
fi

if [ -z "$target_part" ] ; then 
  [ -z "$target_part_via_label" -a -n "$target_part_via_uuid" ] && target_part=$target_part_via_uuid
  [ -n "$target_part_via_label" -a -z "$target_part_via_uuid" ] && target_part=$target_part_via_label
  [ -n "$target_part_via_label" -a -n "$target_part_via_uuid" -a "$target_part_via_label" != "$target_part_via_uuid" ] && target_part=$target_part_via_uuid
fi

#
if [ -z "$target_part" ]; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo "No destination partition was assigned!"
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  USAGE
  exit 1
fi
# Make sure target_part is partition device name, not disk device name
if [ -z "$(echo $target_part | grep -iE "/dev/[hsu][bd][a-z]+[[:digit:]]+")" ]; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo "\"$target_part\" is NOT a valid partition name!"
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  USAGE
  exit 1
fi

#
pt_dev="$(basename $target_part)"  # e.g. sdc1
hd_dev="$(get_diskname $target_part)"   # e.g. sdc
target_disk="/dev/$hd_dev"  # e.g. /dev/sdc
pt_dev_no="$(get_part_number $target_part)"  # e.g. 1

# If the destination disk is not MBR partition table (e.g. it's GPT), exit. This program only works for MBR disk.
if [ -z "$(LC_ALL=C parted -s $target_disk print | grep -iE "^Partition Table:" | grep -iE "msdos")" ]; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo "The partition table of $target_disk is not for MBR (Master Boot Record). Its layout is:"
  LC_ALL=C parted -s $target_disk print
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  echo "This program is for making a bootable disk with MBR partition table."
  echo "For GPT disk, there is no need to run this program. Just make sure the partition is FAT32 with ID=ef00 and all the files are copied on that. That's all."
  echo "Program terminated!"
  exit 1
fi

# Get machine info:
on_this_machine=""
if type dmidecode &>/dev/null; then
  machine_name="$(LANG=C dmidecode -s system-product-name 2>/dev/null | head -n 1)"
  if [ -z "$machine_name" -o "$machine_name" = "To Be Filled By O.E.M." ]; then
    dev_model_shown="Unknown product name"
  else
    dev_model_shown="$machine_name"
  fi
fi
on_this_machine="on this machine \"$dev_model_shown\""

#
if ! grep -qEw $pt_dev /proc/partitions; then
  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
  echo "$target_part was NOT found!"
  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
  echo "Available disk(s) and partition(s) $on_this_machine :"
  echo "--------------------------------------------"
  cat /proc/partitions
  echo "--------------------------------------------"
  echo "Program terminated!"
  exit 1
fi

#
[ "$BOOTUP" = "color" ] && $SETCOLOR_WARNING
echo "This command will install MBR and syslinux bootloader on this machine"
[ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
echo "--------------------------------------------"
[ "$BOOTUP" = "color" ] && $SETCOLOR_WARNING
echo "Machine: $dev_model_shown:"
[ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
parted -s $target_disk print
echo "--------------------------------------------"

if [ "$ocs_batch_mode" = "false" ]; then
  to_continue_or_not "$msg_are_u_sure_u_want_to_continue"
  echo "--------------------------------------------"
fi

# 0. Check if partition is a FAT partition or NTFS partition
# parted -s /dev/hda1 print
# Disk /dev/hda1: 8590MB
# Sector size (logical/physical): 512B/512B
# Partition Table: loop
# 
# Number  Start   End     Size    File system  Flags
#  1      0.00kB  8590MB  8590MB  fat32           
# part_fs="$(LC_ALL=C parted -s $target_disk print | grep -E "^[[:space:]]*${pt_dev_no}\>" | awk -F" " '{print $6}')"
blkinfo="$(mktemp /tmp/blkinfo.XXXXXX)"
LC_ALL=C blkid -c /dev/null $target_part | grep -o -E '\<TYPE="[^[:space:]]*"($|[[:space:]]+)' > $blkinfo
TYPE=""
. $blkinfo

echo "File system of $target_part: $TYPE"
case "$TYPE" in
  fat16|fat32|vfat)    mode="syslinux";;
  ntfs|ext[2-4]|btrfs|xfs|ufs|ffs) mode="extlinux";;
  *)                   
     [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
     echo "$target_part: this doesn't look like a valid FAT, NTFS, ext2/3/4 or btrfs file system."
     [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
     echo "Program terminated!"
     exit 1
     ;;
esac

echo "--------------------------------------------"
# 1. Check if partition start/end on cylinder boundary
# //NOTE// This is not really required. Comment it on Sep/21/2010.
#if [ -n "$(LANG=C fdisk -l $target_disk | grep -iE "(not start on cylinder boundary|not end on cylinder boundary)")" ]; then
#  [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
#  echo "Some partition does not start or end on cylinder boundary! This disk will not be able to boot via syslinux!" 
#  [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
#  echo "Program terminated!"
#  exit 1
#fi

# 2. Bootable ?
bootable="$(LANG=C fdisk -l $target_disk | grep -Ew "^$target_part" | awk -F" " '{print $2}')"
if [ "$bootable" != "*" ]; then
  echo "$pt_dev is not marked as bootable! The partition table of $target_disk:"
  echo "--------------------------------------------"
  echo $dev_model_shown:
  parted -s $target_disk print
  echo "--------------------------------------------"
  if [ "$ocs_batch_mode" = "false" ]; then
    to_continue_or_not "$msg_do_you_want_to_make_it_bootable"
  fi
  echo "Running: parted -s $target_disk set $pt_dev_no boot on"
  parted -s $target_disk set $pt_dev_no boot on
  echo "--------------------------------------------"
fi

# 3. MBR
if [ "$ocs_batch_mode" = "false" ]; then
  to_continue_or_not "Do you want to install mbr on $target_disk $on_this_machine ?"
fi
echo Running: cat "$path_of_prog/utils/mbr/mbr.bin" > $target_disk
cat "$path_of_prog/utils/mbr/mbr.bin" > $target_disk

echo "--------------------------------------------"
# 4.
if [ "$ocs_batch_mode" = "false" ]; then
  to_continue_or_not "Do you want to install the SYSLINUX bootloader on $target_part $on_this_machine ?"
fi
# Since most of the cases when makeboot.sh is run, all the files are in FAT (USB flash drive normally uses FAT), we have to make syslinux executable.
#
# Check if $target_part is mounted or not
mnt_pnt="$(LC_ALL=C df $target_part | grep -Ew $target_part | awk -F" " '{print $6}')"
flag_mount=""
if [ -z "$mnt_pnt" ]; then
  # Not mounted. Mount it.
  destfs_tmpd="$(mktemp -d /tmp/destfs_tmpd.XXXXXX)"
  mount $target_part $destfs_tmpd
  rc=$?
  flag_mount="mounted"
else
  # Already mounted. 
  destfs_tmpd=$mnt_pnt
  rc=0
fi
# Create the syslinux in the destination partition
if [ $rc -eq 0 ]; then
  mkdir -p "$destfs_tmpd/syslinux"
fi

case "$mode" in
  syslinux)
     syslinux_tmpd="$(mktemp -d /tmp/syslinux_tmp.XXXXXX)"
     echo "A filesystem supporting Unix file mode for syslinux is required. Copying syslinux from FAT to /tmp/..."
     cp -fv "$path_of_prog/utils/linux/syslinux" $syslinux_tmpd
     chmod u+x $syslinux_tmpd/syslinux
     check_if_syslinux_runs "$syslinux_tmpd/syslinux"
     if [ $rc -eq 0 ]; then
       echo "Running: $syslinux_tmpd/syslinux -d syslinux -f -i $target_part "
       $syslinux_tmpd/syslinux -d syslinux -f -i $target_part
       s_rc="$?"
       if [ "$s_rc" -ne 0 ]; then
         [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
         echo "Failed to run syslinux!"
         [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
         echo "Program terminated!"
         exit 1
       fi
       echo "done!"
     else
       [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
       echo "Failed to mount FAT partition $target_part!"
       [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
       echo "Program terminated!"
       exit 1
     fi
     [ "$BOOTUP" = "color" ] && $SETCOLOR_WARNING
     echo "//NOTE// If your USB flash drive fails to boot (maybe buggy BIOS), try to use \"syslinux -d syslinux -fs $target_part\", i.e. running with \"-fs\"."
     [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
     if [ -d "$syslinux_tmpd" -a -n "$(echo $syslinux_tmpd | grep "syslinux_tmp" )" ]; then
       rm -rf $syslinux_tmpd
     fi
     ;;
  extlinux)
     extlinux_tmpd="$(mktemp -d /tmp/extlinux_tmp.XXXXXX)"
     echo "A filesystem supporting Unix file mode for extlinux is required. Copying extlinux from FAT to /tmp/..."
     cp -fv "$path_of_prog/utils/linux/extlinux" $extlinux_tmpd
     chmod u+x $extlinux_tmpd/extlinux
     check_if_syslinux_runs "$extlinux_tmpd/extlinux"
     if [ $rc -eq 0 ]; then
       echo "Running: $extlinux_tmpd/extlinux -i $destfs_tmpd/syslinux "
       $extlinux_tmpd/extlinux -i $destfs_tmpd/syslinux
       s_rc="$?"
       if [ "$s_rc" -ne 0 ]; then
         [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
         echo "Failed to run extlinux!"
         [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
         echo "Program terminated!"
         exit 1
       fi
       echo "done!"
     else
       [ "$BOOTUP" = "color" ] && $SETCOLOR_FAILURE
       echo "Failed to mount NTFS partition $target_part!"
       [ "$BOOTUP" = "color" ] && $SETCOLOR_NORMAL
       echo "Program terminated!"
       exit 1
     fi
     if [ -d "$extlinux_tmpd" -a -n "$(echo $extlinux_tmpd | grep "extlinux_tmp" )" ]; then
       rm -rf $extlinux_tmpd
     fi
     ;;
esac
#
if mountpoint $destfs_tmpd >/dev/null 2>&1; then
  if [ "$flag_mount" = "mounted" ]; then
    # mounted by this program. We unmount it.
    umount $destfs_tmpd
  fi
fi
if [ -d "$destfs_tmpd" -a -n "$(echo $destfs_tmpd | grep "destfs_tmpd" )" ]; then
  rm -rf $destfs_tmpd
fi
