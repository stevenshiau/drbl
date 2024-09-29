Summary:        DRBL (Diskless Remote Boot in Linux) package.
Name:           drbl
Version:	5.3.7
Release:	drbl1
License:	GPL
Group:		Development/DRBL
Source0:	drbl-%{version}.tar.xz
URL:		http://drbl.org
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	perl, bash, dialog
Obsoletes:	drbl-gdm, drbl-script, drbl-setup, rh-netinstall, mdk-netinstall, woody-netinstall, memtest86, knoppix-terminalserver
%if 0%{?fedora} >= 37
BuildRequires:  make
%endif

%description
DRBL (Diskless Remote Boot in Linux).
Description:
DRBL provides a diskless or systemless environment for client machines. It works on Debian, Ubuntu, Mandriva, Red Hat, Fedora, CentOS and OpenSuSE. DRBL uses distributed hardware resources and makes it possible for clients to fully access local hardware. It also includes Clonezilla, a partition and disk cloning utility similar to Symantec Ghost(TM) or True Image(TM).
For more details, check http://drbl.org.

%prep
%setup -q -n drbl-%{version}

%build
make all

%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/

%clean
[ -d "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%post

%preun 

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/bin/*
/usr/share/drbl/*
/etc/drbl/*
/usr/share/gdm/themes/drbl-gdm/*

%changelog
* Sat Sep 29 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.7-drbl1
  * Update the language files about msg_mount_ramdisk.

* Wed Sep 25 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.6-drbl1
  * Removed wireless-tools from packages list for live system
    in drbl.conf.
    Package iw should have same function, which is already included
    in live system.
    Ref: https://bugs.launchpad.net/ubuntu/+source/wireless-tools/+bug/2075850

* Sat Sep 14 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.5-drbl1
  * drblpush: service enabled by systemd does not need to be enabled by
    update-rc.d.
  * Add support for DBN 12.5-12.7 and Ubuntu 22.04/24.04.

* Thu Sep 05 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.4-drbl1
  * drbl.conf: reiser4progs was removed from the packages list.

* Tue Aug 06 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.3-drbl1
  * Updated language files by adding "%" in msg_you_must_input_legal_filename.

* Mon Jun 24 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.2-drbl1
  * Removed package cpufrequtils from lists of live system.
    It's not in the Debian repo anymore.

* Wed Jun 12 2024 Steven Shiau <steven _at_ clonezilla org> 5.3.1-drbl1
  * dcs: enabled only when opentracker & ezio exist on the system.

* Mon Jun 10 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.38-drbl1
  * drbl.conf: add cryptsetup in PKG_TO_QUERY.
  * Merge pull request #31 from iamzhaohongxin/patch-1. Update zh_CN.UTF-8
  * Language file ca_ES was updated. Thanks to René Mérou.
  * Language file de_DE was updated. Thanks to Savi G and Michael Vinzenz.
  * Removed duplicated variables msg_ocs_param_ps & msg_ocs_onthefly_param_ps
    in language file en_US. Thanks to Станислав Большаков.

* Mon Apr 29 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.37-drbl1
  * Removed thin-provisioning-tools from packages list of clonezilla live
    due to it breaks the dependences.

* Thu Apr 18 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.36-drbl1
  * Remove package deborphan in live packages list.

* Tue Apr 16 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.35-drbl1
  * Added yq in the live packages list.
  * fix: improved get-nic-devs excludes device name, so that the device wlo1,
    for example, should be kept.

* Sun Apr 07 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.34-drbl1
  * Add powermgmt-base in packages list of ocs live.
  * drbl.conf: Use lz4 instead of liblz4-tool in packages list.

* Wed Mar 13 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.33-drbl1
  * drbl-functions: add support mmdebstrap checking.
  * make-rpm.sh & make-deb.sh: give exit code if script finishes in the end.

* Tue Mar 12 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.32-drbl1
  * Allow mmdebstrap to replace debootstrap in function
    create_live_required_debian_based_prompt of drbl-functions.

* Thu Feb 22 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.31-drbl1
  * Remove package dmraid from the list of gparted live in drbl.conf.

* Sat Jan 13 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.30-drbl1
  * drblsrv: Add an option to remove gnome-initial-setup for Debian.
    The corresponding language files were updated, too.

* Tue Jan 09 2024 Steven Shiau <steven _at_ clonezilla org> 5.2.29-drbl1
  * Language file hu_HU was updated. Thanks to Greg.

* Thu Dec 14 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.28-drbl1
  * A better mechanism learned from newer Debian to load unifont in Debian.

* Mon Dec 04 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.27-drbl1
  * drbl.conf: removed dmraid from required packages list of Clonezilla live.
    It does not exist in Debian Sid anymore.

* Thu Nov 02 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.26-drbl1
  * Language file ca_ES was updated. Thanks to René Mérou.

* Sat Oct 21 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.25-drbl1
  * Language file ja_JP was updated. Thanks to Akira Yoshiyama.

* Tue Oct 17 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.24-drbl1
  * Language file es_ES was updated. Thanks to Juan Ramón Martínez.
  * Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
  * Language files el_GR.UTF-8 & pl_PL were updated. Thanks to
    Stamatis Mavrogiorgis and Kris.
  * Language files de_DE & sk_SK were updated. Thanks to Michael Vinzenz &
    Ondrej Dzivy Balucha.
  * Language file tr_TR was updated. Thanks to Volkan Gezer.

* Thu Oct 05 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.23-drbl1
  * Add option "-edio" in the TUI wizard.
  * Update language files about direct IO descriptions.

* Fri Aug 18 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.22-drbl1
  * Since grub commands "linux/initrd" works for uEFI boot,
    no matter it's secure boot or not. Just use them,
    not using linuxefi/initrdefi.

* Sat Jul 29 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.21-drbl1
  * gen-grub-efi-nb-menu: failed to write menu for memtest86+.

* Fri Jul 28 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.20-drbl1
  * Some more cosmetic rewritting. Less verbose outputs.

* Thu Jul 27 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.19-drbl1
  * drbl.conf: set netinstall for Debian as bookworm.

* Fri Jul 21 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.18-drbl1
  * Add acpitool in live packages list.
  * Default to use -z9p in the expert mode as saving, too.

* Thu Jul 13 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.17-drbl1
  * Include vim instead of vim-tiny in the live system.
  * Default to use zstd (-z9p) in TUI as saving an img.

* Thu Jul 06 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.16-drbl1
  * Package mlocate was replaced by plocate in the
    live system packages list.

* Wed Jun 28 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.15-drbl1
  * Add package ntfs2btrfs in Clonezilla live packages list.

* Thu Jun 08 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.14-drbl1
  * drbl-functions: screen_not_blank honors the variable ocs_screen_blank.
    When ocs_screen_blank="no" is assigned in the boot parameters,
    it won't run.

* Thu Jun 08 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.13-drbl1
  * Add packages zfsutils-linux in the packages list of Clonezilla live.

* Wed May 18 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.12-drbl1
  * drbl-prepare-memtest: Adopt new file name for memtest86+ia32.*.
    It was emtest86+x32.*.

* Sun May 07 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.11-drbl1
  * Allow choosing NIC in lite server mode when multiple network cards exist.
    Thanks to Date Huang and Nate Carr for asking this.
    Ref: https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/6fedbfd6c3

* Tue Apr 18 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.10-drbl2
  * Update drbl.spec for better with rpm.
    Ref: https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/c870bcd449

* Tue Apr 18 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.10-drbl1
  * makeboot.sh: make it run only in x86 arch.

* Tue Apr 11 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.9-drbl1
  * Bug fixed: missed "\" for the next line in drbl-functions introduced in
    https://github.com/stevenshiau/drbl/pull/27/commits

* Mon Mar 27 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.8-drbl1
  * drbl.conf: add dvtm & dtach in live packages list.
  * Merge pull request #27 from kgeorgiy/master
    Bug: Invalid dialog options for '-p' option

* Sat Feb 25 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.7-drbl1

  * Bug fixed: drbl-sl should not modify grub's "--id", do not append
    ${SL_VER}. Just leave it as clonezilla-live-client. Program
    hide_reveal_grub_efi_ent needs it precisely.
    Thanks to Date Huang for reporting this issue.

* Wed Jan 25 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.6-drbl1
  * Show option "-j2" in the restoreparts menu, default off.

* Tue Jan 24 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.5-drbl1
  * drbl-sl: show live version in grub menu.

* Tue Jan 24 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.4-drbl1
  * Update language files about LUKS.

* Sun Jan 08 2023 Steven Shiau <steven _at_ clonezilla org> 5.2.3-drbl1
  * drbl-functions: add "--powersave off" in setterm of the function
    screen_not_blank.

* Fri Dec 30 2022 Steven Shiau <steven _at_ clonezilla org> 5.2.2-drbl1
  * dcs: swtich to detect opentracker, not ocs-bttrack anymore.

* Sat Dec 10 2022 Steven Shiau <steven _at_ clonezilla org> 5.2.1-drbl1
  * drbl-sl: make it work with memtest86+ v6 existing on the system. 
    Avoid the wrong assignment for Linux kernel.

* Sat Nov 26 2022 Steven Shiau <steven _at_ clonezilla org> 5.2.0-drbl1
  * Support memtest86+ v6 naming & mechanism.
    Memtest86+ v6.00 now supports legacy BIOS and uEFI booting.
    Both x86 and x86-64 are supported, too. In DRBl/Clonezilla
    we use shorter file name so that it works in FAT file system:
    memtest86+.bin -> mt86+x32.mbr
    memtest86+x32.bin -> mt86+x32.mbr
    memtest86+x32.efi -> mt86+x32.efi
    memtest86+x64.bin -> mt86+x64.mbr
    memtest86+x64.efi -> mt86+x64.efi

* Fri Oct 28 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.17-drbl1
  * Use OWNER:GROUP, not OWNER.GROUP in chown command.

* Sun Oct 23 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.16-drbl1
  * Language file sk_SK and ja_JP were updated. Thanks to Ondrej Dzivý Balucha
    and Akira Yoshiyama.

* Thu Oct 20 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.15-drbl1
  * Language file tr_TR was updated. Thanks to Volkan Gezer.

* Tue Oct 18 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.14-drbl1
  * Language files de_DE, el_GR.UTF-8, es_ES, fr_FR and pl_PL were updated.
    Thanks to Michael Vinzenz, Stamatis Mavrogiorgis, Juan Ramón Martínez,
    Jean-Francois Nifenecker and Kris.

* Tue Sep 27 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.13-drbl1
  * Update language files about -k0/-k1 in beginner mode of ocs-onthefly.

* Mon Sep 12 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.12-drbl1
  * Show option "-k0" and "-k1" in the restoring, beginner mode.
  * The command egrep was replaced by "grep -E" to avoid grep >= 3.8
    showing warnings.

* Sun Jul 24 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.11-drbl1
  * check_drbl_setup_space: more precise calculation based on the variable
    varlib_NOT_2_be_copied_2_each_client from drbl.conf.

* Mon Jul 04 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.10-drbl1
  * Include package ufw in live system.
  * Add option "-sfs" in the dialog menu. The corresponding language files
    were updated, too.
    Ref: https://github.com/stevenshiau/clonezilla/issues/71

* Sun Jun 12 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.9-drbl1
  * Add duf, duff and dfc in the live packages list.

* Thu May 26 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.8-drbl1
  * Update set_drbl_ocs_extra_param of drbl-functions, more reasonable.
    The corresponding changes to drbl-client-switch was done, too.

* Thu May 26 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.7-drbl1
  * Add the missing ngrep back in the packages list.

* Sun May 22 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.6-drbl1
  * Merge pull request #23 from yosshy/japanese
    Update Japanese translation. Thanks to Akira Yoshiyama.
  * Accidentally removed shc & uml-utilities in the packages list.
    Add them back.

* Sun May 22 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.5-drbl1
  * Update netinstall version for Fedora and OpenSUSE.

* Sat May 21 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.4-drbl1
  * Language files pl_PL and sk_SK were updated. Thanks to kris and
    Ondrej Dzivý Balucha.
  * Add ngrep in the packages list.

* Tue May 17 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.3-drbl1
  * Language file de_DE were updated. Thanks to Michael Vinzenz.
  * Add uml-utilities in live packages list.

* Thu May 12 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.2-drbl1
  * Update language files es_ES, hu_HU & fr_FR.
    Thanks to Juan Ramón Martínez, Greg and Jean-Francois Nifenecker.

* Tue May 10 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.1-drbl1
  * set_drbl_ocs_extra_param: OCS_PARAM_TMP is a global variable.
    No need to pass to function.

* Tue May 10 2022 Steven Shiau <steven _at_ clonezilla org> 5.1.0-drbl1
  * drbl-functions: add a function about using a dialog to ask if
    opening LUKS device.
  * Update language files about LUKS in TUI.

* Mon May 02 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.9-drbl1
  * Updated language files about opening LUKS or not.

* Fri Apr 22 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.8-drbl1
  * drbl-get-dnsserver: support using resolvctl to get DNS setting.
    This makes it work for Ubuntu 22.04.

* Mon Apr 18 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.7-drbl1
  * Updated language file ca_ES. Thanks to René Mérou.

* Tue Mar 29 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.6-drbl1
  * To make it consistent. Put "-k0" even it's in beginner mode for
    restoredisk in the dialog menu.

* Sun Mar 27 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.5-drbl1
  * Check option "exit" earlier in k-related options menu of dialog.

* Sun Mar 27 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.4-drbl1
  * Add the dummy option "-k0" for the dialog of creating partition
    in ocs-sr and ocs-onthefly. It's the same as default action.
    Just easier for us to explain.

* Sun Mar 13 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.3-drbl1
  * Remove s3ql from the packages list of Clonezilla live.

* Sat Mar 12 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.2-drbl1
  * Removed extra unnecessary Alias line in the following files:
    arm-wol.service, drbl-clients-nat.service, drblthincli.service, mkswapfile.service

* Mon Feb 14 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.1-drbl1
  * Add memtester and edac-utils in the packages list for Clonezilla live.

* Thu Feb 03 2022 Steven Shiau <steven _at_ clonezilla org> 5.0.0-drbl1
  * Update language files for the support of LUKS.
  * Add dtrx in the packages list for Clonezilla live.
  * Sync the version number with Clonezilla 5.

* Tue Jan 18 2022 Steven Shiau <steven _at_ clonezilla org> 4.6.7-drbl1
  * Program pixz was replaced by xz since using "-T 0" works the same.
    Hence the description was updated.

* Sun Jan 09 2022 Steven Shiau <steven _at_ clonezilla org> 4.6.6-drbl1
  * Add wavemon in the packages list.
  * Add language files el_GR.UTF-8. Thanks to Stamatis Mavrogiorgis.
  * Add Greek in the languages list.

* Thu Dec 30 2021 Steven Shiau <steven _at_ clonezilla org> 4.6.5-drbl1
  * Language file hu_HU updated. Thanks to Greg.
  * Update netinstall for fedora as 35.

* Mon Dec 27 2021 Steven Shiau <steven _at_ clonezilla org> 4.6.4-drbl1
  * Language files ca_ES, de_DE, es_ES, fr_FR, ja_JP, pl_PL and
    sk_SK were updated. Thanks to René Mérou, Michael Vinzenz,
    Juan Ramón Martínez, Akira Yoshiyama, Jean-Francois Nifenecker,
    Kris, and Ondrej Dzivý Balucha.

* Sun Dec 12 2021 Steven Shiau <steven _at_ clonezilla org> 4.6.3-drbl1
  * put_syslinux_makeboot_for_usb_flash of drbl-functions: 
    revert to use assigned version of syslinux.

* Mon Dec 06 2021 Steven Shiau <steven _at_ clonezilla org> 4.6.2-drbl1
  * Update language files.

* Sun Dec 05 2021 Steven Shiau <steven _at_ clonezilla org> 4.6.1-drbl1
  * Update language files about image volume size (msg_set_image_volume_size).
  * drbl.conf: Update netinstall dor Debian and Ubuntu.

* Sun Nov 21 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.16-drbl1
  * boot-local-efi.cfg: Improved to detect hd1, hd2...
    Thanks to Sung Cho for reporting this issue.
    Ref: https://sourceforge.net/p/clonezilla/bugs/371/

* Tue Nov 16 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.15-drbl1
  * Language files of sk_SK were updated. Thanks to Ondrej Dzivy Balucha.

* Sun Nov 14 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.14-drbl1
  * Japanese language files were updated.
    Thanks to Akira Yoshiyama.

* Wed Nov 10 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.13-drbl1
  * Language files de_DE, hu_HU, es_ES, fr_FR, pl_PL, tr_TR, were updated.
    Thanks to Michael Vinzenz, Greg., Jean-Francois Nifenecker,
    Juan Ramón Martínez, kris, and Volkan Gezer.

* Wed Nov 03 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.12-drbl1
  * Bug fixed: option "-j2" was missing in recovery-iso-zip mode.
    Thanks to Ek Han Heng for reporting this issue.
    Ref:
    https://sourceforge.net/p/clonezilla/discussion/Clonezilla_live/thread/9ffa31f838/

* Wed Oct 27 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.11-drbl1
  * Language files es_ES were updated. Thanks to Juan Ramón Martínez.

* Tue Oct 26 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.10-drbl1
  * Update language files about wired/wireless NIC.
  * Add packages openfortivpn & openconnect in the packages list of
    Clonezilla live.

* Mon Oct 25 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.9-drbl1
  * Update language files about wifi device.

* Thu Oct 21 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.8-drbl1
  * Clean unsupported ones in drbl/setup/files/
  * drblpush: modify the way to get most_related_ver_d, and update some
    comments.

* Tue Oct 19 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.7-drbl1
  * Clean unsupported DBN9.0 files. Update ocsd-rescue.service for DBN-TU.

* Tue Oct 19 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.6-drbl1
  * Bug fixed: "-z9p" was not shown in the save menu for beginner mode.

* Sun Oct 03 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.5-drbl1
  * Enable the option -z9p for Clonezilla SE beginner mode.

* Sun Oct 03 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.4-drbl1
  * Replace "which" with "command -v" in the script because "which"
    command is deprecated.

* Mon Sep 27 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.3-drbl1
  * deb-preconf-drbl was renamed as drbl-deb-preconf.
  * Bug fixed:
    drbl-deb-preconf should not be run again in drblsrv-offline. It only
    runs once at drblsrv.

* Sun Sep 26 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.2-drbl1
  * drbl-functions: add function check_url, and a better way to download
    earlier version of syslinux when the specified version does not
    exist at syslinux repository. Do not assign the versions of 
    syslinux-related pkgs in function put_syslinux_makeboot_for_usb_flash.

* Mon Sep 13 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.1-drbl1
  * Suppress the error message about "setterm -blank 0".

* Sun Aug 29 2021 Steven Shiau <steven _at_ clonezilla org> 4.5.0-drbl1
  * Sync the version number with that of Clonezilla. 

* Sat Aug 28 2021 Steven Shiau <steven _at_ clonezilla org> 4.4.2-drbl1
  * Update language files about reserved image names.
  * ocsd-rescue.service: do not use .include for Debian 10 since
    systemd .include directives are deprecated. Same as that for Debian 11.

* Fri Aug 27 2021 Steven Shiau <steven _at_ clonezilla org> 4.4.1-drbl1
  * drblsrv: /etc/default/nis is not created for newer nis package
    (version >= 4, from Debian 11 or Ubuntu 21.04) by using the option "-s"
    of deb-preconf-drbl.
  * deb-preconf-drbl: add option "-s" to set /etc/default/nis.
    By default /etc/default/nis is not created.

* Thu Aug 26 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.16-drbl1
  * Add support OCS for Debian 11 (Bullseye).
  * Improve makeboot64.bat: checking FAT file system
    Thanks to Geert-Jan Uijtdewilligen.
    Ref:
    https://sourceforge.net/p/clonezilla/support-requests/158/

* Thu Jul 22 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.15-drbl1
  * Update msg_press_space_to_mark_selection in the language files.

* Mon Jul 12 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.14-drbl1
  * Add vifm, ytree, and lfm in the packages list of Clonezilla/DRBL live.

* Fri Jul 09 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.13-drbl1
  * drbl.conf: add packages ncdu & ncdt in the packages list
    of clonezilla/drbl live.

* Mon Jul 05 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.12-drbl1
  * The option "-j2" (clone_hidden_data) should be only enabled
    by default only when it's restoredisk, not restoreparts.
    Ref: https://sourceforge.net/p/clonezilla/bugs/361/

* Mon Jun 21 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.11-drbl1
  * Add function clean_raid_metadata_in_disk in ocs-functions.
    Function clean_filesystem_header_in_partition is renamed as
    clean_filesystem_header_in_dev.
  * ocs-clean-part-fs is renamed as ocs-clean-disk-part-fs
  * debian/control: Depends on dmraid, wipefs

* Sun May 16 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.10-drbl1
  * Add support for Ubuntu 21.04. 

* Sun Apr 25 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.9-drbl1
  * drbl-get-dnsserver: improved for multiple NIC configured with DNS, 
    nameserver_sys can be like: '8.8.8.8 DNS Domain: ~.  8.8.8.8 DNS Domain: ~.'
    Hence we only put correct IPv4 address.
    Ref: https://groups.google.com/g/drbl/c/ebgoMdLIo9c

* Mon Apr 05 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.8-drbl1
  * Add b2sum in gen_CDG_checksums of drbl-functions.

* Sun Mar 21 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.7-drbl1
  * Add dir links for CentOS 7.7-7.9: CO7.7.1908, CO7.8.2003, CO7.9.2009.

* Tue Mar 16 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.6-drbl1
  * The option -sspt of ocs-sr was changed to -scpt so change it in TUI menu
    in drbl-functions and language files.
  * Update language files about types of block device.

* Tue Mar 09 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.5-drbl1
  * Add b2sum support for image chcksum and files in the file system.

* Sun Mar 07 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.4-drbl1
  * A typo was fixed:
    msg_continue_with_weired_partition_table ->
    msg_continue_with_weird_partition_table.

* Sun Mar 07 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.3-drbl1
  * Add -ssnf (--skip-set-netboot-first) in the dcs menu so that 
    the variable efi_netboot_1st_in_nvram in drbl-ocs.conf can be
    changed in the menu when running dcs.
  * Add -sspt (--skip-save-part-table) in the menu for ocs-sr and drbl-ocs.

* Tue Mar 02 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.2-drbl1
  * Include jq in Clonezilla/DRBL live:
    Thanks to Rumata Estorskiy for asking this:
    https://gitlab.com/stevenshiau/clonezilla/-/issues/57

* Sat Feb 20 2021 Steven Shiau <steven _at_ clonezilla org> 4.3.1-drbl1
  * Update the Clonezilla live arch in drblpush:
    Debian-based: i686, i686-pae, amd64
    Ubuntu-based: amd64
  * Update language files about CPU arch of clonezilla live in drblpush.
  * drbl-all-service: remove update-rc.d, use insserv only for Debian
    system.
  * Do not remove username=* in filter_cl_gp_boot_param of drbl-functions.

* Wed Feb 17 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.18-drbl1
  * zh_CN.UTF-8: Thanks Zhiqiang Zhang for updating.

* Tue Feb 16 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.17-drbl1
  * Comment "IPAPPEND 1" in generate-pxe-menu. It fails the live-boot
    when pxebooting a clonezilla/drbl live client.

* Wed Jan 20 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.16-drbl1
  * Update language files about fsck repository file system.

* Tue Jan 19 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.15-drbl1
  * drbl.conf: use exfatprogs instead of exfat-utils in the packages
    list of Clonezilla/DRBL live. Add it to GParted live, too.

* Mon Jan 18 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.14-drbl1
  * Fix a typo in the language file zh_TW.UTF-8.

* Mon Jan 18 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.13-drbl1
  * Update language files about fsck repository file system.

* Tue Jan 12 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.12-drbl1
  * Bug fixed: drbl-sl failed to support GParted live due to the default
    boot parameters are using aufs, not overlay. In addition, the
    function filter_cl_gp_boot_param in drbl-function should 
    support the format of $linux_cmd line in grub.cfg.

* Fri Jan 08 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.11-drbl1
  * Add virt-what in live packages list.

* Fri Jan 01 2021 Steven Shiau <steven _at_ clonezilla org> 4.2.10-drbl1
  * Update language files about samba protocol.

* Mon Dec 28 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.9-drbl1
  * Disable zz-dhclient in the initramfs on DRBL server.
    Ref:
    https://sourceforge.net/p/drbl/discussion/DRBL_for_Debian/thread/791b123348/
* Sat Dec 26 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.8-drbl1
  * Improve parse_cmdline_option to allow multiple "=" in a line, e.g.,
    ocs_live_run="ocs-sr -q2 -j2 -z1p -p poweroff savedisk autoname-wpfx=fox serialno=xyz
    Thanks to Christopher S for reporting this.
    Ref: https://sourceforge.net/p/clonezilla/support-requests/144/

* Fri Dec 25 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.7-drbl1
  * Add glances in the packages list of drbl/clonezilla live.

* Thu Dec 10 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.6-drbl1
  * Language file es_ES was updated. Thanks to Juan Ramón Martínez.

* Tue Dec 08 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.5-drbl1
  * Add more packages in DRBL/Clonezilla live packages list:
    vnstat iperf3

* Tue Dec 08 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.4-drbl1
  * Add more packages in DRBL/Clonezilla live packages list:
    ipv6calc atop usbtop bashtop python3-psutil

* Sun Nov 29 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.3-drbl1
  * Run grep and show 5 lines afterwards only in 
    get_latest_pkg_in_drbl_repository of drbl-functions.

* Sun Nov 29 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.2-drbl1
  * Add package f3 in Clonezilla/DRBL live.

* Sun Nov 22 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.1-drbl1
  * Remove hfsprogs from the default packages list in 
    DRBL/Clonezilla/GParted live since it's now in Debian non-free section.

* Wed Nov 18 2020 Steven Shiau <steven _at_ clonezilla org> 4.2.0-drbl1
  * mkswapfile: Use new name ocs-get-dev-info
  * Sync the version number with Clonezilla.

* Mon Nov 02 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.5-drbl1
  * Add scsitools blktool safecopy gpart to the packages list
    of clonezilla live.

* Thu Oct 29 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.4-drbl1
  * Update opensuse netinstall as 15.2 in drbl.conf.

* Sun Oct 25 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.3-drbl1
  * Bug fixed: ocsd-*.service was not corrected copied by drblpush.

* Sat Oct 24 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.2-drbl1
  * Update ocsd-rescue.service for Ubuntu 20.10 since it requires
    ExecStart. The original inclusion from rescue.service is not working
    anymore.

* Sat Oct 10 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.1-drbl1
  * ocs-onthefly: Update locales about net pipe program netcat and nuttcp.

* Fri Oct 09 2020 Steven Shiau <steven _at_ clonezilla org> 4.1.0-drbl1
  * Sync the option "-p" of ocs-onthefly with ocs-sr, it was "-pa" for
    ocs-onthefly.
    In addition, "-pa cmd" is now "-p true" when shown in dialog.
  * Update language files for updated ocs-onthefly:
    1. Default to use nuttcp.
    2. Use ocs-sr to save and restore pseudo image.

* Tue Sep 29 2020 Steven Shiau <steven _at_ clonezilla org> 4.0.2-drbl1
  * Update drbl.conf:
    Use package name netcat-traditional instead of the fuzzy name: netcat.
    Include uuid-runtime in the Clonezilla live.
    Add nuttcp to PKG_TO_QUERY.
    Update fedora_netinstall_ver as "32".

* Mon Sep 21 2020 Steven Shiau <steven _at_ clonezilla org> 4.0.1-drbl1
  * Add package uuid-runtime in Clonezilla/DRBL packages list.

* Fri Sep 18 2020 Steven Shiau <steven _at_ clonezilla org> 4.0.0-drbl1
  * Add more prompt about the function language_help_prompt_by_idx_no
    of drbl-functions.
  * Sync the version number to that of Clonezilla.

* Sun Sep 13 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.6-drbl1
  * Bug fixed: grub netboot host specific boot issue fixed. Thanks to Mark
    Wiese.
    Ref:
    https://sourceforge.net/p/drbl/discussion/DRBL_for_Debian/thread/6ad0214cc0

* Thu Sep 10 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.5-drbl1
  * Update language file about ocs-onthefly's -rvd option.

* Fri Sep 04 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.4-drbl1
  * Spain Language files were updated. Thanks to Juan Ramón Martínez.

* Mon Aug 17 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.3-drbl1
  * Bug fix: missing assignment for $linux_cmd and $initrd_cmd in the
    grub boot menu created by drbl-usb-netinstall.
  * Rename function output_netinstall_syslinux_pxelinux_menu as
    output_netinstall_boot_menu so its name can cover uefi netboot.

* Tue Aug 11 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.2-drbl1
  * Add the updated Korean language file. Thanks to Hyeonmin Oh.

* Sun Aug 09 2020 Steven Shiau <steven _at_ clonezilla org> 2.33.1-drbl1
  * Add Korean support. Thanks to Hyeonmin Oh and 박규민.

* Fri Jul 17 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.10-drbl1
  * Link pxelinux.0 as lpxelinux.0 in tftp root so that CentOS 7 can work in
    the new drbl config file.

* Fri Jul 03 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.9-drbl1
  * Export linux_cmd and initrd_cmd in grub.cfg, i.e., make them as global
    variables so that the submenu can use that, too.
    Thanks to Chuck for identifying this issue.
    Ref:
    https://sourceforge.net/p/clonezilla/discussion/Clonezilla_live/thread/a7b696d13e/

* Tue Jun 30 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.8-drbl1
  * Bug fixed: wrong commands for parsing $linux_cmd
  * Remove exfat-fuse from packages list. It will be added in run-time since
    Linux kernel 5.7 has a module to support exfat. No need to use fuse
    program for distribution using Linux kernel >= 5.7.

* Mon Jun 29 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.7-drbl1
  * A better mechanism to deal with linuxefi/initrdefi or linux/initrd in
    the grub config. This can avoid using that in the client of arm arch
    (for the future).

* Sun May 31 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.6-drbl1
  * drbl-sl: get the default boot parameters from grub.cfg instead of
    isolinux.cfg since we can locate it in more precise way.

* Fri May 29 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.5-drbl1
  * Make my email address consistent at clonezilla org for all the files.

* Fri May 29 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.4-drbl1
  * grub netboot cfg dir is now at /tftpboot/nbi_img/grub/,
    while for backward compatibility, we still link it to
    /tftpboot/nbi_img/grub-efi.cfg.

* Thu May 28 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.3-drbl1
  * Bug fixed: missing linuxefi module in drbl-gen-grub-efi-nb since
    we have used linuxefi/initrdefi in the grub config file.

* Wed May 27 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.2-drbl1
  * Bug fixed: the created grub menu by drbl-sl and the function
    output_netinstall_syslinux_pxelinux_menu of drbl-functions
    should use linuxefi/initrdefi, not linux/initrd.

* Wed May 27 2020 Steven Shiau <steven _at_ clonezilla org> 2.32.1-drbl1
  * drbl-gen-grub-efi-nb: grub-header.cfg is moved & can assign tftp server
    Move grub-header.cfg to grub.cfg so that it's more flexible.
    If tftp server is assigned for drbl-gen-grub-efi-nb, the IP address
    should be assigned to the menu created by gen-grub-efi-nb-menu.
  * gen-grub-efi-nb-menu: improve tftp & header file.
    1. Add -t|--tftp-server option for assigning the TFTP server.
    2. Move the grub-header.cfg from drbl-gen-grub-efi-nb so that it's more
    flexible.
    3. To avoid conflict with the patch of grub in CentOS/Fedora,
       for GRUB EFI NB MAC/IP config style, the netboot file is now like
       grub.cfg-drbl-00:50:56:01:01:01
       and
       grub.cfg-drbl-192.168.177.2
       not grub.cfg-01-* anymore.
    4. Use linuxefi/initrdefi instead of linux/initrd command in the grub
    config file.
  * dcs: bug - did not switch some client's mode.
  * Follow the change in gen-grub-efi-nb-menu, the grub command in the
    grub config file is now linuxefi/initrdefi instead of
    linux/initrd. Hence the corresponding functions have to be
    changed:
    add_opt_in_grub_efi_cfg_block
    remove_opt_in_grub_efi_cfg_block
  * ocswp-grub2.png: Make characters smaller.

* Fri May 22 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.11-drbl1
  * drbl.conf: add xen-tools in live packages list.

* Tue May 12 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.10-drbl1
  * The option -z5p was missing in the menu due to pxz was not replaced by
    pixz. Thanks to Darkyere for reporting this.
    Ref: https://sourceforge.net/p/clonezilla/bugs/344/

* Thu Apr 30 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.9-drbl1
  * Remove extra drbl-ocs command in unicast of dcs.
  * This release should be ready for Ubuntu 20.04 (Focal).

* Thu Apr 30 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.8-drbl1
  * Update INTERFACESv4 in get_dhcpd_interface. Avoid multicast service
    failure.

* Tue Apr 28 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.7-drbl1
  * Add netinstall for Ubuntu 20.04. Drop 19.10.

* Tue Apr 21 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.6-drbl1
  * Add scdaemon in the drbl/clonezilla packages list.
    Thanks to nurupo for suggesting this.

* Sun Apr 12 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.5-drbl1
    Support detecting more partition name in makeboot.sh. Thanks to
    mauromol for reporting this issue.
    Ref:
    https://sourceforge.net/p/clonezilla/discussion/Help/thread/4008506eeb

* Mon Apr 06 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.4-drbl1
  * Make the template dhcpd.conf generated by drblpush work for
    Raspberry Pi and Rockpro64.
  * Use INTERFACESv4 instead of INTERFACES for dhcpd since it's deprecated
    in Debian/Ubuntu's version.
  * Add pax in the packages list of Clonezilla live.

* Mon Mar 30 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.3-drbl1
  * Fix duplicated -z1p/-z9p dialog in expert mode. Thanks to
    ottokang _at gmail com for reporting this issue.

* Sat Mar 14 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.2-drbl1
  * No more including ufsutils in drbl/clonezilla live.
  * Add required variable PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_ARMHF_ONLY
    in drbl.conf.

* Tue Mar 10 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.1-drbl1
  * Replace pzstd by zstdmt, and add -z1p/-z9p in beginner mode. Thanks to
    Lord65 (lord5319 _at_ gmail com) for this idea.
    Ref: https://github.com/facebook/zstd/pull/1192#issuecomment-397599977

* Fri Mar 06 2020 Steven Shiau <steven _at_ clonezilla org> 2.31.0-drbl1
  * Removed pxz, move packages mbmon and vbetool to X86 and X86-64 sectors
    in drbl.conf.

* Mon Mar 02 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.33-drbl1
  * Add "-p cmd" option for these 2 functions in drbl-functions:
    ocs_sr_param_postaction_after_clone
    ocs_onthefly_param_postaction_after_clone

* Sun Mar 01 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.32-drbl1
  * Update language file ca_ES. Thanks to René Mérou.
  * Update the language file ja_JP. Thanks to Akira Yoshiyama.

* Mon Feb 24 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.31-drbl1
  * Update the language files tr_TR, hu_HU, it_IT, pl_PL.
    Thanks to Volkan, Greg, ski777000, and Gianfranco.
  * Update language file sk_SK. Thanks to ondrej dzivy balucha.
  * Update language file de_DE and fr_FR. Thanks to Michael and
    Jean-Francois.
  * Include packages nvme-cli and scrub in Clonezilla live.
    Thanks to Suncatcher for suggesting this.

* Mon Feb 17 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.30-drbl1
  * Update languge files es_ES. Thanks to Juan Ramón Martínez.

* Fri Jan 24 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.29-drbl1
  * To save space, include mtr-tiny instead of mtr in DRBL/Clonezilla live.

* Fri Jan 24 2020 Steven Shiau <steven _at_ clonezilla org> 2.30.28-drbl1
  * Add mtr dcfldd iotop to packages list of drbl/clonezilla live.
  * Bug fixed: "$#" not ""$?" in argument test of makeboot.sh.

* Thu Dec 26 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.27-drbl1
  * Add bluetooth related packages in DRBL/Clonezilla live packages list:
    bluetooth bluez bluez-tools
  * Check if mcopy exists in makeboot.sh. Thanks to Laurence Mitchell for
    reporting this.

* Sat Dec 07 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.26-drbl1
  * Fix the issue for setting up Ubuntu 19.10. Thanks to Spinage and
    bliard. Ref:
    https://sourceforge.net/p/drbl/discussion/DRBL_for_Debian/thread/33a8153d3d

* Tue Dec 03 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.25-drbl1
  * Update language files about zstd description.

* Tue Nov 19 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.24-drbl1
  * Remove archivemount from packages list of clonezilla live since:
    (1) It requires fuse v2 but now only fuse v3 is available in Debian Sid.
    (2) It's not used basically in Clonezilla live.

* Tue Nov 19 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.23-drbl1
  * Changes in the packages:
    Remove cloudfuse: it's not maintained for more than 4 years, 
    and fuse < 3 is not available in Debian Sid.
    Add s3ql in the packages list so that user can manually mount
    swift/S3 cloud storage.

* Wed Nov 13 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.22-drbl1
  * Update netinstall for fedora 31 and centos 8.

* Wed Nov 06 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.21-drbl1
  * Add tmux in the drbl/clonezilla live pkgs list.
  * Netinstall for Ubuntu is set as bionic and eoan.

* Wed Oct 23 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.20-drbl1
  * Update function parse_cmdline_option so that it can parse the
    boot parameter like ocs_repository from grub.
    Thanks to jeff.sadowski for reporting this issue.
    Ref:
    https://sourceforge.net/p/clonezilla/discussion/Help/thread/ebf65f9bdd/
  * Update Brazilian Portuguese translation. Thank to Rafael Fontenelle for
    updating that.
    Ref: https://gitlab.com/stevenshiau/drbl/merge_requests/13

* Tue Oct 15 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.19-drbl1
  * Update language files about playing sound.
  * Add music123 & sound-icons in the DRBL/Clonezilla packages list.

* Sat Sep 21 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.18-drbl1
  * Add packages mutt and telnet in DRBL/Clonezilla live.

* Sat Sep 07 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.17-drbl1
  * Separate PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf as
    PKG_FROM_DBN_WHICH_OCS_LIVE_MUST_HAVE and
    PKG_FROM_DBN_WHICH_OCS_LIVE_NICE_TO_HAVE
    so that it's easier to be used in other scenario, like for singularity.

* Tue Sep 03 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.16-drbl1
  * Separate pkg variables about x86 and x86-64 in drbl.conf:
    PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_X86_ONLY
    PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_X86_64_ONLY
  * Remove zfs-initramfs and zfsutils-linux from pkg list. They will be
    added by Ubuntu-based Clonezilla live when creating.

* Mon Sep 02 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.15-drbl1
  * Update language files about removing MBR partition table prompts.
  * Move packages zfsutils-linux and zfs-initramfs to amd64 only since it's
    not available on non-amd64 Ubuntu-based Clonezilla live.

* Sun Sep 01 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.14-drbl1
  * Remove zfs-fuse from package list in drbl.conf.

* Sun Sep 01 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.13-drbl1
  * Add packages zfsutils-linux and zfs-initramfs in clonezilla live.

* Mon Aug 26 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.12-drbl1
  * Add thin-provisioning-tools in drbl/clonezilla live packages list, and
    device-mapper-persistent-data in the PKG_TO_QUERY of drbl.conf.
    Thanks to Tseng Wynn (wynn1212 _at_ gmail com) for reporting this bug.
  * Fix typo in zh_TW.UTF-8. Thanks to Chih-Hsuan Yen:
    https://gitlab.com/stevenshiau/drbl/merge_requests/12

* Fri Aug 16 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.11-drbl1
  * Update the mechanism to get bs and comments in drbl-aoe-img-dump

* Tue Aug 13 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.10-drbl1
  * Update language files for input checking related.

* Mon Aug 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.9-drbl1
  * Bug fixed: make sure the syslinux-related files are from same version of
    syslinux packages.

* Mon Aug 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.8-drbl1
  * Update language files for msg_disk_is_full_or_permission_issue.
  * Improvem the mechanism for putting syslinux and extlinux in x64/{syslinux,extlinux} of live system.

* Sun Jul 21 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.7-drbl1
  * Separate 32-bit and 64-bit syslinux when running makeboot.sh
    Thanks to Martin Mokrejs for reporting this issue.
    Ref: https://sourceforge.net/p/clonezilla/bugs/326/

* Thu Jul 18 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.6-drbl1
  * Add the option -iui to the drbl-ocs dialog menu.
    Update language files for the option "-iui".

* Fri Jul 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.5-drbl1
  * Use soft link for CO7.x and RH7.x in /usr/share/drbl/setup/files/RH.

* Fri Jul 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.4-drbl1
  * Bug fixed: Stop mkswapfile service before starting ocsd-run in clients
    for CentOS 7.x.
  * Remove CO5*, add CO7.6.1810 in /usr/share/drbl/setup/files/RH/.

* Fri Jul 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.3-drbl1
    Bug fixed: uEFI boot menu for drbl client was overwritten by wrong
    command in function output_netinstall_syslinux_pxelinux_menu of
    drbl-functions.

* Fri Jul 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.2-drbl1
  * Update prompt about secure netboot for uEFI in drbl-gen-grub-efi-nb.

* Fri Jul 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.30.1-drbl1
  * Support Debian Buster (10.0).
  * Make drbl-syslinux-netinstall use grub for uEFI booting. 
    Rename drbl-syslinux-netinstall as drbl-usb-netinstall,
    while there is still a link for drbl-usb-netinstall to
    drbl-syslinux-netinstall.

* Fri Jul 05 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.11-drbl1
  * Ecryptfs-utils & partimage are not required for DRBL. It's better to
    have that, but not required. This is due to they are removed from Debian
    Buster.

* Mon Jun 03 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.10-drbl1
  * Shift the uEFI boot order.

* Wed May 29 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.9-drbl1
  * Install the required grub module efifwsetup
    before running fwsetup.

* Wed May 29 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.8-drbl1
  * Add uEFI firmware setup menu when running gen-grub-efi-nb-menu

* Fri May 24 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.7-drbl1
  * File ca_ES was updated. Thanks to René Mérou.

* Tue May 21 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.6-drbl1
  * Update language files es_ES and it_IT. Thanks to
    Juan Ramón Martínez and gf.gentili.

* Fri May 17 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.5-drbl1
  * Integrated backup plan in boot-local-efi.cfg. Hence the regexp
    issue in Ubuntu's grub2 can be workarounded.
    Ref: https://bugs.launchpad.net/bugs/1829331

* Thu May 16 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.4-drbl1
  * Add backup plan in case boot-local-efi.cfg fails, since there is
    a bug in Ubuntu's grub commands, including regexp, probe...:
    https://bugs.launchpad.net/bugs/1829331
  * Update language files: de_DE, fr_FR, hu_HU, ja_JP, pl_PL, tr_TR.
    Thanks to Greg, Jean-Francois, Kris, Michael, Volkan, Akira.

* Wed May 08 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.3-drbl1
  * Use boot-local-efi.cfg in gen-grub-efi-nb-menu.

* Wed May 08 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.2-drbl1
  * Add new file boot-local-efi.cfg for booting uEFI local OS.
  * Remove variable LOCAL_EFI_BOOT_GRUB_CFG from drbl-functions.

* Tue May 07 2019 Steven Shiau <steven _at_ clonezilla org> 2.29.1-drbl1
  * Support Ubuntu 19.04.

* Mon Apr 29 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.21-drbl1
  * Include package rdfind in Clonezilla live.

* Mon Apr 08 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.20-drbl1
  * Add package vbetool for Clonezilla live.
    Ref: https://sourceforge.net/p/clonezilla/bugs/321/

* Thu Mar 28 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.19-drbl1
  * Include package mbmon in Clonezilla live.

* Sun Mar 03 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.18-drbl1
  * Add missing variables for language file es_ES.

* Wed Feb 20 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.17-drbl1
  * Bug fixed: drbl-client-service failed for systemd service.
    Thanks to Dr. Yu from NCTU for reporting this issue.

* Tue Feb 19 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.16-drbl1
  * Optimization for Ubuntu 18.04:
    Add systemd-timesyncd in client_services_chklist, man in
    varcache_2_be_copied_2_common_root, and
    snapd in varlib_NOT_2_be_copied_2_each_client
    Thanks to Prof. Yu from NCTU for these suggestions.

* Wed Jan 23 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.15-drbl1
  * Typos in language file zh_TW.UTF-8 were fixed. 

* Wed Jan 16 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.14-drbl1
  * Update language files for ocs-onthefly.

* Sun Jan 13 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.13-drbl1
  * Typo fixed in the USAGE of get-all-nic-ip.
  * Add nuttcp in Clonezilla live packages list.

* Sat Jan 12 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.12-drbl1
  * Update language files about RAM disk in prep-ocsroot.

* Fri Jan 11 2019 Steven Shiau <steven _at_ clonezilla org> 2.28.11-drbl1
  * Update language files required for BT deployment from source device. 

* Wed Dec 19 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.10-drbl1
  * Adding support for Debian 9.5 and 9.6. This release should be ready for
    Ubuntu 18.10, except the DM should be changed to lightdm instead of gdm3.

* Sun Nov 18 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.9-drbl1
  * Update netinstall in drbl.conf.

* Wed Oct 10 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.8-drbl1
  * Clean client's netplan file that are copied from server. Thanks to
    Robert Arkiletian for reporting that.

* Tue Oct 02 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.7-drbl1
  * Add ldmtool to packages list of Clonezilla live.

* Sat Sep 29 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.6-drbl1
  * Add network-manager to packages list of Clonezilla live so that user
    can use nmtui to configure network if it's necessary, especially
    for wifi.

* Wed Sep 26 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.5-drbl1
  * Minor update for language files. 

* Tue Sep 25 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.4-drbl1
  * Variable secure_boot in the programs was renamed to secure_boot_client.
  * Move curl to PKG_FROM_DBN_MINIMAL_NEED from PKG_FROM_DBN in drbl.conf,
    so now curl will be included in Clonezilla live.

* Fri Sep 14 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.3-drbl1
  * Make variable secure_boot to be global, hence it's moved to drbl.conf
    from drbl-gen-grub-efi-nb. Hence both drbl-gen-grub-efi-nb and drblpush
    will use the same setting. By default secure_boot is not enabled due to
    this issue for secure grub boot loader:
    https://lists.gnu.org/archive/html/grub-devel/2016-04/msg00051.html
    It can be enabled in the future if it's patched in the upstream.

* Wed Sep 12 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.2-drbl1
  * Add a workaround to support uEFI secure netboot.
    To enable uEFI network secure boot for clients, use
    standalone DHCP service in Clonezilla lite server
   (Ubuntu-based), not relaying to the existing DHCP service.

* Tue Sep 11 2018 Steven Shiau <steven _at_ clonezilla org> 2.28.1-drbl1
  * Make uEFI secure netboot work on Ubuntu system.

* Wed Sep 05 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.9-drbl1
  * Bug fixed: Varible node_root should be node_rt in function
    disable_lvm2_udevd_rules. Thanks to vicamo for reporting. 
    Ref: https://github.com/stevenshiau/drbl/pull/14

* Tue Sep 04 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.8-drbl1
  * Skip copying /var/lib/lxcfs to drbl clients.

* Sun Aug 19 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.7-drbl1
  * Make makeboot.sh work if dmidecode is not installed.
    Thanks to Clemmitt Sigler for reporting this issue.
    Ref: https://sourceforge.net/p/clonezilla/bugs/302/

* Fri Jul 20 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.6-drbl1
  * Test to see if pxelinux.0 or lpxelinux.0 should be used in drbl.conf.

* Thu Jul 12 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.5-drbl1
  * Language file ca_ES was updated. Thanks to René Mérou.

* Wed Jun 06 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.4-drbl1
  *  Add bind-interfaces for dnsmasq.conf in the function gen_dnsmasq_cfg.
     This will make dnsmasq work with the stub resolver without conflicting.
     Otherwise dnsmasq won't start.
     Ref: https://github.com/systemd/systemd/pull/4061

* Thu May 24 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.3-drbl1
  * Package name btrfs-tools was replaced by btrfs-progs in Debian and Ubuntu.

* Fri May 18 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.2-drbl1
  * New a variable drbl_client_debian_exclude_kernels in drbl.conf so that
    seldom_kernel_filter in drblsrv can use that.

* Thu May 17 2018 Steven Shiau <steven _at_ clonezilla org> 2.27.1-drbl1
  * Initial support for Ubuntu 18.04. Thanks to Robert Arkiletian.

* Mon May 07 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.26-drbl1
  * Add Polish language files. Thanks to kris <ski777000 _at_ gmail com>.

* Mon Apr 23 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.25-drbl1
  * Add ipmitool to clonezilla live packages list.

* Fri Mar 30 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.24-drbl1
  * Better way to check clonezilla live iso or zip in drbl-sl.

* Wed Mar 28 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.23-drbl1
  * Bug fixed: failed to correctly detect iso file in drbl-sl.

* Wed Mar 21 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.22-drbl1
  * Switch keymap configuration method from console-data to
    keyboard-configuration.
    Ref:
    https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=570223
    https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=893612

* Sun Mar 18 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.21-drbl1
  * Bug fixed: When netowrk eth0 is configured, config_drbl_live_network
    failed to start virtual NIC drbl0.

* Tue Mar 13 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.20-drbl1
  * Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
  * Language file tr_TR updated. Thanks to Volkan Gezer.

* Fri Mar 09 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.19-drbl1
  * Update language files de_DE, es_ES, fr_FR, hu_HU, it_IT and sk_SK.
    Thanks to Michael Vinzenz, Juan Ramón Martínez, Jean-Francois Nifenecker,
    Greg Hefty, Gianfranco Gentili, and Ondrej Dzivy Balucha.

* Tue Mar 06 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.18-drbl1
  * Update language files for new prompt in ocs-live-feed-img.

* Sat Mar 03 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.17-drbl1
  * Add grub2-efi-x64-modules and grub2-efi-ia32-modules in PKG_TO_QUERY of drbl.conf.
    Due to CentOS 7.4 has separated grub2-efi-modules as grub2-efi-x64-modules and
    grub2-efi-ia32-modules.

* Thu Feb 22 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.16-drbl1
  * Add those known ARM64 EFI boot files in LOCAL_EFI_BOOT_GRUB_CFG
    of drbl-functions.

* Fri Feb 09 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.15-drbl1
  * Let plymouth run in drbl client of Ubuntu 14.04 so that lightdm can
    start.
  * Better way to deal with update-rc.d and chpasswd in chroot.

* Tue Jan 30 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.14-drbl1
  * Use iproute2 instead of iproute for Debian-based clonezilla live.

* Tue Jan 09 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.13-drbl1
  * Update language files for channel bonding usage.

* Sun Jan 07 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.12-drbl1
  * Typo fixed: repositry -> repository, in "Directory Browser for Clonezilla
    image repository" for English language file.
    Thanks to Ronald F. Guilmette.

* Thu Jan 04 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.11-drbl1
  * Use "lpxelinux.0" instead of "pxelinux.0" in dhcpd.conf. It has more
    features, like support both http and tftp.

* Tue Jan 02 2018 Steven Shiau <steven _at_ clonezilla org> 2.26.10-drbl1
  * Replace all words "M$" by MS. 

* Sat Dec 30 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.9-drbl1
  * Update task_ecryptfs_mount_point in drbl-functions to work with the
    options -pe and -pfe of ocs-sr. This allows user to enter password in
    the command options although it's not safe. Thanks to ub2 _at_ gmx ch
    for requesting this.
    Ref:
    https://sourceforge.net/p/clonezilla/discussion/Clonezilla_live/thread/d3af2134

* Thu Dec 28 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.8-drbl1
  * Include lz4mt package in Clonezilla live.

* Thu Dec 28 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.7-drbl1
  * Add support for lz4mt (-z8p).

* Wed Dec 27 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.6-drbl1
  * Add zstd/pzstd (-z9/-z9p) support.

* Tue Dec 26 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.5-drbl1
  * Remove drbl-chntpw in Clonezilla live. Just use chntpw.
  * Include zstd in Clonezilla live. 

* Wed Dec 13 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.4-drbl1
  * Update netinstall for Fedora as version 27.

* Mon Dec 04 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.3-drbl1
  * Add variable PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_ARM64_ONLY for ARM64 live
    system in drbl.conf.

* Sun Dec 03 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.2-drbl1
  * Update language files for lz4-related variables.
  * Add -z8 (lz4) in the wizard menu.

* Sun Dec 03 2017 Steven Shiau <steven _at_ clonezilla org> 2.26.1-drbl1
  * Separate variables of drbl.conf so it can be used with creating ARM64
    live system in clonezilla programs: create-debian-live and
    create-ubuntu-live.
  * Add "" to the variable nameserver in
    $drbl_common_root/etc/diskless-image/config in drblpush.
  * Use drbl-get-dnsserver in drblpush.
  * Drop support for Ubuntu 14.10, 15.04, 15.10,
    Add files required by Ubuntu 17.04 and 17.10.
  * This release supports Ubuntu 17.10.

* Wed Nov 22 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.17-drbl3
  * Make drbl depend on pxelinux, while clonezilla depends on isolinux.

* Mon Nov 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.17-drbl1
  * drbl-prepare-memtest should not run in arm64 arch.
  * Add initial add support for arm64 in drbl-gen-grub-efi-nb. Not tested yet.

* Fri Oct 27 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.16-drbl1
  * Bug fixed: Make version comparison with epoch work in the function
    get_latest_pkg_in_drbl_repository of drbl-functions.

* Thu Oct 26 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.15-drbl1
  * Include xorriso instead of genisoimage in clonezilla live.
  * Update netinstall for OpenSuSE as 42.3, and Ubuntu as artful.

* Fri Sep 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.14-drbl1
  * Add option -t|--tftp-server to drbl-gen-grub-efi-nb so that we can
    assign the IP address for tftp server. It's intended to make it work for
    grub network boot loader can work with uEFI network booting client.
    # Ref: http://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2017q1/011124.html

* Wed Sep 27 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.13-drbl1
  * Language file zh_CN.UTF-8 was updated. Thanks to Zhiqiang Zhang.
  * Add /EFI/centos/grubx64.efi for local booting test in function
    LOCAL_EFI_BOOT_GRUB_CFG of drbl-functions.

* Mon Sep 25 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.12-drbl1
  * Update language files for more hints about Clonezilla command.

* Thu Sep 14 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.11-drbl1
  * Improve the mechanism to get dns in drblpush.

* Wed Aug 02 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.10-drbl1
  * Add support for CentOS 7.3.

* Mon Jul 31 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.9-drbl1
  * Add package casync to DRBL/Clonezilla live.

* Sun Jul 23 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.8-drbl1
  * Suppress lite server and lite client in the main menu of the
    Clonezilla live icon Clonezilla-live.desktop of DRBL live.

* Mon Jul 10 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.7-drbl1
  * Language file ca_ES was updated. Thanks to René Mérou.

* Sat Jun 24 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.6-drbl1
  * Applied the patch from Georges Khaznadar which addresses the udevadm
    path hard-code issue.
    Ref: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=852562

* Tue Jun 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.5-drbl1
  * Language file hu_HU was updated. Thanks to Greg Marki.

* Tue Jun 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.4-drbl1
  * Language file sk_SK was updated. Thanks to Ondrej Dzivy Balucha.
    Language file es_ES was updated. Thanks to Juan Ramón Martínez.
    Language file de_DE was updated. Thanks to Michael Vinzenz.
    Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
    Language file it_IT was updated. Thanks to Gianfranco Gentili.
    Language file tr_TR was updated. Thanks to Volkan Gezer.

* Tue Jun 13 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.3-drbl1
  * Update language files about SMB versions.

* Mon Jun 12 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.2-drbl1
  * Collected MAC address file with NIC device name not in the form eth*
    was not copied to /etc/drbl/ by drblpush.

* Mon Jun 12 2017 Steven Shiau <steven _at_ clonezilla org> 2.25.1-drbl1
  * Language file hu_HU was updated. Thanks to Greg Marki.
    Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
    Language file tr_TR updated. Thanks to Volkan Gezer.
    Language file de_DE was updated. Thanks to Michael Vinzenz.
    Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
    Language file it_IT was updated. Thanks to Gianfranco Gentili.
  * Add stretch in Debian netinstall list.

* Sun Jun 04 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.16-drbl1
  * Add alsa-utils to Clonezilla live.

* Sun Jun 04 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.15-drbl1
  - Add package espeakup in Clonezilla/DRBL live. Thanks to 
    Nick Gawronski (nick _at_ nickgawronski com) for suggesting
    this for the blind to use Clonezilla live.

* Sat Jun 03 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.14-drbl1
  - Language files es_ES for both bash and perl was updated. Thanks to 
    Juan Ramón Martínez (jrmc_77 _at_ hotmail com)

* Tue May 30 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.13-drbl1
  * Bug fixed: dnsmasq.conf with proxy settings should be only created
    when proxy mode is required. Not to be created by default.

* Mon May 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.12-drbl1
  * Update language file zh_TW.UTF-8. Jfbterm crashes due to shown "，"
    and long description in zh_TW.UTF-8 in the console promt.
    Replace "，" with "," for
    msg_note_you_have_to_make_sure_enough_no_of_ip_addr.

* Thu May 25 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.11-drbl1
  * Implement a better way in drbl-find-dhcp-srv to detect
    DHCP service based on busybox udhcpc.

* Wed May 24 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.10-drbl1
  * Separate detect_dhcp_srv_in_lan in drbl-functions.
    Add option -a|--allow-1-nic to function gen_dnsmasq_cfg in
    drbl-functions.
  * Update language files about ocs-live-feed-img.

* Tue May 16 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.9-drbl1
  * Merge language file tr_TR from Volkan Gezer <volkangeyer _at_ gmail dot
    com>.
  * Add msg_insert_storage_dev_now for all language files.

* Tue May 02 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.8-drbl1
  * Update language files about wait command for ocs-onthefly.

* Sat Apr 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.7-drbl1
  * Update language files about wait command for ocs-live-feed-img.

* Sat Apr 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.6-drbl1
  - Update language files about clonezilla menus.
  - Bug fixed: remove port=0 in gen_dnsmasq_cfg of drbl-functions so that
    DNS query will take effect.
  - Add dnsmasq back to PKG_TO_QUERY in drbl.conf since we have fixed the
    issue that DNS query is not working after dnsmasq is installed.

* Wed Apr 26 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.5-drbl1
  - Update language files about device to remote device cloning.

* Sun Apr 23 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.4-drbl1
  - Sort out the language files about lite server.

* Sat Apr 22 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.3-drbl1
  - Add option -e|--fetch-link to drbl-sl.
  - When file (e.g. memtest) does not exist, the PXE/uEFI menu
    won't be created.

* Fri Apr 21 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.2-drbl1
  - Add grub-efi-amd64-bin in Clonezilla live
  - Add option "-r" to function gen_dnsmasq_cfg in drbl-functions so
    that it can be used in Clonezilla live, not only in DRBL live.

* Thu Apr 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.24.1-drbl1
  - Initial support for Ubuntu 17.04.
  - Move net-tools to the required package for Debian/Ubuntu.
  - Update netinstall Ubuntu and Fedora version number in drbl.conf.

* Thu Apr 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.38-drbl1
  - Update language files about lite server.

* Wed Apr 19 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.37-drbl1
  - Update language files about not support for converting encrypted image.

* Tue Apr 18 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.36-drbl1
  - Update language files for lite server/client.

* Mon Apr 17 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.35-drbl1
  - Add option "-g, --gateway-ip-add" to get-all-nic-ip.

* Mon Apr 17 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.34-drbl1
  - Update language files about To_upstream and In_isolation modes.

* Sat Apr 15 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.33-drbl1
  - Move dnsmasq to drbl/clonezilla live only. Not for installed system.
    It caused DNS resolving failure in Ubuntu 16.04.
    Thanks to Bruce Banner for reporting this issue:
    https://sourceforge.net/p/drbl/discussion/DRBL_for_Debian/thread/f81f06b6/

* Fri Apr 14 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.32-drbl1
  - Update language files to give warning about run ocs-live-get-img
    on clonezilla live lite server.

* Mon Apr 10 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.31-drbl1
  - Update functions about selecting parameters for ocs-live-feed-img and
    drbl-ocs.
  - Update language files for prompting booting in unattended mode about
    ocs-live-feed-img.

* Sun Apr 09 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.30-drbl1
  - Update language files for multicast feeding mechanism.

* Fri Apr 07 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.29-drbl1
  - Add package lighttpd for Clonezilla/DRBL live.

* Sun Mar 26 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.28-drbl1
  - Bug fixed: ocs_prerun* are run twice.
    Ocs_prerun1 and ocs_prerun2 used by drbl live are changed to
    drbl_prerun1 and drbl_prerun2. Otherwise they will be run by S06pre-run
    in drbl-live.d and ocs-live-run-menu.

* Fri Mar 10 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.27-drbl1
  - Bug fixed: failed to get DNS setting in drblpush.

* Thu Mar 02 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.26-drbl1
  - The input network settings for drbl0 will be confirmed before continue in
    drbl live.

* Thu Mar 02 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.25-drbl1
  - Add a mechanism to manually configure drbl0 network settings if DHCP
    server use MAC address to provide fixed address.
  - Update language files for manually set drbl0.
  - Bug fixed: Add username=user in GParted live PXE config in drbl-sl.

* Fri Feb 24 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.24-drbl1
  - Move archivemount to be one of required packages for drbl,
    not only for live system. It might be used in the future for BT.

* Mon Feb 20 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.23-drbl1
  - Spanish language files were revised. Thanks to
    Pablo Hinojosa Nava <pablohn6 _at_ gmail com>
    and
    Juan Ramón Martínez <jrmc_77 _at_ hotmail com>
    Ref:
    https://github.com/Pablohn26/clonezilla/commit/4f6b492b91a92f08d1e1d1626b209a3fdfc8ed73
    https://github.com/Pablohn26/clonezilla/commit/46d1d104d46e56b0f5efc9630ea8e9293747b15f

* Tue Feb 14 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.22-drbl1
  - Write macvlan network config file in /etc/network/interfaces.d/drbl0
    instead of /etc/network/interfaces in config_drbl_live_network of
    ocs-functions.
  - Disable dnsmasq service when uninstall DRBL.
  - Add package sshpass and keychain in DRBL/Clonezilla live.

* Wed Feb 08 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.21-drbl1
  - Suppress the tput error during booting in makeboot.sh and
    drbl-functions.

* Tue Feb 07 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.20-drbl1
  - Suppress the tput error during booting in makeboot.sh and
    drbl-functions.

* Mon Feb 06 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.19-drbl1
  - Remove unnecessary prompt about relay dhcp in drblpush.

* Thu Feb 02 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.18-drbl1
  - Update language files about using proxy DHCP mode. Give warning about
    the risk. 

* Tue Jan 31 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.17-drbl1
  - Detect if terminal supports color output before using color outputs in the
    terminal. Thanks to TF for asking this.
    Rref:
    https://sourceforge.net/p/clonezilla/discussion/Clonezilla_live/thread/ec46f3a3/

* Mon Jan 30 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.16-drbl1
  - Add more prompts in program drbl-find-dhcp-srv.
  - Package dnsmasq should be included for DRBL live only, not for
    Clonezilla live.
  - Update perl language files about only_one_network_card_in_system.

* Sun Jan 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.15-drbl1
  - Bug fixed: return code fixed in drbl-find-dhcp-srv.

* Sun Jan 29 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.14-drbl1
  - Add nmap mechanism as the primary method to detect DHCP service.
  - Change macvlan device name to drbl0 from drblvir0.
  - Add nmap to PKG_FROM_DBN_WHICH_OCS_LIVE_NEED and PKG_TO_QUERY in
    drbl.conf.

* Fri Jan 27 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.13-drbl1
  - Program drblpush should set use_existing_dhcp_srv in drbl.conf if
    it enables proxy DHCP mode.
  - Make proxy DHCP work for dnsmasq < 2.75 but give warning.
  - Add monitoring-plugins-basic in PKG_TO_QUERY of drbl.conf.

* Thu Jan 26 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.12-drbl1
  - Add a mechanism to enable proxy DHCP as 1 NIC.
  - Bug fixed: "IPAPPEND 1" should not be global in pxelinux.cfg. 
    It is only necessary for DRBL clients.
    Otherwise it will confuse local boot, for example.
  - Update language files about proxy DHCP mechanism.

* Sat Jan 21 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.11-drbl1
  - Skip copying /var/lib/docker to common root.

* Wed Jan 18 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.10-drbl1
  - Add shadow-utils as required package in RH-like OS
  - Add dnsmasq in the packages list in DRBL/Clonezilla live.
  - Add a program "drbl-proxy-dhcp" to enable/disable proxy DHCP.
  - Use drbl_bootp=$net_default_next_server in grub netboot. This should
    work for the future grub (after grub git Nov/23/2016).
    Ref:
    http://git.savannah.gnu.org/gitweb/?p=grub.git;a=commit;h=f8c3af3b613f9b1d5123f1ccad565950f82f6959

* Mon Jan 16 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.9-drbl1
  - Remove files for DRBL Debian (v5 and 6) client.
    Add files for Debian 8.7.
  - Append DHCP/BOOTP to the kernel command line, i.e.,
    ip=<client-ip>:<boot-server-ip>:<gw-ip>:<netmask>
    We need this when using proxy DHCP.
  - Add template log for client arch in dhcpd.conf.

* Fri Jan 06 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.8-drbl2
  * Language file sk_SK was updated. Thanks to Ondrej Dzivy Balucha.

* Tue Jan 03 2017 Steven Shiau <steven _at_ clonezilla org> 2.23.8-drbl1
  - Add option "-noabo" in the dialog menu.
  - Language files were updated for option "-noabo".

* Sat Dec 24 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.7-drbl1
  - Add experimental bittorent restoring codes in dcs.

* Mon Dec 19 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.6-drbl1
  - Add package archivemount for drbl/clonezilla live.

* Mon Dec 12 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.5-drbl1
  - Add initial codes about bittorrent restoring. Not finished yet.

* Mon Nov 28 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.4-drbl1
  * Define LOCAL_EFI_BOOT_GRUB_CFG in drbl-functions and use it both in
    gen-grub-efi-nb-menu and ocs-live-boot-menu.

* Sun Nov 27 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.3-drbl1
  - Skip installing package "init" for Debian Wheezy when running
    "drblsrv -i".
    Thanks to Peter Brisson for reporting this issue:
    https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/433ed559/

* Thu Nov 24 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.2-drbl1
  - Add package bicon in drbl/clonezilla live system. 

* Mon Nov 21 2016 Steven Shiau <steven _at_ clonezilla org> 2.23.1-drbl1
  - Add crossmnt option in nfs export for /home & /opt in drbl-nfs-exports.
    This would make automatically mount in clients when /home/partimag is
    mounted in different device on DRBL server.

* Thu Nov 17 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.8-drbl1
  - Change maxswapsize default value to 1024 MB. 

* Mon Nov 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.7-drbl1
  - Make service be started with systemd command first. This should fix an
    issue that rpc-statd service was not started on Ubuntu 16.10.
  - Remove portmap in drbl_server_service_chklist.
    Add rpc-statd in client_services_chklist.
  - Add packages sysstat and iftop in the clonezilla/drbl live packages
    list.
* Tue Nov 01 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.6-drbl1
  - Add a mechanism to check if selinux enabled or not in RH-like system.
  - Language files updated for selinux checking description.
  - Language file ca_ES was updated. Thanks to René Mérou.

* Mon Oct 31 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.5-drbl1
  - Add p7zip-full in drbl/clonezilla live packages list.

* Thu Oct 27 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.4-drbl1
  - Remove ncpfs from clonezilla/drbl live packages list. It's not in the
    Debian repository anymore.

* Tue Oct 25 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.3-drbl1
  - Suppress some unnecessary error or warning messages when running drblpush -i.
    e.g. append option "-d" to "cp --parents" to suppress the copying about
    linking files.

* Tue Oct 25 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.2-drbl1
  - Add yakkety in the netinstall for Ubuntu. 

* Tue Oct 25 2016 Steven Shiau <steven _at_ clonezilla org> 2.22.1-drbl1
  - Move package initscripts from PKG_FROM_DBN to PKG_TO_QUERY in drbl.conf.
  - Add clonezilla SE client service for Ubuntu 16.10.
  - Initial support for Ubuntu 16.10.

* Wed Oct 19 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.11-drbl1
  - Add ext4magic & myrescue in the packages list of
    Clonezilla/DRBL live system.

* Tue Oct 18 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.10-drbl1
  - Forgot to load grub.cfg-$IP before grub.cfg for uEFI netboot client.
    Thanks to Anshu Arya for reporting this issue.
    Ref: https://sourceforge.net/p/drbl/discussion/DRBL_for_Debian/thread/73a26bf9
  - Run deploy_pxecfg_grubefi_files inside drbl-ocs because the prompt to
    start clonezilla SE service only mentions to run drbl-ocs.

* Thu Oct 13 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.9-drbl1
  - Add option "-u, --user" for drbl-fuu so that drbl-cp-user, drbl-rm-user,
    drbl-get-user can be used to assign some specific users.

* Thu Oct 13 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.8-drbl1
  - Add packages os-prober & dislocker for Clonezilla/DRBL live packages
    list.

* Sat Oct 01 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.7-drbl1
  - Language file hu_HU was updated. Thanks to Greg Marki.
  - Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
  - Language file de_DE was updated. Thanks to Michael Vinzenz.
  - Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
  - Language file it_IT was updated. Thanks to Gianfranco Gentili.
  - Language files es_ES were updated. Thanks to Juan Ramón Martínez
    and Alex Ibáñez López.

* Mon Sep 26 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.6-drbl1
  - If batch mode is on, do not append "-c" in the beginner mode
    for ocs-sr menu.

* Mon Sep 19 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.5-drbl1
  - Add support for Debian 8.6. 

* Mon Sep 19 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.4-drbl1
  - Update language files. Thanks to Rafael Fontenelle for reporting this.
    Ref: https://sourceforge.net/p/clonezilla/bugs/263/

* Fri Sep 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.3-drbl1
  -  Add options -sfsck and -senc in the Clonezilla live interactive menu.

* Fri Sep 09 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.2-drbl1
  - Separate the reboot/poweroff prompt messages in menu for Clonezilla SE
    and Clonezilla live.
  - Update language files about poweroff/reboot, and removing source or
    destination disk after cloning.

* Thu Sep 08 2016 Steven Shiau <steven _at_ clonezilla org> 2.21.1-drbl1
  - Bug fixed: Replace boot paramater noprompt with noeject since live-boot
    >= v3 uses noeject, not noprompt.
  - Ask the post action (choose, reboot, poweroff) before starting cloning.
    Thanks to Aaron Burling (aaron_burling _at_ lkstevens wednet edu) for this idea.

* Tue Aug 30 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.38-drbl1
  - Polish the program makeboot.sh.
    Applied the changes from David Tonhofer.
    Ref: https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/cf6f506b
  - Missing quotes in the echo command of makeboot.sh. Thanks to David
    Tonhofer.
    Ref: https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/a852d0a8

* Wed Aug 17 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.37-drbl1
- Skip stopping or starting service if it's masked
  in drbl-all-service.

* Sun Aug 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.36-drbl1
- Drop the support for boot paramter ocs_chk_img and ocs_fsck_src_part
  in drbl-functions. Only honor the options of ocs-sr by "-scr", "-scs",
  "-fsck", "-fsck-y".
- Also make something like "ocs-sr -x -scr" work. It won't ask about if
  "-scr" should be used or not. Thanks to Aaron Burling
  (aaron_burling _at_ lkstevens wednet edu) for reporting this issue.

* Sun Jul 24 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.35-drbl1
* Add powertop in the packages list of Clonezilla/DRBL live. 

* Mon Jul 18 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.34-drbl1
- Move function get_dir_filesystem from drbl-functions to
  ocs-functions. 

* Fri Jul 08 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.33-drbl1
- Update language files for exiting dir browsing.

* Fri Jul 08 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.32-drbl1
- Update Fedora netinstall ver as 24 in drbl-ocs.conf.
- Update language files for exiting dir browsing.

* Thu Jul 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.31-drbl1
- Update language file zh_TW.UTF-8 for bind mount.

* Thu Jul 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.30-drbl1
- Update language files for ocs-live-bind-mount use in prep-ocsroot and ocs-live-run-menu.

* Wed Jul 06 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.29-drbl1
- Update language files for ocs-live-bind-mount use.

* Mon Jun 27 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.28-drbl1
- When option "-k1" or "-k2" of ocs-sr or drbl-ocs is chosen, "-icds" is on automatically.
- Language files updated for fuse-related messages.
- Add "-batch" in the TUI for saving mode.

* Tue Jun 21 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.27-drbl1
- Use shorter name for fsck-related options, i.e.  "-fsck-src-part" is replaced by "-fsck", and "-fsck-src-part-y" is replaced by "-fsck-y".

* Mon Jun 20 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.26-drbl1
- Clean tmp file parttable-ocs.* when exiting.

* Mon Jun 20 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.25-drbl1
- Add package qemu-utils for Clonezilla/DRBL live system.

* Sun Jun 19 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.24-drbl1
- Improve drbl-get-nfsserver by using mount status to get nfs server first, if it's not found, then gateway will be used.

* Sat Jun 18 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.23-drbl1
- Bug fixed: failed to parse correct domain if no port is assigned.

* Thu Jun 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.22-drbl1
- Update function filter_cl_gp_boot_param of ocs-functions to filter toram option. Otherwise if toram=live,syslinux shown in drbl live client, it will crash.

* Thu Jun 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.21-drbl1
- Bug fixed for using toram=live mode. Now it works when using toram=live,syslinux.

* Thu Jun 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.20-drbl1
- Program drbl-sl supports toram=live mechanism, so it will check the file /lib/live/mount/medium/live/{Clonezilla-Live-Version, DRBL-Live-Version,GParted-Live-Version}, too.

* Tue Jun 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.19-drbl1
- New program "drbl-uriparse" added. It can be used to parse the URI to get the attribute.

* Fri Jun 10 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.18-drbl1
- Bug fixed: extra "if" in the if block of drblsrv.

* Fri Jun 10 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.17-drbl1
- Remove package init for Ubuntu 14.04 since it still uses upstart, not systemd.

* Tue Jun 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.16-drbl1
- Bug fixed: the mode for drblpush was 644, not 755. Thanks to Danny Russ | KSC for reporting this.
- Due to the change in Debian Sid that "init" is not essential any more.  It has to added as a required package in drbl.conf.  Ref: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=756023

* Mon Jun 06 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.15-drbl1
- Use xz format for drbl tarball for Debian.

* Mon Jun 06 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.14-drbl1
- Drop the requirement of mkswap-uuid. Modern mkswap has the option to do that. 

* Sat Jun 04 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.13-drbl1
- Add dhcp-vendor-id=DRBLClient in clonezilla_se_live_opts in drbl-sl.

* Fri Jun 03 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.12-drbl1
- Add netework boot paramter "dhcp-vendor-id=DRBLClient" for drbl-live clients.
- Use a flexible network device name instead of eth0 for alias network device in function config_drbl_live_network of drbl-functions.
- Fixed wrong descriptions in msg_ocs_param_fsck_src_part_yes for zh_TW.UTF-8.

* Sun May 22 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.11-drbl1
- Add support for Debian 7.11 and 8.5.

* Tue May 17 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.10-drbl1
[Ceasar Sun]
- drbl-login-switch now supports the config for Xenial.

* Sun May 15 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.9-drbl1
- Add an option "-o" to drbl-sl so that different cases can be used.

* Sat May 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.8-drbl1
- Remove the option "--force-yes" of apt-get when installing required packages on Debian. It was for legacy Debian/Ubuntu.

* Sat May 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.7-drbl1
- install-kernel-for-client: avoid getting empty line for kernel version.

* Sat May 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.6-drbl1
- install-kernel-for-client: Better to parse kernel version, avoid getting empty line.

* Fri May 13 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.5-drbl1
- Add package dos2unix in Clonezilla/DRBL live packages list. 

* Thu May 12 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.4-drbl1
- [Ceasar Sun] Fix the nis failed to start in xenial.

* Tue May 10 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.3-drbl1
- Update netinstall for Ubuntu as "wily xenial" in drbl.conf. 

* Mon May 02 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.2-drbl1
- Remove cryptsetup for Ubuntu-based Clonezilla live temporarily
  from drbl.conf. Due to this issue:
  https://bugs.launchpad.net/ubuntu/+source/cryptsetup/+bug/1528861 
  It will be added for Debian-based Clonezilla live when creating.
- Add package console-common for Clonezilla live again because we have
  removed cryptsetup and plymouth for Ubuntu-based Clonezilla live.
- Remove vblade for DRBL server temporarily since it will cause
  depending issue for runit on Ubuntu 16.04.

* Mon Apr 11 2016 Steven Shiau <steven _at_ clonezilla org> 2.20.1-drbl1
- Remove drbl client's files for Ubuntu <= 13.10.
- Add initial support for Ubuntu 16.04. Not finished.

* Mon Apr 04 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.16-drbl1
- Add support for Debian 7.10 and 8.4.

* Tue Mar 29 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.15-drbl1
- Add GNU/Linux distribution network installation for uEFI network boot clients.

* Mon Mar 21 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.14-drbl1
- Add "exit" option parallel to the beginner/expert selection.

* Mon Mar 14 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.13-drbl1
- Now all the supported GNU/Linux has option "-V" for sort, so just use it instead of using the function get_sort_V_opt to decide.

* Mon Mar 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.12-drbl1
[Ceasar Sun]
- Support destination dir name with white space for makeboot.sh.
[Robert Rubino]
- Add an error routine to makeboot.bat and makeboot64.bat.

* Mon Mar 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.11-drbl1
- Add client files for Ubuntu 15.10.

* Mon Mar 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.10-drbl1
- Add support for Debian 8.3.

* Mon Mar 07 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.9-drbl1
- Remove scientific linux i386 net install in drbl.conf since it does not exist.
- Fix typos in changelog.

* Sat Mar 05 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.8-drbl1
- Apply the patch for ru_RU.UTF-8 from https://github.com/stevenshiau/drbl/pull/6. Thanks to don Rumata.
- Update language files for ocs-match-checksums.

* Wed Mar 02 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.7-drbl1
- Bug fixed: do not strip the word about kernel or linux-image in pkg-ver-latest

* Wed Mar 02 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.6-drbl1
- Use "sort -V" instead of awk in pkg-ver-latest.

* Thu Feb 18 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.5-drbl1
- Update language files for the checksum results log file prompt.

* Wed Feb 17 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.4-drbl1
- Bug fixed: gen_CDG_checksums failed to list all files for checksum files.
- Update language files for better description about checksum.

* Tue Feb 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.3-drbl1
- Update language files for better description about checksum.

* Tue Feb 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.2-drbl1
- Update language files for better description about checksum.

* Mon Feb 15 2016 Steven Shiau <steven _at_ clonezilla org> 2.19.1-drbl1
- Language files were updated for options -gmf and -cmf, etc.
- Add "-cmf" & "-gmf" in dialog menu.
- Add sha512sum and refine the function gen_CDG_checksums.

* Wed Jan 20 2016 Steven Shiau <steven _at_ clonezilla org> 2.18.12-drbl1
- Remove console-common for pkgs list:
  https://bugs.launchpad.net/ubuntu/+source/cryptsetup/+bug/1528861

* Sat Jan 16 2016 Steven Shiau <steven _at_ clonezilla org> 2.18.11-drbl1
- Functions add_opt_in_pxelinux_cfg_block, remove_opt_in_pxelinux_cfg_block, add_opt_in_grub_efi_cfg_block, and remove_opt_in_grub_efi_cfg_block of drbl-functions failed to deal with 'locales=' and 'keyboard-layouts='. This makes drbl-ocs-live-prep can not preset locales and keyboard-layouts.

* Mon Jan 04 2016 Steven Shiau <steven _at_ clonezilla org> 2.18.10-drbl1
- List kmod or module-init-tools in the package for suggestions in drbl.conf. This change was due to the change in mkpxeinitrd-net.

* Thu Dec 24 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.9-drbl1
- Package console-common is not included in Clonezilla/DRBL/GParted live because it's deprecated: https://bugs.launchpad.net/bugs/1528861

* Tue Dec 22 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.8-drbl1
- Package perl-modules was replaced by perl in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf.

* Mon Dec 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.7-drbl1
- Update msg_ocs_param_t in language files in en_US and zh_TW.UTF-8.
- [Ceasar Sun]
  Add Conflicts=mkswapfile.service to avoid DRBL service mkswapfile to be
  started in ocsd-run.service.
  Add support for Fedora 22 and 23.

* Mon Dec 14 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.6-drbl1
- Adding ocsd files for CentOS 7.2.

* Sat Dec 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.5-drbl1
- "Shoutdown" should be "Desligar" in luanguage file pt_BR. Thanks to Luciano (lboni2 _at_ yahoo com br) for correcting this.
- Give warning about grub2 uEFI NB on CentOS 7 for grub2 versions 2.02-0.17 and 2.02-0.23 in drblsrv.
- Add OCS files (ocsd-*.service) for Clonezilla SE clients.
- Apply the patches from Ceasar Sun to initial support Fedora >=21.

* Mon Nov 23 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.4-drbl1
- Switch to use "-scs" instead of "-sc" although "-sc" is still working. This will be easier to tell the differences between saving and restoring image. 

* Sat Nov 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.3-drbl1
- Add options -sc0 and -scr for checking image integrity before restoring an image. The former is to check on Clonezilla server, and the latter is to check on Clonezilla client.
- Language files were updated for options -sc0 and -scr.

* Mon Nov 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.2-drbl1
- Adding fatresize in the packages list for clonezilla/drbl live.

* Tue Nov 10 2015 Steven Shiau <steven _at_ clonezilla org> 2.18.1-drbl1
[ Ceassar Sun ]
- Adding syslinux-common as required pkg in drbl.conf for Debian-like Linux. This is used to support Linux Mint.
- Adding mdm support for drbl-login-switch.
- Adding breakpoints in init.drbl.
- Adding support for Linux Mint.

* Tue Nov 3 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.12-drbl1
- Adding package fatresize in the DRBL/Clonezilla live packages list.

* Mon Nov 2 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.11-drbl1
- More tests about if $GRUB_CONF exists before going on in some functions of drbl-functions about grub2 uEFI network boot.

* Sat Oct 31 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.10-drbl1
- Check if file $GRUB_CONF exists first in hide_reveal_grub_efi_ent and some functions in drbl-functions.

* Sat Oct 31 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.9-drbl1
- When grub-mkimage or grub-mknetdir not found, drbl-gen-grub-efi-nb shows warning messages only instead of error message because older version of GNU/Linux (e.g. CentOS 6) does not support creating grub uEFI network boot image.

* Sat Oct 31 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.8-drbl1
- Test if GRUB_CONF exists before modifying it in tune-clientdir-opt.
- Adding support for CentOS 6.7.

* Fri Oct 30 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.7-drbl1
- Adding boot parameter "stick-to-pxe-srv" for DRBL live clients.  This mechanism is used to stick to the PXE server when live-boot trying to lease IP address by using the boot parameter "stick-to-pxe-srv". It will drop the DHCP server without providing filename, so it can partially solve the issue that 2 DHCP servers co-exist on the same LAN. By default the max lease loop number is 10 times. The boot parameter "ethdev-dhcp-max-loop" can be used to assign the max number. //NOTE// This mechanism is only for DRBL/Clonezilla SE live.

* Tue Oct 20 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.6-drbl1
- Suppress the error message in hide_reveal_pxe_img, use warning only.
- Polish the output messages in hide_reveal_grub_efi_ent.

* Mon Oct 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.5-drbl1
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Mon Oct 05 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.4-drbl1
- Update the help message of drbl-live.
- Bug fixed: read the ocs_client_no_per_NIC from /etc/ocs/ocs-live.conf in higer priority than that of $drbl_setup_path/files/ocs/live-hook/ocs-live-hook.conf in drbl-live.

* Tue Sep 29 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.3-drbl1
- Show Grub CPU and platform in the preconfig of grub uEFI netboot.

* Wed Sep 23 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.2-drbl1
- Use the same prompt "Local operating system (if available)" for uEFI netboot, as that of PXE.

* Tue Sep 22 2015 Steven Shiau <steven _at_ clonezilla org> 2.17.1-drbl1
- For all cases, dcs clean the UEFI NB config files because now local-disk is always revealed.
- Bug fixed: dcs -> local did not switch that for local-disk in grub uEFI netboot mode.
- Reveal local-disk in the uEFI netboot menu by default. We have listed most of the OSes.
- Convert the ":" in the MAC address based file name to "-" for grub uEFI netboot mode, i.e.  something like: grub.cfg-01-00-0c-29-1d-9a-d1, not grub.cfg:01:00:0c:29:1d:9a:d1

* Mon Sep 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.12-drbl1
- Update Forcevideo-drbl-live to work with the latest Sid. Thanks to Eric Reischer (emr _at_ hev psu edu) for reporting this issue.

* Mon Sep 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.11-drbl1
- Bug fixed: wrong info about prompt for grub uEFI netboot.

* Sun Sep 20 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.10-drbl1
- More grub2 file system modules were added in drbl-gen-grub-efi-nb so that local disk boot is supported for uEFI network boot menu.
- Live system hostname is assigned as ocs-client in Clonezilla SE of DRBL live, while drbl client is assigned as drbl-client. This is to avoid confusion.

* Sat Sep 19 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.9-drbl1
- Since we have used grub embedded preconfig way in drbl-gen-grub-efi-nb to solve this grub uEFI network booting restoring issue in Debian: http://lists.gnu.org/archive/html/help-grub/2015-09/msg00035.html. Therefore no more disabling efi_netboot_1st_in_nvram in drbl-ocs.conf.

* Sat Sep 19 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.8-drbl1
- Bug fixed: the variable was not protected when writing the preconfig file with cat command in drbl-gen-grub-efi-nb.

* Sat Sep 19 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.7-drbl1
- Forget about condition test for the existing of config file in grub embedded preconfig file. Just use configfile module to make that in drbl-gen-grub-efi-nb.

* Fri Sep 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.6-drbl1
- The /tftpboot/nbi_img/grub.cfg/grub.cfg-01:$net_default_mac has higher priority than /tftpboot/nbi_img/grub.cfg/grub.cfg. By doing this, we do not have to patch the grub2 as described here: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=793760

* Thu Sep 17 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.5-drbl1
- Change ocs_client_trig_type=proc-cmdline in drbl-ocs.conf when running drbl-live start.

* Tue Sep 15 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.4-drbl1
- Link the kernel and initrd of clonezilla live in /tftpboot/nbi_img/ to that of drbl live for DRBL live system.

* Tue Sep 15 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.3-drbl1
- Switched to use live system for DRBL client due to the missing /tmp or /dev/ issue.
- Disabled updating initramfs when starting, because use_run_in_initrd and use_dev_pts_in_initrd in linuxrc.conf have fit the status in Sid.

* Sat Sep 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.2-drbl1
- Bug fixed: Live system for Clonezilla jobs in Clonezilla SE was not working for the uEFI network booting environment. 
- Bug fixed: Program tune-clientdir-opt should not reveal the Clonezilla menu. Let dcs to reveal or hide that.

* Thu Sep 10 2015 Steven Shiau <steven _at_ clonezilla org> 2.16.1-drbl1
- Adding file type "tar" in function gen_CDG_checksums of drbl-functions.
- Due to the issue /tmp or /dev missing issue: http://lists.freedesktop.org/archives/systemd-devel/2015-September/034175.html, DRBL live now switch to use drbl-live-ocs-prep for Clonezilla SE client, i.e. less use NFS root.
- Adding file type "tar" in function gen_CDG_checksums of drbl-functions.
- Option "-p" was added so that drbl-sl supports the mounted or unzipped live dir.

* Mon Sep 07 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.31-drbl1
- Option "-n" should be added for mount command when mounting /dev in read-only / (hence read-only /etc).

* Mon Sep 07 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.30-drbl1
- Option "-b" was added was added to drbl-live.
- A tag file will be added in /tfptboot/node_root/drbl_ssi/ when drbl-live is run.
- Default to use "-t devtmpfs" instead of "-t udev" for mount command in init.drbl.
- The flag TMPFS_RUN was changed to "true" by default in init.drbl
- Reverted to create /dev/{console,null} in $drbl_common_root/. It's required in some cases.
- Corresponding change was done in drblpush with TMPFS_RUN in init.drbl.

* Sun Sep 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.29-drbl1
- Adding support files for Debian 7.9 and 8.2 in /usr/share/drbl/setup/files/DBN/.

* Sun Sep 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.28-drbl1
- Client's /etc/fstab was changed. For nfs root, we set the option as "rw" so that checkroot.sh in Debian sysvinit could update the /etc/mtab.
- The /proc in drbl client's /etc/fstab is commented. It's done by udevd automatically.
- No more creating /dev/{console,null} in $drbl_common_root/. It's done by udevd automatically.

* Thu Sep 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.27-drbl1
- Package strace was added in clonezilla/drbl live system.
- Set nosuid,nodev in /etc/fstab for client's /tmp dir.
- Disabled workaround for dm after nis in drbl-live.

* Tue Sep 01 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.26-drbl1
- Put tmp.mount back for DRBL client. It was disabled in Debian patched systemd.

* Tue Sep 01 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.25-drbl1
- Bug fixed: DRBL client sometimes failed to mount nfs due to remote-fs service starts first. A workaround was added. (https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=768006)

- Reverted the previous implementation for /etc/fstab.

* Fri Aug 28 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.24-drbl1
- An insurance to make sure that all mounting in /etc/fstab are done.

* Thu Aug 27 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.23-drbl1
- Functions add_opt_in_pxelinux_cfg_block and add_opt_in_grub_efi_cfg_block were improved to have an option "-n".
- Using boot parameters for switching clients' mode (text or graphical) in systemd.

* Mon Aug 24 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.22-drbl1
- Bug fixed: For Debian >=8 the file /var/lib/nfs/state was missing which caused rpc.statd failing to start in DRBL client.

* Thu Aug 20 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.21-drbl1
- Adding support for Debian 8.1.

* Mon Aug 17 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.20-drbl1
- Make sure there is no white space in the end of opt_content in function add_opt_in_pxelinux_cfg_block in drbl-functions. This could reduce the chance that boot parameters are wrongly parsed by Linux kernel.

* Sun Aug 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.19-drbl1
- Files isolinux.bin and memdisk should be extracted and put to syslinux in get_syslinux_binary_for_dos_linux of drbl-functions.

* Tue Aug 11 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.18-drbl1
- Package zerofree was added in the packages list for DRBL/Clonezilla live.

* Tue Aug 11 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.17-drbl1
- Language files were updated for the option "-k1", both GPT and MBR format are supported.

* Thu Jul 30 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.16-drbl1
- Disabled efi_netboot_1st_in_nvram when server is Debian or Ubuntu due to grub does not have the patch (https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=793760).
- Package grub2-efi-modules added in the packages list "PKG_TO_QUERY" in drbl.conf.

* Thu Jun 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.15-drbl1
- The useless note about option "-z3" was removed. Thanks to Marc Grondin (marcfgrondin _at_ gmail com) for reporting this.

* Sat Jun 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.14-drbl1
- Language file es_ES was updated. Thanks to Juan Ramón Martínez.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Sun May 31 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.13-drbl1
- Functions confirm_continue_or_not_default_quit, confirm_continue_or_not_default_continue, and confirm_continue_no_default_answer were moved from ocs-functions to drbl-functions.
- Checking the grub2 version in blacklist for CentOS/RHEL when running drblsrv.
- Language file es_ES was updated. Thanks to Juan Ramón Martínez.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file sk_SK was updated. Thanks to Ondrej Dzivy Balucha.
- Language file ca_ES was updated. Thanks to René Mérou.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- drbl-sl should skip ipxe.efi when searching kernel.

* Thu May 28 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.12-drbl1
- Improvement: better way to get clientdir for GRUB uEFI NB boot parameters in udhcpc-post.

* Wed May 27 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.11-drbl1
- Functions add_opt_in_pxelinux_cfg_block, remove_opt_in_pxelinux_cfg_block, add_opt_in_grub_efi_cfg_block and remove_opt_in_grub_efi_cfg_block were moved from ocs-functions to drbl-functions.

* Wed May 27 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.10-drbl1
- Package udisks was replaced by udisks2 in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf.
- Program tune-clientdir-opt now supports GRUB EFI NB.
- Program drbl-gen-grub-efi-nb put more info in the uEFI NB bootlader file info.

* Sun May 24 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.9-drbl1
- The corresponding tag files bootx64.efi.info/bootia32.efi.info will be created if the creating command runs successfully.

* Fri May 22 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.8-drbl1
- Only for those non-stop cases we will clean the GRUB UEFI NB config files in dcs. Otherwise the local-disk boot normally won't work.

* Fri May 22 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.7-drbl1
- If the latest version of fine tune ocs systemd files for DRBL clients are not found, the most related one will be use. E.g. CO7.1.1503 not found, the existing one CO7.0.1406 will be used.

* Thu May 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.6-drbl1
- Bug fixed: wrong if block for local-disk in hide_reveal_grub_efi_ent.

* Thu May 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.5-drbl1
- Minor improvement for generate-pxe-menu in the parameters while loop.
- An option was added to set the menu background mode in gen-grub-efi-nb-menu.
- GRUB efi modules part_gpt part_msdos boot multiboot were added in the bootx64.efi in gen-grub-efi-nb-menu so that we can chainloader to EFI on the local disk, like "chainloader /EFI/redhat/grub.efi +1".
- Thanks to Danny Russ | KSC for helping this GRUB EFI network boot solution.
- File drbl-efi-pxe-sw was renamed as drbl-syslinux-efi-pxe-sw.

* Mon May 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.4-drbl1
- Due to a bug "error: timeout: could not resolve hardware address" (http://sourceforge.net/p/xcat/bugs/4658/) in grub2-efi modules, the grub2-efi-modules or grub2-efi can not be listed in PKG_TO_QUERY of drbl.conf.

* Mon May 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.3-drbl1
- The package name for grub2-efi modules is grub2-efi-modules, not grub2-efi on CentOS.

* Mon May 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.2-drbl1
- drbl.conf: grub-efi-amd64-bin grub2-efi added in PKG_TO_QUERY.
- Suppress the findind error message in drbl-gen-grub-efi-nb.

* Mon May 18 2015 Steven Shiau <steven _at_ clonezilla org> 2.15.1-drbl1
- New file set-default-grub-efi-img was added. It will be used to set the menuentry for GRUB EFI NB was added.
- New file drbl-gen-grub-efi-nb was added so that it can prepare GRUB EFI network boot files (/tftpboot/nbi_img/bootx64.efi).
- New file gen-grub-efi-nb-menu was added so that it can be used to create the GRUB EFI NB config files in /tftpboot/nbi_img/grub-efi.cfg/.
- This is the initial version for using GRUB EFI NB as the uEFI network boot clients due to the syslinux.efi is not working with iPXE clients.

* Fri May 15 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.12-drbl1
- Adding drbl-efi-pxe-sw so it's easier to switch that on CentOS.
- Adding the ocs service for CentOS 7.1.1503.

* Thu May 14 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.11-drbl1
- Bug fixed: some more files (drblsrv-offline and mknic-nbi) need to be fixed so that it can be used for Linux kernel version 4.

* Tue May 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.10-drbl1
- Bug fixed: failed to identify the iso file in drbl-sl on Ubuntu 15.04. Thanks to Jasper Aorangi for reporting this (https://sourceforge.net/p/clonezilla/bugs/225/).

* Sun May 10 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.9-drbl1
- Language file hu_HU was updated. Thanks to Michael Munger.

* Sat May 09 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.8-drbl1
- Adding package tinc in Clonezilla/DRBL live. Thanks to Michael Munger (michael _at_ highpoweredhelp com) for suggesting this.

* Wed May 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.7-drbl1
- Language files for Hungarian were added. Thanks to Greg Marki (info.mlc _at_ freemail hu) for providing the files.

* Wed May 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.6-drbl1
- Suppress the messages about client's upstart files not found.

* Tue May 05 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.5-drbl1
- Network installation for Ubuntu has been updated to trusty and vivid in drbl.conf.
- Initial support for Ubuntu 15.04.

* Mon May 04 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.4-drbl1
- Bug fixed: the original /sbin/init was overwritten in DRBL live when running drblpush.

* Sun May 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.3-drbl1
- Bug fixed: wrong including path in ocsd-rescue.service for Debian machine.

* Sun May 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.2-drbl1
- Bug fixed: if block error in drblpush.
- Service drbl-clients-nat.service for systemd should be removed when uninstalling.

* Sun May 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.14.1-drbl1
- Updating Debian netinstall as jessie in drbl.conf because it's in stable status now.
- Adding support for Debian Jessie and Sid with systemd.
 
* Sun Apr 19 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.18-drbl1
- Updating language files for S3 and Swift.

* Thu Apr 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.17-drbl1
- Package cloudfuse was added in the packages list of Clonezilla live.
- A mechanism to avoid cloudfuse with ecryptfs was added because there is
an similar issue as this https://github.com/s3fs-fuse/s3fs-fuse/issues/166

* Sat Apr 11 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.16-drbl1
- A mechanism to avoid AWS S3 with ecryptfs was added because there is
an issue: https://github.com/s3fs-fuse/s3fs-fuse/issues/166

* Fri Apr 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.15-drbl1
- Package s3fs was added in the packages list of Clonezilla live.

* Thu Apr 02 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.14-drbl1
- Package ca-certificates was added in the packages list of Clonezilla live.

* Sun Mar 29 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.13-drbl1
- Package ifenslave was added in the packages list of Clonezilla live.
- Language files were updated for checking if the image repository is writable or not.

* Wed Mar 25 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.12-drbl1
- Updating netinstall for opensuse as 13.2.

* Mon Mar 23 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.11-drbl1
- Package zbackup was added in the packages list of Clonezilla live.

* Thu Mar 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.10-drbl1
- Function drbl_service_ctl was added in drbl-functions so that it can be used for start/stop/restart sysv/upstart/systemd service.

* Mon Mar 09 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.9-drbl1
- Option "-irvd" was added to Clonezilla menu.

* Thu Mar 05 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.8-drbl1
- Some ecryptfs-related options from drbl-ocs.conf were moved to drbl-functions.

* Tue Feb 17 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.7-drbl1
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.

* Mon Feb 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.6-drbl1
- Language file es_ES was updated. Thanks to Juan Ramón Martínez.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file en_US wad updated.
- Language file sk_SK was updated. Thanks to Ondrej Dzivy Balucha.
- Language file ca_ES was updated. Thanks to René Mérou.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Fri Jan 30 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.5-drbl1
- Package gdisk-noicu is now replaced by gdisk in Debian respository.
- File system ecryptfs is not always built-in, so trying to modprobe before checking it.
- Bug fixed: grand_jobs_before_exit not grand_task_before_exit.

* Thu Jan 29 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.4-drbl1
- Package bindfs was added in the packages list of DRBL/Clonezilla live.
- Language files were updated for WebDAV image server.
- Bindfs middle layer for WebDAV+eCryptfs was added.

* Sun Jan 25 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.3-drbl1
- Mergeing the patch from Ceasar to fix the boot haning issue of Fedora 21 client.

* Wed Jan 21 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.2-drbl1
- Language files were updated.
- Package refit was removed from DRBL/Clonezilla live packages list since it does not exist in Debian repository anymore.

* Mon Jan 19 2015 Steven Shiau <steven _at_ clonezilla org> 2.13.1-drbl1
- Merged the patch from Ceasar to support Fedora 21.

* Sat Jan 17 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.14-drbl1
- An option "exclude_eth_nics" was added in drbl.conf so that some network card can be excluded in drblpush.

* Fri Jan 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.13-drbl1
- Bug fixed: the previous workaround by removing services in client's /etc/rcS.d/ causes clients fail to reboot or shutdown. Forget it.

* Fri Jan 16 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.12-drbl1
- Bug fixed: drbl-clean-dhcpd-leases failed to restart dhcpd service for non-systemd environment.
- Bug fixed: Somehow the unnecessary services in client's /etc/rcS.d/ cause the console behaves weird. Removed them.

* Wed Jan 14 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.11-drbl1
- Package ecryptfs-utils is now listed as required package for DRBL.

* Tue Jan 13 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.10-drbl1
- Adding firstboot.DBN8.0.drbl.

* Mon Jan 12 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.9-drbl1
- Adding a link file firstboot.DBN7.8.drbl for Debian 7.8. Same link files for older versions, too.
- Language files were updated for variables changed and drbl-ocs.
- Force to show only unencrypted images for Clonezilla SE in dcs option.

* Wed Jan 07 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.8-drbl1
- Language files were updated for p2v and the menus in ocs-sr.

* Tue Jan 06 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.7-drbl1
- Variable "target_dir_enc_mntpnt" was changed to shorter one "ecrypt_mntpnt" in drbl-functions.
- Avoid using "rm -r" if possible.

* Mon Jan 05 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.6-drbl1
- Language files were updated for converting encrypted/decrypted images.

* Sat Jan 03 2015 Steven Shiau <steven _at_ clonezilla org> 2.12.5-drbl1
- Adding return code for function task_ecryptfs_mount_point.
- Language files were updated for encrypting and decrypting existing images.

* Mon Dec 29 2014 Steven Shiau <steven _at_ clonezilla org> 2.12.4-drbl1
- Adding package ntpdate in the packages list of Clonezilla/DRBL live.

* Sat Dec 27 2014 Steven Shiau <steven _at_ clonezilla org> 2.12.3-drbl1
- Language file zh_TW.UTF-8 was updated.
- Supporting netinstall of Fedora 21.

* Fri Dec 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.12.2-drbl1
- Updating msg_encrypt_img_dir_is_now_as in all language files.
- The target_dir_enc_mntpnt is just a mounting point. Therefore when program exists, just use rmdir not "rm -rf" to avoid accidentally removing wrong directory.

* Thu Dec 25 2014 Steven Shiau <steven _at_ clonezilla org> 2.12.1-drbl1
- Adding encryption function for Clonezilla image. Now it's OK for Clonezilla live, not yet for Clonezilla SE.
- Remove zh_TW.BIG5 language option.

* Thu Dec 25 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.16-drbl1
- File Known_issues_Big5.txt was removed.
- Known_issues.txt and RELEASE-NOTES were updated.
- Adding package ecryptfs-utils in the packages list of DRBL/Clonezilla live.

* Wed Dec 10 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.15-drbl1
- The language files about stable Clonezilla live was updated as i586 instead of i486.

* Wed Dec 10 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.14-drbl1
- Now i586 instead of i486 Clonezilla live is in the stable release, therefore the corresponding changes were done.

* Mon Dec 08 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.13-drbl1
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language file ca_ES was updated. Thanks to René Mérou.

* Fri Dec 05 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.12-drbl1
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language files sk_SK was updated. Thanks to Ondrej Dzivy Balucha.
- Adding support for Debian 7.7.

* Mon Dec 01 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.11-drbl1
- Language files tr_TR for bash and perl were updated. Thanks to Volkan.

* Fri Nov 28 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.10-drbl1
- Bug fixed: failed to get the ethernet card for multicast in CentOS 7.
- Adding comments in the /etc/sysconfig/dhcpd which is not used anymore for CentOS/Fedora using systemd.

* Fri Nov 28 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.9-drbl1
- Bug fixed: for CentOS 7, there is no need to copy the modified halt and rc.sysinit files for DRBL client.

* Fri Nov 28 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.8-drbl1
- Adding support for CentOS 6.6.

* Thu Nov 27 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.7-drbl1
- Bug fixed: drbl-etc-hosts failed to put the correct hostname for drbl clients in some cases.

* Wed Nov 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.6-drbl1
- Bug fixed: when one of the assigned IP addresses for DRBL clients is used by DRBL server, drblpush failed to deploy that completely.

* Tue Nov 25 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.5-drbl1
- A mechanism to check if i386 library (libc6-i386 or glibc.i686) exists on x86-64 system when running makeboot.sh due to syslinux included in Clonezilla live is 32-bit.

* Wed Nov 12 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.4-drbl1
- Supporting i586 linux image kernel for clients on Debian Sid.

* Mon Nov 10 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.3-drbl1
- Bug fixed: Service statd in Ubuntu 14.10 was not started for locking files.
- The service plymouth should not be set as manual otherwise for DRBL client X won't start.

* Mon Nov 10 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.2-drbl1
- Bug fixed: missing drbl-all-service was restored.

* Sun Nov 09 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.1-drbl1
- A better mechanism (function is_systemd_init) to detect if systemd used as init was implemented.
- Bug fixed: for Ubuntu 14.10, there is no corresponding service name in /etc/init.d/. We should use universal way to deal with service start and stop, i.e. using command "service".

* Wed Nov 05 2014 Steven Shiau <steven _at_ clonezilla org> 2.11.0-drbl1
- Updating network installation of Ubuntu as "trusty utopic".

* Wed Nov 05 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.7-drbl1
- Adding initial support for Ubuntu 14.10.
- Updating drbl-client-boot-default.conf and S00wait-drbl-default for Ubuntu DRBL clients.

* Sun Nov 02 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.6-drbl1
- Language file es_ES was updated. Thanks to Juan Ramón Martínez.
- Language files tr_TR for bash and perl were updated. Thanks to Volkan.
- Updating function gen_CDG_checksums of drbl-functions to make more compatible with markdown format.
- Bug fixed: for class C network, using 253 clients was not working. Thanks to Eric Frost for reporting this issu.

* Thu Oct 02 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.5-drbl1
- Updating scientific_netinstall_ver as 7x, and centos_netinstall_ver as "6 7" in drbl-ocs.conf.
- Adding syslinux-efi in the required packages for Debian. Otherwise uEFI network booting client won't work.
- Updating drbl-netinstall for CentOS 7 by adding inst.repo boot parameter.

* Mon Sep 29 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.4-drbl1
- Updating drbl-live-hadoop to version 0.3 from Thomas Tsai.

* Sun Sep 28 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.3-drbl1
- Language files were updated for restoring image of a partition to different partition.

* Wed Sep 17 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.2-drbl1
- Comments about uEFI network booting were updaetd in generate-pxe-menu.
- Reverted to use iproute instead of iproute2 so that Wheezy won't fail.

* Mon Sep 15 2014 Steven Shiau <steven _at_ clonezilla org> 2.10.1-drbl1
- Merging the files supporting systemd for CentOS 7 and Fedora 20 from Ceasar Sun.

* Fri Sep 05 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.22-drbl1
- Package davfs2 and f2fs-tools were added in the packages list of DRBL/Clonezilla live.

* Thu Sep 04 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.21-drbl1
- Adding package iw and list iproute2 instead of iproute in packages list of DRBL/Clonezilla live.

* Wed Aug 27 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.20-drbl1
- Package sysvinit-core is removed from drbl.conf because Ubuntu does not have it yet. We have to add that in the packages list when creating Debian-based live system.

* Tue Aug 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.19-drbl1
- A better checking mechaism for sysvinit and systemd packages coexisting on a system is used.
- Program drbl-prepare-pxelinux was updated due to new path for new syslinux-efi has syslinux.efi in /usr/lib/SYSLINUX.EFI/.

* Sun Aug 24 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.18-drbl1
- A workaround to avoid the bug of dpkg version 1.17.13. It fails to update /var/lib/dpkg/available in bootstrap environment. Therefore the option --print-avail fails. We switched to use "dpkg -L" in function chk_deb_installed of drbl-functions.

* Fri Aug 22 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.17-drbl1
- Put sysvinit-core in the packages list of clonezilla/debian/gparted live of drbl.conf. This is due to the pacakge init has switched to the default init system to systemd-sysv. We are not ready for that yet.

* Tue Aug 19 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.16-drbl1
- Language file tr_TR was added. Thanks to Ömer YILDIZ <oyildiz _at_ teknoplan.com.tr> for providing that.

* Sat Aug 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.15-drbl1
- Adding firstboot.DBN7.6.drbl for updated Debian Wheezy.

* Sat Aug 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.14-drbl1
- Adding package syslinux-util in PKG_TO_QUERY of drbl.conf.

* Sat Aug 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.13-drbl1
- Package syslinux-utils is now added in the packages list of Clonezilla and DRBL live due to the changes in Debian syslinux 6.03-pre19 packaging.

* Tue Aug 12 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.12-drbl1
- Package rfkill was added in the packages list of Clonezilla and DRBL live.

* Wed Aug 06 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.11-drbl1
- Package fstransform was added in the packages list of Clonezilla and DRBL live.
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Wed Jul 09 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.10-drbl1
- Bug fixed: drbl-sha1pass failed due to "use" instead of "require" was used. Thanks to monkeyzilla <monkeyzilla _at_ users sf net> for reporting it.

* Thu Jun 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.9-drbl1
- Language files sk_SK was updated. Thanks to Ondrej Dzivy Balucha.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language file es_ES was updated. Thanks to Alex Ibáñez López.
- Bug fixed: file memdisk of pxelinux 6.x should be put in /tftpboot/nbi_img/, not in /tftpboot/nbi_img/bios/.

* Tue Jun 24 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.8-drbl1
- Language file de_DE was updated. Thanks to Michael Vinzenz.

* Mon Jun 23 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.7-drbl1
- Language file ca_ES was updated. Thanks to René Mérou.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.

* Sun Jun 22 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.6-drbl1
- Language file es_ES was updated by Juan Ramón Martínez.

* Sun Jun 22 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.5-drbl1
- Program makeboot.sh was patched by Ceasar Sun to support xfs, ufs and ffs.
- Language files were improved. Thanks to Philippe Prevost <philippe-prevost _at_ hotmail com>.

* Sun Jun 01 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.4-drbl1
- The usage of drbl-sl was updated to latest version number, and the text shown on PXE boot menu for zip should be the same as that of iso one.

* Fri May 30 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.3-drbl1
- Language files for Slovak were added. Thanks to Ondrej Dzivy Balucha <balucha _at_ horizon sk> for providing this.
- Bug fixed: The ca_ES of perl file linking was missing in Makefile of language dir.
- Switching to use debconf-set-selections to preconfigure settings.

* Mon May 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.2-drbl1
- A program "drbl-live-hadoop" was added. This is still in testing.
- Language files were updated for ocs-img-2-vdk.

* Wed May 21 2014 Steven Shiau <steven _at_ clonezilla org> 2.9.1-drbl1
- The grep function "NEWER" was renamed as "GREP_NEWER" and defined only in drbl-functions, used for all related scripts.
- Program drbl-list-tarball was renamed as list_available_tarball.
- Program list_latest_tarball was added and used in function get_syslinux_binary_for_dos_linux of drbl-functions.

* Sat May 17 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.25-drbl1
- Package diskscan was added in Clonezilla live packages list.

* Sat May 10 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.24-drbl1
- Bug fixed: Starting IP address of the range was not used. Thanks to Andrew Parker for reporting this issue (https://sourceforge.net/p/drbl/bugs/12/).

* Thu May 01 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.23-drbl1
- The doc URL was changed to drbl.org from drbl.sourceforge.net.

* Sun Apr 27 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.22-drbl1
- Adding modified halt and rc.sysinit for DRBL clients of CentOS 6.5.

* Sat Apr 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.21-drbl1
- Adding firstboot.DBN7.5.drbl for Debian 7.5.

* Sat Apr 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.20-drbl1
- It's rpcbind-boot service only, we do not have to modify portmap.conf for Ubuntu 12.04.
- A workround to keep console in vt 1 when booting for Ubuntu 12.04 in select-in-client mode.

* Sat Apr 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.19-drbl1
- Bug fixed: when in restoreparts mode, "-t" option should be set by default (drbl-functions).

* Wed Apr 23 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.18-drbl1
- File set-netboot-1st-efi-nvram should be in Clonezilla.

* Wed Apr 23 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.17-drbl1
- Updating comments in drblpush for dhcpd.conf.

* Sat Apr 19 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.16-drbl1
- Updating network installation list for Ubuntu as "precise and trusty" in drbl.conf.

* Sat Apr 19 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.15-drbl1
- Removing "mkdir /run/rpcbind" in init.drbl because it's useless.
- The rpcbind-boot.conf instead of rpcbind.conf for drbl clients is modified to be start on startup. This fixed the issue that when init starts, the dir /run/rpcbind/ does not exist.
- The plymouth related part in /etc/init/rc.conf was disabled otherwise when select-in-client mode of clonezilla is run in vt1, the virtual console will be switched to vt7.
- Program drbl-client-root-passwd failed on Ubuntu 14.04, so updating the function create_chpasswd_env of drbl-functions.

* Fri Apr 18 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.14-drbl1
- Bug fixed: "service mountall start" in drbl-client-boot.conf of Ubuntu 12.04 drbl client should not be commented. Previous change should be reverted.

* Fri Apr 18 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.13-drbl1
- Adding comment when modifying a file in function switch_upstart_service of drbl-functions.
- customized plymouth.conf for Ubuntu 12.04 drbl clients was added. This is a workaround to https://bugs.launchpad.net/ubuntu/precise/+source/mountall/+bug/1233610

* Wed Apr 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.12-drbl1
- Appending "-" in the default hostname prefix of drblpush.
- Program drbl-etc-hosts was updated to work with the default hostname prefix.
- The function get_gdm_kdm_conf_filename of drbl-functions was updated to find and create the lightdm.conf for Ubuntu 14.04.

* Wed Apr 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.11-drbl1
- Adding Ubuntu 14.04 support.
- The dir /run/rpcbind should be created by init.drbl so that when rpcbind service starts, it can touch the files under the path.

* Sat Apr 12 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.10-drbl1
- Adding variable drbl_nfs_prot in drbl.conf.
- Adding nfs4 support in mknic-nbi. The whole support for nfs4 in drbl is not ready yet.

* Sat Apr 12 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.9-drbl1
- Unmounting bind directory under /tftpboot/ if it exists. Otherwise when running "drblsrv -u", it might clean the bind source dir on system.

* Thu Apr 03 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.8-drbl1
- Bug fixed: Mageia's path for vmlinuz and initrd were changed. The corresponding changes were done in drbl-netinstall.
- The version of netinstall in drbl.conf was updated.

* Tue Apr 01 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.7-drbl1
- Bug fixed: drbl-prepare-pxelinux failed to copy correct *.c32 of bios to /tftpboot/nbi_img/. It caused amd64 system failed to boot via pxelinux, isolinux or syslinux.
- An option "-v" was added to drbl-prepare-pxelinux for verbose output.

* Sat Mar 29 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.6-drbl1
- Bug fixed: drbl-sl failed to detect iso file for file package >=5.17.

* Wed Mar 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.5-drbl1
- Bug fixed: the hostname assignment syntax was not working for perl <= 5.14.
 
* Wed Mar 26 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.4-drbl1
- The message when searching and copying mbr.bin is suppressed. 

* Tue Mar 25 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.3-drbl1
- Program drbl-ipcalc-list was updated by Ceasar Sun for some more checking.
- Only when old clients-of-*.txt exists it will be moved.

* Tue Mar 25 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.2-drbl1
- The support for using network class A and B on DRBL server was added.
- The default rule for hostname of clients was changed to ${prefix}${ip//./-}".
- The method to disable upstart service of Ubuntu client was improved.

* Mon Mar 24 2014 Steven Shiau <steven _at_ clonezilla org> 2.8.1-drbl1
- Initial support for using network class A and B on DRBL server.

* Sun Mar 23 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.40-drbl1
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez.
- Program drbl-ipcalc-list was updated by Ceasar Sun to support option "-r".
- Program drbl-ipcalc-range was removed because drbl-ipcalc-list has same feature.
- Program get-client-ip-list uses drbl-ipcalc-list, not drbl-ipcalc-range anymore.

* Wed Mar 19 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.39-drbl1
- Bug fixed: drbl-ipcalc-range was missing.

* Wed Mar 19 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.38-drbl1
- Program drbl-ipcalc-list was tuned so it's easier to read.
- A program drbl-ipcalc-range was added, and is used in get-client-ip-list to get correct DRBL class A or B layout's clients.

* Mon Mar 17 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.37-drbl1
- Two options were added to makeboot.sh: -L and -U. Patch provided by Ceasar Sun.

* Mon Mar 17 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.36-drbl1
- Program get-client-ip-list was updated with missing function "USAGE", and the codes were revised, too.
- Language files were updated.

* Sat Mar 15 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.35-drbl1
- A workaround to let DRBL live client start lightdm after nis was added in drbl-live.
- Program drbl-live was rewritten with more functions so it's easier to read.
- Usage message of drbl-ipcalc-list was updated.

* Fri Mar 14 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.34-drbl1
- Function parse_cmdline_option was improved to avoid some runtime error.

* Fri Mar 14 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.33-drbl1
- Variable "messages_shown_preference" in drbl.conf was moved to drbl-ocs.conf and renamed as "ocs_prompt_mode".

* Sat Mar 08 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.32-drbl1
- The codes of prepare-files-for-PXE-client were rewritten so that it's can be reused for drbl-prepare-pxelinux. An option "-p" was added to put pxelinux-related files only. 
- Bug fixed: the "-d" option of drbl-prepare-pxelinux failed to process EFI files of syslinux.

* Fri Mar 07 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.31-drbl1
- Program drbl-list-tarball was added to replace list_available_tbz2 and list_latest_tbz2.
- Program drbl-prepare-pxelinux and the function get_syslinux_binary_for_dos_linux of drbl-functions was modified to use syslinux xz tarball instead of bz2 tarball because the latest testing one does not provide bz2 format anymore.

* Wed Mar 05 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.30-drbl1
- The network-manager service of DRBL Ubuntu client is disabled. This issue exists specially on Ubuntu Saucy.

* Mon Mar 03 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.29-drbl1
- The variable msg_remember_poweroff_reboot_when_ocs_sr_is_done in language file ja_JP.UTF-8 was updated to avoid triggering jfbterm crash.

* Fri Feb 21 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.28-drbl1
- Function parse_cmdline_option of drbl-functions was updated to accept all print characters ([[:print:]]) since now we use eval to run it.

* Tue Feb 18 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.27-drbl1
- The prompt about running syslinux in stupid mode in makeboot.sh has been updated by adding "-d syslinux".

* Mon Feb 17 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.26-drbl1
- Return status of syslinux/extlinux in makeboot.sh will be checked.

* Sun Feb 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.25-drbl1
- Adding firstboot.DBN7.4.drbl for Debian 7.4.
- Adding unattended option (-b) to makeboot.sh.

* Sun Feb 09 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.24-drbl1
- Function parse_cmdline_option of drbl-functions was updated to accept more characters, including "[", "]", and ";".
- Program parted instead of fdisk is used in makeboot.sh to show the destination disk partition layout. Thanks to Ady (ady-sf _at_ hotmail com) for this suggestion.

* Thu Feb 06 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.23-drbl1
- Function parse_cmdline_option of drbl-functions was updated to accept pipe sign (|). Thanks to Fuchs (fusi1939 _at_ users sf net) for this suggestion.

* Tue Jan 28 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.22-drbl1
- Program makeboot.sh was improved. The directory "/syslinux" on the destination partition should be checked. If it does not exist, we should create it. Thanks to Ady (ady-sf _at_ hotmail com) for this suggestion.

* Mon Jan 20 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.21-drbl1
- Function put_syslinux_makeboot_for_usb_flash in drbl-functions and drbl-sl have been updated corresponding to the unification of syslinux and isolinux dirs in the Clonezilla/DRBL/GParted live iso and zip.
- A dir "/utils/win64" was added to be used to run syslinux in Win64 env.
- An option "-d syslinux" was added when running syslinux in makeboot.sh/makeboot.bat/makeboot64.bat. Thanks to Ady (ady-sf _at_ hotmail com) for this suggestion.

* Thu Jan 16 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.20-drbl1
- Language file ca_ES was updated. Thanks to René Mérou.

* Tue Jan 14 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.19-drbl1
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Thu Jan 09 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.18-drbl1
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Mon Jan 06 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.17-drbl1
- Adding package chntpw in the packages list for Clonezilla live.

* Fri Jan 03 2014 Steven Shiau <steven _at_ clonezilla org> 2.7.16-drbl1
- Adding package bcache-tools in the packages list for Clonezilla live.

* Thu Dec 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.15-drbl1
- Program drbl-prepare-pxelinux supports the path for testing version of syslinux.
- Program put_syslinux_makeboot_for_usb_flash put both files for syslinux and isolinux, in order to make versions consistent.

* Mon Dec 23 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.14-drbl1
- Spanish language file was updated. Thanks to Juan Ramón Martínez <jrmc77 _at_ terra es>.

* Wed Dec 18 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.13-drbl1
- Removing the testing words for options z5p and z6p in language files.

* Sun Dec 15 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.12-drbl1
- Bug fixed: mbr.bin should not be put in efi32 or efi64 dirs by drbl-prepare-pxelinux.

* Sun Dec 15 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.11-drbl1
- Adding firstboot.DBN7.3.drbl for Debian 7.3.

* Sun Dec 15 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.10-drbl1
- Bug fixed: drbl-prepare-pxelinux failed to prepare mbr.bin from syslinux 6 on Debian system.

* Thu Dec 12 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.9-drbl1
- One more sentence about ocs-cvtimg-comp was added in language files.

* Wed Dec 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.8-drbl1
- One more sentence about ocs-cvtimg-comp was added in language files.

* Tue Dec 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.7-drbl1
- Package pv was added in PKG_TO_QUERY of drbl.conf.

* Tue Dec 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.6-drbl1
- One more sentence about ocs-cvtimg-comp was added in language files.

* Sun Dec 08 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.5-drbl1
- Language files were updated by adding some sentences related to ocs-cvtimg-comp.

* Sun Dec 08 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.4-drbl1
- Language files were updated by adding some sentences related to ocs-cvtimg-comp.
- Comments were added in drbl-functions.

* Sun Dec 08 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.3-drbl1
- Language files were updated by adding some sentences related to ocs-cvtimg-comp.

* Sat Dec 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.2-drbl1
- Adding pixz in in PKG_FROM_DBN_MINIMAL_NEED of drbl.conf.

* Tue Nov 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.7.1-drbl1
- Adding isolinux and pxelinux in PKG_FROM_DBN_MINIMAL_NEED of drbl.conf. This is used for live system with syslinux version 6.

* Wed Nov 20 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.15-drbl1
- The "quiet" parameter will only be put for Debian or Ubuntu clients. Not for other distributions.

* Wed Nov 20 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.14-drbl1
- Bug fixed: plymouth.override for Ubuntu <= 13.10 will cause lightdm not starting. Therefore it's only used for Ubuntu >= 13.10.

* Wed Nov 20 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.13-drbl1
- Package htop was added in the Clonezilla live packaegs list.
- Auto-login for Ubuntu 13.10 client did not work.

* Tue Nov 19 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.12-drbl1
- "PATH" configuration of pxelinux only exists when version >= 5, so program generate-pxe-men should not add it when pxelinux version is < 5.

* Tue Nov 19 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.11-drbl1
- A better method to disable plymouth service was added for DRBL Ubuntu client.
- "quiet" was added in the boot parameters of DRBL clients.

* Tue Nov 19 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.10-drbl1
- Bug fixed: plymouth should not be started for DRBL clients on Ubuntu 13.10 when Clonezilla job is run.

* Tue Nov 05 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.9-drbl1
- Bug fixed: mbr.bin of syslinux was not put in /usr/share/drbl/syslinux/bios/.

* Tue Oct 29 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.8-drbl1
- Minor bug about udev if block in drblsrv was fixed.
- Temporarily removing isolinux and pxelinux from PKG_FROM_DBN_MINIMAL_NEED in drbl.conf due to the local boot issue for pxelinux 6.2 (http://www.syslinux.org/archives/2013-October/021010.html).

* Mon Oct 28 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.7-drbl1
- Adding CentOS 5.10 support.

* Mon Oct 28 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.6-drbl1
- Linking pxelinux module files in /tftpboot/nbi_img so it could be compatible with older version.

* Mon Oct 28 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.5-drbl1
- Bug fixed: drbl-prepare-pxelinux failed to put the efi part of upstream syslinux 6.
- Bug fixed: ldlinux.e32 and ldlinux.e64 should not be put in sys_pxelinux_v5p_required_c32 of drbl.conf.

* Sun Oct 27 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.4-drbl1
- Bug fixed: drbl-gen-pxe-nbi should not remove /tftpboot/nbi_img/{bootx64.efi,bootia32.efi}
- Adding more general network booting settings in dhcpd.conf for PXE and EFI clients. However, the config for EFI clients are not ready yet.

* Sun Oct 27 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.3-drbl1
- The extlinux won't be installed when "drblsrv -i" is run.

* Sun Oct 27 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.2-drbl1
* Files bootia32.efi and bootx64.efi should be prepared in /tftpboot/nbi_img/ in prepare-files-for-PXE-client.

* Sun Oct 27 2013 Steven Shiau <steven _at_ clonezilla org> 2.6.1-drbl1
- Adding firstboot.DBN7.2.drbl for Debian 7.2.
- Supporting pxelinux 6.

* Wed Oct 23 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.14-drbl1
- Updating netinstall versions of Ubuntu and Fedora in drbl.conf.

* Wed Oct 16 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.13-drbl1
- Adding pause 1 sec in drbl-live.

* Mon Oct 14 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.12-drbl1
- Bug fixed: drbl-ssi-client-prepare failed to set the autologin account for lightdm.

* Thu Oct 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.11-drbl1
- Adding option --ipv4 for tftpd-hpa because DRBL now does not support IPv6, and if we force to disable it by adding "ipv6.disable=1" in boot parameter, without using option --ipv4 the tftpd-hpa won't start (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=544089).

* Thu Oct 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.10-drbl1
- Adding a line feed before running mknic-nbi in drbl-live.

* Wed Oct 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.9-drbl1
- Bug fixed: mknic-nbi should be run in drbl-live. Because it is run in chroot when DRBL live is created. However, the variable use_run_in_initrd and use_dev_pts_in_initrd in initramfs' /etc/linuxrc.conf (i.e. "/usr/lib/mkpxeinitrd-net/initrd-skel/etc/linuxrc.conf") need to be updated in the run time. Otherwise it might cause some modules fail to be loaded.

* Tue Oct 08 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.8-drbl1
- Adding makeboot64.bat which runs syslinux64.exe.

* Mon Oct 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.7-drbl1
- Bug fixed: package name is dosfstools instead of mkdosfs in drbl.conf.

* Sun Oct 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.6-drbl1
- Adding mkdosfs in the packages list of drbl.conf for Debian system.

* Sun Oct 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.5-drbl1
- Adding txt2html in the packages list of drbl.conf for Debian system.

* Wed Oct 02 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.4-drbl1
- Bug fixed: Making mountkernfs.sh and mountdevsubfs.sh start with updating /etc/mtab, otherwise when it's run 2nd time with reload (e.g. mountkernfs.sh reload), it will complain. 

* Wed Sep 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.3-drbl1
- Removing localepurge in the Clonezilla live packages list. We have to install that in live-hook because localepurge >= 0.7.3 the preseeding has to be done before localepurge is installed (http://bugs.debian.org/724491).

* Wed Sep 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.2-drbl1
- Adding debconf-utils in the required packages list in drbl.conf due to the need for debconf-set-selections.

* Mon Sep 23 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.1-drbl1
- Removing those not supported release in drbl/setup/files/Ubuntu/, only 12.04, 12.10, 13.04, and 13.10 were kept now.
- Adding firstboot for Debian 7.1 DRBL client.

* Sun Sep 22 2013 Steven Shiau <steven _at_ clonezilla org> 2.5.0-drbl1
- Adding support for Ubuntu 13.10.

* Mon Sep 16 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.39-drbl1
- The unnecessary variables wget* in drbl.conf were removed.

* Thu Sep 12 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.38-drbl1
- The DRBL URL was changed as http://drbl.org from http://drbl.sf.net in drbl-syslinux-netinstall and generate-pxe-menu.

* Mon Sep 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.37-drbl1
- Removing hwinfo from live system packages list in drbl.conf because it's removed from Ubuntu Saucy and we use lshw instead.

* Mon Sep 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.36-drbl1
- Removing hal from live system packages list in drbl.conf.

* Sat Sep 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.35-drbl1
- Minor updates about the the question mark after $msg_are_u_sure_u_want_to_continue for language files.

* Sat Aug 31 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.34-drbl1
- Changed messages_shown_preference="cmd" in drbl.conf.

* Sat Aug 31 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.33-drbl1
- Netinstall for Debian Squeeze was removed in drbl.conf, while wheezy is kept.
- Variable msg_prompt_for_insert_USB_dev_if_necessary and msg_do_not_close_window_until_clone_finish in language files were updated.
- A variable messages_shown_preference was added in drbl.conf.

* Tue Aug 27 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.32-drbl1
- Bug fixed: drbl-all-service failed to stop or restart nfs-server in Fedora 17.

* Mon Aug 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.31-drbl1
- Bug fixed: nfs service was not started or stopped by drbl-all-service in CentOS 6. Thanks to hihcheng Huang (shihcheng0527 _at_ gmail com) for reporting this issue.

* Sun Aug 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.30-drbl1
- Bug fixed: option of switch-pxe-menu was changed to avoid confusion.
- Variable clonezilla_client_menu_label_prefix was added in drbl.conf.

* Sat Aug 24 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.29-drbl1
- Usage of drbl-client-switch was updated.
- Two contral variables, ocs_fsck_src_part and ocs_chk_img, were added in drbl-functions.

* Tue Aug 13 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.28-drbl1
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Sun Aug 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.27-drbl1
- Using gdisk-noicu in the packages list of Clonezilla live instead of gdisk (drbl.conf).

* Sat Aug 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.26-drbl1
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Sat Aug 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.25-drbl1
- Language file ca_ES was updated. Thanks to René Mérou.

* Fri Aug 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.24-drbl1
- The netinstall for Ubuntu in drbl.conf was updated as precise and raring.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.

* Wed Aug 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.23-drbl1
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez.

* Sun Jul 28 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.22-drbl1
- Language files were updated by adding some sentences related to prep-ocsroot.

* Fri Jul 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.21-drbl1
- Adding efibootmgr in the packages list for quering in drbl.conf.

* Tue Jul 23 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.20-drbl1
- Language files were updated. Words about updating EFI NVRAM were added.
- An option "-iefi" was added in in the restoring dialog menu.

* Tue Jul 23 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.19-drbl1
- Package "lsof" was added in the packages list of Clonezilla live.

* Tue Jun 18 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.18-drbl1
- Package efibootmgr was added in Clonezilla live packages list.

* Tue Jun 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.17-drbl1
- CentOS 6.4 support was added.

* Sun Jun 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.16-drbl1
- Bug fixed: a variable lib_NOT_2_be_copied_2_common_root in drbl.conf was added so that it's easier to exclude the /lib/live/mount dir, the mounting point of Debian live 3.x, when running drblpush.

* Sun Jun 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.15-drbl2
- Making the desktop icon files of drbl live as executable.

* Thu Jun 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.15-drbl1
- Bug fixed: drbl-client-boot.conf for Ubuntu 12.04 and 12.10 should be improved as that for Ubuntu 13.04. Otherwise lightdm won't start in DRBL client.

* Sun May 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.14-drbl1
- Bug fixed: "-r" option for Clonezilla might be duplicated when "-k1" option is enabled.

* Sat May 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.13-drbl1
- Bug fixed: for expert mode, the postrun action for Clonezilla live should be asked, not be skipped. Thanks to SourceJo for reporting this issue (https://sourceforge.net/p/clonezilla/discussion/Open_discussion/thread/3f3bb67d/?limit=25#5973).

* Fri May 17 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.12-drbl1
- Bug fixed: the dhcpd.conf created on Ubuntu 12.04 won't be started due to an extra "," in the end of name server list.

* Thu May 16 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.11-drbl1
- Program makeboot.bat was updated with a better mechanism to prevent run program on wrong disk.

* Wed May 15 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.10-drbl1
- Adding LSB info in modified service networking of DRBL clients.

* Tue May 14 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.9-drbl1
- Adding zfs-fuse in the Clonezilla/DRBL live CD packages list.

* Tue May 14 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.8-drbl1
- Bug fixed: the shared object exposed by the kernel, i.e. linux-vdso.so.1 and linux-gate.so.1, should be skipped when copying shared objects to /tftpboot/node_root/ since they do not exist on the file system. 
- Package sysklogd was replaced by rsyslog in the Clonezilla/DRBL live CD packages list.

* Sun May 12 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.7-drbl1
- Bug fixed: We should not overwrite the /etc/init.d/networking of Ubuntu's DRBL client. Since it's linked to /lib/init/upstart-job. 

* Sun May 12 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.6-drbl1
- Adding support for Debian Sid (ATM it's Jessie). The networking service for DRBL clients was added so that it's easier to deal with network status file.

* Thu May 09 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.5-drbl1
- Bug fixed: function drbl-functions failed to append /sbin/ in the PATH.

* Tue May 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.4-drbl1
- Adding package nwipe in the packages list of Clonezilla live.

* Mon May 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.3-drbl1
- The variable sys_pxelinux_required_c32 of drbl.conf was changed to sys_pxelinux_v5p_required_c32.
- Updating function put_syslinux_makeboot_for_usb_flash so that the menu.c32/vesamenu.c32/chain.c32 will always the same version with those downloaded c32 files.

* Mon May 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.2-drbl1
- Set "greeter-show-manual-login=true" for lightdm of DRBL client in drbl-login-switch.
- Function restore_lvm2_udevd_rules was moved from ocs-functions to drbl-functions because it's required for Clonezilla SE.
- Function disable_lvm2_udevd_rules was added in drbl-functions because it will be used in drblpush and ocs-lvm2-stop.

* Sat May 04 2013 Steven Shiau <steven _at_ clonezilla org> 2.4.1-drbl1
- Minor typo in en_US was fixed.
- Package lziprecover was added.
- Adding Ubuntu 13.04 in this release. Not well tested yet.

* Wed Apr 24 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.28-drbl1
- Putting OpenSuSe netinstall version as 12.3 in drbl.conf.

* Wed Apr 24 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.27-drbl1
- Making ldlinux.c32, libcom32.c32, libutil.c32 downloaded from tarball mode as 644, not vfat's 755.

* Sat Apr 20 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.26-drbl1
- Package f2fs-tools was added in the live CD packages list in drbl.conf.

* Wed Apr 17 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.25-drbl1
- Function put_syslinux_makeboot_for_usb_flash in drbl-functions was updated for Syslinux 5.x. Three more c32 modules are required.
- Bug fixed: swapon command should not be run in background in mkswapfile, otherwise swap size might be not counted immediately.

* Tue Apr 02 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.24-drbl1
- Suppress nm-tool stderr in drblpush in case the program is not installed.

* Mon Apr 01 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.23-drbl1
- If display manager is not found, skip the rest with different prompt in drbl-login-switch.

* Fri Mar 29 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.22-drbl1
- Bug fixed: function set_ocs_sr_extra_param in drbl-functions has been improved. If postrun action is assigned, we should not ask it.

* Fri Mar 29 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.21-drbl1
- Juan Ramón Martínez's email address in the language files were updated.

* Tue Mar 26 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.20-drbl1
- Bug fixed: i386 version of Clonezilla live was used when running drblpush with clonezilla_live_mode option 0. Thanks to Yitzon Belandria <yitzon _at_ gmail com> for this bug report.

* Mon Mar 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.19-drbl1
- Message msg_etherboot_5_4_is_required in drbl-sl was disabled.

* Mon Mar 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.18-drbl1
- When the DNS server in /etc/resolv.conf is 127.0.0.1 from network-manager, the real DNS got from nm-tool will be used for DRBL clients. 
- Excluding LXC network deivce lxc* because they won't be DRBL clients.

* Wed Mar 20 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.17-drbl1
- SHA256SUMS will be created by function gen_CDG_checksums.

* Wed Mar 13 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.16-drbl1
- DSL and Puppylinux were removed from the supporting list in drbl-sl.

* Mon Mar 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.15-drbl1
- Bug fixed: for restoreparts mode, we should not turn on "-g auto" option by default. 

* Wed Mar 06 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.14-drbl1
- Language files were updated. Words about Etherboot were removed.
- The prompt about etherboot requirement was removed from drblpush.

* Mon Mar 04 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.13-drbl1
- Adding keyutils in Clonezilla live packages lists. Thanks to Joe M. for this suggestion.
- Bug fixed: alias network card configuration can not be parsed. Thanks to Pat Gilbert <pat.gilbert _at_ gmail com> for reporting this issue.

* Fri Mar 01 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.12-drbl1
- Bug fixed: we should also test udevd since the udev on CentOS 5.9 is older version. Thanks to Aaron for reporting this issue.
- Files halt and rc.sysinit for CentOS 5.9's client were added.

* Fri Mar 01 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.11-drbl1
- File firstboot.DBN6.0.7.drbl for Debian 6.0.7 was added.

* Thu Feb 28 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.10-drbl1
- Bug fixed: extlinux should be required for Clonezilla live, not DRBL.

* Mon Feb 25 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.9-drbl1
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language file es_ES was updated. Thanks to Alex Ibáñez López.

* Thu Feb 21 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.8-drbl1
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Thu Feb 21 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.7-drbl1
- Language file ca_ES was updated. Thanks to René Mérou.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file de_DE was updated. Thanks to Michael Vinzenz.

* Sun Feb 17 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.6-drbl1
- Variable msg_ocs_param_srel was added in language files.
- An option -srel|--save-restore-error-log to force saving error log in the image dir was added in clonezilla SE related menu.

* Mon Feb 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.5-drbl1
- Adding firstboot.DBN7.0.drbl for Debian 7.0.

* Mon Feb 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.4-drbl1
- Bug fixed: typo in prepare-files-for-PXE-client.

* Mon Feb 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.3-drbl1
- Excluding linux kernel with name "-dbg" for Debian-based DRBL.
- Bug fixed: for Syslinux 5, 3 more files are required to be put in /tftpboot/nbi_img/, i.e. ldlinux.c32, libcom32.c32, libutil.c32.

* Sun Feb 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.2-drbl1
- Package udisks was added the packages list for Clonezilla live.  Thanks to fusi1939 for this suggestion.

* Thu Feb 07 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.1-drbl1
- Bug fixed: for Syslinux 5, 3 more files are required, i.e. ldlinux.c32, libcom32.c32, libutil.c32

* Tue Feb 05 2013 Steven Shiau <steven _at_ clonezilla org> 2.3.0-drbl1
- The patches from Ceasar Sun for Fedora 17/18 were applied.

* Tue Jan 29 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.6-drbl1
- Netinstall version for Fedora was changed to 18 in drbl.conf.
- Language file ca_ES for perl script was added. Thanks to René Mérou.

* Tue Jan 22 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.5-drbl1
- Files about fail-mbr.bin have been removed since now Partclone (>=0.2.58) has included that.

* Mon Jan 14 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.4-drbl1
- Bug fixed: makeboot.sh failed to run with path name containing white space.
- Lucid netinstall was removed from drbl.conf since another LTS (precise) is available already.

* Fri Jan 11 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.3-drbl1
- Bug fixed: drblpush failed to identify the new, different arch of iso for the alternative testing Clonezilla live on the repository.
- Language files (perl) were updated. 

* Thu Jan 10 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.2-drbl1
- Function active_proc_partitions was moved to ocs-functions from drbl-functions.
- An option "-s" to assign syslinux version was added to drbl-syslinux-netinstall.

* Tue Jan 08 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.1-drbl1
- Put option "-nogui" in the higher position of the menu.

* Thu Jan 03 2013 Steven Shiau <steven _at_ clonezilla org> 2.2.0-drbl1
- Checking if blkid exists in makeboot.sh. Adding a prompt about GPT disk.
- Package libdata-validate-ip-perl was added in the packages list for Clonezilla live.
- Some big changes in the Clonezilla codes, therefore increase the 2nd major version number.

* Wed Dec 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.52-drbl1
- Package extlinux was added in the packages list for DRBL so then Clonezilla.
- Program extlinux now will be put in dir util/linux/ in Clonezilla/DRBL/GParted live.

* Wed Dec 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.51-drbl1
- Comments in drbl-functions were updated.

* Tue Dec 25 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.50-drbl1
- Bug fixed: parse_cmdline_option in drbl-function failed to parse boot parameter containing "$" character. Thanks to kuen-shieh yang <kuenshieh _at_ gmail com> for reporting this issue.

* Mon Dec 24 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.49-drbl1
- Bug fixed: Program makeboot.sh should check the destination disk is MBR or not.

* Sun Dec 23 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.48-drbl1
- Adding package exfat-utils and exfat-fuse in Clonezilla live packages list.

* Sat Dec 22 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.47-drbl1
- Adding package tree in Clonezilla live packages list.

* Tue Dec 04 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.46-drbl1
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez

* Tue Dec 04 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.45-drbl1
- Language file zh_TW was updated.

* Tue Dec 04 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.44-drbl1
- Bug fixed: Wrong path for the rerun command of drbl-ocs.

* Tue Dec 04 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.43-drbl1
- Bug fixed: Wrong path for the rerun command of drbl-ocs.

* Mon Dec 03 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.42-drbl1
- Typo in scripts/bin/drbl-langchooser for Catalan was fixed.

* Mon Dec 03 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.41-drbl1
- Language file ca_ES was updated. Thanks to René Mérou.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Sat Dec 01 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.40-drbl1
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file ca_ES was updated. Thanks to René Mérou.
- Bug fixed: no more using cdebootstrap when creating Clonezilla/DRBL/GParted live, therefore the function create_live_required_debian_based_prompt in drbl-functions should check debootstrap, not cdebootstrap.

* Fri Nov 30 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.39-drbl1
- Language files were updated. Using "Catalan | català" instead of "Catalonia | Catalunya". 

* Fri Nov 30 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.38-drbl1
- Language files were updated.

* Fri Nov 30 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.37-drbl1
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Fri Nov 30 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.36-drbl1
- Bug fixed: drbl ocs-live mode failed to download i686 version of Clonezilla live in drblpush, because the file name should use *-i686-pae*.
- Bug fixed: drbl-fuu failed to deal with file name with white space. Thanks to <himaboy826 _at_ gmail com> for reporting this bug.

* Wed Nov 28 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.35-drbl1
- Language file ca_ES was added. Thanks to René Mérou and Innocent De Marchi.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language ca_ES was added in the Clonezilla live menu.

* Tue Nov 20 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.34-drbl1
- Language file es_ES of bash was updated and a typo in language file en_US was fixed. Thanks to Juan Ramón Martínez (JRMC77 _at_ terra es).

* Wed Nov 07 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.33-drbl1
- Bug fixed: A workaround to identify initrd on CentOS 5 was added in drbl-sl.

* Tue Nov 06 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.32-drbl1
- Bug fixed: DRBL_SCRIPT_PATH was not set in drbl-conf-functions. Thanks to explosions for reporting this issue.

* Sun Nov 04 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.31-drbl1
- Using syslinux/pxelinux 4.06 in drbl/clonezilla.

* Fri Nov 02 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.30-drbl1
- Adding mpg123 for Clonezilla live. It might be useful to play sound when Clonezilla job is done. Thanks to FlyFox for this idea.

* Thu Nov 01 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.29-drbl1
- Bug fixed: no more removing ip=frommedia for PXE client as live-boot 2.0.15-1.drbl15 and 3.x have no issue to use that. If it's removed, Ubuntu-based Clonezilla live won't enter rc-sysinit.conf until failsafe.

* Sun Oct 28 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.28-drbl1
- Bug fixed: typo of msg_autohostname_is_reserved_for_save_mode in en_US was fixed.

* Sat Oct 27 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.27-drbl1
- Bug fixed: the service listed in /etc/drbl/client-extra-service was not on on the client if it's not on on the server. Thanks to Odin Nøsen <odin _at_ gnuskole no> for reporting this issue.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.26-drbl2
- Files halt.CO6.3.drbl and rc.sysinit.CO6.3.drbl were added.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.26-drbl1
- Bug fixed: "drbl_syscfg" instead of "drbl_setup_cfg" should be used, and drbl_setup_cfg was removed from drbl.conf. Thanks to Odin Nøsen <odin _at_ gnuskole no> for reporting this issue.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.25-drbl1
- Bug fixed: exporting /opt/ should be appended, not overwritten the previous exported dir.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.24-drbl1
- Bug fixed: drbl clients should mount server's /opt/ when it is exported on server.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.23-drbl1
- Only when dir /opt exists, drbl-nfs-export will export that dir.

* Fri Oct 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.22-drbl1
- Bug fixed: /opt dir should be exported for NFS clients since some packages (e.g. google-chrome) will be installed in that dir. Thanks to Odin Nøsen <odin _at_ gnuskole no> for reporting this issue.

* Wed Oct 24 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.21-drbl1
- Bug fixed: version sorting option "-V" should be used with sort in function find_next_release_version_number.

* Wed Oct 24 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.20-drbl1
- A function find_next_release_version_number was added for using in creating Clonezilla/DRBL/GParted live.

* Thu Oct 18 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.19-drbl1
- Bug fixed: sort and uniq should not be used in init.drbl since these programs are not in /bin instead they are in /usr/bin. This will cause Debian and Ubuntu drbl client fail to boot.

* Thu Oct 18 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.18-drbl1
- Bug fixed: For Ubuntu 12.04 and 12.10, linux-image-extra should be installed to. So we can support more hardware for DRBL clients.
- Changed the default option for client's kernel arch to the same as server for Debian.

* Thu Oct 18 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.17-drbl1
- Bug fixed: dracut should not be listed in PKG_TO_QUERY, we have to put it in PKG_TO_QUERY_RH otherwise it will cause Ubuntu or Debian fail to finish drblsrv.

* Wed Oct 17 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.16-drbl1
- Bug fixed: Some more minor bugs fixed for Fedora 17 were applied.

* Tue Oct 16 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.15-drbl1
- Bug fixed: Some problem for linking /var/run and /var/lock on Fedora 17. Reverted to the previous status.

* Tue Oct 16 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.14-drbl1
- More comments were added for not getting IPv6 in drbl-get-ipadd and init.drbl.
- Bug fixed: Linked files /var/run and /var/lock were not copied in client's /var/.

* Sun Oct 14 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.13-drbl1
- Bug fixed: IPv6 address should not be gotten since for the NFS of DRBL only IPv4 is supported.

* Sat Oct 13 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.12-drbl1
- Bug fixed: kernel package of FC17 on repository could not be found.

* Fri Oct 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.11-drbl1
- Bug fixed: typos in drbl-all-service were fixed.
- Bug fixed: the warning about fine-tune rc.sysinit and halt should not be given for Fedora 17 since there is no such files exist.

* Fri Oct 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.10-drbl1
- Bug fixed: yum repository files drbl-*-list should use "$basearch" instead of "$ARCH" so that the architecture could be correct.
- Bug fixed: for CentOS/RHEL 6 or Fedora 17, dracut instead of mkinitrd is required. Therefore using PKG_TO_QUERY="mkinitrd dracut" in drbl.conf.

* Fri Oct 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.9-drbl1
- Bug fixed: YP update command for Fedora 17 was added.

* Fri Oct 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.8-drbl1
- Bug fixed: Some bugs for Fedora 17 were fixed.

* Thu Oct 11 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.7-drbl1
- Bug fixed: Failed to serve Fedora 17. The patches from Ceasar Sun were merged. Some minor bugs still have to be fixed later.
- Bug fixed: Files for Ubuntu 12.10 were added. It should be able to serve ubuntu 12.10.

* Tue Oct 02 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.6-drbl1
- Ubuntu Quantal netinstall was enabled in drbl.conf.

* Mon Oct 01 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.5-drbl1
- Avoiding the warning messages when running Debian 6.0.6.

* Mon Sep 24 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.4-drbl1
- Comments in drbl-ipcalc-list were updated.
- Bug fixed: drbl-ipcalc-list should skip network and broadcast IP address.
- Bug fixed: when OS_Version does not match, drblpush should use the most related rc.sysinit and halt files for clients. Othereise the possibility that clients fail to boot will be high.

* Wed Sep 05 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.3-drbl1
- A shell script "drbl-run-parts" was added.
- Package "crontabs" is no more required for Fedora as now we use drbl-run-parts.

* Mon Aug 27 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.2-drbl1
- Language files were updated. Variable "msg_autoproductname_is_a_reserved" was added, and a typo en en_US was fixed.

* Sun Aug 26 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.1-drbl1
- Bug fixed: /usr/share/drbl/{sbin,bin} was not in the PATH in init.drbl.
- Removing the vague "Something went wrong" prompts.

* Sat Aug 25 2012 Steven Shiau <steven _at_ clonezilla org> 2.1.0-1drbl
- Updating files in dir debian so less lintian warnings.

* Sat Aug 25 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.14-1drbl
- Files renamed, so using ocs-srv-live instead of ocs-srv-live.sh, drbl-sl instead of drbl-SL.sh.

* Fri Aug 24 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.13-1drbl
- Adding the interpreter's magic number for drbl-perl-functions, drbl-conf-functions, and drbl-functions to avoid lintian's warning.
- Updating debian/control to follow Debian's policy.
- To follow Debian's policy, the program drbl-SL.sh was renamed as drbl-sl, and drbl-live.sh was renamed as drbl-live.

* Wed Aug 22 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.12-1drbl
- A typo in language file en_US was fixed.  Thanks to René Mérou.
- Function gen_CDG_checksums will generate a html format for CHECKSUMS file.

* Mon Aug 20 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.11-1drbl
- Bug fixed: Failed to parse boot parameter like: "mount UUID=X /mnt" in grub booting. Thanks to nottaken37 for reporting this issue (https://sourceforge.net/projects/clonezilla/forums/forum/663168/topic/5133379).
- Variable msg_client_job_are_logged_in in language files was updated. Thanks to René Mérou.

* Sun Aug 19 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.10-1drbl
- Using $desktop_user_group_debian instead of hardcoded strings in drblpush.  Thanks to dwight (http://sourceforge.net/tracker/?func=detail&atid=537327&aid=3559290&group_id=73280).

* Fri Aug 17 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.9-1drbl
- Improvement: drbl-SL.sh now supports Clonezilla and GParted live zip file format.

* Mon Aug 13 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.8-1drbl
- Bug fixed: drblsrv-offline should be in /usr/sbin instead of /usr/share/drbl/sbi/.

* Sun Aug 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.7-1drbl
- A better way to append drbl-related PATH was adopted.

* Sun Aug 12 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.6-1drbl
- Using /usr/share/drbl instead of /usr/share/drbl/ so that no "//" in the PATH.

* Sat Aug 11 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.5-1drbl
- Function gen_CDG_checksums was added in drbl-funtions.

* Sat Aug 11 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.4-1drbl
- Function get_latest_pkg_in_drbl_repository was added in drbl-funtions.

* Thu Aug 09 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.3-1drbl
- Remove those related to "$DRBL_SCRIPT_PATH" from language files.

* Thu Aug 09 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.2-1drbl
- Bug fixed: get-assigned-hn-by-ip searched the wrong path.
- Put the GPL text file instead of COPYING because ocs-iso, create-*-live need that.
- Put the file license of fail-mbr.bin as BSD. Orgad Shaneh has decided the license.

* Wed Aug 08 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.1-1drbl
- Adding firstboot.DBN6.0.5.drbl for Debian 6.0.5.

* Mon Aug 06 2012 Steven Shiau <steven _at_ clonezilla org> 2.0.0-1drbl
- DRBL Version 2. New files arch so it's easier to be packaged in Debian.

* Wed Jul 25 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.19-1drbl
- Minor improving in set-default-pxe-img.
- The function get_pxecfg_image_block in drbl-functions should not be case sensitive for label name.

* Thu Jul 12 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.18-1drbl
- Language file de_DE was updated. Thanks to Michael Vinzenz.

* Thu Jul 05 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.17-1drbl
- Forcing to run "make -C /var/yp all", i.e. not only "make -C /var/yp", when updating YP in drblpush.
- Language files were updated. The warning about -z3 was removed. Thanks to mmx.

* Fri Jun 29 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.16-1drbl
- Some notes were added in drbl-sha1pass.

* Mon Jun 25 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.15-1drbl
- Program drbl-sha1pass was improved so that it will work for perl <=5.9.

* Tue Jun 19 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.14-1drbl
- Program mkswapfile was updated to skip mounting extended partition. Othewise it might be hang due to a mount bug.

* Mon Jun 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.13-1drbl
- Services ethtool, openssh-server and postfix were added to the checklists in start-srv-after-ifup.
- Skip removing /lib/init/rw in Debian clients during bootinig.

* Sun Jun 17 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.12-1drbl
- Environmental ADDRFAM=inet was added in start-srv-after-ifup so that mountnfs in if-up.d/ will be run.

* Tue Jun 12 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.11-1drbl
- Package ddrescue was removed from the packages list of Clonezilla live because it's no more in Debian Sid, and we already have gddrescue. Ref: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=677101

* Tue Jun 12 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.10-1drbl
- Updating Fedora netinstall as 17 in drbl.conf.
- Updating function output_netinstall_syslinux_pxelinux_menu in drbl-functions so that Fedora 17 netinstall boot parameter inst.repo could be generated.

* Thu May 24 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.9-1drbl
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Fri May 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.8-1drbl
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.

* Fri May 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.7-1drbl
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Fri May 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.6-1drbl
- Bug fixed: drbl-SL.sh failed to find vmlinuz for Clonezilla live iso in OpenSuSE 11.3. Thanks to melnikok for this bug report.

* Fri May 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.5-1drbl
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file es_ES was updated. Thanks to Alex Ibáñez López.
- Package cifs-utils instead of smbfs is listed as Clonezilla live package in drbl.conf. Ref: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=620847

* Fri May 04 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.4-1drbl
- Netinstall for Ubuntu has changed to "lucid oneiric precise" in drbl.conf.

* Thu May 03 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.3-1drbl
- Using Digest::SHA instead of Digest::SHA1 in drbl-sha1pass.

* Wed May 02 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.2-1drbl
- TIMED_LIGHTDM_TIME_DEFAULT="30" was added in drbl.conf.
- Autologin/Normallogin/Timelogin was added for lightdm in drbl-login-switch.
- Program drbl-client-root-passwd now supports Ubuntu 12.04.

* Tue May 01 2012 Steven Shiau <steven _at_ clonezilla org> 1.12.1-1drbl
- Removing libdigest-sha1-perl from drbl.conf. It's no more in new GNU/Linux.
- Using "udev" instead of "none" for mounting /dev in DRBL clients.
- File drbl-client-boot.conf for Ubuntu 12.04 was added.
- File drblpush was modified to make drbl work on Ubuntu 12.04.
- A better file drbl-client-boot.conf for Ubuntu 11.10 was added. This should fix the issue that keyboard and mount not working on DRBL clients. Thanks to timothyshelley for reporting this issue.  Ref: https://sourceforge.net/projects/drbl/forums/forum/394008/topic/5189191

* Tue Apr 17 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.15-1drbl
- Language files were updated.

* Mon Apr 09 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.14-1drbl
- Language files were updated.

* Sun Apr 08 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.13-1drbl
- Package vlan was added in Clonezilla live packages list in drbl.conf. Thanks to ggarland <ggarland_99 _at_ yahoo com> for this suggestion.

* Sat Apr 07 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.12-1drbl
- Wicd autostart in DRBL clients is disabled in DRBL live.

* Tue Apr 03 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.11-1drbl
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Tue Mar 27 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.10-1drbl
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Sun Mar 25 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.9-1drbl
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.

* Sun Mar 18 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.8-1drbl
- Adding packages dnsutils for Clonezilla live.
- Adding package syslinux in drbl-bug-report.

* Sun Mar 11 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.7-1drbl
- Bug fixed: regular expression in  list_available_rpm was fixed.

* Sat Mar 10 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.6-1drbl
- Forcing drbl-prepare-pxelinux to be run in drblsrv-offline if gpxelinux.0 is not found. Thanks to Tomas Moler for reporting this issue.

* Thu Mar 01 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.5-1drbl
- Updating opensuse netinstall as 12.1 in drbl.conf.

* Thu Feb 23 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.4-1drbl
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez (JRMC77 _at_ terra es).

* Tue Feb 14 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.3-1drbl
- Bug fixed: function get_syslinux_binary_for_dos_linux in drbl-functions failed to get the latest version.

* Sat Feb 11 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.2-1drbl
- Language files were updated.

* Thu Feb 02 2012 Steven Shiau <steven _at_ clonezilla org> 1.11.1-1drbl
- Language files were updated.
- Option -fsck-src-part-y was added for dialog menus about running fsck with option -y in drbl-functions.

* Tue Jan 31 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.90-1drbl
- Network installation for Fedora has been updated to 16 in drbl.conf.
- The mode of Language file zh_CN.UTF-8 is changed to 644.

* Tue Jan 31 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.89-1drbl
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Files firstboot.DBN6.0.4.drbl and firstboot.DBN6.0.3.drbl were added.

* Mon Jan 30 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.88-1drbl
- The updates repository path of Centos 6 was added in drblsrv.

* Wed Jan 25 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.87-1drbl
- Put grub-pc instead of dummy package grub in the packages list of Clonezilla live.

* Mon Jan 23 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.86-1drbl
- Package sysklogd was added back in the packages list of Clonezilla live, which was due to the new initscripts (2.88dsf-16) breaking it.

* Mon Jan 23 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.85-1drbl
- Function disable_apt_lang_translation was added in drbl-functions.

* Mon Jan 23 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.84-1drbl
- Language file es_ES was updated. Thanks to Alex Ibáñez López.

* Sat Jan 21 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.83-1drbl
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.

* Fri Jan 20 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.82-1drbl
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file es_ES was updated. Thanks to Alex Ibáñez López.
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Fri Jan 20 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.81-1drbl
- Language files were updated.

* Fri Jan 20 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.80-1drbl
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- File drbl-functions was updated for the option -icds of drbl-ocs and ocs-sr.

* Tue Jan 10 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.79-1drbl
- Language files were updated.

* Tue Jan 10 2012 Steven Shiau <steven _at_ clonezilla org> 1.10.78-1drbl
- Language files were updated.

* Wed Dec 28 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.77-1drbl
- Use syslinux/pxelinux 4.05 in drbl/clonezilla.

* Thu Dec 22 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.76-1drbl
- Package pv (pipe viewer) was added in the packages list of Clonezilla live. (https://sourceforge.net/tracker/?func=detail&atid=671653&aid=3463112&group_id=115473).

* Wed Dec 21 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.75-2drbl
- Typo in changelog fixed. It should be CentOS 6.2 support was added.

* Wed Dec 21 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.75-1drbl
- CentOS 6.1 support was added.

* Wed Dec 21 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.74-1drbl
- Package sysklogd was removed temporarily in the packages list of Clonezilla live due to the new initscripts (2.88dsf-16) breaks it.

* Tue Dec 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.73-1drbl
- Desktop icon file Grandr.desktop was replaced by Display.desktop.

* Wed Dec 14 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.72-1drbl
- More improvements to make Fedora 14 and CentOS 5/6 DRBL clients reboot faster. Remove those unnecessary file systems mounting and unmounting. Thanks to Robert Arkiletian for helping this issue.

* Wed Dec 14 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.71-1drbl
- CentOS 6.1 support was added.
- Bug fixed: /dev/shm and tmpfs won't be umounted or remounted when halting or reboot in Fedora 14 and CentOS 5/6. This will make Fedora 14/CentOS 6 DRBL clients halt and reboot faster. Thanks to Robert Arkiletian for this bug report.

* Mon Dec 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.70-1drbl
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez (JRMC77 _at_ terra es).

* Mon Dec 05 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.69-1drbl
- Bug fixed: Failed to create SSI template tarball if only Clonezilla box mode or SSI mode is enabled, while the rest if full mode. Thanks to hsueh.chih.sun for reporting this issue.

* Wed Nov 30 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.68-1drbl
- The option "-z7" was added in the Clonezilla-related TUI menus.
- Language files were updated.

* Fri Nov 25 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.67-1drbl
- Package libdigest-sha1-perl was removed from the list of Clonezilla live. Since for Sid the perl has built-in function. (Ref: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=591091).

* Mon Nov 21 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.66-1drbl
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Sat Nov 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.65-1drbl
- Language file pt_BR was updated. Thanks to Marcos Pereira da Silva Cruz. 
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Language file es_ES was updated. Thanks to Alex Ibáñez López.
- Packages dirvish, rsnapshot, and lrzip were added in the Clonezilla live packages list in drbl.conf. Package crontabs, which provides run-parts, was added in PKG_FROM_RH in drbl.conf.

* Thu Nov 10 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.64-1drbl
- Language file es_ES was updated. Thanks to Alex Ibáñez López.

* Mon Nov 07 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.63-1drbl
- Language files were updated.

* Sun Nov 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.62-1drbl
- Language files were updated.
- Function get_sort_V_opt was added in drbl-functions.
- Program get-client-ip-list was improved with better sorting.
- Bug fixed: get-client-ip-list failed to give correct clients' IP addresses if server's IP address is in the range in dhcpd.conf.
- Use function get_sort_V_opt in drblsrv.
- The missing icons of Grandr.desktop and GParted.desktop on DRBL live have been fixed.

* Thu Nov 03 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.61-1drbl
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Package acpi was added in Clonezilla live.

* Wed Nov 02 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.60-1drbl
- Language file de_DE was updated. Thanks to Michael Vinzenz.
- Default not to turn on "-fsck-src-part".

* Mon Oct 31 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.59-1drbl
- Language file fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Fri Oct 28 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.58-1drbl
- Language files were updated.

* Tue Oct 25 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.57-1drbl
- Ubuntu 11.10 support was added. //NOTE// This is not finished yet.
- S00wait-drbl was added in /etc/rcS.d so rcS won't start too fast in Ubuntu's upstart.
- YP is configured not to show hashed password. Thanks to Robert Arkiletian <robark _at_ gmail com>.

* Fri Oct 21 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.56-1drbl
- Language files were updated.

* Thu Oct 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.55-1drbl
- Language files were updated.

* Thu Oct 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.54-1drbl
- Put "wait" command in the end of drbl-doit so it won't enter shell before the jobs are done.

* Thu Oct 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.53-1drbl
- Language files were updated.

* Thu Oct 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.52-1drbl
- Language files were updated.

* Mon Oct 17 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.51-1drbl
- Language files were updated.
- Function get_existing_language in drbl-functions was updated to show locales in natual language, not locales.

* Mon Oct 17 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.50-1drbl
- Program cpufrequtils was added in Clonezilla live packages list.

* Sat Oct 15 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.49-1drbl
- Wallpaper image files for Clonezilla live grub2 boot menu were added.

* Sun Oct 02 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.48-1drbl
- The year of copyright in the boot menu was updated.
- The dir /dev/shm of the DRBL client is created with mode 1777. The makes Google Chrome can run.
- The tmpfs dirs (/dev/pts, /dev/shm, /sys, /proc) are shown in DRBL client's /etc/fstab.

* Thu Sep 29 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.47-1drbl
- Bug fixed: tmpfs file systems should not be umounted in boot.localfs of OpenSuSE 11.3.

* Mon Sep 26 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.46-1drbl
- The usage of drbl-syslinux-netinstall was updated.
- Bug fixed: Wrong function name USAGE in mknic-nbi.

* Tue Sep 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.45-1drbl
- Language files updated.

* Tue Sep 20 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.44-1drbl
- Files rc.sysinit.CO5.7.drbl and halt.CO5.7.drbl were added.

* Sun Sep 18 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.43-1drbl
- Improvement: Now the RPM repositories of drbl stable/testing/unstable won't be mixed. They will be separate.

* Sat Sep 17 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.42-1drbl
- Bug fixed: Function make_random_password in drbl-functions failed to separate "[", "]", and $ is not escaped. Thanks to Robert Arkiletian for this bug report.
- Bug fixed: drbl-prepare-pxelinux might fail due to a file belongs to 2 RPM packages.

* Mon Sep 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.41-1drbl
- Bug fixed: Function parse_cmdline_option in drbl-functions was improved. Make the parsing for ocs_lang="" correct.

* Sat Sep 10 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.40-2drbl
- Spec file was modified to use noarch instead of i386.

* Thu Sep 08 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.40-1drbl
- Function parse_cmdline_option in drbl-functions was improved to accept the /proc/cmdline parsed by grub2 1.99. Now it works for 3 cases in /proc/cmdline: E.g. (1) ocs_prerun="sleep 5" (2) ocs_prerun=\"sleep 5\" and (3) "ocs_prerun=sleep 5".

* Wed Aug 31 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.39-1drbl
- Language files updated.

* Wed Aug 31 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.38-1drbl
- Option "-irhr" was added in dcs.
- Language files updated.

* Wed Aug 24 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.37-1drbl
- To avoid the failure message during RH-like Linux booting, "true" was added in firstboot instead of just commenting the command.
- Program arm-wol was improved to exit with correct retval.
- This version should be ready for CentOS 6.0.

* Tue Aug 23 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.36-1drbl
- Bug fixed: Wrong path for RH_RPMS_os_update_dir of CentOS 6 in drblsrv.

* Mon Aug 22 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.35-1drbl
- Netinstall for CentOS has been moved to 5 and 6 in drbl.conf.
- CentOS 6.0 support was added.
- Service nfs and nfslock were not restarted when running "drbl-all-service restart" on CentOS 6.0.

* Mon Aug 22 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.34-1drbl
- Language files updated.

* Mon Aug 22 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.33-1drbl
- Bug fixed: For Ubuntu 10.10 and 11.04, i586 kernel should not be an option.

* Tue Aug 16 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.32-1drbl
- Program list_latest_deb was updated to use "ls -v" methoed.
- Program partclone-utils was added in Clonezilla live packages list.

* Sun Aug 14 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.31-1drbl
- Language file en_US was slightly updated.

* Sat Aug 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.30-1drbl
- File firstboot.DBN6.0.2.drbl was added.

* Sat Aug 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.29-1drbl
- Bug fixed: fail to test if "sort -V" works or not.

* Fri Aug 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.28-1drbl
- Version sorting (--version-sort) of sort will be used when sorting the kernels of CentOS if it's found (Not working for CentOS 5.6).
- /dev/pts won't be mounted in initrd when /run is not mounted (mknic-nbi).

* Fri Aug 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.27-1drbl
- "devpts" is used for /dev/pts on the client's /etc/fstab.
- Two more flags were implemented in mknic-nbi: use_run_in_initrd and use_dev_pts_in_initrd.

* Fri Aug 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.26-1drbl
- Files rc.sysinit and halt for CentOS 5.6 client were added.

* Thu Aug 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.25-1drbl
- German language file was added. Thanks to Michael Vinzenz <michael.vinzenz _at_ scalaris com>.

* Sat Aug 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.24-1drbl
- The execution of drbl-prepare-memtest and drbl-prepare-pxelinux were moved to drblsrv-offline from drblsrv.

* Sat Aug 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.23-1drbl
- Program drblsrv-offline supports linux kernel 3. 

* Fri Aug 05 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.22-1drbl
- A prompt was added if ntfsprogs will be installed in Debian Linux.
- The Makefile in lang dir was not updated for de_DE.

* Fri Aug 05 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.21-1drbl
- German language files were added. Thanks to Michael Vinzenz <michael.vinzenz _at_ scalaris com>.
- Since ntfs-3g in Debian Sid provides ntfsprogs, we should not include that in PKG_FROM_DBN of drbl.conf. A dynamic detection was added in drblsrv.

* Thu Aug 04 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.20-1drbl
- Program mknic-nbi supports linux kernel 3.
- Language file es_ES of bash was updated. Thanks to Juan Ramón Martínez (JRMC77 _at_ terra es).
- If dir /run is found on server, add that in /tftpboot/node_root/.
- Program gawk has some dynamic libs in /usr/lib, so drblpush must prepare that, too.

* Wed Jul 27 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.19-1drbl
- "oneiric" was added in the netinstall of drbl.conf, while maverick was removed.

* Tue Jul 26 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.18-1drbl
- Restored "ntfs-3g" in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf. It's not duplicated.

* Tue Jul 26 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.17-1drbl
- Duplicated "ntfs-3g" was removed from PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf.

* Fri Jul 22 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.16-1drbl
- Package fbcat was listed for Clonezilla live instead of fbgrab in drbl.conf.

* Mon Jul 18 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.15-1drbl
- Function parse_cmdline_option of drbl-functions was updated to allow ">,^, or *".

* Wed Jul 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.14-1drbl
- Function parse_cmdline_option of drbl-functions was updated to allow "$" because it is required by samba share with hidden share. Thanks to nottaken37. (Ref: https://sourceforge.net/projects/clonezilla/forums/forum/663168/topic/4589215)

* Thu Jun 23 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.13-1drbl
- Language files were updated.
- Big5 language files for traditional Chinese were removed. Now only UTF-8 is supported.

* Sun Jun 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.12-1drbl
- Language file for Brazilian Portuguese (pt_BR) was added. Thanks to Marcos Pereira da Silva Cruz <marcospcruz _at_ gmail com>.

* Mon May 30 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.11-1drbl
- A workaround was added to solve ntfs-3g and ntfsprogs conflict in Debian Sid. However, a better method should be implemented in the future.

* Thu May 26 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.10-1drbl
- Netinstall version for fedora was updated to 15 in drbl.conf.

* Thu May 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.9-1drbl
- Patch from Ceasar Sun was applied so that drbl-netinstall could support Mageia. 

* Thu May 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.8-1drbl
- Program drbl-netinstall was updated to work with Scientific Linux 6.
- Switch to use 6x as the default netinstall version for Scientific Linux in drbl.conf.

* Fri May 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.7-1drbl
- Program drbl-SL.sh was improved to work with XZ compression initrd.

* Fri May 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.6-1drbl
- Version number of syslinux can be assigned in get_syslinux_binary_for_dos_linux & put_syslinux_makeboot_for_usb_flash of drbl-functions.
- By default the syslinux_binsrc_url in drbl.conf is set as "http://free.nchc.org.tw/syslinux".

* Tue May 03 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.5-1drbl
- Bug fixed: test before reading /etc/lsb-release in drbl-functions.

* Tue May 03 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.4-1drbl
- Bug fixed: The method to decide using insserv or update-rc.d failed.

* Tue May 03 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.3-1drbl
- A better method to decide using insserv or update-rc.d for Debian and Ubuntu was implemented in drbl-client-switch and drblsrv.

* Tue May 03 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.2-1drbl
- An option "-d|--deploy-to-system-too" was added to drbl-prepare-memtest and drbl-prepare-pxelinux.
- A better method to decide using insserv or update-rc.d for Debian and Ubuntu was implemented in drbl-all-service and drbl-client-service.

* Mon May 02 2011 Steven Shiau <steven _at_ clonezilla org> 1.10.1-1drbl
- A better method to decide using insserv or update-rc.d for Debian and Ubuntu was implemented in drblpush.
- Ubuntu 11.04 was supported in this release.

* Sun May 01 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.23-1drbl
- By default in mknic-nbi we switch to not including all firmwares in initrd, because what "modinfo -F firmwares" should be trusted.

* Thu Apr 28 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.22-1drbl
- Function parse_cmdline_option of drbl-functions was updated to allow "@" because it is required by sshfs.

* Tue Apr 26 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.21-1drbl
- Minor improvement for drbl-prepare-memtest.
- The variable syslinux_binsrc_url in drbl.conf was updated.
- Typos "comamnd" were fixed. Thanks to pascaldevuyst for reporting this.
- The program drbl-prepare-pxelinux was added, so no more binary pxelinux-related files in drbl package.

* Tue Apr 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.20-1drbl
- Program get_memtest86+.sh was removed, since drbl-prepare-memtest has replaced it.
- Program list_available_tbz2 was slightly improved.
- Function get_syslinux_binary_for_dos_linux was improved to automatically detect the latest version of syslinux.

* Tue Apr 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.19-1drbl
- The "gPXE" part is replaced by "iPXE".
- "insserv", if found, will be used in drbl-client-service, drbl-all-service, drblsrv, and drblpush for Debian environment.

* Sun Apr 17 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.18-1drbl
- The program drbl-prepare-memtest was added to replace the pre-buildin binary memtest86+ program.

* Wed Apr 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.17-1drbl
- Let NFS mount points /usr and /var not to be checked in mountnfs.sh in DRBL clients.

* Tue Apr 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.16-1drbl
- Suppress the warning messages when using insserv to add services in drbl-all-service.

* Tue Apr 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.15-1drbl
- Suppress the warning messages when using insserv to add services in dcs.

* Tue Apr 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.14-1drbl
- To suppress the already mounted message, "checkroot.sh" of a Debian DRBL client won't mount /tftpboot/node_root again.
- Bug fixed: the mode remote-linux-txt of dcs was not working.

* Mon Apr 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.13-1drbl
- Bug fixed: "nolock" option is still for init.drbl.

* Mon Apr 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.12-1drbl
- Bug fixed: "nolock" option is for drbl live only.

* Mon Apr 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.11-1drbl
- "rsize=65536,wsize=65536" for NFS clients was removed from init.drbl. Let mount and kernel decide that.

* Mon Apr 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.10-1drbl
- "mount.nfs" from distribution system is used.  "/tftpboot/node_root" in /etc/fsta is kept in drbl clients.
- "rsize=65536,wsize=65536" for NFS clients was removed. Let mount and kernel decide that.
- "insserv" instead of update-rc.d will be used to add or remove service if insserv is found on Debian.

* Wed Apr 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-22
- "drbl-all-service" was improved to use insserv and workaround rpcbind service restart too fast error.

* Mon Apr 04 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-21
- Bug fixed: udpcast was not listed in PKG_FROM_DBN_MINIMAL_NEED of drbl.conf.

* Mon Apr 04 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-20
- Program syslinux64.exe will be put in function get_syslinux_binary_for_dos_linux of drbl-functions.
- Network installation for OpenSuSE was changed to 11.4 in drbl.conf by default.
- Let nfs-common deal with the required package (rpcbind or portmap), not to list portmap in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf, otherwise nfs-common 1.2.3 won't start if portmap is installed.

* Mon Mar 28 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-19
- Bug fixed: autologin failed in gdm3. Thanks to TACO <joey741019 _at_ gmail com> for this bug report.

* Fri Mar 25 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-18
- Typo fixed: "Mater Boot Record" -> "Master Boot Record". Thanks to rookieace1 for this bug report.

* Wed Mar 23 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-17
- File firstboot.DBN6.0.1.drbl was added.

* Sun Mar 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-16
- Packages hal and pcscd were added in the list of drbl.conf for Clonezilla live.

* Sun Mar 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-15
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Sat Mar 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-14
- Program disktype was added in the query packages list drbl.conf.

* Fri Mar 11 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-13
- Program ufsutils was added in the packages list of Clonezilla live in drbl.conf.
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language files es_ES was updated. Thanks to Alex Ibáñez López.

* Wed Mar 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-12
- Language file fr_FR was updated.

* Wed Mar 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-11
- Use Debian wheezy and Lucid natty in drbl.conf.
- Add the missing packages hwinfo and lzop in drbl.conf for Clonezilla live.

* Wed Mar 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-10
- The packages list for Debian in drbl.conf was sorted.

* Wed Mar 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-9
- Package lzop, ntfsprogs, and partimage should be in PKG_FROM_DBN_MINIMAL_NEED of drbl.

* Wed Mar 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-8
- Language files were updated.
- Put packages pigz, pbzip2, and udpcast to the packages list for every distribution in drbl.conf. No more listing for DRBL.
- Program drbl-bug-report was changed due to the packages list changed in drbl.conf.

* Sun Mar 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-7
- Config file drbl.conf was improved so when running "drblsrv -u", not too many programs from distribution will be erased.

* Sun Mar 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-6
- Package drbl-lzop was replaced by lzop. If the GNU/Linux distribution provides ntfsprogs, drblsrv will use it from distribution. If not, the pacakge in DRBL repository is the back up plan.

* Sat Mar 05 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-5
- Packages drbl-ntfsprogs and drbl-partimage were replaced by ntfsprogs and partimage. If the GNU/Linux distribution provides ntfsprogs and partimage, drblsrv will use them from distribution. If not, those in DRBL repository are the back up plan.

* Tue Mar 01 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-4
- Package gdisk was added in PKG_TO_QUERY of drbl.conf.
- Option "-batch" instead of "-b" in ocs-sr and ocs-onthefly is used by default. This will avoid the problem when using in the boot prameters, init will honor it.

* Sat Feb 19 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-3
- Language file zh_TW was updated.

* Fri Feb 18 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-2
- Language files were updated.

* Fri Feb 18 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.9-1
- An option to check if the image is restorable was added in the wizard.

* Thu Feb 17 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-29
- Bug fixed: in dcs, the shutdown command for DRBL clients was reboot.

* Wed Feb 16 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-28
- Function get_existing_partitions_from_img changed in ocs-functions, the dcs was modified accordingly.
- Language files were updated.

* Sun Feb 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-27
- Bug fixed: syntax error in drblpush.

* Sun Feb 13 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-26
- Service binfmt-support was added in client_services_chklist of drbl.conf.
- A workaround to avoid weird nfs locking issue in Ubuntu 10.10 was added in drblpush.

* Thu Feb 10 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-25
- Russian language files were updated. Thanks to Anton Pryadko.
- Bug fixed: DRBL Squeeze client should not use startpar when booting. Otherwise some drbl/clonezilla services won't work.
- An option -b|--drbl-client-ip was added in get-all-nic-ip.
- The ocs_server got in DRBL-SL.sh is chosen from those connected to DRBL clients, no uplink one.

* Sun Feb 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-24
- The virtual block device (/dev/vd[a-z]) support was added. Thanks to Cyril Roos for providing patch.

* Mon Jan 31 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-23
- Character in drbl-langchooser was updated.

* Mon Jan 31 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-22
- Language file zh_TW.UTF-8 was updated.
- Bug fixed: drbl-SL.sh should exclude the boot parameter "ip=frommedia" so that /etc/resolv.conf will be updated.

* Sat Jan 29 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-21
- New upstream memtest86+ 4.20.

* Sun Jan 16 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-20
- A variable instead of real IP address got from the machine was used in the Clonezilla live and GParted live pxelinux config examples when running generate-pxe-menu.

* Wed Jan 12 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-19
- An option -s|--server-ip was added in drbl-SL.sh.
- Code rewritten for get-drbl-conf-param.
- An option --drbl-ocs-live-server was added for drblpush.
- Bug fixed: --skip-drbl-ocs-live-prep wrongly parsed in drblpush.

* Sun Jan 09 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-18
- File firstboot.DBN6.0.drbl was added.
- Usage message of drblpush was updated. 
- The option --skip-drbl-ocs-live-prep was added drblpush. This is specially used for DRBL live.
- Program drbl-live.sh uses --skip-drbl-ocs-live-prep to use existing files.

* Fri Jan 07 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-17
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.

* Thu Jan 06 2011 Steven Shiau <steven _at_ clonezilla org> 1.9.8-16
- Language file it_IT was updated. Thanks to Gianfranco Gentili.
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Language files es_ES was updated. Thanks to Alex Ibáñez López.

* Tue Dec 28 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-15
- A better method was implemented to query if a package is available in Debian package repository. Thanks to max2107 for this bug report.

* Thu Dec 23 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-14
- File timesync on DRBL client was removed. We should let user to that by themselves.

* Wed Dec 22 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-13
- Bug fixed: drbl-client-root-passwd was not working on OpenSuSE 11.1.

* Sat Dec 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-12
- Language files were updated.

* Fri Dec 17 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-11
- Language files were updated.

* Thu Dec 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-10
- Bug fixed: dcs failed to use account "user" to send reboot command to Clonezilla live client of Clonezilla SE.
- Bug fixed: The *-info.txt created by drbl-SL.sh should not be appended. It should be overwritten every time drbl-SL.sh is run.

* Wed Dec 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-9
- Program expect was added in the required list for DRBL server. We need that for ssh login the Clonezilla live clients of Clonezilla SE.
- Program drbl-doit was improved to send command to Clonezilla live clients of Clonezilla SE.

* Mon Dec 13 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-8
- An option to choose alternative Clonezilla live as client's running OS was added.
- Language files were updated.

* Thu Dec 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-7
- A program drbl-kbdchooser was added to replace the deprecated command "dpkg-reconfigure console-data".
- Language files were updated.

* Tue Dec 07 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-6
- Package gdisk was added in the Clonezilla live packages list in drbl.conf.

* Mon Nov 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-5
- The dir /dev/shm should be mounted as mode 777 in Fedora, otherwise google-chrom won't start. Thanks to Bryan Buchanan <bryanb _at_ webbtide com> for the bug report.

* Wed Nov 24 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-4
- Bug fixed: /dev/stderr not found before entering rc in Fedora 14.

* Wed Nov 24 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-3
- A better way to deal with package name dhcp-client in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf for Debian and Ubuntu.

* Wed Nov 24 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-2
- The bug, /usr is busy when rebooting Fedora 14 client, was fixed.
- The package name isc-dhcp-client is used instead of isc-dhcp-client in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED of drbl.conf.

* Mon Nov 22 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.8-1
- Fedora 14 support was added (Not well tested).

* Sat Nov 06 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-28
- Netinstall for Fedora was changed to be 14 in drbl.conf.

* Tue Oct 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-27
- Package btrfs-tools was added in drbl.conf for GParted live.

* Tue Oct 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-26
- New upstream pxelinux 4.03.

* Fri Oct 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-25
- Minor update (prdownloads.sf.net -> downloads.sf.net) for the example in drbl-SL.sh.

* Wed Oct 13 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-24
- Bug fixed: dhcp3 on Ubuntu 10.10 not started.

* Wed Oct 13 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-23
- Language files were updated.
- Function parse_cmdline_option was updated to allow "=" and ",". Thanks to Jacobo Vilella Vilahur for this bug report (https://sourceforge.net/tracker/?func=detail&atid=671650&aid=3081655&group_id=115473).
- The netinstall of ubuntu was change to 10.04 and 10.10 in drbl.conf.

* Fri Oct 01 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-22
- Minor update for drbl-get-netmask.
- Program drblpush was improved to work with dhcpd 4 and alias IP address.

* Thu Sep 30 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-21
- Bug fixed: wrong line feed in get-all-nic-ip.

* Thu Sep 30 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-20
- Ubuntu 10.10 support was added (not tested yet).
- Minor improvement for drbl-get-ipadd.
- Program get-all-nic-ip now can get ppp* device. Thanks to sonic484 for reporting this issue.

* Mon Sep 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-19
- Jazz Wang suggested to addn an option "-n" to tcpdump in drbl-collect-mac.
- Bug fixed: The new boot parameter "ocs_client_no_per_NIC" was not working for DRBL live.

* Mon Sep 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-18
- Option "-i" was added in makeboot.sh and makeboot.bat.
- Environmental variable LC_ALL is honored by drblpush now.

* Thu Sep 23 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-17
- The package name drbl3-server for Debian Squeeze was changed to isc-dhcp-server, so more files were changed correspondingly.

* Thu Sep 23 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-16
- The package name drbl3-server for Debian Squeeze was changed to isc-dhcp-server, and dhcp3-client was changed to dhcp-client in drbl.conf.

* Wed Sep 22 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-15
- No more checking if partition starts or ends on cylinder boundary when running makeboot.sh.

* Sun Sep 19 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-14
- Program makeboot.sh was improved to allow running with full path.
- The yum repository should not be removed when uninstalling drbl. Thanks to Robert Arkiletian for this bug report.
- "nomodeset" should not be added for DRBL client. Thanks to Robert Arkiletian for this bug report.

* Wed Sep 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-13
- Some minor updates in drbl-bug-report.

* Fri Sep 03 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-12
- Mirror update about the output message color of drblpush.

* Thu Sep 02 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-11
- The netinstall of opensuse was change to 11.3 in drbl.conf.

* Mon Aug 30 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-10
- Russian language files were updated. Thanks to Anton Pryadko.

* Mon Aug 30 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-9
- Package btrfs-tools was added in the required one for Clonezilla live.

* Sun Aug 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-8
- Bug fixed: drbl4imp should be in /opt/drbl/sbin, not linked to /opt/drbl/setup/.

* Sun Aug 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-7
- Bug fixed: No drblsrv, drblpush and drbl4imp were found in /opt/drbl/sbin.

* Sun Aug 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-6
- Bug fixed: No more linking drblsrv, drblpush and drbl4imp from /opt/drbl/setup.

* Sun Aug 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-5
- The related codes about drbl-etherboot were removed in drblpush.
- No more drblsrv, drblpush and drbl4imp in /opt/drbl/setup/.

* Fri Aug 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-4
- Small English Grammatical Errors were fixed. Thanks to Mike Taylor (https://sourceforge.net/tracker/?func=detail&atid=671650&aid=3054348&group_id=115473).
- Wrong Message from drblpush about text/graphical PXE boot menu was fixed. Thanks to Mike Taylor (https://sourceforge.net/tracker/?func=detail&atid=671650&aid=3054362&group_id=115473).

* Fri Aug 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-3
- Package genisoimage was added in the required one for Clonezilla live.

* Fri Aug 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-2
- Typos in the Russian language file was fixed.

* Thu Aug 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.7-1
- Prompt about live-build version in drbl-functions was updated.
- Typos in the language files were fixed. Thanks to Anton Pryadko for the bugs report.
- Now drbl script will honor environmental variable LC_ALL, then LANG.
- Russian language files were added. Thanks to Anton Pryadko for providing the language files.

* Thu Aug 19 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-43
- Make user-setup as the required package for clonezilla/gparted live. In case it is not included by the live-build. This is specially for Ubuntu-based Clonezilla live.

* Thu Aug 19 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-42
- Remove a useless comment in the language file en_US.
- Commands in prepare-files-for-PXE-client about drbl-etherboot will be tested before run.

* Wed Aug 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-41
- Do not remove ethtool, tcpdump, dos2unix and lftp when uninstall drbl on OpenSuSE, since some of them are required packages (especially ethtool) for many programs.
- Remove installing drbl-etherboot when running drblsrv -i. Since etherboot is not maintained anymore and now we have gPXE.

* Sun Aug 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-40
- Make busybox as the required package for clonezilla/gparted live. In case it is not included by the live-build. This is specially for Ubuntu live case since it will use busybox-initramfs.

* Sun Aug 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-39
- Make sudo as the required package for clonezilla/gparted live. In case it is not included by the live-build.

* Sun Aug 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-38
- Program "makeboot.bat" was improved to avoid using the different command "find" from cygwin. Thanks to lryoung for providing this solution.
- Function create_live_required_debian_based_prompt in drbl-functions was improved to work with live-build (the new package name for live-helper).

* Mon Jul 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-37
- New upstream pxelinux 4.02.
- Bug fixed: drbl-syslinux-netinstall option error, failed to use the existing downloaded files.

* Tue Jul 20 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-36
- Bug fixed: get-client-ip-list should include drbl-functions.

* Thu Jul 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-35
- Language files fr_FR was updated. Thanks to Jean Francois Martinez <jfm512 _at_ free fr>
- Language file es_ES of perl was updated. Thanks to Juan Ramón Martínez.

* Sun Jun 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-34
- Put package drbl-ntfsprogs only for DRBL, not for Clonezilla live, since for Clonezilla live, it's better to use ntfsprogs, otherwise the 32-bit drbl-ntfsprogs won't work in pure amd64 Clonezilla live.

* Sun Jun 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-33
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Minor codes improvements were done in drbl-functions, switch-pxe-menu and hide_reveal_pxe_img.
- Program drbl-client-switch now can accept options for mode2.

* Sat Jun 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-32
- Put packages console-data console-setup console-common kbd as the required ones since live-helper changed to depend on keyboard-configuration which is not the one we need.

* Sat Jun 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-31
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- Language files es_ES and it_IT were updated. Thanks to Alex Ibáñez López and Gianfranco Gentili.

* Wed Jun 23 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-30
- The Clonezilla backgroud photo in the boot menu was updated.

* Wed Jun 23 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-29
- By default "nomodeset" is used in the boot parameters.

* Mon Jun 21 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-28
- Program mkswapfile was modified to be started in runlevel 2 for insserv.

* Fri Jun 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-27
- Make drbl-clients-nat work with insserv.

* Tue Jun 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-26
- Bug fixed: drbl-SL.sh failed to identify correct kernel in the Clonezilla live.

* Tue Jun 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-25
- Bug fixed: /sbin/mount.nfs will be copied to client only if it exists (CentOS 4.x).

* Tue Jun 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-24
- Bug fixed: Files rc.sysinit and halt for DRBL client were not included.

* Tue Jun 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-23
- Files rc.sysinit and halt for DRBL client were added.

* Tue Jun 15 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-22
- Boot parameter ramdisk_size should be adjusted according to the size of initrd-pxe.img.
- Variables of add_param_in_pxelinux_cfg_drbl_related_block and del_param_in_pxelinux_cfg_drbl_related_block in drbl-functions were renamed to avoid confusion.

* Wed Jun 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-21
- Package binutils was added in the required list for all the supported distributions. We need program strings in network initrd.

* Tue Jun 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-20
- Language files were updated.

* Mon Jun 07 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-19
- Files for Fedora 13 client was added.
- This release should support Fedora 13.

* Sun Jun 06 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-18
- Program drbl-ipcalc-list was added.
- Netinstall for Fedora was changed to be 13 in drbl.conf.

* Fri May 28 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-17
- The patched file plymouth.conf was improved for Ubuntu 10.04 DRBL clients so it won't enter virtual console 7 when running clonezilla job.

* Thu May 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-16
- A better method to avoid running makeboot.bat on the MS windows system drive was added. Thanks to timobeil for this idea.
- A prompt to run syslinux with extra options (-sr) was added in makeboot.bat. Thanks to pama123 for inspiring this idea.
- Programs rc.sysinit and halt for CentOS 5.5 were added.
- A patched file plymouth.conf will be used in the Ubuntu 10.04 DRBL clients so it won't enter virtual console 7 when running clonezilla job.

* Fri May 21 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-15
- Function canonical_hostname_prep was added in drbl-functions.

* Tue May 11 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-14
- RELEASE-NOTES was updated.

* Tue May 11 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-13
- Package gzrt was added in the packages list for Clonezilla live in drbl.conf.

* Mon May 10 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-12
- Openvz kernel for DRBL clients will be excluded when running drblsrv.

* Sun May 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-11
- Language files were updated.

* Sat May 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-10
- The usage function in drbl4imp was updated.
- One more prompt in drbl4imp was added.

* Sat May 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-9
- drbl4imp was improved with options "-r|--drbl-mode, -x|--limit-pxe-drbl-client, -u|--live_client_cpu_mode.
- Do not touch ntp.conf in drblsrv.

* Wed May 05 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-8
- New upstream memtest86+ 4.10.

* Sun May 02 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-7
- Program drbl-SL.sh was improved to allow using nfsroot as an option.
- Now we can choose the CPU arch for clients in drblpush when using Clonezilla live to do clonezilla job.
- Language files were updated.

* Thu Apr 29 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-6
- The netinstall for Ubuntu was updated to be "karmic" and "lucid" in drbl.conf.
- No more modifying the /etc/ntp.conf on the server when running drblpush.

* Tue Apr 27 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-5
- Duplicated command check_if_root was removed in drbl-SL.sh.
- Programs drblpush and tune-clientdir-opt now work for using clonezilla-live as the client's OS in Clonezilla SE mode.
- A typo was fixed in drbl-netinstall.
- Language files were updated.

* Mon Apr 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-4
- Bug fixed: mounted-varrun on Ubuntu 10.04 should be started in drbl-client-boot.conf so /var/run/utmp will be started.
- Program drbl-SL.sh was improved to work with drbl-ocs-live-prep.

* Sat Apr 24 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-3
- For readonly dir, "async and no_subtree_check" are used in /etc/exports (drbl-nfs-exports).
- On the diskless client side, "soft" was added for readonly mounting, and "hard,intr" was added for readwrite mounting.

* Fri Apr 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-2
- Bug fixed: Random password not working when running "drbl-useradd -s".

* Wed Apr 14 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.6-1
- Minor update for hide_reveal_pxe_img.
- Minor coding update in drbl-functions.
- Boot parameter ocs_server will be append in pxelinux config when using drbl-SL.sh. This release supports Clonezilla-live based client to do clonezilla job.

* Tue Apr 13 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-83
- Make deb-preconf-drbl work for tftpd-hpa version >= 5.0.
- Funtion active_proc_partitions in drbl-functions was improved to only active found disk in /proc/partitions.

* Wed Apr 07 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-82
- Ubuntu 10.04 (beta) support was added.

* Sat Apr 03 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-81
- New upstream syslinux 3.86.
- DRBL SSI template tarball will be extracted with -m option in the client.

* Thu Apr 01 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-80
- Program drbl-syslinux-netinstall was improved to show more prompts.

* Tue Mar 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-79
- Packages console-common and eject were added in Clonezilla live packages list.

* Fri Mar 12 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-78
- Language file ja_JP.UTF-8 was updated. Thanks to Annie Wei and Akira YOSHIYAMA.

* Tue Mar 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-77
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- clonezilla-jobs.log will be put in /var/log/clonezilla/ now.

* Mon Mar 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-76
- Package "zfs-fuse" should not be listed in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED. We will add that when creating clonezilla live.

* Mon Mar 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-75
- PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_CHKLISTS was rolled back to PKG_FROM_DBN_WHICH_OCS_LIVE_NEED.

* Sun Mar 07 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-74
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- drbl-client-boot.conf was improved to avoid mountall issue in Ubuntu 9.10 (https://bugs.launchpad.net/ubuntu/+source/mountall/+bug/470776)

* Sat Mar 06 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-73
- Language files es_ES and it_IT were updated.  Thanks to Alex Ibáñez López and Gianfranco Gentili.

* Fri Mar 05 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-72
- Packages foremost and zfs-fuse were added in the packages list of Clonezilla live.
- Improve get-rpm-list-from-yum, get_extract_syslinux.sh, get_memtest86, makeboot.sh, drbl-ssi-client-prepare, drbl-functions, drblsrv, drbl-SL.sh, drblpush (purge), drbl-collect-mac, and drbl-syslinux-netinstall, to avoid potential "rm -rf" error.
- Minor updates for drbl-fuu and drbl-fuh.
- Bug fixed: For Ubuntu 9.10, xz-utils conflicts with lzma, and lzma is essential.
- Variable PKG_FROM_DBN_WHICH_OCS_LIVE_NEED was changed to PKG_FROM_DBN_WHICH_OCS_LIVE_NEED_CHKLISTS in drbl.conf.

* Mon Mar 01 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-71
- Code clean: "local OCS_OPTS" is useless in drbl-functions.

* Sun Feb 28 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-70
- Package fbgrab was listed as the clonezilla live package in drbl.conf. Thanks to daix for this idea.
- Boot parameter ocs_se_save_extra_opt has been renamed as dcs_save_extra_opt, andocs_se_restore_extra_opt has been renamed as dcs_restore_extra_opt.

* Fri Feb 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-69
- Bug fixed: dcs failed to ask about input image and disk name when dcs_input_img_name is assigned.

* Fri Feb 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-68
- Bug fixed: a typo in program dcs.

* Fri Feb 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-67
- Bug fixed: Program dcs did not honor dcs_input_img_name.

* Thu Feb 25 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-66
- Prompt in drbl-client-switch was improved.
- Programs ocs-srv-live.sh, drbl-live.sh, and dcs will load the settings of /etc/ocs/ocs-live.conf if it exists.

* Thu Feb 25 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-65
- The boot parameter "dcs_choose_client", which can be one of these values: "All" or "Part", will be honored by dcs.
- The boot parameter "dcs_input_img_name", which can be one of these values: "in_server" or "in_client", will be honored by dcs.
- The boot parameter "dcs_cast_mode", which can be one of these values: "multicast", "broadcast", and "unicast", will be honored by dcs.
- The env boot parameters $ocs_se_restore_save_opt and $ocs_se_restore_extra_opt, will be honored by dcs and put to the drbl-ocs command options.

* Wed Feb 24 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-64
- Due to chain.c32 fails to boot local OS in syslinux 3.85, roll back to 3.84.

* Sun Feb 21 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-63
- New upstream syslinux 3.85.

* Thu Feb 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-62
- An issue about template_root.tgz was not created and used in DRBL SSI mode. Thanks to vakopian for this bug report.

* Thu Feb 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-61
- Reorder the z5p and z6p in the menu.

* Thu Feb 18 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-60
- Minor update about comment in drblsrv.
- Programs pigz pbzip2 lbzip2 were added in the packages list for Clonezilla live.

* Wed Feb 17 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-59
- Language files were updated.

* Tue Feb 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-58
- BSD netinstall lists were updated in drbl.conf and drbl-netinstall. Now it works for both FreeBSD 7.x and 8.0.

* Tue Feb 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-57
- Bug fixed: when querying package name, name like "xz" will be parsed incorrectly.

* Tue Feb 16 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-56
- Menu to show -z4, -z5|-z5p (for xz and pxz), -z6|-z6p (for lzip and plzip) options were added and improved in drbl-functions.
- Package xz|xz-utils, pxz, lzip and plzip were added in the list PKG_TO_QUERY in drbl.conf.
- Language files were updated.

* Thu Feb 11 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-55
- Package sysklogd was added in Clonezilla live packages list. Thanks to tl4ever for this suggestion.

* Tue Feb 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-54
- Dir debian for creating deb was added.

* Tue Feb 09 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-53
- drbl-functions was improved to work with live-helper 2.0.

* Sat Feb 06 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-52
- Program will be checked if exists in makeboot.sh. Thanks to Odile Bénassy for this bug report.

* Wed Feb 03 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-51
- Support Debian 5.0.4.

* Wed Feb 03 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-50
- Package grub was listed to Clonezilla live instead of all supported GNU/Linux distributions.

* Tue Feb 02 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-49
- Release notes were updated.

* Tue Feb 02 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-48
- Gtk mode netinstall for Debian Squeeze is no more, so drbl-netinstall was modified to adopt this.

* Tue Feb 02 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-47
- A comment about portmap was added in drblpush.
- Package name "grub" was removed in drbl.conf since it's nearly installed and it will make grub-pc to be removed on Ubuntu 9.10.

* Tue Jan 26 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-46
- Default to turn off loopback interface only for portmap on Debian Sid.

* Thu Jan 21 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-45
- RPM spec file was updated.

* Thu Jan 21 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-44
- Package nano was added in the list for Clonezilla live.

* Wed Jan 20 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-43
- Release notes were updated.

* Fri Jan 08 2010 Steven Shiau <steven _at_ clonezilla org> 1.9.5-42
- Bug fixed: the S19ocs-run job was run twice in Clonezilla SE. Thanks to martinr88 for this bug report.
- The PATH in drbl-functions was modified by putting /usr/sbin in higher proiroty than /sbin to avoid grub-install warning.

* Thu Dec 31 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-41
- Bug fixed: rc-sysinit.conf should be started after drbl-client-boot.conf in Ubuntu 9.10. Thanks to martinr88 for this bug report.

* Wed Dec 30 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-40
- Variables in language files were updated.

* Tue Dec 29 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-39
- Boot parameter "noprompt" was added for clonezilla live or gparted live when running "drbl-SL.sh -i".
- Bug fixed: The condition to check the required size and generate the SSI template tarball were fixed. It's should be none-full-drbl-mode "-a" none-full-clonezilla-mode, not none-full-drbl-mode "-o" none-full-clonezilla-mode.

* Mon Dec 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-38
- Bug fixed: kdm config was not found correctly in OpenSuSE 11.x. Thanks to Tsung-Lung Li for this bug report.

* Sat Dec 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-37
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.

* Fri Dec 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-36
- Language file ja_JP.UTF-8 was revised by Akira YOSHIYAMA.

* Thu Dec 24 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-35
- Language file es_ES was updated. Thanks to Juan Ramón Martínez.
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.

* Wed Dec 23 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-34
- Force to use sulogin instead of recovery-menu in Ubuntu 9.04 client, otherwise the error messages of Clonezilla will be overwritten.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.

* Tue Dec 22 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-33
- Package bind9-host instead of host was added in the Clonezilla live pcakges list.

* Sun Dec 20 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-32
- New upstream syslinux 3.84.

* Wed Dec 16 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-31
- Package host was added in the Clonezilla live pcakges list.
- Bug fixed: boot.udev should be started only in runlevel 1 in DRBL client in SuSE.

* Tue Dec 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-30
- Prompts in install-kernel-for-client was updated.

* Tue Dec 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-29
- Bug fixed: Only try to get client's CPU arch when there is boot/System.map* in /tftpboot/node_root/.

* Tue Dec 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-28
- New option -o|--link-detect-timeout was added in mknbi-nic.

* Mon Dec 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-27
- A workaround was added to force to mount NFS dir in drbl-client-boot.conf. It will avoid the problem described in https://bugs.launchpad.net/ubuntu/+source/mountall/+bug/470776.

* Mon Dec 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-26
- Comment was added in drbl.conf.

* Tue Dec 08 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-25
- Package pbbuttonsd, which provides program "run-parts", was added to the required packages list in SuSE.

* Mon Dec 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-24
- Force to run "zypper refresh" after repository is set.

* Mon Dec 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-23
- Bug fixed: We should filter .delta.rpm and .rpm.metalink files in list_available_rpm for OpenSuSE. Thanks to bri70123 for this bug report.

* Mon Nov 30 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-22
- Bug fixed: Failed to install the correct kmp package in OpenSuSE 11.1 and 11.2.

* Sat Nov 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-21
- Bug fixed: drblpush error was fixed.

* Sat Nov 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-20
- Minor prompt updated in drblsrv.
- Some improvements for making drbl work on OpenSuSE 11.2. 
- Make haldaemon is the Should-Start list in the firstboot for OpenSuSE 11.x.
- The packages *kmp-* of OpenSuSE 11.2 will be installed in the client's kernel modules if they can be found on server.

* Wed Nov 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-19
- Bug fixed: The method to filter CPU arch in Mandriva 2010.0 failed. It's fixed.

* Wed Nov 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-18
- Program drblsrv and drblpush work for mandriva 2010.0. Modified programs halt and rc.sysinit for Mandriva 2010.0 was added.
- Package cdrdao was added in the Clonezilla live packages list.

* Mon Nov 23 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-17
- The netinstall lists in drbl.conf were updated to be Fedora 12, OpenSuSE 11.2 and Mandriva 2010.0.
- Programs drblsrv and drblpush works for Fedora 12. Program find-url-in-yum-set works for XML results queried from mirrorlist. Program init.drbl was improved to work better with udevadm/udevtrigger/udevstart.
- Service abrtd was added for DRBL clients if exists.
- Bug fixed: If "-p true" is assigned for ocs-sr, it fails to enter command line prompt on Fedora 12.

* Fri Nov 20 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-16
- Bug fixed: drblsrv broken on SuSE 11.1 x86_64.
- /var/lib/ntp/proc won't be copied to DRBL client. The variables in drbl.conf have been changed (varlib_NOT_2_be_copied -> varlib_NOT_2_be_copied_2_common_root, varlib_NOT_2_be_copied_2_each_client -> varlib_NOT_2_be_copied, varcache_2_be_copied_2_common_root, varcache_2_be_copied).
- Suppress the harmless error messages when checking the disk usage space in check_drbl_setup_space.
- Suppress the harmless error messages when searching available packages on CentOS.
- Package fsarchiver was added in the package lists for DRBL live and Clonezilla live.

* Thu Nov 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-15
- A wake-on-LAN bug was fixed in drbl-doit. Thanks to Hedy for reporting this problem.

* Thu Nov 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-14
- Bug fixed: /etc/gdm/gdm.conf for autologin/timedlogin were not modified in Ubuntu 9.10.
- For general purpose, the pae kernel for client is excluded for Ubuntu 9.10's client.

* Thu Nov 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-13
- Bug fixed: /etc/gdm/gdm.conf for autologin/timedlogin were not modified in Ubuntu 9.10.
- The dir "backuppc" was appended to the variable varlib_NOT_2_be_copied in drbl.conf. Thanks to Rico CHen.

* Sun Nov 08 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-12
- Package wpasupplicant is included in Clonezilla live. Thanks to Thierry_bo for this request.
- Language files were updated.
- An option to ignore CRC checking of partclone was added.

* Thu Nov 05 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-11
- "text" was added to boot parameter for Clonezilla.
- Bug fixed: linux-remote-txt was not working in dcs.
- Force to use sulogin instead of recovery-menu by modifying /etc/init/rcS in drblpush for Ubuntu 9.10. This will avoid the recovery-menu overwrite the output when something goes wrong.

* Thu Nov 05 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-10
- Language files were updated.

* Wed Nov 04 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-9
- Now drblpush works for tftpd-hpa version 5.0.

* Tue Nov 03 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-8
- Minor updates for function config_drbl_live_network in drbl-functions.

* Tue Nov 03 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-7
- Parameter "async" in /etc/exports was removed. Thanks to icegood for this bug report.

* Wed Oct 21 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-6
- Functions get_block_line_in_upstart_conf and switch_upstart_service were added in drbl-functions.
- Bug fixed: The start stanza in /etc/init/{gdm,kdm,xdm}.conf should be modified by drblpush.

* Mon Oct 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-5
- mountall.conf and mountall-net.conf of upstart in DRBL client will not be started.

* Sun Oct 18 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-4
- Check if file exists before modifying /etc/init/*.conf.

* Sat Oct 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-3
- drbl-netinstall is updated for Ubuntu karmic.

* Sat Oct 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-2
- Change netinstall of Ubuntu to be "jaunty karmic" in drbl.conf.
- /etc/init/gdm.conf should not be treated as GDM config, it's for upstart.
- drbl-client-boot.conf was added for Ubuntu 9.10, and it will be copied to drbl client's /etc/init/.
- This release should be ready for Ubuntu 9.10.

* Wed Oct 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.5-1
- drblpush was updated for Ubuntu 9.10.
- drbl-all-service was updated to make it work with upstart or sysv service.

* Mon Oct 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-70
- Bug fixed: drbl-ssi-client-prepare should not replace other NFS server in /etc/fstab.

* Sat Oct 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-69
- Run swapon command in the background in client's mkswapfile service.

* Fri Oct 09 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-68
- RELEASE-NOTES was updated.
- New upstream syslinux 3.83.

* Wed Oct 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-67
- The patched "rc-sysinit.conf" for Ubuntu 9.10 was updated.

* Fri Oct 02 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-66
- Auto login user accounts in DRBL live now will be in the group "autologin" and have the privilege to shutdown or reboot the client machine in XFCE.
- By default the user accounts for auto login will use /bin/bash as login shell if /bin/bash is found.
- Now drblpush will accept the hostname prefix beginning with a digit.
- Some drbl scripts were slightly modified.

* Thu Sep 24 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-65
- Function copy_exec in drbl-functions was renamed to be copy_exec_drbl since we need to use "cp -pL" instead of "ln -s".
- An option "-nf|--no-all-firmwares" was added in mknic-nbi. By default, if firmwares are found in /lib/firmware/, mknic-nbi will copy all of them to the created PXE initramfs. With this flag, the one reported by "modprobe -F firmware" will be copied only. This looks good, but actually some firmwares (e.g. ipw2100 in Ubuntu 9.04) are required but are not reported by "modprobe -F firmware".

* Thu Sep 24 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-64
- New upstream memtest86+ 4.00.

* Mon Sep 21 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-63
- An option (-w|--include-wireless-modules) was added in mknic-nbi. By default now we won't include wireless modules.

* Thu Sep 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-62
- Language file ja_JP.UTF-8 was revised by Akira YOSHIYAMA.
- /sbin and /usr/sbin/ were added to PATH in makeboot.sh.

* Tue Sep 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-61
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- Language file it_IT was updated. Thanks to Gianfranco Gentili.

* Mon Sep 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-60
- Language files fr_FR was updated.  Thanks to Jean-Francois Nifenecker.
- Language file ja_JP.UTF-8 was updated. Thanks to Annie Wei.

* Mon Sep 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-59
- File firstboot.DBN5.0.3.drbl for Debian 5.0.3 was added.
- Dir "/var/lib/hadoop" is excluded when creating client's files in /tftpboot/nodes/.
- Spanish language file was updated. Thanks to Juan Ramón Martínez <jrmc77 _at_ terra es>.

* Fri Sep 04 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-58
- Packages tofrodos, dos2unix and unix2dos were listed in the variable PKG_TO_QUERY in drbl.conf.

* Sun Aug 30 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-57
- Package dbus was added in the list for Clonezilla live in drbl.conf.

* Sun Aug 30 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-56
- Packages dmsetup, dmraid, kpartx and device-mappe were listed in the query packages for DRBL in drbl.conf.
- The patched rc-sysinit.conf for Ubuntu 9.10's upstart was added.

* Fri Aug 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-55
- Packages dmsetup, dmraid and kpartx were added in the list of Clonezila live in drbl.conf. Thanks to Joshua for this hint.

* Fri Aug 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-54
- Ready for Ubuntu 9.10.
- Package vmfs-tools was added in the list for Clonezilla live.
- By default "-r" option is on for clonezilla.
- Programs halt.CO5.3.drbl and rc.sysinit.CO5.3.drbl were added.

* Wed Aug 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-53
- The function to get GDM_CFG in drbl-functions was improved to avoid getting te example one.
- No more patch rc-deafult in Ubuntu 9.10 or later in drblpush, since the new upstart work for rc 1.

* Wed Aug 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-52
- Programs install-kernel-for-client and update-drbl-client-kernel-from-server were improved to copy or sync the firmwares from server to client's common root.

* Tue Aug 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-51
- Function copy_exec was added in drbl-functions.

* Wed Aug 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-50
- Hints in drbl-SL.sh were updated.
- Services hal and dbus in clients now are not S20 only anymore for Debian-based system.

* Mon Aug 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-49
- RELEASE-NOTES was updated.

* Mon Aug 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-48
- Language files were updated.
- An option -fsck-src-part|--fsck-src-part was added for ocs-sr and drbl-ocs.
- Package hfsprogs is listed for Clonezilla live and Clonezilla SE.

* Sun Jul 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-47
- The program makeboot.sh will be checked if run as root.

* Tue Jul 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-46
- Language file zh_CN was updated. Thanks to Zhiqiang Zhang.
- makeboot.sh was improved to allow USB device /dev/ub[a-z]. Thanks to the patch from tv.debian _at googlemail com.
- Language file ja_JP.UTF-8 was updated. Thanks to Akira YOSHIYAMA.
- The variable name sanboot_img_dir was changed to be sanboot_img_dump_dir in drbl.conf. aoe_shelf_max and aoe_slot_max were changed to be 15 instead of 20.
- Package names genisoimage and mkisofs are put in the variable PKG_TO_QUERY in drbl.conf. This will avoid the mkisofs problem in Ubuntu 9.04.
- The variable name sanboot_img_dir was changed to be sanboot_img_dump_dir in drbl.conf. aoe_shelf_max and aoe_slot_max were changed to be 15 instead of 20. drbl-aoe-img-dump was changed correspondingly.
- drbl-aoe-serv now supports an option "-d" to allow more images in one more directories.
- Package smartmontools was added in DRBL/Clonezilla live.

* Fri Jul 03 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-45
- Language files es_ES, fr_FR, and it_IT were updated.  Thanks to Alex Ibáñez López , Jean-Francois Nifenecker and Gianfranco Gentili.

* Wed Jul 01 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-44
- Bug fixed: drbl-live-conf-X and Forcevideo-drbl-live failed to respect environmental variable LANG.

* Tue Jun 30 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-43
- File files/DBN/DBN5.0.2/firstboot.DBN5.0.2.drbl was added.
- File drbl-live-conf-X was added.
- Lauguage file is used in Forcevideo-drbl-live.
- Language files were updated.

* Mon Jun 29 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-42
- Directory boinc-client/projects is excluded when creating drbl client's /var/lib/.

* Fri Jun 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-41
- A variable "desktop_user_group_debian" was added so it's easier to add group for users. Also, the group "dialout" was added for the users in the client.

* Thu Jun 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-40
- rc.sysinit.FC11.drbl was added.
- drblsrv and drblpush were updated for FC11.
- In drbl-SL.sh, we do not put ip=frommedia because the /etc/resolv.conf got in live-initramfs won't exist after initramfs is done.        
- Language files and icons files of ja_JP.UTF-8 were updated. Thanks to Annie Wei and Akira YOSHIYAMA.
- The dhcpd config dir is in /etc/dhcp/ in Fedora 11, so drbl.conf and parse_dhcpd_conf were updated, too.
- Daemons pcscd and cpuspeed were added in the checklists for DRBL client's daemons.
- Program drbl-langkbdconf-bterm was removed, since now we will reuse ocs-langkbdconf-bterm.

* Sun Jun 21 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-39
- Language files and icons language files were updated.  Thanks to Alex Ibáñez López , Jean-Francois Nifenecker, Gianfranco Gentili, and Zhiqiang Zhang.

* Wed Jun 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-38
- A mode "1280x800" was added in the list in Forcevideo-drbl-live.
- DRBL live desktop icons text were updated.

* Mon Jun 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-37
- "LANG=C" is replaced with "LC_ALL=C" for all the scripts.

* Mon Jun 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-36
- Forcevideo-drbl-live was added.

* Sun Jun 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-35
- The program drbl-langkbdconf-bterm used to config language and keyboard for DRBL live was added.

* Fri Jun 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-34
- Default to use Fedora 11 netinstall in drbl.conf.

* Wed Jun 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-33
- New upstream syslinux 3.82.

* Mon Jun 08 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-32
- A file fail-mbr.bin was added. Thanks to Orgad Shaneh.

* Sun May 31 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-31
- New upstream syslinux 3.81.

* Thu May 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-30
- An option for using rescue mode of partclone when saving an image was added.
- Language files were updated.

* Tue May 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-29
- Boot parameter "ip=frommedia" was added back in generate-pxe-menu for Clonezilla live.
- drbl-SL.sh was improved to work with Clonezilla live, GParted live, Puppylinux 4.1.2. The support for PLD, INSERT, PUD and GeeXbox were removed.

* Wed May 20 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-28
- The pxe initramfs of client will try "5" times when requesting IP address.
- drbl-useradd was improved so the input password won't be shown on the screen.

* Mon May 18 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-27
- RELEASE-NOTES was updated.

* Sun May 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-26
- A function rep_whspc_w_udrsc was added to make language files easier to be written.

* Wed May 13 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-25
- Package grub-pc was removed from Clonezilla live package lists since it will conflict with grub1.

* Wed May 13 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-24
- Package grub-pc was added in the Clonezilla live package lists so ext4 grub boot partition can be supported.

* Tue May 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-23
- drbl-useradd was improved for adding single user account.

* Mon May 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-22
- Bug fixed: For Debian lenny, Ubuntu 8.10 or later, we should not allow network to be down when halting. Otherwise wake-on-LAN won't work.

* Mon May 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-21
- Bug fixed: some lines in ja_JP.UTF-8 should not contain space.

* Mon May 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-20
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei and Akira YOSHIYAMA.
- Language files zh_CN.UTF-8 was updated. Thanks to Zhiqiang Zhang.

* Sat May 09 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-19
- Language files es_ES, fr_FR, and it_IT were upudated. Thanks to Alex Ibáñez López,Jean-Francois Nifenecker and Gianfranco Gentili.   

* Thu May 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-18
- Program makeboot.sh was improved to run syslinux without "-s" and with a prompt.

* Thu May 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-17
- Program makeboot.sh was improved to work better in the prompts.
- "nolocales" was added and "ip=frommedia" was removed in generate-pxe-menu for Clonezilla live.

* Wed May 06 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-16
- New upstream syslinux 3.80.
- New program isohybrid was included.
- Package w3m was added in the list for Clonezilla live.
- Prompt in drbl-bug-report was slightly improved.
- drbl-netinstall was improved so that gtk netinstall mode of ubuntu jaunty and debian lenny are possible.

* Mon May 04 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-15
- Update mandriva network installation as 2009.1 in drbl.conf. Prompt message was updated in drblsrv for Mandriva 2009.1. This release supports Mandriva 2009.1 now.
- /etc/event.d/rc1 will be modified only if it exists in drbl client.
- The error message when ls /usr/lib/locale will be suppressed in drbl-functions.
- The comand to run drbl-ocs again will be recorded as a script in /tmp/ after dcs with clonezilla-start is used.

* Tue Apr 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-14
- Prompt was polished.
- Language files updated. 

* Tue Apr 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-13
- Language files updated. 
- Put save tasks and restore tasks in order in dcs.
- Package wireless-tools is included in Clonezilla live.
- The mode of Clonezilla will be shown when inputting data or choosing parameters. Thanks to the suggestion from aikenann _at_ gmail com.

* Tue Apr 28 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-12
- dcs will exit 0 if it is run normally.

* Sat Apr 25 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-11
- Language files updated. 

* Fri Apr 24 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-10
- Package vim-common was removed in PKG_TO_QUERY in drbl.conf since partclone.ntfsreloc can do the job, we do not need xxd anymore.

* Thu Apr 23 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-9
- firstboot.DBN5.0.1.drbl was added.

* Thu Apr 23 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-8
- Package vim-common was added in PKG_TO_QUERY in drbl.conf.

* Thu Apr 23 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-7
- Package bsdmainutils was added in the list for clonezilla live, since we need hexdump. Package vim-common was added since we need /usr/bin/xdd in the future.

* Tue Apr 21 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-6
- Package udpcast was added in the list for clonezilla live.

* Sun Apr 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-5
- File hdt.c32 from syslinux was added.

* Sun Apr 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-4
- Language files updated. 
- New upstream syslinux 3.75.
- Option "-q2" (partclone > partimage > dd) is the default option.
- Function parse_cmdline_option in drbl-functions was improved with option -c to accept the kernel command line file so it's easier to test.
- Package lzma was listed in the list in drbl.conf, and option -z4 can be selected in dcs now.

* Mon Apr 13 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-3
- Language files updated. 
- Typos were fixed in drbl-functions and language files.
- Bug fixed: parse_cmdline_option was improved (":" is possible in ocs_prerun, e.g.).

* Sat Apr 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-2
- Language files updated.
- New upstream syslinux 3.74.

* Fri Apr 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.4-1
- RELEASE-NOTES was updated.
- Language files updated.
- Beginner or expert mode options are added for Clonezilla SE.
- Network installation configs were updated to be squeeze and jaunty in drbl.conf.

* Sun Apr 05 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-43
- Spanish language file was updated. Thanks to Juan Ramón Martínez <jrmc77 _at_ terra es>.

* Sat Apr 04 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-42
- Packages hal, dmsetup, dmraid and kpartx were moved from create-gparted-live to the list in drbl.conf.

* Tue Mar 31 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-41
- -j2 and -j3 were merged to be a single parameter -j2. Thanks to Orgad Shaneh for this idea.
- msg_ocs_param_j3 in language file was removed.

* Sun Mar 29 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-40
- The prompt to use space key to mark the selections was added for most of the checklist type of dialog.
- Shorter prompt for (-z3, lzop) was used.

* Fri Mar 27 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-39
- Prompts were updated in drblpush.
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language files it_IT was updated. Thanks to Gianfranco Gentili.
- Language files zh_CN.UTF-8 was updated. Thanks to Zhiqiang Zhang.
- Language files es_ES was updated. Thanks to Alex Ibáñez López.
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei.

* Fri Mar 20 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-38
- Bug fixed: ntfsclone was not able to run on amd64 Debian Lenny due to /emul was not copied to /tftpboot/node_root. Thanks to Olivier Korn (https://sourceforge.net/tracker2/?func=detail&atid=671650&aid=2693933&group_id=115473) and Jose Luis (https://sourceforge.net/forum/message.php?msg_id=6873691).

* Thu Mar 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-37
- A function turn_on_ipv4_forward was added so that we can reuse it.

* Thu Mar 19 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-36
- Language files updated.
- Package vim-common list was moved from create-gparted-live to drbl.conf.

* Wed Mar 18 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-35
- Another warning about -z3 (lzop) was added in dcs/ocs-sr menu.
- Language files updated.

* Mon Mar 16 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-34
- Language files updated.
- A prompt to use space key to mark the selection was added for checklist dialog.

* Mon Mar 16 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-33
- Language files updated.

* Sat Mar 14 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-32
- generate-pxe-menu was updated to put ip=frommedia for Clonezilla live and GParted live pxelinux boot config.
- Language files updated.
- An option -e2 (to use the CHS from EDD when running sfdisk) was added in dcs.

* Sat Mar 07 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-31
- Desktop icon files of DRBL live were updated with language es_ES. Thanks to Alex Ibáñez López <alex.ibanez _at_ gmail com>.
- Minor updates for comments in drbl-nfs-conf.
- New variable nfs_client_extra_opt was added in drbl.conf, and will be used in drbl-gen-client-files.

* Thu Feb 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-30
- Merged the revised language file en_US. Thanks to Dylan Pack <sarpulhu _at_ gmail com>.

* Wed Feb 18 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-29
- firstboot.DBN5.0.drbl was added.
- Bug fixed: "get-all-nic-ip -c" failed to identify if NICs are "eth0 eth0:1", e.g.
- drbl-aoe-serv was improved to give error message if no NIC was found.
- vim-tiny was added in the list for clonezilla live.

* Thu Feb 12 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-28
- A function to check live helper and cdebootstrap version required when creating clonezilla/gparted/drbl was added.

* Wed Feb 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-27
- hwinfo was added in the packages query list in drbl.conf.

* Sat Jan 31 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-26
- Language files updated. Question mark should follow word without space. Thanks to carlfk.
- Bug fixed: Extracting syslinux 3.73 failed. It was OK for version syslinux 3.72 or earlier.

* Thu Jan 29 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-25
- Patched rc-default for Ubuntu 9.04 was added.
- New upstream syslinux 3.73.

* Thu Jan 29 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-24
- Bug fixed: "edd=on" parsing failed when running "drblsrv -i" first time.

* Mon Jan 26 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-23
- DRBL and Clonezilla related packages version info will be saved in drbl_ssi dir by drbl-gen-ssi-files.

* Sat Jan 24 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-22
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language files zh_CN.UTF-8 was updated. Thanks to Zhiqiang Zhang.
- Language files it_IT was updated. Thanks to Gianfranco Gentili.
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei.

* Wed Jan 21 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-21
- Bug fixed: Language file es_ES for bash script was broken.
- A small script check-lang.sh was added in language files to check if the UTF-8 language files work.

* Tue Jan 20 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-20
- Comment in function parse_cmdline_option was updated.
- Spanish language files were updated. Thanks to Juan Ramón Martínez <jrmc77 _at_ terra es>.
- Boot parameter "edd=on" will be added by generate-pxe-menu if EDD is builtin in kernel and default to be off.

* Sat Jan 17 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-19
- Option -j2 and -j3 for saving or restoring hidden data were added in dcs.
- Language files updated.

* Fri Jan 16 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-18
- Language files es_ES were converted to UTF-8 by "iconv -f iso-8859-1 -t utf-8 es_ES -o es_ES.UTF-8".

* Thu Jan 15 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-17
- Bug fixed: "single" service should be moved to S90 in rc1.d in SuSE 11.1 clients. Otherwise S19ocs-run won't be started.
- Bug fixed: Package "binutils" is required in Clonezilla live since we need strings from it to parse syslinux.
- Spanish language files were added. Thanks to Juan Ramón Martínez <jrmc77 _at_ terra es>.

* Sun Jan 11 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-16
- Bug fixed: The prompt to run ocs-sr command with options was buggy due to dialog add more " in OpenSuSE 11.1.
- Package kexec-tools was added to Clonezilla live. Thanks to Carl Karsten for this idea.
- makeboot.sh was updated with LANG=C in most of the commands.
- mkswapfile service is improved with some prompts.
- Force to restart dbus of DRBL client after nfs service is started so that the rest of services will go without any problem in OpenSuSE 11.1.

* Sat Jan 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-15
- Bug fixed: drbl*.repo in rpm-md-repos should not be copied again. It's already there.

* Sat Jan 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-14
- Bug fixed: rpm-md-repos was not installed in the Makefile.
- Bug fixed: drbl*.repo in rpm-md-repos should be copied to system when running drblsrv -i.

* Sat Jan 10 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-13
- Typos in language file en_US were fixed. Thanks to Juan Ramón Martínez Castillo.
- drbl-functions was improved to find the right custom.conf for gdm in OpenSuSE 11.1.
- drblpush was improved to work with opensuse 11.1.

* Tue Jan 06 2009 Steven Shiau <steven _at_ clonezilla org> 1.9.3-12
- A new program find-url-in-rpm-md-set was added for parsing OpenSuSE rpm md config file.
- Programs drblsrv-offline and install-kernel-for-client were improved to find kernel version number for package rpm.
- Minor updated for drblsrv-offline.
- Program drblsrv was updated to support zypper for OpenSuSE 11.1.
- Language files updated.

* Mon Dec 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-11
- Default to use opensuse 11.1 netinstall in drbl.conf.
- Bug fixed: duplicated fixing waitnfs.sh in drblpush.sh. Thanks to Enix <Wang.TW _at_ gmail com>.

* Fri Dec 26 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-10
- Language files updated.
- Language files it_IT were updated. Thanks to Gianfranco Gentili.

* Thu Dec 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-9
- Language files it_IT were updated. Thanks to Gianfranco Gentili.

* Thu Dec 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-8
- Language files updated.
- An option -z2p for parallel bzip2 was added.
- Package pbzip2 is in the lists for drbl and clonezilla live.

* Thu Dec 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-7
- Language files it_IT were updated. Thanks to Gianfranco Gentili.

* Wed Dec 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-6
- New upstream memtest86+ 2.11.
- Language files updated.
- An option "-e1 auto" was added to dcs.

* Mon Dec 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-5
- Language files it_IT for bash and perl were added. Thanks to Gianfranco Gentili.
- Language file it_IT was added, so drbl-langchooser was modified, too.

* Fri Dec 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-4
- gdm of DRBL client should be started later so that keyboard and mouse will work (Was S13, now S30).

* Thu Dec 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-3
- Language files updated.
- Bug fixed: mac-grp-* should not be case sensitive. Thanks to Steven K. for this bug report.

* Wed Dec 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-2
- Prompt message was updated.

* Sat Dec 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.3-1
- Fedora 10 is supported.
- Default to use language en_US in drbl-nfs-exports.

* Mon Dec 08 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-21
- Language files updated.

* Mon Dec 08 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-20
- RELEASE-NOTES was updated.
- hexedit and cryptsetup were added in Clonezilla live.
- Language files updated. Some typos in en_US were fixed. Thanks to Jason <kindofabuzz _at_ gmail com> and John Clegg.

* Mon Dec 01 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-19
- Default to use Fedora 10 netinstall in drbl.conf.

* Thu Nov 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-18
- Language files updated.
- "-b" option was added to restore mode in Clonezilla. Thanks to Jean-Francois Nifenecker.

* Sat Nov 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-17
- Comment "export LC_ALL=C" for Ubuntu in drblsrv.
- New upstream memtest86+ 2.10.

* Wed Nov 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-16
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei.
- By default we turn off -gm for clonezilla when saving an image.

* Mon Nov 10 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-15
- Bug fixed: The function to parse /proc/cmdline for ocs_* was improved. It failed on Ubuntu 8.10. Thanks to Orgad Shaneh for reporting this bug.

* Sun Nov 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-14
- Language files zh_CN.UTF-8 for shell script was added. Thanks to Liang Qi.
- Bug fixed: /etc/event.d/rc-default of clients should be patched on Ubuntu 8.10. Thanks to cer85, AsGF2MX and Jonathan Krishnanantham.

* Fri Nov 07 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-13
- Language files zh_CN.UTF-8 for shell script and zh_CN.UTF-8 for drblpush were added. Thanks to Liang Qi.
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.

* Wed Nov 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-12
- Do not force to use LC_ALL=C in drblsrv for Debian or Ubuntu.

* Mon Nov 03 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-11
- Language files updated.

* Mon Nov 03 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-10
- Language files updated.

* Sat Nov 01 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-9
- Bug fixed: If CPU level of client is chosen as same level with that in server, kernel-desktop pacakge in Mandriva 2009.0 should be used.

* Sat Nov 01 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-8
- drblsrv was updated for Mandriva 2009.0.
- Bugs fixed: rc.sysinit and halt for Mandriva 2009.0 were updated.
- /etc/init.d/netfs of Mandriva 2009.0 will be modified not to exit if /var/lock/subsys/network does not exist when deployed to client.
- PAM_need_files was upated in function create_chpasswd_env in drbl-functions for Mandriva 2009.0.

* Fri Oct 31 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-7
- Replace drbl.sf.net with drbl.name in drblpush.
- drbl-netinstall was updated to provide an option to run generate-pxe-menu.

* Thu Oct 30 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-6
- Bug fixed: Not only CentOS 5, but also CentOS 5.* only i686 kernel are available, no i586 one.
- Netinstall for Mandriva was updated with 2009.0 in drbl.conf.
- Default to let client use same arch kernel with server for Ubuntu.
- rc.sysinit and halt for Mandriva 2009.0 were added (Not tested yet).

* Sun Oct 26 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-5
- makeboot.sh was improved: Check if "not end on cylinder boundary", too.
- VERSION.txt and README.txt for syslinux were added in /utils/ for drbl/clonezilla live usb flash drive version.

* Sat Oct 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-4
- makeboot.sh was polished.

* Thu Oct 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-3
- Update ubuntu netinstall as "hardy intrepid" in drbl.conf.

* Tue Oct 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-2
- Language files updated.

* Tue Oct 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.2-1
- A varialble syslinux_binsrc_url was added in drbl.conf.
- A function get_syslinux_binary_for_dos_linux was added in drbl-functions.
- Turn on -f option of syslinux.exe in makeboot.bat.
- syslinux.exe should not be in drbl package, so it was removed.
- makeboot.sh was added to make USB flash drive bootable on GNU/Linux.
- Language file zh_CN.UTF-8 was added. Thanks to Zhiqiang Zhang.
- drbl-langchooser was updated with zh_CN.UTF-8 listed.

* Mon Oct 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-48
- An option to reboot or shutdown for ocs-sr was added.

* Sun Oct 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-47
- drbl-nfs-exports was slightly updted.

* Sun Oct 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-46
- Bug fixed: drbl-live.sh failed.

* Sat Oct 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-45
- drbl-all-service was slightly updated.

* Fri Oct 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-44
- Two options were added for Clonezilla: generate/check MD5SUMS and SHA1SUMS.
- Language files updated.
- Web doc is not included since a lot of php files are useless.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-43
- Bug fixed: pigz was not installed in clonezilla live.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-42
- Bug fixed: Failed to run with option -z1p if 2 or more CPUs exist in Ubuntu-based Clonezilla live.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-41
- Language files updated.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-40
- Bug fixed: Failed to show option -z1p if 2 or more CPUs exist in Ubuntu-based Clonezilla live.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-39
- Two more examples (GParted/Clonezilla live) were added in generate-pxe-menu.

* Tue Oct 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-38
- A checking mechanism for default gateway was added for drbl live. Ref: http://sourceforge.net/forum/message.php?msg_id=5421762

* Mon Oct 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-37
- drbl-functions was updated so that only in multiple CPUs system the -z1p option will be shown for clonezilla.
- cdrecord is removed from Clonezilla live since wodim replaces that. Thanks to Orgad Shaneh.

* Sun Oct 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-36
- ms-sys was removed from Clonezilla live packages list, since it's not available in Debian Lenny.

* Sat Oct 11 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-35
- dmidecode, mbr, ms-sys and wipe were added in the packages list of Clonezilla live.
- install-mbr was added in the packages list of gparted live.
- gpxe was added in the packages list.

* Wed Oct 08 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-34
- dmidecode was added in the PKG_TO_QUERY list in drbl.conf.
- Option -z1p for clonezilla was added in drbl-functions.
- pigz will be installed when running drblsrv. This will allow us to compress the image in parallel. Remember to use i586 or i686 kernel for your DRBL clients.
- Language files updated.

* Tue Oct 07 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-33
- Package usbutils was added in Clonezilla live packages list. Thanks to carlfk for this suggestion.  
- Functions related to turn_on_hd_dma were polished. Thanks to Carl Karsten for this bug reporting.
- An option was added: --dump-mbr-in-the-end. This option allows us to use dd to dump the MBR (total 512 bytes, i.e. 446 bytes (executable code area) + 64 bytes (table of primary partitions) + 2 bytes (MBR signature; # 0xAA55) = 512 bytes) _after_ disk image was restored. This is an insurance for some hard drive has different numbers of cylinder, head and sector between image was saved and restored."
- Language files updated.

* Sun Oct 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-32
- davfs2 was removed in the clonezilla live list, since it is not suitable for larger file transfer. The cache mechanism is the key problem (ref: https://sourceforge.net/forum/forum.php?thread_id=2248597&forum_id=82589). Thanks to Louie Chen.

* Wed Oct 01 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-31
- Bug fixed: ifupdown was forced to be added in drbl/clonezilla live. Otherwise Lenny-based Clonezilla live will go wrong with network client. Thanks to Louie Chen.
- Typos fixed: Some prompts about /etc/apt/sources.list were wrong.
- Now default we allow DRBL clients to edit boot parameters.

* Sun Sep 28 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-30
- New upstream syslinux 3.72.

* Tue Sep 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-29
- Bug fixed: Only when /etc/init.d/mkswapfile is available drbl-aoe-img-dump will stop swapfile function.

* Mon Sep 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-28
- Bug fixed: drbl-aoe-img-dump should stop mkswapfile in the beginning so that -x option will work.

* Mon Sep 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-27
- Prompt was updated in mknic-nbi.
- Bug fixed: "continue" should not be used in function stop of drbl-aoe-serv.

* Sun Sep 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-26
- Some minor updates in drbl-aoe-img-dump and drbl-aoe-srv.
- An option (-x) to run drbl-aoe-img-dump interactively was added.

* Fri Sep 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-25
- A new variable $debian_pkgs_for_gparted was added in drbl.conf.
- Bug fixed: we should dump a "disk" instead of a partition when using drbl-aoe-img-dump. ///NOTE/// The parameters of drbl-aoe-img-dump was changed! Now only 2 paremeters are required. No more 3.

* Fri Sep 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-24
- Bug fixed: "/" problem with perl for some cases. Thanks to Will Esselink for reporting this bug.

* Wed Sep 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-23
- The volume size of clonezilla image can be assigned when running dcs to save an image.

* Tue Sep 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-22
- Only run drbl-aoe-srv when AoE image is found during uninstallation.
- Warning messages were removed in drbl-aoe-srv and drbl-aoe-img-dump. Will give warning in release notes.

* Mon Sep 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-21
- vblade service will be asked if to be stopped when uninstall drbl.

* Mon Sep 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-20
- drbl-aoe-serv was polished and minor bugs fixed.
- Stop service mkswapfile before dumping in drbl-aoe-img-dump.

* Sat Sep 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-19
- traceroute and iputils-ping were added in the Debian Live template packages list.

* Fri Sep 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-18
- Bug fixed: Failed to remove old client dir in /tftpboot/nodes/. Thanks to Louie Chen for reporting this bug.

* Thu Sep 11 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-17
- Typo fixed in en_US. Thanks to Spiros Georgaras.

* Tue Sep 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-16
- drbl-syslinux-netinstall was updated with more options.

* Tue Sep 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-15
- Comments were updated in drbl-aoe-img-dump and drbl-aoe-serv
- A new program drbl-syslinux-netinstall was added to create netinstall zip for USB flash drive.

* Mon Sep 08 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-14
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei.

* Sat Sep 06 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-13
- A prompt in drbl-live-boinc was updated.

* Wed Sep 03 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-12
- "boinc_cmd --set_network_mode always" was added in drbl-live-boinc, suggested by Jazz.

* Wed Sep 03 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-11
- Language files updated.
- Add option to run boinc command always in drbl-live-boinc.

* Sat Aug 30 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-10
- Bug fixed: gateway was assigned wrong one in dhcpd.conf when there are 2 NICs.

* Sat Aug 30 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-9
- Bug fixed: force to set the mac address as lowercase in drbl-aoe-img-dump.
- A function parse_cmdline_option was added in drbl-function.

* Thu Aug 28 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-8
- iproute/iproute2 was added in the installation list.
- drbl-aoe-serv was updated so that the running port for vbladed will be the right one if available.
- -e|--accept-one-nic option was added in drbl4imp.

* Thu Aug 28 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-7
- Bugs fixed: Public IP address should be included in drbl-yp-securenets and get-ip-link-2-drbl-srv.
- Better method to search available NIC so get-all-nic-ip now runs faster.
- New programs "get-port-link-2-drbl-srv" and "drbl-tune-pxecfg-block" were added.
- generate-pxe-menu was updated about AoE label.
- Two options for get-all-nic-ip were added: -u|--uplink-eth-port and -c|--drbl-client-eth-port.
- Two programs drbl-aoe-img-dump and drbl-aoe-serv were added so it's easier to work with AoE booting.

* Mon Aug 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-6
- Broadcast mode for Clonezilla was added in dcs.

* Mon Aug 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-5
- Prompt in drbl-netinstall was updated.
- Bug fixed: drblpush should not link /tftpboot/node_root/tmp/boot/boot.
- pbzip2 was removed in the installation list.
- Bug fixed: Debian/Ubuntu DRBL client should have a dir /tmp/boot.
- rc.sysinit and halt for CentOS 5.2 were added.
- Language files updated.
- The function to enter volume file size was added in drbl-functions.

* Thu Aug 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-4
- pbzip2 was added in the installation list.
- Some files were updated since locales maybe not in a archive file, it can be a dir tree in /usr/lib/locales. They are: drblpush and drbl-functions.
- Bug fixed: One ethernet port of public IP address failed to run as a drbl server.

* Sat Aug 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-3
- Bug fixed: One ethernet port of public IP address failed to run as a drbl server.

* Fri Aug 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-2
- An extra line (. /etc/diskless-image/config) in drbl-ssi-client-prepare was removed.
- drblpush now works for one NIC server (no alias IP address is required), and should work for public IP address (not tested yet).

* Fri Aug 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.1-1
- "-r" option of clonezilla was turned off by default in drbl-function, since this might cause some problems if an unknown partition exists. Thanks to Thomas Moler.
- init.drbl was updated to work with class B IP address with netmask 255.255.0.0.
- drblpush now can work with ethernet port with private IP address class B and netmask 16. It was only for netmask 24.

* Wed Aug 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-52
- Packages aoetools and vblade were added in the list PKG_TO_QUERY.

* Tue Aug 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-51
- "5x" is used now for scientific linux netinstall, which means the latest one.

* Tue Aug 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-50
- An example about AoE booting was added in generate-pxe-menu.

* Tue Aug 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-49
- sanboot.c32 was added in pkg/syslinux, and it will be copied to /tftpboot/nbi_img when running drblsrv.

* Tue Aug 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-48
- gpxelinux.0 was added in dir pkg/syslinux, it will be copied to /tftpboot/nbi_img when running drblsrv.

* Mon Aug 04 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-47
- Update drbl-functions for language as only en_US.UTF-8, zh_TW.BIG5, and zh_TW.UTF-8.
- New upstream syslinux 3.71. Syslinux 3.7x is NOT buggy for USB flash drive booting, it's because we use syslinux 3.6x to make 3.7x image bootable.

* Sun Aug 03 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-46
- Use centos_netinstall_ver="4 5" in drbl.conf since that means the latest centos. It is actually link to the latest one.

* Wed Jul 30 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-45
- jfbterm was added in the package lists for clonezilla live.

* Tue Jul 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-44
- Language files updated.

* Fri Jul 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-43
- Use variable PKG_FROM_DRBL_FOR_CLONEZILLA_LIVE instead of PKG_FROM_DRBL_INSTALLED_IN_SYSTEM in drbl.conf.

* Fri Jul 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-42
- Bug fixed: drbl-langchooser does not load DIA if ocs-live.conf does not exist.

* Thu Jul 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-41
- Language files updated.

* Thu Jul 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-40
- Package gpm was added in Clonezilla live.
- Language files updated.
- The function ocs_advanced_param_post_mode_after_clone was added for dcs and drbl-functions.

* Tue Jul 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-39
- Function get_existing_language was added in drbl-functions.
- Since syslinux is buggy for USB flash drive booting, back to syslinux 3.63 from 3.70.
- Language files updated.

* Sun Jul 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-38
- glibc-i18ndata was added as a requirement in OpenSuSE packages list.
- drblsrv was modified because yum repository setting dir is different in OpenSuSE 11.0.

* Sat Jul 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-37
- firstboot.SUSE11.0.drbl was added.
- opensuse-11.0.repo and opensuse-updates-11.0.repo were added.

* Fri Jul 11 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-36
- RELEASE-NOTES was updated.
- New upstream syslinux 3.70.
- Package mdadm was added to Clonezilla live package lists.
- The language selection is listed in alphabetic order in drbl-langchooser.
- Opensuse 11.0 was added in netinstall list.
- File mboot.c32 will be copied to /tftpboot/nbi_img/ by drblsrv.
- Japanese languages file was updated. Thanks to Akira Yoshiyama.

* Tue Jun 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-35
- dcs was updated with full path prompt for drbl-ocs.

* Sat Jun 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-34
- Packages gmailfs was removed from the list in clonezilla/drbl live since it's old and will add 5 MB more for the Live CD.

* Sat Jun 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-33
- Language files updated.

* Fri Jun 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-32
- Packages davfs2 and gmailfs were listed to be added in clonezilla/drbl live.

* Wed Jun 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-31
- Language files fr_FR was updated. Thanks to Jean-Francois Nifenecker.
- Language files ja_JP.UTF-8 was updated. Thanks to Annie Wei.

* Sat Jun 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-30
- Language files updated.

* Fri Jun 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-29
- About Clonezilla live: Package curlftpfs was removed in drbl.conf since the one in etch is not working, and it does not exist in Lenny now.

* Fri Jun 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-28
- Lenny was added in the netinstall list for Debian.

* Fri Jun 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-27
- Commentes were updated in generate-pxe-menu.

* Fri Jun 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-26
- Package ntp/xntp should not be necessary for drbl. The related item was removed in drbl.conf.
- mboot.c32 was added in pkg/syslinux.
- An example for Xen client was added in generate-pxe-menu.

* Thu Jun 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-25
- Language files updated. Thanks to Jean-Francois Nifenecker for updating fr_FR..

* Fri Jun 06 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-24
- Language files updated.

* Thu Jun 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-23
- Do not append "server pool.ntp.org" and "server stdtime.sinica.edu.tw" in /etc/ntp.conf. Thanks to Louie Chen for identifying this problem.
- drbl-langchooser was updated by using "French | Français" instead of "French" only. Thanks to Jean-Francois Nifenecker for this idea.
- Language files updated.

* Tue May 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-22
- Language file ja_JP.UTF-8 for bash was updated. Thanks to Akira YOSHIYAMA.
- Hostname assigned function is disabled in drbl-live-boinc, since it will make application (firefox, xfce...) won't start in the DRBL live server.

* Mon May 26 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-21
- Full path for exec file was removed in parse_apt_url_get_rpm.sh.
- Language file fr_FR for bash was updated. Thanks to Jean-Francois Nifenecker.

* Fri May 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-20
- firstboot.DBN-TU.drbl was updated since if X.org >= 7.3, it's not necessary to run.

* Fri May 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-19
- A function to assign hostname in drbl-live-boinc was added again.

* Fri May 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-18
- Remove the hostname assigned function, and ask the mode (text/graphical) for clients in drbl-live-boinc. 

* Fri May 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-17
- A function to assign hostname in drbl-live-boinc was added.

* Thu May 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-16
- Bug fixed: typos fixed in drbl-live-boinc 

* Thu May 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-15
- drbl-live-boinc was added to start boinc client in DRBL live.
- drbl-functions and drbl-live.sh were updated because of drbl-live-boinc.

* Thu May 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-14
- drbl-functions was slightly updated.

* Thu May 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-13
- New upstream syslinux 3.63.

* Tue May 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-12
- Bug fixed: "ocs" should be cloneizlla in Clonezilla-live.desktop.

* Tue May 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-11
- Grandr.desktop updated.

* Tue May 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-10
- Bug fixed: ocs-live.conf in the live hook dir should be ocs-live-hook.conf in drbl-live.sh

* Tue May 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-9
- Grandr.desktop was added in desktop-icons/drbl-live/ 

* Mon May 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-8
- Language files updated for fr_FR.

* Mon May 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-7
- drbl-useradd-range was updated to show accounts when removing.
- Run tune-debian-dev-group-perm to add users to group "audio cdrom plugdev floppy video" in drbl-useradd.
- Usage messages were updated in tune-debian-dev-group-perm.
- Language files updated.

* Sun May 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-6
- Bug fixed: drbl-useradd drbl-userdel were updated.

* Sun May 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-5
- Status is shown when searching kernel rpm in repository in drblsrv.
- Full paths were removed in drbl-3n-conf, drbl-gen-client-files, drbl-gen-pxe-nbi, prepare-files-for-PXE-client, switch-pxe-menu, tune-debian-dev-group-perm.
- File drbl-src-img-mnt was removed.
- File useradd-file.sh is renamed as drbl-useradd-file.
- File useradd-list.sh is renamed as drbl-useradd-list.
- File useradd-range.sh is renamed as drbl-useradd-range.

* Sun May 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-4
- Bug fixed: The output of "rpm -q $PKG" will be appended with .i[356]86, so drblsrv failed to install i386 glibc and openssl.

* Sat May 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-3
- rc.sysinit.FC9.drbl was updated.
- Bug fixed: Firstboot should not ask account and ntp in drbl clietn again in Fedora 9.

* Fri May 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-2
- rc.sysinit and halt for Fedora 9 were added.
- fedora_netinstall_ver="9"
- Bug fixed: list_available_rpm, list_available_deb, list_available_tbz2 failed to run.
- Thanks to Jean-Francois Nifenecker for updating French files.

* Thu May 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.9.0-1
- Comments in drbl-functions were updated.
- File create-RH-apt-enabled-cd and drbl-create-RH-apt-enabled were removed.
- Files lvm2-start.sh  lvm2-stop.sh were moved to package clonezilla and renamed as ocs-*.
- File create_pxe_nbi_files is renamed as drbl-gen-pxe-nbi.
- File clean-dhcpd-lease is renamed as drbl-clean-dhcpd-leases.
- File autologin-home-reset is renamed as drbl-autologin-home-reset.
- File gen_client_files.sh is renamed as drbl-gen-client-files.
- File gen_ssh_host_key is renamed as drbl-gen-ssh-host-keys.
- File gen_ssi_files is renamed as drbl-gen-ssi-files.
- File prepare_files_for_PXE_client is renamed as prepare-files-for-PXE-client.
- File select_hosts is renamed as select-drbl-clients.
- File update_client_kernel_from_server.sh is renamed as update-drbl-client-kernel-from-server.
- File tw-bterm was removed.
- File check_dm is renamed as drbl-check-dm.
- File detect_cdrom is renamed as drbl-detect-cdrom.
- File check_kernel_cpu_arch is renames as drbl-check-kernel-cpu-arch.
- File fbasename was removed. We can use "xargs basename" to replace that.
- File get_common_usersname is renames as drbl-get-common-username.
- File get_drbl_conf_param is renames as get-drbl-conf-param.
- File gethostip.pl is renames as drbl-gethostip.
- File get_ip is renames as drbl-get-ipadd.
- File drbl_ssi_client_prepare is renames as drbl-ssi-client-prepare.
- File get_mac is renames as drbl-get-macadd.
- File get_netmask is renames as drbl-get-netmask.
- File get_network is renames as drbl-get-network.
- File get_nfsserver is renames as drbl-get-nfsserver.
- File ipcalc is renames as drbl-ipcalc.
- File wakeonlan is renames as drbl-wakeonlan.
- File socket.pl is renames as ocs-socket (in Clonezilla).
- File sha1pass is renames as drbl-sha1pass.

* Tue May 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-20
- Language files updated.

* Tue May 13 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-19
- Language files updated.
- Format the hint messages in select_hosts.
- ja_JP language files were included (from Akira YOSHIYAMA <yosshy _at_ debian or jp>).
- Japanese and French languages options were added.
- Program langchooser was renamed as drbl-langchooser

* Sun May 11 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-18
- Language files updated.

* Fri May 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-17
- Language files updated.

* Wed May 07 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-16
- Language files updated.

* Wed May 07 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-15
- Packages open-iscsi and aoetools were listed in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.
- Language files updated.
- Package "patch" is listed in PKG_FROM_DBN_MINIMAL_NEED in drbl.conf.

* Tue Apr 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-14
- Language files updated.
- By default we turn on "-r" for restoring.

* Tue Apr 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-13
- whiptail instead of dialog is used if detected.
- If port # is not assign, set it as default in mknic-nbi.
- Language files updated.
- Option "-r" was listed when restoring image in clonezilla.

* Mon Apr 28 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-12
- An example to use different DHCP service ports was added in dhcpd.conf.

* Sun Apr 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-11
- Language files updated.
- An option -P|--udhcpc-port was add for mknic-nbi.

* Sun Apr 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-10
- Language files updated.

* Sun Apr 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-9
- Language files updated.

* Sun Apr 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-8
- Bug fixed: We still have to remove those services (kbd-conf and Forcevideo-drbl-live) in drbl-live.sh.

* Sun Apr 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-7
- Since now we use update-rc.d instead of copying services directly into /etc/rcS.d, it's not necessary to modify drbl-live.sh. Revert to old one.

* Sat Apr 26 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-6
- Bug fixed: Remove the services we put only for DRBL live server when creating drbl live. Those services (kbd-conf and Forcevideo-drbl-live) should not for drbl clients.

* Fri Apr 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-5
- Language files updated.
- Netinstall for Ubuntu now set as "gutsy hardy" in drbl.conf.

* Fri Apr 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-4
- Language files updated.

* Fri Apr 25 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-3
- Language files updated.
- exit option was added with -k*/-j0 in drbl-funtions.

* Thu Apr 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-2
- Hints in dcs was updated.

* Thu Apr 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.3-1
- Language files updated.
- Bug fixed: sis900 image should not come with full path in dhcpd.conf (created by drblpush).
- More messages were added in firstboot in Debian like linux.
- Update some functions in drbl-functions for proportional partition size creation.

* Tue Apr 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-67
- Ready for Mandriva 2008.1.
- Known_issues.txt and Known_issues_Big5.txt were updated for Mandriva 2008.1.
- Ready for Fedora 8.93 (Fedora 9 preview).

* Sun Apr 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-66
- Dummy package sysutils was removed in PKG_FROM_DBN in drbl.conf.

* Sun Apr 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-65
- Set mandriva_netinstall_ver="2008.1" in drbl.conf.

* Thu Apr 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-64
- RELEASE-NOTES was updated.
- Language files updated.
- Bug fixed: drbl live was not able to start.

* Mon Apr 14 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-63
- Language files updated.
- xfsdump and lspci were added for Clonezilla live in drbl.conf.

* Wed Apr 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-62
- Language files updated.

* Sun Mar 30 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-61
- Update scientific_netinstall_ver="5.1" in drbl.conf.
- Language files updated.

* Sat Mar 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-60
- Turn off the following netinstall in drbl.conf: redhat, debian sarge, mandriva 2007, fedora 7, ubuntu feisty and opensuse 10.2.

* Sat Mar 29 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-59
- Language files updated.

* Wed Mar 26 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-58
- Language files updated.

* Mon Mar 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-57
- Language files updated.

* Fri Mar 21 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-56
- encfs was added in the pkg lists for clonezilla live.
- Use "Exec=sudo gparted" instead of "Exec=gksudo gparted" in the GParted icon in drbl live.

* Wed Mar 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-55
- kbd instead of console-tools is used in clonezilla live template.

* Wed Mar 19 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-54
- Language files updated.

* Tue Mar 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-53
- Language files updated.

* Sat Mar 15 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-52
- RELEASE-NOTES was updated.
- Bug fixed: Public IP address setup in init.drbl was broken due to grep without -w.

* Sun Mar 09 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-51
- sdparm was added in Clonezilla live.

* Thu Mar 06 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-50
- README files in pkg dir were updated.

* Wed Mar 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-49
- PXE boot menu help messages are Refined.
- Language files updated.

* Wed Mar 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-48
- Language files updated.
- New PXE boot background. More info will be shown in pxelinux boot menu.

* Wed Mar 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-47
- Language files updated.

* Wed Mar 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-46
- Language files updated.

* Wed Mar 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-45
- pxelinux.cfg/default will be renamed as pxeinux.cfg/default.drblsaved when running generate-pxe-menu.
- zip and unzip were added in the required list in drbl.conf.
- Bug fixed: drbl-pxelinux-passwd was broken.
- New upstream syslinux 3.62. syslinux.exe and a batch file makeboot.bat are included in drbl now.

* Sun Mar 02 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-44
- FreeBSD and OpenBSD net install are supported in drbl-netinstall.
- vmware-server was added in varlib_NOT_2_be_copied in drbl.conf.

* Wed Feb 27 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-43
- Language files updated.

* Sun Feb 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-42
- binutils was removed from PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Sat Feb 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-41
- binutils, zip and unzip were added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Fri Feb 22 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-40
- New upstream memtest86+ 2.01.

* Wed Feb 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-39
- New background image for clonezilla live boot menu so that we can show some help messages in isolinux.

* Mon Feb 18 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-38
- Some typos in language files were fixed.

* Sun Feb 17 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-37
- Prompt in drbl-login-switch was updated.

* Sat Feb 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-36
- RELEASE-NOTES updated.

* Sat Feb 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-35
- client-extra-service, client-ip-hostname, client-append-fstab in /opt/drbl/conf were renamed with .example appended. This will avoid they are removed when upgrading drbl. Thanks to Dave Haakenhout <Dave.Haakenhout _at_ nccw nl>

* Sat Feb 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-34
- netinstall in dcs was refined.

* Sat Feb 16 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-33
- dcs now can accept MODE2 as netinstall, Ex: "dcs -nl netinstall netinstall-CentOS-4.6-i386". Thanks to Barny Sanchez for this idea.

* Tue Feb 12 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-32
- Language files updated.
- disktype was added in PKG_FROM_DBN_MINIMAL_NEED in drbl.conf.
- url_site in drbl.conf was changed to something like debian_url_site so that we can assign different repositories for different distributions.

* Mon Feb 11 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-31
- wget should be in PKG_FROM_DBN_MINIMAL_NEED in drbl.conf. Thanks to vascoman for reporting this bug.

* Sun Feb 10 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-30
- Language files updated.
- -k is checked when restoreparts in dcs.

* Fri Feb 08 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-29
- New upstream memtest86+ 2.00.

* Mon Feb 04 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-28
- New upstream syslinux 3.61.

* Sat Feb 02 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-27
- Language files updated.

* Sat Feb 02 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-26
- Language files updated.

* Thu Jan 31 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-25
- An example was added in drbl-collect-mac.

* Thu Jan 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-24
- Bug fixed: If the login shell is not bash, drblpush will give some error messages about drbl-functions. Thanks to Thomas Tsai.

* Thu Jan 24 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-23
- Language files updated.

* Wed Jan 23 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-22
- Function install_curl_etc_via_yum_if_necessary in drblsrv was renamed as get_url_ocs_then_install_curl_etc_via_yum_if_necessary.
- Bug fixed: find-url-in-yum-set was updated to cover some format of fedora repo (like "baseurl = http://..., the extra space before and after =).
- To avoid yum-updatesd-help locking problem, use "killproc yum-updatesd-help" in drblsrv.

* Sun Jan 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-21
- New upstream syslinux 3.60.

* Sun Jan 20 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-20
- Package refit was added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.
- Language files updated.
- Polish drblpush and some for Ubuntu 8.04.

* Sat Jan 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-19
- A variable PKG_FROM_DRBL_INSTALLED_IN_SYSTEM was added in drbl.conf.

* Sat Jan 05 2008 Steven Shiau <steven _at_ clonezilla org> 1.8.2-18
- An experimental option -q2 for clonezilla was added (Priority: ntfsclone, partclone > partimage > dd), therefore drbl-functions was updated.
- Language files updated.
- partclone was added in PKG_FROM_DRBL in drbl.conf.
- dcs was updated with new option for clonezilla ---rm-win-swap-hib and -t1.

* Sat Dec 29 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-17
- The color for warning messages was changed to "bold yellow" in drblpush.

* Sat Dec 29 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-16
- Typos in language files fixed. Thanks to evilmrb.

* Tue Dec 25 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-15
- kbdconf-bterm was moved to package clonezilla.
- console-data and console-tools are used now instead of console-common in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Mon Dec 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-14
- drbl.spec was updated.

* Mon Dec 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-13
- Suppress the error messages when searching /lib/modules/*/ubuntu/modules in drblsrv.

* Mon Dec 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-12
- netinstall setting for centos now is 4.6/5.1.
- Apply a workaround from https://bugs.launchpad.net/ubuntu/+source/upstart/+bug/65230 for messy console login bug in Ubuntu clients.
- This release should be ready for Debian Lenny.

* Sat Dec 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-11
- Turn on drbl-netinstall verbose message by default.
- rc.sysinit and halt for CentOS 4.6 were added.

* Thu Dec 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-10
- -o0|-o1 were added in drbl-functions for image saving.

* Thu Dec 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-9
- comments in kbdconf-bterm were updated.

* Sun Dec 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-8
- Bug fixed: If client machines are selected, in some cases they were parsed incorrectly. Thanks to Jazz Wang for identifying that.
- deborphan was added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.
- rc.sysinit and halt for CentOS 5.1 were added.

* Thu Dec 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-7
- New upstream syslinux 3.54

* Wed Dec 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-6
- Bug fixed: drblsrv should only use latest kernel deb if 2 kernel debs exist in /var/cache/apt/archives (Ex: linux-image-2.6.18-5-486_2.6.18.dfsg.1-13etch4_i386.deb, linux-image-2.6.18-5-486_2.6.18.dfsg.1-13etch5_i386.deb).
- Language files updated.
- linux-ubuntu-modules for Ubuntu >= 7.10 will be installed by default in drblsrv.

* Wed Dec 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-5
- RELEASE-NOTES updated.

* Sun Dec 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-4
- Language files updated.

* Sun Dec 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-3
- Language files updated.

* Sun Dec 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-2
- Language files updated.

* Sat Dec 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.2-1
- Language files updated.
- New param in drbl-functions: -q1 (--force-to-use-dd) was added.

* Thu Nov 29 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-51
- Bug fixed: YP data should be updated after YP service is up in drbl-live.sh.

* Mon Nov 26 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-50
- RELEASE-NOTES updated.
- Bug fixed: i386 glibc & openssl were not found in DRBL for Fedora 8.

* Fri Nov 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-49
- Bug fixed: YP data should be updated after accounts are created and after YP service is up in drbl-live.sh.

* Fri Nov 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-48
- Bug fixed: YP data should be updated after accounts are created in drbl-live.sh.

* Thu Nov 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-47
- Bug fixed: if the url is IP address based in yum config, it will be parsed incorrectly. Thanks to David from NCHC.
- New upstream syslinux 3.53.

* Sun Nov 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-46
- Option --no-prompt-drbl-live was added for drbl-live.sh.

* Fri Nov 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-45
- language files updated.

* Fri Nov 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-44
- language files updated.

* Fri Nov 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-43
- fedora 8 was set, fedora core 6 was removed for netinstall in drbl.conf.
- remove dhcp-common in PKG_TO_UNINSTALL_PART2_DBN in drbl.conf.

* Mon Nov 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-42
- comments updated in halt.FC8.drbl.

* Mon Nov 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-41
- language files updated.
- should be ready for Fedora 8.

* Mon Nov 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-40
- language files updated.
- confirm to start DRBL live or not in DRBL live.
- lshw was added in PKG_TO_QUERY in drbl.conf.

* Sun Nov 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-39
- language files updated.

* Sun Nov 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-38
- language files updated.

* Sun Nov 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-37
- language files updated.
- lshw was added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Sun Nov 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-36
- language files updated.

* Fri Nov 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-35
- language files updated.
- wodim cdrecord net-tools were added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf. Thanks to Spiros Georgaras.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-34
- bug fixed: if LANG is nothing, drblpush fails.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-33
- bug fixed: if LANG is nothing, drblsrv fails.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-32
- a prompt is shown in the beginning of drbl-live.sh.
- language files updated.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-31
- language files updated.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-30
- language files updated.

* Thu Nov 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-29
- language files updated.

* Wed Oct 31 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-28
- language files updated.

* Wed Oct 31 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-27
- language files updated.

* Wed Oct 31 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-26
- language files updated.

* Wed Oct 31 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-25
- language files updated.

* Tue Oct 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-24
- language files updated.

* Mon Oct 29 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-23
- language files updated.

* Wed Oct 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-22
- rewrite function chk_deb_installed in drbl-functions. Thanks to Louie Chen.

* Wed Oct 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-21
- language files updated.

* Wed Oct 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-20
- since ubuntu 7.10 (gutsy) was released, set ubuntu_netinstall_ver="dapper feisty gutsy" in drbl.conf.
- by default, -z1 set for clonezilla. Thanks to Mark Binner, tw.chi.ming _at gmail com, and ripper-cz for their experience. 
- new mechanism, the language files are renamed to match the locale setting so that it's possible for other developer to create local version. The filename was en, tw.BIG5, tw.UTF-8, now they are en_US, zh_TW.BIG5, zh_TW.UTF-8.  Will try to use gettext in the future.
- language files updated.

* Fri Oct 19 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-19
- language files updated.

* Thu Oct 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-18
- an option --prepare-ocsroot was added to drbl-live.sh.

* Thu Oct 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-17
- update language files.
- option --no_nis_update was added when run drbl-login-switch in drbl-live.sh.
- option -s was added in drbl-live.sh.
- minor bug fixed for drbl-nfs-exports.

* Thu Oct 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-16
- clonezilla-live.desktop was updated.

* Thu Oct 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-15
- bug fixed: language file en was forced to load.
- bug fixed: language icons on desktop of drbl live were fixed for clonezilla.

* Thu Oct 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-14
- update language files.

* Wed Oct 17 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-13
- bug fixed: typos fixed in language files. Thanks to Louie Chen.
- update comment in gen_client_files.sh.
- add a mechanism to allow only PXE/Etherboot client lease IP address or not.
- update language files.

* Tue Oct 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-12
- update comment about "allow member..." in drblpush.
- update drbl-live.sh, use $drbl_setup_path/files/ocs/live-hook/ocs-live.conf instead of fixed path name.
- bug fixed: use a workaround "< /dev/stdin" to avoid tftpd-hpa read problem after it is restarted in drbl-live.sh.
- function is_boot_from_live is added in drbl-functions.
- check is_boot_from_live in drbl-live.sh

* Mon Oct 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-11
- *.desktop in files/misc/desktop-icons are moved to files/misc/desktop-icons/drbl-live.

* Mon Oct 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-10
- /etc/init.d/halt of OpenSuSE is modified to avoid all processes are killed by fuser (drblpush).
- Comment the TCPwrapper related files in DRBL client which are copied from server.

* Sat Oct 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-9
- remove some $DRBL_SCRIPT_PATH in drblpush, since it's set in PATH in the beginning of script.
- bug fixed: since --not-add-start-drbl-srvi is not used, we have to start all drbl related services after dhcpd.conf is modified.

* Fri Oct 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-8
- add --not-add-start-drbl-srvi for drblpush in drbl-live.sh.

* Fri Oct 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-7
- error message is suppressed if /etc/resolv.conf is not found in drbl-live.sh
- do not prompt IP address from 2nd NIC in drbl-live.sh

* Fri Oct 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-6
- -b|--not-add-start-drbl-srvi was listed in help message of drblpush.

* Fri Oct 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-5
- an option -b|--not-add-start-drbl-srvi was added in drblpush so that it's can be used when the config is done, the service won't added and started.

* Fri Oct 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-4
- polish drbl-nfs-exports.
- add firstboot for OpenSuSE 10.3 cient.
- language files updated.
- highlight the last prompt in drbl-live.sh.
- add some mechanism to avoid default gateway and dns is set twice in drbl-live.sh.
- This release is almost ready for OpenSuSE 10.3. However, still need some improvement.

* Thu Oct 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-3
- list selections instead of yes/no for device and image name in dcs.

* Thu Oct 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-2
- ftp.twaren.net is used all instead of diskless.nchc.org.tw in drblsrv.

* Thu Oct 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.1-1
- change the opensuse (10.2 & 10.3) and mandriva (2007.1 & 2008.0) netinstall setting in drbl.conf.
- add modified rc.sysinit & halt for MDV2008.0.
- add nfs-server in drbl_server_service_chklist in drbl.conf for Mandriva 2008.
- glibc-i18ndata was added in PKG_FROM_MDK in drbl.conf for Mandriva 2008.
- force to install gpm in Mandriva 2008.
- consolekit, which is necessary for CD/USB stick automount in Mandriva 2008 in client_services_chklist in drbl.conf. cups (for Fedora, Mandriva) and cupsys (for Debian) are also added.
- add a repository ftp.twaren.net when running drblsrv in Mandriva.
- use chklist for nfs/nfs-server in drbl-nfs-exports.
- NFS_SRV_NAME is tested then be assigned in drbl.conf.
- Bug fixed: In Mandriva 2008.0, there is some special service start name "S-1", like: rc3.d/S-1nfs-server, we have to remove it in client. The old method won't.
- Use TIMEOUT= 3 secs instead of 9 secs in the workaound for mountnfs.sh or waitnfs.sh bug in debian & ubuntu.
- Do not remove account nobody in DRBL cient, since we need nobody as local account for some services.
- This release should work for Mandriva 2008.0.

* Tue Oct 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-27
- rc.sysinit & halt are ready for FC7.92.

* Mon Oct 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-26
- update language files.

* Sun Oct 07 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-25
- Polish drbl-live.sh.

* Sun Oct 07 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-24
- mc was added in drbl live/clonezilla live.
- use sudo instead of gksudo in Start_DRBL.desktop & Stop_DRBL.desktop.

* Sat Oct 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-23
- fix the position of "allow members of "DRBL-Client";" in drbl-live.sh
- auto login accounts are created in drbl-live.sh instead of ocs-srv-live-hook.

* Fri Oct 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-22
- Bug fixed: dhcpd service should be restarted after dhcpd.conf is modified in drbl-live.sh

* Fri Oct 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-21
- turn on the options in dhcpd.conf so that only PXE/Etherboot/DRBL client can lease IP address in drbl live.
- use language files in drbl-live.sh
- update language files.

* Fri Oct 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-20
- bug fixed: /etc/hosts.allow should be append in drbl-live.sh.
- add -w|--without-sorting for get-client-ip-list.
- add a message to run drblpush with config file in drblpush.
- update language files.

* Thu Oct 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-19
- run drblpush in drbl-live.sh.
- bug fixed: /etc/hosts.allow will be put with 20 clients in a line in drbl-live.sh

* Thu Oct 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-18
- typo fixed in language file.
- reformat the comments in dhcpd.conf (created by drblpush).
- a workaround to avoid the bug of mountpoint/mountnfs.sh in debian when newer kernel (2.6.22) is used.

* Fri Sep 28 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-17
- add config file prompt in drbl-netinstall help message.
- ethtool is added in Clonezilla live. Thanks to kovvu for this suggestion.
- bug fixed: if kernel package is symbolic link file, install-kernel-for-client should work.

* Wed Sep 26 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-16
- new upstream syslinux 3.52.

* Fri Sep 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-15
- update release notes.

* Fri Sep 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-14
- update release notes.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-13
- Bug fixed: netinstall image should be removed before drbl config files are removed.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-12
- Bug fixed: drbl-netinstall temp dirs were not removed.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-11
- rewrite drbl-netinstall, use function to do most of the things. Now it will skip downloading if netinstall images exists in /tftpboot/nbi_img/.
- update release notes.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-10
- update language files.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-9
- remove extra space line in drbl-netinstall.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-8
- add --nocancel and use LANG=en_US.UTF-8 in langchooser.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-7
- format the hint again.

* Thu Sep 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-6
- update language files.
- add a hint to use space key to mark the selection in dcs.

* Wed Sep 19 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-5
- packages pppoe pppoeconf were added in variable PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Wed Sep 19 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-4
- update language files.
- bug fixed: netinstall temp dirs were not removed in drbl-netinstall.

* Mon Sep 17 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-3
- update comments in dhcpd.conf (drblpush).

* Mon Sep 17 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-2
- By default, turn off 'allow members of "DRBL-Client";', otherwise the restored OS (either GNU/Linux or M$ Windows) won't be able to lease IP address if DHCP client is used in the restored OS.

* Sun Sep 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.8.0-1
- put log and class mechanism in the dhcpd.conf created by drblpush.
- Now the dhcp service which uses range statement, i.e. not providing static IP address to clients, in DRBL server will only allow PXE, Etherboot or DRBL client (in pxe initrd) to lease IP address. The vendor-class-identifier mechanism is used, and dhcpd.conf only allows PXEClient, Etherboot, or DRBLClient to lease IP address. The host statement is not affected by this new introduced mechanism.

* Fri Sep 14 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-24
- ncpfs is added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Thu Sep 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-23
- Bug fixed: the netmask in dhcpd.conf created by drblpush is not always 24, the IP address is not always to start with drbl server +1.
  
* Thu Sep 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-22
- Bug fixed: config file for drblpush can be in the working dir.

* Wed Sep 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-21
- man is added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Wed Sep 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-20
- Bug fixed: nfs-common should be installed in clonezilla live, otherwise lockd won't work.

* Wed Sep 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-19
- Bug fixed: in Fedora 7, service ConsoleKit is necessary for client.

* Mon Sep 10 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-18
- add "a" (=ask) for language option.
- bug fixed: failed to use en if LANG is nothing in drbl-perl-functions. Thanks to Louie Chen for reporting this bug.

* Sun Sep 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-17
- No more asking language index by default in the drbl-related commands. It will use the environment variable "LANG". If you still want to choose the language, use something like "/opt/drbl/sbin/dcs -l ask".

* Sun Sep 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-16
- language files are updated.

* Wed Sep 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-15
- bug fixed: DRBL SSI/Clonezilla box failed to boot. Thanks to Louie Chen for reporting this bug.

* Wed Sep 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-14
- 2 more scripts were added: list_available_tbz2, list_latest_tbz2

* Mon Sep 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-13
- typos in language files were fixed. Thanks to Louie Chen for identifying them.
- use tar.bz2 instead of tar.gz for drbl src.

* Sun Sep 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-12
- add selinux in variable diskless_root_dir_2 in drbl.conf.
- bug fixed: excluding nfs in the remounting list in halt in drbl client (Newer RedHat-like only). This bug only ran into problem in updated Fedora 7 or later.

* Sat Sep 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-11
- update language files.
- update comments in drblsrv-offline.

* Thu Aug 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-10
- minor update prompt in init.drbl.
- improve the mechanism to use nosharecache option for nfs in init.drbl and /etc/fstab. This will fix the bug https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=251655.
- update init.drbl, format the output.
- update language files.

* Tue Aug 28 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-9
- package mkswap-uuid is added in PKG_FROM_DRBL in drbl.conf.

* Tue Aug 28 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-8
- verbose output when running drbl-netinstall in drblsrv.
- update the language files.
- add a mechanism to use nosharecache option for nfs in init.drbl. This will fix the bug https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=251655.

* Fri Aug 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-7
- new upstream syslinux 3.51.

* Thu Aug 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-6
- clean the mtab in $drbl_common_root copied from server (drblpush).
- refine init.drbl.
- package pcmciautils was added in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.
- add OSSII support in drbl-functions. Only drblsrv-offline works for OSSII.
- use variable ocs_param_o0 and ocs_param_o1 in dcs so that it's easier to run the files in $OCS_PRERUN_DIR before clone.

* Thu Aug 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-5
- add dvd+rw-tools udftools for PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf. Thanks to Yavuz Onder for this idea.
- apply the patches from Bryan McLellan. Use a bash function make_random_password to replace random_pw_gen.pl.

* Wed Aug 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-4
- For netinstall files, rewrite generate-pxe-menu based on files in /tftpboot/nbi_img instead of rpm or dpkg query.
- drbl-netinstall.sh was added so that the netinstall rpm/deb is not necessary in the repository any more.

* Tue Aug 14 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-3
- use variables savedisk_preset and saveparts_preset from drbl-ocs.conf in dcs.

* Thu Aug 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-2
- language files updated.
- add -n for some mounts in init.drbl.
- change with lenny/sid in /etc/debian_version in drbl-functions.
- add 7.10 supports in drblpush.
- remove initrd-tools in PKG_FROM_DBN in drbl.conf.
- this release "should be" ready for Ubuntu 7.10 Alpha 4.

* Fri Aug 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.12-1
- typo fixed in drbl-functions.
- remove legacy examples.

* Fri Aug 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-40
- update language files, typo fixed.
- do not remove wget, lftp, gawk when uninstalling drbl in debian.
- bug fixed: /var/yp/nicknames should be copied to client, otherwise "ypcat passwd" won't work. Thanks to Louie Chen for reporting this bug.
- bug fixed: For Debian, if $drbl_common_root/etc/udev/rules.d/z25_persistent-net.rules exists, remove it. Since it contains the network MAC address from drbl server, and we should let client automatically create that. Thanks to Louie Chen for reporting this bug.

* Wed Jul 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-39
- shift -k/-r higher in drbl-functions so it's easier to be checked.

* Wed Jul 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-38
- update language files. Add more comments about GNU/Linux device name to M$ windows device names.
- update dcs, put more hints.

* Wed Jul 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-37
- update language files.
- use --menu instead of --radiolist in most of the dialog programs.
- add "curlftpfs tofrodos" in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Sun Jul 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-36
- update drbl-SL.sh to support GeeXBox 1.1, and make sure DSL 3.4 is OK, too.

* Tue Jul 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-35
- add libdigest-sha1-perl in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.
- background the command in drbl-client-reautologin
- update language files.
- add checkbox -ntfs-ok|--ntfs-ok when using dcs. With this option, we can force to save the partition or aviod the false alarm caused by ntfsresize.

* Mon Jul 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-34
- update language files.

* Sun Jul 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-33
- use yellow and red instead of bold yellow and bold red in drblpush.
- back to use gpgkey=http://drbl.nchc.org.tw/GPG-KEY-DRBL instead of gpgkey=file:///opt/drbl/pki/rpm-gpg/RPM-GPG-KEY-DRBL in drbl*.repo.

* Sat Jun 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-32
- update language files.

* Sat Jun 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-31
- put language option en when running drbl-doit in drbl-client-reautologin.

* Sat Jun 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-30
- update drbl-functions so that in Scientific Linux, the FULL OS is shown as SL.  Now drblsrv-offline should work with SL5.0.
- use gpgkey=file:///opt/drbl/pki/rpm-gpg/RPM-GPG-KEY-DRBL instead of gpgkey=http://drbl.nchc.org.tw/GPG-KEY-DRBL in drbl*.repo.
- add prompt to run drblsrv-offline if drblsrv fails.

* Tue Jun 26 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-29
- bug fixed: get_existing_partitions_from_img should not skip mounted partition in the server, since it's nothing to do with that in clients (dcs). Thanks to cyleen2345 _at_ yahoo com tw for reporting this bug.

* Sun Jun 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-28
- bug fixed: The updated kernel in Fedora 7 is not listed when running drblsrv.

* Mon Jun 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-27
- format the variables in mknic-nbi.

* Sun Jun 17 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-26
- bug fixed: An extra space in parse_dhcpd_conf is removed. Thanks to criupf for reporting this bug.
- use dhcp_server_name in mknic-nbi, and it's rewritten.

* Mon Jun 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-25
- bug fixed: ocs_opt in /proc/cmdline is filtered in firstboot for Debian and Ubuntu.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-24
- suppress the error messages about /tftpboot/nodes/$IP/etc/inittab if no that file.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-23
- prepare rpcbind in drblpush also.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-22
- minor changes in drblpush.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-21
- if no setting in /etc/sysconfig, exit 0 in drblthincli.
- FC6.93 files are removed.
- update rc.sysinit for FC7, was for FC6.93. halt.default-RH.drbl and rc.sysinit.default-RH.drbl are updated.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-20
- update comments in drblsrv.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-19
- update i686_pkg_check_list_RH_like in drbl.conf.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-18
- those i686 packages should be checked in drblsrv-offline also.
- update RELEASE-NOTES.

* Mon Jun 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-17
- update language files.

* Sun Jun 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-16
- do not exit immediataly when one service fails in drblpush (drbl-all-service).
- move service and restart in the end of drblpush.

* Sun Jun 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-15
- update find-url-in-yum-set for FC7.
- rewrite function to deal with those packages has different arch rpms (i386, i486, i586, i686) in repository. This is specially for Redhat, Fedora, CentOS.
- this release should work for FC7.

* Fri May 25 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-14
- bug fixed: the stale 01-MAC file should be removed when using dcs -> part -> IP.
- a minor bug about drbl-powerful-thin-client is fixed.

* Tue May 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-13
- halt.CO4.5.drbl and rc.sysinit.CO4.5.drbl are ready for CentOS 4.5.
- update RELEASE-NOTES.

* Mon May 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-12
- update language files.

* Fri May 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-11
- bug fixed: in AMD64 Etch, the kernel name is no more amd64-k8, only amd64. Thanks to flossy (flossymike) for reporting this.
- Ready for PuppyLinux 2.16 and DSL 3.3 in drbl-SL.sh.

* Mon May 14 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-10
- /etc/ethers is renamed as /etc/ethers.orig to avoid network lag when running drblpush -i.
- regroup the IP/MAC group list in dialg in select_hosts.
- dcs will try to use the number of selected clients for multicast clonezilla default inputted client number.
- update language files.

* Fri May 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-9
- create /dev/{console,null} right after tmpfs /dev is mounted in init.drb.

* Thu May 10 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-8
- FC5.92 files (halt, rc.sysinit) are removed. FC7 files (halt, rc.sysinit) are added.
- put locales in required for debian like Linux (drbl.conf).

* Mon May 07 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-7
- portmap is replaced by rpcbind in FC7, so add rpcbind in the checklist in drbl.conf. About ready for FC7.

* Mon May 07 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-6
- when adding drbl urpm repository, use "url/RPMS.drbl-stable with ../base/synthesis.hdlist..." instead of "url/base with synthesis.hdlist...". Otherwise in Mandriva 2007.1, it won't work. Should be the bug in urpmi-4.9.21-1mdv2007.1.
- add gpm in client_services_chklist in drbl.conf (especially for MDV2007.1, it's a must for firstboot).
-Turn on mode selection in firstboot in MDV2007.1 client.

* Mon May 07 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-5
- add delimiter in drblsrv for CentOS 5 kernel prompt.
- update halt and rc.sysinit for Mandriva 2007.1. Install gpm when running drblsrv in Mandriva 2007.1. Note! DRBL is NOT ready for Mandriva 2007.1 yet in this release.

* Sun May 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-4
- Bug fixed: kernel in release was not listed when running drblsrv for CentOS 5.
- temporarily set only kernel i686 for CentOS 5, since in the repository, only i686 kernel is officially supported.

* Sun May 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-3
- add function get_dir_filesystem() in drbl-functions to show the filesystem of input dir.
- update language files.
- ready for CentOS 5.0.

* Thu May 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-2
- skip modifying /etc/inittab for client if no /etc/inittab (drbl_ssi_client_prepare)

* Tue May 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.11-1
- minor bug fixed in switch-pxe-menu. Thanks to kachim kachim <k4chim _at_ gmail com>.
- add portmap in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf).
- update language files.
- minor bug fixed: grep -Ew instead of grep -e in drbl-cp-host.
- minor bug fixed: drbl-fuh.
- kbdconf-bterm is moved from /opt/drbl/bin/ to /opt/drbl/sbin/

* Wed Apr 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-9
- update language files.

* Sat Apr 14 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-8
- add testdisk in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf
- use "Part" instead of "Select" for dialog in dcs.

* Thu Apr 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-7
- update dcs, make it more straightforward.
- update select_hosts to allow client-(MAC|IP)-group-X where X is non-digits, and  some minor bugs fixed.
- update language files.

* Thu Apr 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-6
- update language files.

* Wed Apr 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-5
- update language files.
- add pwgen in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf

* Mon Apr 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-4
- typos ms_choose_* fixed as msg_choose_* in language files.
- append a space after $DIA_ESC in dcs and drbl-functions.
- add perl-modules in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED in drbl.conf.

* Fri Apr 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-3
- update prompt in drblpush.

* Mon Apr 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-2
- update generate-pxe-menu, for FC 4 and later, no more ramdisk_size.

* Sat Mar 24 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.10-1
- update generate-pxe-menu for Ubuntu Feisty, which uses initramfs so ramdisk_size is no more.
- update language files.
- bug fixed: drblpush is not able to change mode in pxelinux.cfg/default when system already is in DRBL SSI/Clonezilla box mode.

* Fri Mar 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-80
- use better method to assign kernel arch for Ubuntu.

* Thu Mar 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-79
- bug fixed: not smp, it's generic for kernel in Ubuntu 7.04

* Thu Mar 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-78
- bug fixed: /etc/event.d/rc-default wrong version.

* Thu Mar 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-77
- it's not necessary to create /etc/inittab for Ubuntu 6.10 or 7.04 anymore, since now clonezilla won't use that to switch runlevel.
- shorten TIMEOUT as 90 in client's /etc/init.d/waitnfs.sh due to this bug: https://bugs.launchpad.net/ubuntu/+source/sysvinit/+bug/93634

* Thu Mar 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-76
- patch Ubuntu 7.04 rc-default when running drblpush.

* Thu Mar 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-75
- create locale en_US.UTF-8 if not available in kbdconf-bterm and DRBL server (drblpush).

* Wed Mar 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-74
- add unfs3 in drbl_server_service_chklist (drbl.conf) and in drbl-all-service for DRBL live usage.

* Wed Mar 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-73
- bug fixed: wrong path when writing LANG in client's /etc/default/locale

* Wed Mar 21 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-72
- rename boot background image file name.
- add file drbllogo.png.
- drbl-live.sh is added to control the DRBL live server.

* Sun Mar 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-71
- bug fixed (useradd -g, not -G) in drbl-useradd. Help usage is added also.
- bug fixed in get_existing_autologin_account when autoloing is set and it's DRBL SSI mode, since dhcpd.conf no longer has any hostname.

* Sun Mar 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-70
- put unifont.bgf in /opt/drbl/lib in DRBL and Clonezilla live (was in /opt/lib/).

* Sun Mar 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-69
- kudzu typo fixed in drblsrv. Thanks to Piotr Wyrobek <pitrew _at_ gmail com>.

* Fri Mar 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-68
- add reiser4progs hfsutils ntfsprogs in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf).

* Tue Mar 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-67
- update language files.

* Sat Mar 10 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-66
- update language files.
- use varibles memtest_filename and drbl_logo variables in generate-pxe-menu.

* Sat Mar 10 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-65
- update language files.
- use drbllogo.png instead of drbl-pxe.png, since "-" is not accepted in isolinux.

* Fri Mar 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-64
- nis serivce should be earlier than gdm in debian.

* Thu Mar 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-63
- add console-common in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED, psmisc in PKG_FROM_DBN_MINIMAL_NEED (drbl.conf)
- /opt/drbl/bin/kbdconf-bterm is added for clonezilla live to do keyboard config.

* Tue Mar 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-62
- bug fixed: if drbl mode is none, and full clonezilla mode, client will fail boot normally.

* Tue Mar 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-61
- use $SETCOLOR_FAILURE to show no default display manager in drblpush.

* Sun Mar 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-60
- update RELEASE-NOTES.

* Sun Mar 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-59
- add variable MSWIN_ADMIN_ID in drbl.conf, use that in dcs.

* Sat Mar 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-58
- update language files.
- add reiserfsprogs e2fsprogs dosfstools xfsprogs jfsutils for debian in drbl.conf.
- reorg the variable about PKG_FROM_DBN_MINIMAL_NEED and PKG_FROM_DBN_WHICH_OCS_LIVE_NEED

* Thu Mar 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-57
- update comments in drblsrv.
- update language files.

* Wed Feb 28 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-56
- add ddrescue and gddrescue in drbl.conf (for Debian Live CD for Clonezilla).
- sort those PKG_FROM_DBN_* in drbl.conf.
- force to strip the unnecessary quotation ', this is specially for dialog (from cdialog) in Mandriva. Otherwise it will cause -p reboot becomes '-p reboot', which is wrong option in dcs.

* Mon Feb 26 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-55
- add an option skip with the options -y[0-2] in dcs and ocs-sr.
- update language files.

* Thu Feb 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-54
- update drbl-SL.sh to work with Debian Live 20070219.

* Tue Feb 20 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-53
- drbl-SL.sh works for INSERT 1.39a, PuppyLinux 2.14.

* Sun Feb 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-52
- bug fixed: variable not found, it should be maxswapsize instead of MaxSwapSize in files/misc/mkswapfile.

* Fri Feb 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-51
- add "--braodcast" in drbl-functions for clonezilla.

* Thu Feb 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-50
- wait before enter drbl SSI question in drblpush.

* Thu Feb 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-49
- add comments in /opt/drbl/setup/files/Ubuntu/6.10/rc-default.

* Thu Feb 15 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-48
- new upstream syslinux 3.36.
- use a workaround to avoid upstart bug in Ubuntu 6.10 (https://launchpad.net/ubuntu/+source/upstart/+bug/85014)

* Fri Feb 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-47
- new upstream syslinux 3.36-pre10.

* Fri Feb 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-46
- bug fixed: generate-pxe-menu honors the drbl_mode and clonezilla_mode in /etc/drbl/drbl_deploy.conf. This will avoid DRBL SSI mode and Clonezilla box mode fail after generate-pxe-menu is run again after "drblpush -i" is done.
- new upstream syslinux 3.36-pre6.

* Mon Feb 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-45
- update drbl-SL.sh so that we can force some distribution as Debian-live.

* Mon Feb 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-44
- add lvm2 in PKG_FROM_DBN_MINIMAL_NEED in drbl.conf.

* Sat Feb 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-43
- update language files.

* Fri Feb 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-42
- load language file automatically for drbl-SL.sh when uninstalling drbl.

* Thu Feb 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-41
- language support, -d/-V are added in drbl-SL.sh.
- update Usage in drbl-SL.sh.

* Thu Feb 01 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-40
- PUD GNU/Linux is supported by drbl-SL.sh.

* Tue Jan 30 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-39
- add mtools in PKG_FROM_DBN in drbl.conf.
- add a dir /opt/drbl/image for background images in syslinux/pxelinux/isolinux and grub.
- use variable ocs_logo_img_syslinux and ocs_logo_img_grub in drbl.conf.

* Mon Jan 29 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-38
- prepare a dir for ocs lock file in drblpush.
- update language file, avoiding some annoying Big5 characters.
- new upstream syslinux-3.35.

* Fri Jan 26 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-37
- add isolinux_file="$pxelinux_binsrc_dir/isolinux.bin" and isolinux_bg_img="$pxelinux_binsrc_dir/ocslogo.png" in drbl.conf
- language set can use zh_TW.BIG5 or zh_TW.UTF-8.
- update language files.

* Tue Jan 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-36
- add no warranty notice in dcs for clonezilla.

* Tue Jan 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-35
- add fbset in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf)

* Tue Jan 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-34
- add localepurge in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf)

* Tue Jan 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-33
- use "Traditional Chinese" instead of "Chinese Traditional"

* Tue Jan 23 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-32
- add "ssh sshfs smbfs lftp dhcp3-client testdisk" in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf)

* Mon Jan 22 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-31
- add bogl-bterm and whiptail in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf).
- mv create-debian-live to package clonezilla.
- /opt/drbl/bin/langchooser, /opt/drbl/sbin/tw-bterm are added.

* Thu Jan 18 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-30
- function added root_over_nfs in drbl-functions.

* Wed Jan 17 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-29
- add screen in $PKG_FROM_DBN_WHICH_OCS_LIVE_NEED
- add -x for shutdown command with cygwin clients in dcs.

* Tue Jan 16 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-28
- replace all /tftpboot/node_root/ with $drbl_common_root in drblpush.
- add comment in $drbl_common_root/sbin/fsck.nfs.
- Debian Etch has NetworkManager/NetworkManagerDispatcher under dbus, we can not let it start in client. Otherwise the network in client will be reset.
- new upstream memtest80+ 1.70
- add tar in PKG_FROM_DBN_MINIMAL_NEED.
- use variable pxelinux_binsrc_dir in drbl.conf, add mbr.bin from syslinux in /opt/drbl/pkg.
- clean /boot/initrd*.bak in create-debian-live
- add package syslinux from GNU/Linux as a requirement in drbl.conf, since when we create ocs live media (usb), it's necessary.

* Sun Jan 14 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-27
- add ntfs-3g in PKG_FROM_DBN_WHICH_OCS_LIVE_NEED (drbl.conf).

* Sat Jan 13 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-26
- add gzip in PKG_FROM_DBN_MINIMAL_NEED, and add another PKG_FROM_DBN_WHICH_OCS_LIVE_NEED="less"
- update languages for ocs-iso.

* Fri Jan 12 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-25
- add util-linux in PKG_FROM_DBN_MINIMAL_NEED (drbl.conf).

* Thu Jan 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-24
- bug fixed: when dcs -d3 is running, select_hosts should run -d3, too.

* Thu Jan 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-23
- update sbin/create-debian-live, add /etc/rc2.d/S99ocs-live in squashfs.

* Thu Jan 11 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-22
- add bzip2 and procps in PKG_FROM_DBN (drbl.conf).
- now $PKG_FROM_DBN_MINIMAL_NEED and $PKG_FROM_DBN in drbl.ocs
- add sbin/create-debian-live

* Wed Jan 10 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-21
- update prompt in check_kernel_nfsd_tcp_config.
- new function: The script in the direcoty $POST_RUN_DIR will be run before drblpush is run and after it's finished.
- switch-pxe-menu, select_hosts support -d[0-4], dcs will also pass -d[0-4] to them when call them.

* Tue Jan 09 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-20
- bug fixed: now the variable is drbl_mode instead of drbl_ssi_mode

* Mon Jan 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-19
- update language files.
- re-org the mode layouts in dcs, rename "others" as "more".

* Mon Jan 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-18
- bug fixed: language file syntax error.

* Mon Jan 08 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-17
- 3 modes for drbl_mode: full_drbl_mode, drbl_ssi_mode, none. 3 modes for clonezilla mode: full_clonezilla_mode, clonezilla_box_mode, none.
- some options will be hidden in dcs if appropriate files do not exist in system.

* Sat Jan 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-16
- bug fixed: drbl-SL.sh failed to uninstall Debian-live.
- drbl-SL works for GeeXbox 1.0 and 2.0 preview.
- now the estimated ramdisk_size is based on initrd size, client's ram size is also estimated by * 3.

* Sat Jan 06 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-15
- update help message in set-default-pxe-img
- drbl-SL supports debian live etch.

* Fri Jan 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-14
- separate -y0/-y1/-y2 for clonezilla-start in dcs.

* Fri Jan 05 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-13
- Since now clonezilla and drbl are decoupled in PXELinux menu, when clonezilla_box_mode is off, drbl_ssi_mode maybe still on. We have to show all the menus in dcs.
- use script /opt/drbl/bin/hide_reveal_pxe_img instead of fnction.

* Thu Jan 04 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-12
- when gen_client_files.sh is run in drblpush, we put ocs related services in client's rc1.d, and ocs-run is put also.
- since now drbl and clonezilla are decoupled, we should not suppress these mode when clonezilla box mode is chosen in drblpush: $swap_create="no"; $client_startup_mode="2"; $set_client_root_passwd="no"; $set_DBN_client_audio_plugdev="no"; $set_client_alias_IP="no";         

* Wed Jan 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-11
- update help message in mknic-nbi.
- modified linuxrc for puppylinux 2.13 is added.
- Since now the clonezilla and drbl labels are separated in PXELINUX menu, no more program turn-drbl-ssi-mode. It is replaced by tune-clientdir-opt.
- use tune-clientdir-opt instead of turn-drbl-ssi-mode in drblpush.

* Wed Jan 03 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-10
- update RELEASE-NOTES
- add 1 in clonezilla block template (generate-pxe-menu)

* Tue Jan 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-9
- update RELEASE-NOTES

* Tue Jan 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-8
- update RELEASE-NOTES

* Tue Jan 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-7
- add label clonezilla when using generate-pxe-menu to create the pxelinux config. This will allow clonezilla to be decoupled with drbl menu in pxelinux.

* Tue Jan 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-6
- init.drbl will ignore those ocs_opt bootparam when passing to init.

* Tue Jan 02 2007 Steven Shiau <steven _at_ clonezilla org> 1.7.9-5
- change exec /sbin/init.orig $* -> exec /sbin/init.orig `cat /proc/cmdline` $* in init.drbl.
- update comments in drbl-functions for single user mode password.
- use function check_if_run_in_drbl_server in dcs.
- deploy service ocs-run from clonezilla to /tftpboot/node_root/etc/init.d in drblpush.
- update some prompt in arm-wol.
- update language help in drbl-functions.

* Thu Dec 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.9-4
- update language help in drbl-functions.
- we can choose only the disk we want to restore when there are more than 2 disks in an saved image.

* Wed Dec 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.9-3
- when serial console parameters are found in $pxecfg_pd/pxelinux.cfg/default. Force to use text PXELINUX menu, no graphic background.

* Wed Dec 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.9-2
- bug fixed: opensuse-10.2.repo was missing.

* Wed Dec 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.9-1
- add a function run_drblsrv_offline in drblsrv.
- bug fixed: serial console parameters was not created in PXE linux config file.
- if serial console for client is set, force to use menu.c32 for PXE Linux menu.
- if text mode login for client is set, force to use menu.c32 for PXE Linux menu.

* Tue Dec 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-23
- "-p true" is added in dcs and drbl-functions.
- add -d[34] for gdialog and kdialog in dcs.

* Tue Dec 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-22
- typo corrected: New NBI initrd size (uncompressed) should be in KB instead of in MB in drbl-SL.

* Mon Dec 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-21
- drbl-pxe-passwd (option -b) can turn on/off and assign MENU PASSWD for some specific lable blocks.

* Sun Dec 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-20
- turn on -c before saving in drbl-functions.
- -c option is added for drbl-ocs.

* Sat Dec 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-19
- remove --no-shadow in dcs, add -- in $DIA in drbl-functions so that whiptail works with dcs.
- add -d[0-2] so that we can choose to use dialog, Xdialog or whiptail in dcs.
- rename package partimage as drbl-partimage.
- put $DRBL_SCRIPT_PATH/sbin:$DRBL_SCRIPT_PATH/bin before original PATH in drbl-functions. This will put partimage/ntfsclone/lzop from drbl in higher priority.
- provide -y0/-y1 and -p xxx choice when in select-in-client mode (dcs).

* Thu Dec 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-18
- update language files.

* Thu Dec 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-17
- default to turn on -c (confirm) in dcs when using select-in-client mode (dcs).
- check if image name is reserved name when saving image in dcs.

* Wed Dec 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-16
- To avoid confusion, package lzop is renamed as drbl-lzop, and exec file is in /opt/drbl/bin/lzop

* Wed Dec 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-15
- rename ask_if_skip_set_ocs_extra_param as set_drbl_ocs_extra_param, and move it from dcs to drbl-functions. set_ocs_sr_extra_param is also added.
- a mode "select_in_client" in added in dcs, and use shorter option  (such as clonezilla-save-disk -> save-disk) in dcs.
- change the ocs parameter option in dcs: -p true -> -p choose, this will allow us to choose to reboot or enter single user mode when clone finishes.
- Now the lease time (300 secs) in dhcpd.conf is much shorter than before. Add DHCPD_DEFAULT_LEASE_TIME="300" and DHCPD_MAX_LEASE_TIME="300" in drbl.conf, use that in dhcpd.conf. 
- update language files.

* Tue Dec 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-14
- bug fixed: should be exit 1 in mkswapfile.

* Tue Dec 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-13
- if mkswapfile is nonthing, return 1 (mkswapfile).
- update prompt in mknic-nbi.
- The function name in mountnfs.sh in etch is changed, so modify the code in drblpush.

* Sat Dec 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-12
- We can let DRBL server as or not as NAT server (drblpush)
- new upstream syslinux 3.32-pre8

* Sat Dec 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-11
- Bug fixed: DRBL SSI fails to boot in Sarge. By using create_dev() and put it in the early stage in init.drbl, and do not redirect stderr and stdout to /dev/null when untar etc/var/opt tarball in drbl ssi mode, if redirect, and without creating dev files before this, it will fail to boot in sarge or older dists (Those shows "Warning:unable to open an initial console" when entering init.drbl). Therefore DRBL SSI and clonezilla box will fail!

* Fri Dec 15 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-10
- bug fixed: typo in default clonezilla image path (drblpush).

* Fri Dec 15 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-9
- only the path is not under /mnt, /media and /tmp can be the clonezilla image repository (drblpush).
- check if dcs is run in drbl server, if it's in client, abort.
- add "iptables -P OUTPUT ACCEPT" in drbl-nat-rules.
- update prompts for nisdomain, dnsdomain... (drblpush).

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-8
- update RELEASE-NOTES for drbl-etherboot.
- update prompts in drblpush.

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-7
- update comments in mknic-nbi.
- initramfs is turn on only for kernel 2.6.15 or later.

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-6
- update prompts.
- remove stalled files in /opt/drbl/setup/files/.
- bug fixed: rpm complained /static/sh is required.

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-5
- move del_param_in_pxelinux_cfg_drbl_related_block() and  add_param_in_pxelinux_cfg_drbl_related_block() to drbl-functions from mknic-nbi.

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-4
- update language files.
- bug fixed: we should create the pxelinux menu file, then use mknic-nbi, which will update pxelinux menu file (drblsrv-offline).

* Thu Dec 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-3
- update prompt in mknic-nib.
- update language files.
- if kernel 2.6 is found, default to use initramfs (mknic-nbi), now mknic-nbi will add or del ramdisk_size/ramdisk_blocksize in pxelinux.cfg/default.

* Tue Dec 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-2
- package etherboot is renamed to drbl-etherboot to avoid confusion with that from GNU/Linux distribution. Therefore drblpush, drbl.conf and prepare_files_for_PXE_client are modified.
- /etc/opt/kde3/share/config/kdm/kdmrc is no more in OpenSUSE 10.2, so get_gdm_kdm_conf_filename in drbl-functions is modified.

* Mon Dec 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.8-1
- reorg file arch:/opt/drbl/setup/files/ -> /opt/drbl/setup/files/{DBN,RH,MDK,SUSE}/.
- add -t|--initfs-type support in mknic-nbi.
- supports OpenSuSE 10.2.

* Sat Dec 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-12
- bug fixed: The partitions are not shown in the batch prompt when doing restore-partitions of clonezilla in dcs (drbl-client-switch).
- update language files.
- If files are put in /tftpboot/node_root/drbl_ssi/clients/$IP/, it will be copied to DRBL client when client boots. By doing this, we can assign some special setting for DRBL SSI client. Check /tftpboot/node_root/drbl_ssi/clients/00_README for more details.
- add function is_drbl_client in drbl-functions.

* Mon Dec 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-11
- add ntfs-3g in PKG_TO_QUERY (drbl.conf).
- bug fixed: when stop clonezilla in dcs, if $LIST_HOST is on, we should only stop those clients, otherwise the pxelinux config files will be in a mess (dcs).

* Sun Dec 03 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-10
- graphical boot for Fedora can be on by either (1) generate-pxe-menu -g y (2) graphical_boot=yes in drbl.conf.
- new upstream DSL 3.1, modified linuxrc, and drbl-SL.sh examples are updated.
- comment 'option host-name "$label";' in drblpush, and will remove that in the future since it's useless. Client's hostname actually is not assigned there.
- if root, copy id_rsa.pub as authorized_keys in clients only, no more copying private key (drbl-doit).

* Tue Nov 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-9
- if desired kernel is not found in release repository, use the one in updates repository as default in RH/FC/MDV (drblsrv).
- force to upgrade kudzu when updated version is released in FC6.

* Mon Nov 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-8
- update language files.

* Sun Nov 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-7
- A setdefault function is added in dcs -> switch-pxe-menu, now we can switch any revealed menu (including those small linux, DSL, PuppyLinux) as client's default boot menu.
- update language files.
- add delete_label_block_pxe_img in drbl-functions.
- drbl-SL.sh now supports uninstall. and now the mode to install or uninstall [-i|-u] (such as "drbl-SL.sh -i *.iso") must be assigned.
- add SL remove function in drblsrv.

* Fri Nov 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-6
- Rename /opt/drbl/conf/drbl-client-ip-hostname as /opt/drbl/conf/client-ip-hostname.
- update the contents of /opt/drbl/conf/client-ip-hostname.

* Fri Nov 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-5
- Bug fixed: some case in Clonezilla, save and restore loop forever. Thanks to Dave Haakenhout <Dave.Haakenhout _at_ nccw nl>. This is done by reporting lowecase MAC address in get_mac so that the created PXE config file in the server is lowercase.
- parse_dhcpd_conf only creates lowercase MAC address table.
- drbl-collect-mac converts the collected MAC address to lowercase.
- force to install gpm for MDV2006/MDV2007 since released cdialog can not work correctly without gpm running.
- two types of lzma is supported in drbl-SL.sh.
- record IP hostname list in /etc/drbl/IP_HOST_TABLE.
- now we can assign client hostname in /opt/drbl/conf/drbl-client-ip-hostname before running drblpush -i.
- DBN4.0/firstboot.DBN4.0.drbl added.

* Thu Nov 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-4
- Change the mode of linuxrc-*.drbl to be 644 in files/INSERT, this will avoid the rpm check if /bin/ash exists.

* Thu Nov 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-3
- bug fixed: put the missing file /opt/drbl/setup/files/INSERT/default/linuxrc.INSERT-default.drbl

* Thu Nov 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-2
- update usage and example url in drbl-SL.sh
- add INSERT Linux support in DRBL-SL.sh
- add notes in Small Linux linuxrc.
- merge drbl-pld-rescue.sh into drbl-SL.sh, no more drbl-pld-rescue.sh. Now drbl-SL.sh supports these 4 small linux: DSL, PuppyLinux, INSERT and PLD.

* Wed Nov 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.7-1
- update language files, add msg_ocs_param_ns.
- add "-ns" for clonezilla in dcs.
- add a command sbin/drbl-pld-rescue.sh to load PLD Linux Rescue CD to DRBL environment.

* Sat Nov 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-35
- For root account, we will NOT copy authorized_keys, since the root in the client should not share the same authorized_keys with that in server. For normal user, we let user can ssh login back to server and other machine without password. (drbl-doit)
- For better security, /tftpboot/nodes mode is 700.

* Thu Nov 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-34
- update language file.
- update linuxrc for PuppyLinux 2.12*.

* Tue Nov 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-33
- bug fixed: drbl-SL.sh now works for PuppyLinux 2.12beta2.

* Mon Nov 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-32
- Change the mode of linuxrc-*.drbl to be 644 in files/Puppylinux and files/DSL, this will avoid the rpm check if /bin/ash and /static/sh exists.

* Mon Nov 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-31
- add drbl-SL.sh so that we can load DamnSmallLinux iso (dsl-3.0.1.iso) and PuppyLinux iso (puppy-2.11-seamonkey-xorgdrvrs.iso) to DRBL environment.

* Thu Nov 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-30
- suppress the grep /etc/kudzu error.

* Thu Nov 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-29
- Improve the kernel installation checking mechanism for clients (drblsrv).

* Thu Nov 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-28
- Bug fixed: fixed the wrong path for MDV2006 urpm.addmedia.

* Wed Nov 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-27
- report more info (such as server CPU, memory size, client no and all the DRBL-related packages) in drbl-bug-report, and now output the result to a file, not in stdout any more.
- exclude /etc/selinux/targeted when create DRBL SSI etc tarball.

* Tue Nov 07 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-26
- stop yum-updated service to avoid conflict in FC, we will resume it when packages installation finish.

* Tue Nov 07 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-25
- get_common_usersname is rewritten based on /var/yp/Makefile.
- bug fixed: FC6, the RPM-GPG-KEY-fedora & RPM-GPG-KEY are only in /etc/pki, not in /usr/share/doc/fedora-release* any more.

* Mon Nov 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-24
- default to suppress the output of depmod, and -v for install-kernel-for-client and update_client_kernel_from_server.sh.
- add -v|--verbose option for drblsrv and drblsrv-offline.
- pass -v option to update_client_kernel_from_server.sh from drblpush.

* Sun Nov 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-23
- create $drbl_common_root/lib/modules/$KERNEL_VER/volatile in drblsrv-offline instead of drblpush.
- add --just-cp-files for install-kernel-for-client, --extra-client-kernel-pkg for drblsrv-offline.
- drblsrv will download restricted modules in Ubuntu if /etc/init.d/linux-restricted-modules-common exists.
- depmod uses -b /tftpboot/node_root instead of chroot.
- add comment in drbl-function for create_depmod_env and clean_depmod_env

* Thu Nov 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-22
- do not copy /etc/selinux/targetd to client, since selinux is disabled in client, this will save about 40 MB space for each client in FC6.

* Thu Nov 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-21
- replace $newroot with $drbl_common_root (drblpush)
- won't write "KUDZU_ARGS=-q" again if it exists when running drblpush again.

* Thu Nov 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-20
- language file updated.
- client_services_chklist is put in drbl.conf instead of drblpush.
- bug fixed: In FC6 client, if different NIC is detected, ifcfg-ethx will be created with dhcp onboot=yes. We remove network or network-up service in client to avoid the ifcfg-eth0 with dhcp and onboot=yes re-generated by kudzu to take effect.

* Thu Nov 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-19
- bug fixed: in clonezilla box mode, if $ocsroot is /opt/foo, now client will not fail to use that.

* Wed Nov 01 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-18
- exclude some seldom kernel for Debian etch (drblsrv).

* Mon Oct 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-17
- add prompt to solve the problem when http://ftp.isu.edu.tw is used in CentOS.

* Mon Oct 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-16
- update language files and programs, some typos fixed.

* Mon Oct 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-15
- update prompt messages in drblpush.
- bug fixed: show only the latest glibc/openssl rpm if it's necessary to reinstall them (drblsrv-offline).
- add mysql in varlib_NOT_2_be_copied (drbl.conf).
- rm /etc/init.d/drbl-clients-nat when uninstall drbl in debian (drblsrv).

* Sun Oct 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-14
- add add/del option for drbl-all-service.
- update dcs with drbl-all-service.
- drblpush now use drbl-all-service to add and start DRBL-related services.

* Sat Oct 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-13
- bug fixed: if optimization CPU level is chosen, drblsrv will fail to download the kernel for client if server is i686. Now use linux-image-2.x.y-generic for i686, and linux-image-2.x.y-386 for i386.

* Thu Oct 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-12
- update language files.
- bug fixed: dcs should not clean any PXE host-based config file for all the case, only for some cases.

* Wed Oct 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-11
- update language files.
- FC6 released, so update rc.sysinit with FC6 (was from FC5.92)

* Wed Oct 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-10
- if /opt/drbl/conf/client-local-fstab exists, we will append the fstab to all client's /etc/fstab.
- change /etc/drbl/client-extra-service to /opt/drbl/conf/client-extra-service, now drblpush will read /opt/drbl/conf/{client-extra-service, client-append-fstab).
- rename /opt/drbl/conf/dcsrc to /opt/drbl/conf/dcsrc.example, avoid confusion.
- add drbl_setup_cfg="$DRBL_SCRIPT_PATH/conf" in drbl.conf.
- add "-b" when prompting run drbl-ocs again.
- update language files.

* Sun Oct 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-9
- increase the rsize and wsize to 65536 (was 8192) for NFS client parameters (init.drbl and gen_client_files.sh).

* Sat Oct 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-8
- put usage_details following usage so that it's easier to modify in drblpush.
- if $ocsroot is not under /home, or if $ocsroot is a mount point, we have to export it (drbl-nfs-exports and gen_client_files.sh)

* Fri Oct 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-7
- update the language files.

* Thu Oct 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-6
- use $ocs_lock_dir/clonezilla.lock instead of $drbl_syscfg/clonezilla.lock (ocs_lock_dir is /var/lock/clonezilla).

* Thu Oct 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-5
- format the output message for drbl-pxelinux-passwd.
- update language file.
- put $diskless_root_dir_1 and $diskless_root_dir_2 in drbl.conf instead of drblpush
- now we can assing clonezilla image dir when running drblpush.
- add parameter "-o|--clonezilla_home DIR" in drblpush.
- use $drbl_syscfg/clonezilla.lock instead of $ocsroot/clonezilla.lock.
- public_ip_list should be defined in drblpush, not drbl.conf.
- read ocsroot from drbl.conf as the default value when running drblpush.
- add glibc version and arch in bin/drbl-bug-report (for RH-like and Suse).

* Thu Oct 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-4
- switch-pxe-bg-mode more verbose when changing mode.
- add "switch-pxe-bg-mode" in dcs -> others.

* Thu Oct 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-3
- update the language file for mkswapfile in drblpush.
- if udev is found in the server, we won't try to see if dev and MAKEDEV rpm exist in the repository.
- For FC6, since start_udev uses udevtrigger now instead of udevstart, we add this in init.drbl "[ -x /sbin/udevtrigger ] && /sbin/udevtrigger".
- change "-i|--skip-client-kernel-install" to "-p|--skip-client-kernel-install" to avoid confusion with "drblsrv -i".

* Wed Oct 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-2
- use $DRBL_SCRIPT_PATH/sbin/drblpush instead of $DRBL_SCRIPT_PATH/setup/drblpush in dcs.
- bug fixed: we should read all the config parameters, those missing are: $client_root_passwd $client_pxelinux_passwd $clonezilla_box_mode $drbl_ssi_mode $account_passwd_length and $client_autologin_passwd. Hence "drblpush -c /etc/drbl/drblpush.conf" works now.

* Tue Oct 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.6-1
- update language files.
- now user can assign some directories in drbl.conf so that client will NFS mount it automatically.
- rewrite drbl-nfs-exports and gen_client_files.sh, make it more compact.
- this release is ready for CentOS 4.4, Ubuntu 6.10, Fedora Core 6 (use drblsrv-offline instead of drblsrv), and Mandriva 2007.0.

* Tue Oct 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-15
- update scripts in setup/files/default/.

* Tue Oct 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-14
- update some comments in drblsrv and drblpush.

* Tue Oct 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-13
- bug fixed: some directories should not be umounted when halt (CentOS 4.4).

* Tue Oct 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-12
- bug fixed: in CentOS 4.4, the mirrorlist query policy changes, we have to follow that in drblsrv.
- bug fixed: /tftpboot/node_root/var/lock/rpm/ is necessary for installing the kernel for client (install-kernel-for-client).

* Mon Oct 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-11
- bug fixed: For SuSE, actually the config file is in /etc/opt/kde3/share/config/kdm/kdmrc, therefore put /etc/ in the beginning in drbl-functions.

* Mon Oct 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-10
- only when /var/lib/{rpm,dpkg} exists, we will create /tftpboot/nodes/$ip/var/lib/{rpm,dpkg}. This fixed the bug that auto login account does not match the hostname when auto login is chosen in DRBL SSL mode.
- bug fixed: we should use the existing nisdomainname as the default value if it exists.

* Mon Oct 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-9
- remove unnecessary script sbin/modify_gdm_cfg_block.
- bug fixed: GDM_CFG & KDM_CFG should be queried to obtained by rpm or dpkg in drbl_ssi_client_prepare, and the auto login id now can match the hostname.
- init.drbl now will mount /var/lib/{dpkg,rpm} before running drbl_ssi_client_prepare if it's DRBL SSI mode.
- we show 3 different modes: Full DRBL mode, DRBL SSI mode and Clonezilla box mode when booting running init.drbl so that it won't confuse people why in Clonezilla mode, it still shows DRBL SSI mode.
- GDM_CFG, FAC_GDM_CFG and KDM_CFG are got in drbl-functions, no more set in drbl.conf.
- in dcs, -z3 is always the default one no matter it's ntfsclone or partimage.  Give more example, like sda, sda1 sda2 in clonezilla save.

* Sun Oct 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-8
- for NIS domainname, we will not use "localdomain" and "(none)" (drblpush).
- use a better method to select the kernel for clients in RH/MDK, now we can also choose the kernel running in the server if the CPU arch meets.

* Fri Oct 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-7
- make updates of urpmi in MDV2007 work.

* Thu Oct 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-6
- use dnsdomainname and nisdomainname to get the system setting in the server instead of parse_net_conf (drblpush).
- fixed the bug that client's gdm theme is not correctly set in the client (drblpush).
- default to show -j0 (off) in dcs (not -j) now, since now we change the create_part_by_sfdisk=yes as default.

* Thu Oct 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-5
- if domainname is "localdomain", we use default vaule: drbl.sf.net in drblpush.

* Thu Oct 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-4
- if required packages are not installed, it's possible to continue in drblsrv-offline.
- use apt/yum to uninstall package drbl when uninstalling.

* Wed Oct 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-3
- reiserfs program and ddrescue are not necessary programs (drbl.conf).
- add ramdisk_blocksize=1024 for client's kernel parameter in generate-pxe-menu (http://www.mail-archive.com/rhelv5-beta-list@redhat.com/msg00086.html), since in kernel 2.6.18, CONFIG_BLK_DEV_RAM_BLOCKSIZE=4096 in FC5.92 is too small for network initrd.
- For kernel 2.6.18, it seems if root is ro, all the mount later (such as /etc, /var) will be ro in init.drbl, so remount the root filesystem read-write in init.drbl.
- Do not set drbl theme GDM config in the server and drbl.spec, only for clients.
- add an option (set_drbl_gdmgreeter) in drbl.conf so that we can decide to set DRBL gdm greeting background for DRBL clients or not.
- If drbl SSI and clonezilla box is not set, template tarball won't be created when running drblpush.
- bug fixed: unable to get nisdomainname in parse_net_conf in FC.
- we can always set domainname and nisdomainname everytime when running drblpush.
- This release should work in FC6.

* Thu Sep 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-2
- bug fixed: list_available_rpm and list_available_deb fail for http repository.

* Thu Sep 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.5-1
- bug fixed: unable to find dm in Mandriva with check_dm.
- use "XFdrake --auto" in firstboot for MDV 2007.0.
- use grep -E '\.deb\>' & grep -E '\.rpm\>' instead of grep -E '\.deb$' & grep -E '\.rpm$' in list_available_deb list_available_rpm for ftp repository
- Some repo output DOS (CR/LF), convert to Unix format: sed# 's/.$//' in list_available_deb list_available_rpm.
- rewrite the method to add urpmi repository in mandriva, just use "--distrib --probe-synthesis"
- new upstream syslinux 3.31.
- for newer distribution, since no smp kernel package availalbe, we won't ask if client will use smp kernel or not.
- This version is beta release for Mandriva 2007.0 RC2 and Ubuntu 6.10 beta.

* Mon Sep 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-20
- turn on gpgcheck for all drbl-*.repo
- if more than one kernel rpm in repository, we can choose any one of them now.
- remove mkswapfile and drbl-nat.up.rules when uninstalling.
- delete useless script sbin/get_pxelinux_passwd.
- ask if want to use graphic pxe boot menu for clients.

* Sun Sep 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-19
- change #!/bin/sh to #!/bin/bash for language files.
- update output messages for gen_ssh_host_key.
- This release and clonezilla should work for Ubuntu Edgy (6.10) now.

* Sun Sep 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-18
- bug fixed: if /etc/rc2.d/S99[gk]dm does not exist in server, now it will be created in client, and we set it as S13[gk]dm for all debian-based distribution. Hence gdm/kdm starts earlier than before.
- add subtree_check and no_subtree_check for exports in drbl-nfs-exports
- move drblthincli to S12drblthincli for all debian-based distribution.
- new upstream syslinux 3.31-pre4.

* Fri Sep 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-17
- To avoid there is no input output in rc running, we add exec </dev/console >/dev/console 2>&1 in firstboot for DBN-TU. Thanks to Scott James Remnant (keybuk).
- move firstboot for Debian to rcS.d
- create /etc/inittab for client when using upstart.

* Thu Sep 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-16
- since Ubuntu edgy uses dash as the default sh (/bin/sh), to avoid error in dash, we use "> /dev/null 2>&1" instead of "&>/dev/null" in perl (drblpush)
- if "drblsrv-offline -i", we still create the NBI.
- add usplash as client service in ubuntu or debian.
- check if the dm exists or not before set that for client, if not, show warning.
- this is an alpha release for Ubuntu Edgy. (Clonezilla is not ready for edgy).

* Wed Sep 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-15
- change the #!/bin/sh to #!/bin/bash in /opt/drbl/setup/files/*

* Wed Sep 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-14
- change the #!/bin/sh to #!/bin/bash in /opt/drbl/{bin,sbin}/*

* Tue Sep 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-13
- reset some stale status (such as stop clonezilla), since maybe drblpush is run again.
- if pxelinux passwd is not set, will force to disable to avoid the stale setting.

* Tue Sep 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-12
- new upstream syslinux 3.30.

* Sun Sep 17 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-11
- new upstream syslinux 3.30-pre10.

* Sat Sep 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-10
- Set the color for unselected menu item and timout message in PXE boot menu.

* Sat Sep 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-9
- new upstream syslinux 3.30-pre9.

* Fri Sep 15 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-8
- Now clonezilla can not be multi-image, so it will be a mess if just stop some clients. Therefore if IP_LIST exists, we still stop all the clonezilla process.
- In debian unstable, the mountnfs.sh from initscripts 2.86.ds1-19 or later use the same skill with waitnfs.sh, so we use the same way to fix the NFS problem.

* Thu Sep 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-7
- update the drbl-pxe.png and RELEASE-NOTES. 

* Thu Sep 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-6
- update the drbl-pxe.png.

* Wed Sep 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-5
- new upstream syslinux 3.30-pre5.
- default to use vesamenu.c32 instead of menu.c32.
- check if necessary packages are installed when using apt-get install in drblsrv.

* Tue Sep 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-4
- change the filename in drbl*.repo, gpgkey=http://drbl.nchc.org.tw/GPG-KEY-DRBL (was gpgkey=http://drbl.nchc.org.tw/RPM-GPG-KEY-DRBL)

* Mon Sep 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-3
- bug fixed: we should choose advanced parameters, then to see if it's necessary to choose the image name (if -u, not necessary) in dcs.

* Sun Sep 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-2
- when using dcs to swith client's mode,  keep the way pxelinux config menu is, just change the default mode, not not reset to default (3 menus).
- bug fixed: parse host client (-h) error in drbl-powerful-thin-client
- in dcs, If the mode is autologin or timed login graphic mode, we should switch to graphic mode first.

* Sun Sep 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.4-1
- use drblsrv-offline in drblsrv.
- update the language files.
- add options -a|--no-prompt-different-arch-pkgs, -c|--no-required-pkgs-check and -i|--skip-client-kernel-install in drblsrv-offline.
- bug fixed: "-p true" description missing in dcs.
- find the etherwake/ether-wake program first in drbl-doit. For FC: ether-wake, for Debian: etherwake.
- Bug fixed: in Mandrake 10.0, for init.drbl, we put dev.tgz as the first priority, higher than udev, so that if necessary, such MDK 10, we can force to use dev.tgz instead of udev. (Since in MDK10, there is /sbin/udev, but no /sbin/udevstart or /sbin)

* Mon Sep 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.3-2
- make the i386/i586 glibc prompt more specific in drblsrv-off.

* Wed Aug 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.3-1
- add scripts create_pxe_nbi_files and prepare_files_for_PXE_client so that it's easier to reuse them.
- use $PKG_FROM_RH, $PKG_FROM_MDK, $PKG_FROM_SUSE, $PKG_FROM_DBN, $PKG_TO_QUERY, $PKG_FROM_DRBL in drblsrv and drbl.conf
- add drblsrv-offline (only works for kernel 2.6 (udev)) and install-kernel-for-client. Now we can install the necessary packages by any means then run "drblsrv-offline" to configure the server. Check /opt/drbl/doc/examples/drblsrv-offline*.txt to see how to use it. For paramaters of drblsrv-offline, use "drblsrv-offline --help" to get them. Note! You still have to run "/opt/drbl/sbin/drblpush -i" after drblsrv-offline.
- when local kernel in the server is chosen, we force to use the KARCH from the server, otherwise maybe the kernel in the repository has different CPU arch.
- use "dpkg -L drbl &> /dev/null" instead of "dpkg -s drbl &> /dev/null" to check if drbl deb is installed or not.
- add "-p poweroff" for clonezilla in dcs.
- move "perl -p -i -e "s/^[[:space:]]*set -e.*/#set -e/g" /etc/init.d/tftpd-hpa"
from drblsrv to drblpush.

* Sun Aug 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-13
- new upstream syslinux-3.20.

* Fri Aug 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-12
- create /etc/ethers and update the arp data before send wake-on-LAN packets in drbl-doit.

* Thu Aug 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-11
- update language files.
- default to turn off -hn0 in dcs. 

* Thu Aug 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-10
- update language files.

* Thu Aug 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-9
- correct some typos in language files.

* Thu Aug 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-8
- add message for ntfs-3g or nfsmount is necessary when -hn0/-hn1 is on in dcs.
- update language files.

* Wed Aug 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-7
- create directory $POST_RUN_DIR in drbl-ocs instead of drblsrv.

* Wed Aug 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-6
- update RELEASE-NOTES. 

* Wed Aug 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-5
- update RELEASE-NOTES and Known_issues.txt.

* Wed Aug 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-4
- add "-o" in dcs for clonezilla.
- default to turn off -j in dcs when using clonezilla restoring.
- create the dir for clonezilla post run when clone finishes in drblsrv.
- new upstream syslinux-3.20-pre19.
- do not remove the kernel deb in /var/cache/apt/archives since our search result is unique enough in drblsrv (for Debian based).
- add drbl-bug-report so it's easier to get info to debug.
- use etherwake (if it exists and run by root) for the higher priority than wakeonlan.

* Sun Aug 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-3
- add drbl-chntpw as the necessary package for DRBL.

* Sat Aug 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-2
- default to turn on -j in dcs when using clonezilla restoring.

* Sat Aug 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.2-1
- add gpgkey in drbl*.repo.
- use drbl_yum_repo_list in drbl.conf and drblsrv.
- update language files.
- new upstream syslinux-3.20-pre11.

* Tue Jul 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-18
- fixed the typos in language files.

* Tue Jul 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-17
- suppress some error messages in mkswapfile for read-only filesystem.
- dcs only update the DRBL SSI image when DRBL SSI mode is on

* Sun Jul 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-16
- add file start-srv-after-ifup to be called by waitnfs.sh.

* Sun Jul 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-15
- update RELEASE-NOTES.

* Sun Jul 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-14
- new upstream syslinux-3.20-pre10.

* Sat Jul 15 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-13
- update language files for clonezilla.
- add -j in dcs for clonezilla.

* Thu Jul 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-12
- echo line feed when mounting nfs in waitnfs.sh.
- add initscripts as a necessary package in Debian/Ubuntu, just in case.

* Wed Jul 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-11
- fix the bug that mountnfs.sh is not run before waitnfs.sh in dapper.

* Wed Jul 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-10
- remove lzop when uninstalling.
- use language file for balcklist of yum repository.
- stop clonezilla when uninstalling.
- fix the bug that mountnfs.sh is not run before waitnfs.sh

* Sat Jul 01 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-9
- fix the wrong version in changelog.

* Thu Jun 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-8
- the mount point for restricted modules should be created in server, not in client.

* Thu Jun 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-7
- add bin/get-rpm-list-from-yum
- create the mount point for restricted modules in dapper.

* Wed Jun 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-6
- add yum_repo_blacklists to avoid some uncompatible yum repository.

* Tue Jun 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-5
- update language files and prompts.

* Tue Jun 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-4
- bugs fixed: fails to get kernel for clients based on get_inst_rpm.

* Mon Jun 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-3
- when put file into user's home in drbl-fuu, chown only change mode for target files.

* Mon Jun 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-2
- update language files.

* Mon Jun 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.7.1-1
- Use lftp for http/ftp instead of lynx in list_available_rpm and list_latest_rpm, since (1). For some apache2, "lynx -dump" will get the html format instead of plain text (2). lynx does not respect environment variables http_proxy and ftp_proxy.
- list_latest_rpm now is based on list_available_rpm.
- use curl to get the baseurl from mirrorlist in find-url-in-yum-set since it respects environment variables http_proxy and ftp_proxy.
- mostly use get_inst_rpm instead of rpm -Uvh ...

* Tue Jun 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-25
- use yellow for warning/prompt, red for fail in drblpush.
- drbl-collect-mac now uses language files info.

* Tue Jun 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-24
- split -y option to -y0 and -y1 so that the default PXE menu can be assigned in dcs.

* Mon Jun 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-23
- update prompt to show the collected MAC files are located in /etc/drbl.

* Mon Jun 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-22
- install lzop also.
- import pub GPG keys for Mandrake/Mandriva.
- use "--auto --force" for urpmi.

* Mon Jun 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-21
- bug fixed: when drbl-ssi is off, we should ask clonezilla box mode also in dcs.
- let image and device name can be inputted again in dcs.

* Sat Jun 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-20
- now dcs can read ~/.dcsrc for pre-setting value, and an example is put in /opt/drbl/conf/dcsrc.
- make -x and -g auto on when start clonezilla in dcs.

* Sat Jun 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-19
- update the language file for -u and -y under clonezilla in dcs.
- -y now can work with multicast in dcs.

* Thu Jun 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-18
- bug fixed: in Mandrake 9.2, nfs daemon counts "NFSDCOUNT" can not be found in drbl-nfs-exports.

* Thu Jun 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-17
- update echos to avoid confision in mknic-nbi.

* Thu Jun 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-16
- update some variables and echos to avoid confision in mknic-nbi.

* Thu Jun 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-15
- install lvm2 if it's found in repository

* Tue Jun 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-14
- now the advanced parameters and compression parameters will be shown directly to user without asking if want to skip or not in dcs.
- default to use ntfsclone when saving image in dcs.
- when ntfsclone is chosen, and lzop is available, -z3 is the default in dcs.

* Mon Jun 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-13
- show "-r" option for clonezilla in dcs.

* Sun Jun 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-12
- new upstream syslinux 3.20-pre9.

* Sat Jun 03 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-11
- For Fedora Core 5 with x86_64 arch, all kernels have SMP support, even though the name will not contain smp.

* Fri Jun 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-10
- bug fixed: -a is missed in dcs/clonezilla-start/save

* Thu Jun 01 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-9
- copy all /lib/security/* to client, no matter client's /lib/security dir exists or not, otherwise maybe client won't able to login.

* Wed May 31 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-8
- add -a, -nogui, and -v for clonezilla advanced parameters in dcs.
- bug fixed: when restoring partitions, client partitions are wrongly parsed in dcs.

* Mon May 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-7
- add description how to reconfigure X (firstboot) in debian.
- update dcs and language files for ntfsclone and lzo options.
- install drbl-ntfsprogs.

* Thu May 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-6
- if no local file system is mounted, then do not run umount -r -d in Dapper /etc/init.d/umountfs.

* Thu May 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-5
- update some echo messages and package description.
- turn on bootmisc.sh in Debian for client rcS.d so that runlevel can get the init level by reading /var/run/utmp, and to avoid /etc/nologin to be created by set DELAYLOGIN=no in client's /etc/default/rcS.
- turn on service linux-restricted-modules-common in client in Ubuntu.

* Wed May 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-4
- use "beginner, medium and expert" instead of "low, medium and high" in firstboot of Debian.

* Wed May 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-3
- xorg.conf md5sum should be created in /var/lib/x11/xorg.conf.md5sum, not /var/lib/xfree86 in Dapper.
- rewrite firstboot for Debian 3.0, 3.1, Testing/Unstable, and now it will ask the questions level before reconfiguration.

* Wed May 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-2
- a workaround for SMP kernel selection in Ubuntu Dapper.

* Wed May 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.6-1
- ready for Dapper, alpha release.
- make client can use i486 kernel in Dapper, although the kernel image linux-image-2.6.15-23-386_2.6.15-23.39_i386.deb (Dapper beta) -> the name implies 386, but actually it's 486.

* Tue May 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-6
- in OpenSuSE 10.1, xfs need account nobody, which only exists in YP, so we have to make xfs runs after ypbind.
- Do not umount -t tmpfs when rebooting in SuSE.

* Mon May 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-5
- network service in OpenSuSE 10.1 is added, so it will be easier to config 2nd network interface card in client.

* Mon May 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-4
- bug fixed: the repository URL is wrong in opensuse10.0.
- New way to find a sutiable kernel (both in update and release) in SuSE.

* Mon May 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-3
- bug fixed: /dev/console and /dev/null are not created in OpenSuSE 10.1.
- bug fixed: haldaemon (which needs some *.so in /opt/, /usr) is started before nfs.
- add touching /var/lib/nfs/state for client.

* Sun May 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-2
- remove umount /sys fail message is shown when reboot or shutdown.
- bug fix: unable to login console in client in OpenSuSE 10.1.

* Thu May 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.5-1
- ready for OpenSuSE 10.1, alpha release.
- add powersaved in the client checklist in drblpush for OpenSuSE 10.1.

* Wed May 17 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-6
- update language files.

* Tue May 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-5
- show the OS url to debug when kernel is not available in drblsrv.
- update the language files.

* Tue May 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-4
- Terminate drblsrv if no kernel is available, show some messages also.

* Tue May 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-3
- new upstream syslinux 3.20-pre8.
- fix the bug that kdebase3-kdm is not listed to find KDM_CFG in SuSE.
- suppress the warnings about socket files in /var/ in gen_ssi_files.
- make $drbl_common_root/drbl_ssi/template_*.tgz can read by root only, better security.
- bug fixed: unsable to find the right path for CentOS mirrorlist in find-url-in-yum-set.
- bug fixed: unable to get yum repository URL and path for find-url-in-yum-set in FC5.

* Mon May 8 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-2
- update the language files.
- update release notes and other docs.
- if multicast, ask the time_to_wait, clients_to_wait in dcs.
- rewrite code to use funtions do_clonezilla_save_dev and do_clonezilla_restore_dev in dcs.

* Mon May 8 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.4-1
- update AUTHORS, Changelog.
- remove save & restore hda1 menu in dcs.
- add function countdown.
- add "-p true" in dcs.

* Mon May 8 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-21
- bug fixed, $KDE_CFG now can be found correctly in OpenSuSE 10.0.

* Sun May 7 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-20
- copy $etherboot_pxe to /tftpboot/nbi_img, too.
- put deprecated message in dcs for clonezilla save/restore hda1, we will remove save & restore hda1 menu in the future release.

* Mon May 1 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-19
- bug fixed: dynamically get DHCPDLEASE_DIR, since it changed from FC5.

* Mon May 1 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-18
- update comment in init.drbl
- comment the /dev/fd0 in client's /etc/fstab, let user to handle that if it is necessary. If it's not commented, it will cause problem in newer GNU/Linux.

* Fri Apr 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-17
- use better method to get kernel image name in debian

* Thu Apr 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-16
- update netinstall description in dcs.
- bug fixed: unable to clean normal user account in common root. 

* Wed Apr 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-15
- KARCH_LIST will be nothing if we can not find the kernel config file, so we choose to use the same arch of server for client in Debian.

* Mon Apr 17 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-14
- start arm-wol when client boots, not before it poweroffs.
- add installation for package etherwake/ether-wake.

* Thu Apr 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-13
- fix the bug for unable to put the auto/timed login account in gdm custom.conf.

* Thu Apr 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-12
- use a better method to decide the kernel name is debian.
- make KDM_CFG search better.

* Wed Apr 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-11
- minor bug fixed: In SSI mode, some of the client IP addresses won't be shown in the hosts.deny warning message.

* Wed Apr 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-10
- minor bug fixed.

* Tue Apr 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-9
- fix the bug for unable to clean fedora-core.repo when uninstalling.

* Tue Apr 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-8
- add suggestion to defrag NTFS filesystem in language files for clonezilla.

* Tue Apr 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-7
- Ready for Ubuntu Breezy amd64

* Mon Apr 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-6
- /mnt for client now is tmpfs, which will allow Mandriva to mount cdrom automatically.

* Sat Apr 8 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-5
- fix the bug for undefining the $FC_CORE_REPO
- make drblsrv work with CentOS new mirrorlist method.

* Fri Apr 7 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-4
- create console and null only if /dev/{console,null} not exists

* Fri Apr 7 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-3
- update RELEASE.
- add -nu option for mknic-nbi to exclude the USB keyboard related modules.

* Fri Apr 7 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-2
- do not run post in drbl.spec, modify preun.

* Fri Apr 7 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.3-1
- do not use create_authconfig_env, modify client's /etc/nsswitch.conf directory in RH/FC.
- ready for fedora core 5.

* Wed Mar 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-14
- make terminal mode unaviaiable in dcs when in clonezilla box mode.

* Tue Mar 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-13
- fix the bug that arm-wol is not on when running drblpush.

* Tue Mar 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-12
- stop the nfs and yp services then remove the setting when uninstalling.

* Tue Mar 28 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-11
- add ethtool in the pacakge list to be installed.
- modify the method to filter CPU arch since only k7-smp and i686-smp exist in Debian.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-10
- add arm-wol to let client arm Wake on LAN before it poweroffs.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-9
- do not using option "--drbl-ssi" of drbl-nfs-exports in drblpush, since it's no more in drbl-nfs-exports. 

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-8
- use FULL_OS_Version="Debian Testing-Unstable" for Debian Etch.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-7
- exclude tmpfs|none when rebooting in etch.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-6
- fix the bug that /var/lib/rpm instead of /var/lib/rpm is monted in debian when rpm is installed.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-5
- polish codes in drblpush.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-4
- modify /etc/X11/gdm/factory-gdm.conf only if it exists.
- polish codes in drblpush.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-3
- fix a bug where no path for umountfs for Etch in drblpush.

* Mon Mar 27 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-2
- add drbl-etc-hosts in drbl-3n-conf to update client's /etc/hosts.
- make init.drbl work with udev in Etch where no udevstart exists.
- drblsrv and drblpush work in Debian Etch.

* Sun Mar 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.2-1
- add openssl-perl arch check and install for CentOS 4.3
- initial release for CentOS 4.3

* Sun Mar 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-10
- use drbl-etc-hosts to create /etc/hosts.

* Sat Mar 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-9
- fix some typos in language files.

* Sat Mar 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-8
- do not restart YP before drbl-all-service restart in drblpush.

* Fri Mar 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-7
- do not export /tftpboot/nodes/$IP if it does not exist (drbl-nfs-exports).
- fix the bug for unable to get drbl_ssi_mode in drbl-nfs-exports.

* Fri Mar 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-6
- rm /var/lib/nfs/rmtab to avoid a long time try when restart NFS
- set the NFS daemon number setting in drbl-nfs-exports
- move code about NFSD_RATIO to drbl-nfs-exports
- add bin/get-necessary-nfsd-no

* Fri Mar 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-5
- remove -i in halt* to avoid network down. Need this for Wake on LAN before shutdown.
- fix the bug for showing prompt to run drbl-ocs again.
- add wake on LAN prompt.
- make drbl-3n-conf only work in drbl SSI mode.

* Thu Mar 23 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-4
- fix the bug that IP fixed to eth0, eth0:1 for drbl-yp-securenets
- do not remove fastboot when client boots.
- add # Modified by DRBL in some modified scripts.
- rewrite some codes and file arch: use files/{RH,FC,MDK,MDV,DBN...}/ directory arch.
- add drbl-3n-conf in dcs.

* Wed Mar 22 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-3
- Generate the ssh hostkey for the template so that client won't have to generate in DRBL SSI mode.
- fix the bug for unable to set swap file size in client.

* Tue Mar 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-2
- update with syslinux 3.20-pre7
- use drbl-nfs-exports instead of code in drblpush to create /etc/exports in server

* Mon Mar 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.1-1
- make some management scripts in sbin work with DRBL SSI by using /opt/drbl/bin/get-client-ip-list instead of "for i in $drblroot/*"
- drbl_ssi_client_prepare will prepare the autologin/timedlogin ID in gdm/kdm config.
- rename drbl-user-env-switch as drbl-user-env-reset
- drbl-user-env-reset replace autologin-home-reset-from-server
- add --no-gen-ssi when run some scrtips.
- now we can choose DRBL SSI in drblpush.

* Wed Mar 15 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-16
- add option to turn on/off clonezill_box_mode in /etc/drbl/drbl_deploy.conf
- add -f for cp -a in copy_rc1d_for_drbl_ssi and remove_rc1d_for_drbl_ssi

* Tue Mar 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-15
- modify boot.rootfsck, we comment "mount -f /" to avoid / be mounted twice in SuSE.

* Tue Mar 14 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-14
- add drbl-ssi in dcs.

* Mon Mar 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-13
- create an empty dir /etc/X11 when in clonezill box so that kudzu will not complain about no /etc/X11 to write X config.

* Mon Mar 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-12
- use yellow instead of red for single in init.drbl.
- comment "mount -f /" in rc.sysinit of clients for RH-like.

* Mon Mar 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-11
- Put a tag for FC3 or newer so that rc.sysinit will know it's a readonly root. Put an empty file so rc.sysinit won't complain ($drblroot/$ip/etc/rc.readonly)

* Sun Mar 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-10
- bug fixed, when drbl deb is created, not by alien, we can put dependances. therefore the tftp is installed with default on /etc/inetd.conf, not standalone daemon. We have to turn off it in client, use perl, not update-inetd.
- bug fixed for get-client-ip-list, now the IP in range should be got correctly.
- add an option to exclude xorg.conf/XF86Config/XF86Config-4 in gen_ssi_files
- add more options for turn-drbl-ssi-mode 
- Comment nfs / in fstab of clients, it's not necessary, otherwise it will mount twice.
- since in busybox 1st stage, client will mount /tftpboot/node_root, not /tftpboot/$ip, so "ln -fs $drbl_common_root /tftpboot/$ip" is not necessary.

* Fri Mar 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-9
- fix the bug that when in English, dcs fails.

* Fri Mar 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-8
- bugs fixed: (1) unable to set client's root passwd (2) /tftpboot/nodes/$IP is not exported when in normal mode.

* Fri Mar 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-7
- add a mechanism to check if class A/B is used, if so, set warning if multicast clonezilla used.

* Thu Mar 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-6
- bug fixed: total_client_no_for_checking is not assigned.

* Wed Mar 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-5
- add ssh public key for client root so that we can run drbl-doit.
- refine drbl_ssi_client_prepare.

* Wed Mar 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-4
- polish drbl4imp.
- let /opt/drbl created from tarball when in clonezilla box.
- exclude some graphic applications settting in /etc when in DRBL SSI mode.

* Tue Mar 07 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-3
- make system upgrade option default is "NO".
- turn off ntp when client is in clonezilla box mode.
- If hostname is found in /etc/hosts, use that in DRBL SSI client.
- add option "-z|--clonezilla_box" in drbl4imp, so now "drbl4imp -z y -p 50" will create a clonezilla box server serving 50 clonezilla clients..

* Mon Mar 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-2
- update langauge file.
- export /var/lib/{rpm,dpkg} and /var/spool/mail when it's DRBL SSI, but when client is in clonezilla box and rc1.d, client won't mount them.
- mv "-g auto" ealier in dcs.

* Mon Mar 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.6.0-1
- fix the bug that when run drbl-all-service restart, drbl-clients-nat does not restart in debian-based dists.
- mv copy_rc1d_for_drbl_ssi & remove_rc1d_for_drbl_ssi from ocs-functions to drbl-functions.
- add "-p" option for gen_ssi_files.
- add clonezilla box mode.
- drbl-doit now get IP list from dhcpd.conf instead of /tftpboot/nodes/*.

* Sat Mar 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.8-5
- improve init.drbl and use drbl_ssi_client_prepare, make it modify client hostname and yp server dynamically.

* Fri Mar 03 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.8-4
- For debina based, back convert x86-64 to x86_64 for menu parse, since alien convert x86_64 to x86-64 in generate-pxe-menu.
- fix the bug for gen_ssi_files.

* Thu Mar 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.8-3
- update the know issue doc.

* Thu Mar 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.8-2
- add $sis900_zpxe, since all-in-one pxe image sometimes does not work for sis900 NIC.

* Thu Mar 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.8-1
- add a workround for sis900, thanks to Alexander Heinz for providing this solution in syslinux mailing list.
- add necessary package file.
- add drbl single system image SSI files (Not ready yet).

* Sat Feb 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-8
- use better way to detect if partimage-server is installed.

* Sat Feb 25 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-7
- Alien does not make obsoletes in RPM spec to deb. Now remove obsolete packages when install packages for debian. Especially partimage-server in B2D. Since partimaged is in DRBL partimage.

* Fri Feb 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-6
- put Obsoletes partimage-server in partimage instead of drbl. 

* Fri Feb 24 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-5
- refine drbl-doit.
- put partimage-server in Obsoletes.

* Sun Feb 19 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-4
- not so verbose when adding user to device group in Debian.
- add language support for drbl-login-switch.
- add language option for gen_client_files.sh.

* Sat Feb 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-3
- add an option to set the pause time (secs) after network card is up. This is specially for some switch which need extra time to link, check https://sourceforge.net/forum/message.php?msg_id=3583499 for more details.

* Sat Feb 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-2
- refine drbl-login-switch.
- fix the bug that when random password is chosen, the /etc/drbl/auto_login_id_passwd.txt is not created.

* Sat Feb 18 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.7-1
- client IP will skip the one server using.
- AUTO_LOGIN_ID_PASSWD file is in /etc/drbl/auto_login_id_passwd.txt, no more in working directory when run drblpush or drbl-login-switch.
- if password_opt is assigned, drbl-login-switch will force to set the password for client.
- fix a bug when no client-IP-group-* or client-MAC-group-* exists, dcs still shows client-IP-group-* or client-MAC-group-*.
- add acpid and acpi-support for clients for Ubuntu.

* Sun Feb 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-29
- /tftpboot/nodes/$IP/node_root/dev/{console,null} are character special files, force to remove it before creating them in the clients.

* Sun Feb 12 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-28
- remove mode "remote-linux", only remote-linux-gra and remote-linux-txt left in dcs. Force to write the right /etc/inittab of clients when switching to remote-linux-gra or remote-linux-txt.

* Sat Feb 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-27
- change the hdparm from S42 to S60 (which is far after S41force-load-ide so we can access IDE device after IDE-related modules are loaded and ready).

* Fri Feb 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-26
- fix a bug, remove an extra ) in init.drbl.

* Fri Feb 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-25
- fix the bug for unable to get the IP address when there is alias IP address in init.drbl.

* Mon Feb 06 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-24
- update some prompts in init.drbl.

* Sun Feb 05 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-23
- add echo for mounting /etc /var /usr in init.drbl.

* Sat Feb 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-22
-  mknod console and null in common root dev directory, so now in Debian no more "Warning: unable to open an initial console."

* Thu Feb 02 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-21
- update init.drbl so that when booting, some service will not complain /initrd is busy (/initrd/proc and /initrd must be umount in order).

* Wed Feb 01 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-20
- fix the parameter HOST_MAC_TABLE bug.
- move select_hosts from /opt/drbl/bin to /opt/drbl/sbin
- add client group support, now we just have to put files like /etc/drbl/client-{MAC,IP}-group-{1-9} (listed line by line) then we can select in dcs.
- fix a bug that Mandriva 2006.0 OS_Version is parsed wrong.

* Tue Jan 31 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-19
- default is not to restart NFS in dcs.

* Tue Jan 31 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-18
- update language file.

* Mon Jan 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-17
- change the hdparm from S07 to S42 (which is after S41force-load-ide so we can access IDE device after IDE-related modules are loaded) for Debian.

* Mon Jan 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-16
- Create a dummy NIC conf file so that hotplug won't complain no NIC config in Debian.

* Mon Jan 30 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-15
- use new program tune-debian-dev-group-perm instead of tune-debian-audio-plugdev-perm.

* Sun Jan 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-14
- gdmgreeter maybe in /usr/bin/gdmgreeter (sarge) or /usr/lib/gdm/gdmgreeter (breezy)

* Sun Jan 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-13
- create an empty network/interfaces for client so that hotplug won't complain that in Debian or Ubuntu.

* Sun Jan 29 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-12
- add file get_mac so that we can get the NIC MAC address.

* Thu Jan 26 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-11
- add .x86_64 for those packages in opensuse 10.0 x86_64 version.

* Sat Jan 21 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-10
- add "reiserfs" extra option for fedora netinstall.

* Fri Jan 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-9
- polish drbl-doit.

* Fri Jan 20 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-8
- update syslinux 3.20-pre6.
- we should use "wakeonlan -i $IP $MAC" to send WOL message so that any client in any ethernet port will be waked.
- update with wakeonlan version 0.41 from Jose Pedro Oliveira <jpo at di.uminho.pt>.

* Mon Jan 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-7
- reset OS variables in drbl-functions.

* Mon Jan 16 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-6
- make pxelinux menu show Ubuntu if it's Ubuntu.

* Fri Jan 13 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-5
- fix the bugs that dhcp3-server and tftpd-hpa is not on after reboot the Debian server.

* Wed Jan 11 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-4
- update dcs with new netinstall format.

* Tue Jan 10 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-3
- add fedora legacy repository in apt repository example.
- use another method the get RH VER in check_distribution_name of drbl-functions to avoid the segmentation fault in RH9.

* Mon Jan 09 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-2
- update syslinux 3.20-pre4.
- fix a bug for unable to tell CentOS 4.0/4.1/4.2 in drbl-functions.
- use $FULL_OS_Version instead of short name (OS_Version).

* Sun Jan 08 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.6-1
- fit the new netinstall package name "netinstall-$dist-$ver-$arch" in generate-pxe-menu and drblsrv.
- use a better method to get OS_Version in check_distribution_name of drbl-functions.

* Sat Jan 07 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.5-33
- force to create DRBL B2D client's /media, but for other distributions, we will
test it before create it.

* Sat Jan 07 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.5-32
- rc.boot should be in $ihost/etc/rc.boot/ in tune-debian-audio-plugdev-perm
- B2D pureGnome 20051212 does not have hotplug* in rcS.d, but pureKDE has. Anyway, for to link them in rcS.d.
- since B2D does not have /media, but it will create and use that once you plug the usb devices, so now we decide to mkdir media for client anyway.

* Wed Jan 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.5-31
- correct typo in drbl-client-switch
- move total_nfsd calculation into drbl_server_parse in drblpush so that -c will work.

* Wed Jan 04 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.5-30
- minor bug fixed in check_switch_on_off() of drbl-functions. 

* Tue Jan 03 2006 Steven Shiau <steven _at_ clonezilla org> 1.5.5-29
- fix the typo in comments "drbl-testin" -> "drbl-testing"
- autologin account's group and home directory is queried from system in autologin-home-reset.
- add a function in dcs: reset-autologin-account

* Mon Dec 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-28
- Typo issue!!! NFS daemon number in RH-like shoule be RPCNFSDCOUNT instead of RPPPCNFSDCOUNT For Mandrake 9.2-10.1, we should use NFSDCOUNT.

* Fri Dec 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-27
- modify tune-debian-audio-plugdev-perm:
- check if pmount and pumount exits before chgrp
- deal with dev tarball /dev/mixer* /dev/dsp*

* Thu Dec 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-26
- In Debian, drbl-nat-rules should start in runlevel 2 3 4 5 to let B2D work.

* Wed Dec 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-25
- chgrp /usr/bin/pumount in tune-debian-audio-plugdev-perm, thanks to Cass Evert.

* Sun Dec 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-24
- typo fixed in language file bash/en.

* Sun Dec 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-23
- update language files. 

* Sun Dec 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-22
- do not prompt restart message after tune-debian-audio-plugdev-perm if drbl clients exist.
- update language files. 

* Sun Dec 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-21
- use tune-debian-audio-plugdev-perm in drblpush.

* Sun Dec 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-20
- add /opt/drbl/sbin/tune-debian-audio-plugdev-perm so that it's easier to open plugdev and audio to all users in the DRBL Debian client.

* Sat Dec 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-19
- update the comments for kernel 2.6.13-15-default issue.

* Sat Dec 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-18
- add bugzilla prompt for kernel 2.6.13-15-default issue.

* Sat Dec 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-17
- Force to stop drblsrv if SuSE/OpenSuSE 10.0 is running with kernel 2.6.13-15-default, since it is BUGGY! 

* Sat Dec 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-16
- add warning about SuSE/OpenSuSE 10.0 with kernel 2.6.13-15-default is BUGGY 

* Thu Dec 8 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-15
- update language files for ocs-onthefly.

* Sat Dec 3 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-14
- update language files for ocs-onthefly.

* Thu Nov 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-13
- check if kernel 2.6 is running in sarge.
- add nc or netcat package as a necessary package for ocs-onthefly.

* Fri Nov 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-12
- fixed some comment typos.

* Wed Nov 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-11
- add lynx installation first in Mandriva.
- move lynx and lftp in SuSE ealier.
- add lftp installation with lynx for all RPM distributions.

* Sun Nov 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-10
- fix typos in drblpush.
- add necessary packages coreutils gzip bzip2 since we now use cat/zcat/bzcat in clonezilla.

* Sat Nov 05 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-9
- add PATH=$PATH:/sbin/:/usr/sbin before running route -n.

* Sat Nov 05 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-8
- add /sbin:/usr/sbin in the PATH in bin/get-nic-devs and bin/get_network.

* Wed Nov 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-7
- fix the bug that unable to change client's root passwd in server in SuSE.
- tune the boot.idedma/force-load-ide/parse-load-mod-suse for SuSE.
- client won't run ld.config (turn off /etc/init.d/boot.ldconfig and comment the ld.config in /etc/init.d/nfs).

* Mon Oct 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-6
- update some PAM necessary lib in create_chpasswd_env in drbl-functions.

* Mon Oct 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-5
- add mkinitrd-net removal in Debian.

* Sun Oct 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-4
- add yast2 -i yum and copy drbl*.repo/opensuse.repo to /etc/yum.repos.d/
- fix a bug that only i586 glibc will be installed.

* Sun Oct 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-3
- finished parsing yum repository then force to install kernel or i586 packages (glibc...)

* Sat Oct 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-2
- remove powersaved in SuSE DRBL client, let user add that by themselves.
- for SuSEs, in nfs of client, we have to recreate ld.so.cache since /etc/init.d/boot.ldconfig is run before nfs. It won't include some remote NFS directory (like /opt/kde/lib... /opt/gnome/lib...

* Sat Oct 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.5-1
- update the MENU LABEL for OpenSuSE, we should use sed -e before SuSE in generate-pxe-menu.
- use "uname -m" to set x86_64/amd64/i386 for all the distributions.
- add ssh can be accessed in SuSE firewall.
- hwscan only exists in SuSE 9.3, in 10.0 or later it's gone! Let hwscan only run in SuSE 9.3 client.
- use mkpxeinitrd-net instead of mkinitrd-net now.
- Let OpenSuSE 10.0 can use yum (not finished!)

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-21
- update dev.DBN3.1.tgz with B2D 200510 version.
- add opensuse network installation.

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-20
- comment "umount -a" in /etc/init.d/{reboot,halt} for B2D.

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-19
- add notmpfs in perl script (process /etc/init.d/halt of B2D).

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-18
- fix the bug for put the wrong perl script (process /etc/init.d/halt of B2D) in SuSE block.

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-17
- add /etc/sysconfig/i18 reading if it's B2D.
- exclude umounting tmpfs in /etc/init.d/umountfs of clients.
- add a perl script to process /etc/init.d/halt of B2D.

* Thu Oct 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-16
- rm client-extra-service in the Makefile, do not put it in /etc/sysconfig/
- create a template /etc/drbl/client-extra-service if it not found in drblpush.

* Wed Oct 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-15
- fix the bug that we use wrong variable for querying installed_openssl

* Wed Oct 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-14
- update the language files.
- support -y of drbl-ocs in dcs.

* Tue Oct 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-13
- tune the halt script for CentOS 4/4.1/4.2.

* Mon Oct 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-12
- fix the loss of rc.sysinit.CO4.2.drbl and halt.CO4.2.drbl.

* Thu Oct 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-11
- Mandriva 2006 support.
- fix the bug for unable to copy rc.sysinit.MDVXXX.drbl to clients in drblpush.

* Tue Oct 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-10
- add mandriva network installation.

* Tue Oct 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-9
- fix the bug: put wrong search pattern for ethernet port for WAN connection in drblpush.

* Tue Oct 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-8
- use route -n to get the ethernet port for WAN connection in drblpush.

* Tue Oct 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-7
- fix another bug of drbl4imp which unable to get the locale.

* Mon Oct 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-6
- fix the bug of drbl4imp which unable to get the locale.

* Mon Oct 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-5
- set Flags: seen in all output in sbin/deb-preconf-drbl

* Mon Oct 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-4
- add --force-yes for apt-get install when it's Ubuntu.
- update some data for sbin/deb-preconf-drbl, use egrep instead of fgrep.

* Mon Oct 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-3
- Support Debian testing/unstable, especially Ubuntu 5.10 (Breezy).

* Sat Oct 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-2
- update mknic-nbi with parameter -m|--modules to work with mkinitrd-net 1.15-8drbl.

* Fri Oct 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.4-1
- use drbl-core/pre-drbl as 3rd apt repository so that we can separate that with OS in RH/FC apt repository (Which only used in RH 8.0/9, FC 1/2).

* Fri Oct 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-41
- use only one name drbl-testing instead of drbl-test/drbl-testing.
- remove function setup_MDK_apt
- add support for CentOS 4.2

* Thu Oct 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-40
- use install_lynx_via_${installer}_if_necessary for yum/apt so that in FC1/RH it will be ok.

* Wed Oct 12 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-39
- show the whole command when run drbl-ocs so that it's easier to copy that for later use.

* Tue Oct 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-38
- use diffrent variables rc_install_kernel & rc_get_kernel when downloading and installing kernel.
- update the usage info of mknbi-nic.

* Tue Oct 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-37
- fix a variable typo.

* Tue Oct 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-36
- Use rpm -ql centos-release | grep "RPM-GPG-KEY-centos4" to get the key since CO4/4.1 use the same PATH /usr/share/doc/centos-release-4/

* Mon Oct 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-35
- use umount -l /initrd in init.drbl to ignore the busy warning.

* Mon Oct 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-34
- Suport CentOS 4.1.
- We should check CentOS-Base.repo not CentOS-Base for yum in CentOS

* Fri Oct 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-33
- add option for -z0/-z1/-z2 in dcs.

* Fri Oct 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-32
- now back to the exact size of swapfile, do not use the size difference since we can use stat to get the right file size.

* Fri Oct 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-31
- add an option -n|--netdev in mknbi-nic so it can assign the priority of network card in client to request IP address when client booting in pxelinux.

* Wed Oct 05 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-30
- make get-nic-devs accept other name not only ethx for /proc/net/dev

* Tue Oct 04 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-29
- Show warning if user use drbl-cp-host to copy files into those directories not /etc, /var, /root.
- if existing swap file size difference is < 5%, we will accept that.
- update with syslinux 3.10-pre3, which fixed the pxelinux menu.c32 password bug.
- do *NOT* specify the salt for pxelinux SHA1 password, let the program pick a random one.
- make the network device name more general in dhcpd port file.

* Sun Oct 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-28
- DRBL client can be only NIS client, NIS slave is not necessary.
- we should create /var/lib/xfree86/xorg.conf.md5sum instead of /var/lib/xfree86/XF86Config-4.md5sum in Ubuntu Hoary.

* Sun Oct 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-27
- use new version memtest86+ 1.65.

* Thu Sep 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-26
- fix the bug for unable to append the modules list in parse-load-mod-suse.

* Wed Sep 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-25
- try to use the hwdata to load more modules in SuSE, like scsi devices.

* Tue Sep 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-24
- delete an extra ;; in drblpush.

* Mon Sep 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-23
- create a CLEAN rc.boot/boot.local/rc.local to avoid some commands copied from server (add for Debian/SuSE).

* Mon Sep 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-22
- add services hwscan parse-load-mod-suse force-load-ide in boot.d so that we can load some modules for chips and IDE storage deevices.

* Sun Sep 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-21
- We need "grep -o", and the grep in woody does not have that option, so use the one from backports.
- Note, now we need to use the backports in /etc/apt/sources.list, check /opt/drbl/doc/install_notes_Debian.txt for more details.

* Sat Sep 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-20
- fix a bug for unable to clean unnecessary files in /tftpboot/nbi_img when uninstalling drbl.

* Sat Sep 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-19
- add a parameter "-e" for clonezilla in dcs

* Wed Sep 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-18
- remove extra command "break" in drblsrv.
- fix the bug for unable to get network/netmask in SuSE.

* Tue Sep 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-17
- add a function to set pxelinux password in drblpush.
- fix the bug, we should put the dhcpd.conf file, not only path in bin/parse_dhcpd.conf

* Tue Sep 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-16
- add woody-netinstall in Obsoletes in drbl.spec.

* Tue Sep 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-15
- add libdigest-sha1-perl as a necessary package in Debian in drblsrv.
- make symbolic links in sbin/{drblsrv,drblpush} from setup/{drblsrv,drblpush}.

* Mon Sep 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-14
- bin/get_ip and bin/drbl-doit use $PATH instead of /sbin/ifconfig.
- use /opt/drbl/bin/get_ip to get the ipaddress instead of /opt/drbl/bin/parse_net_conf

* Sat Sep 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-13
- perl -pi -e 's|^#!/bin/sh|#!/bin/bash|' *
- excluding multicast mode when -u for clonezilla is chosen in dcs.
- make multicast as the default mode in dcs.

* Wed Sep 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-12
- now we can assign the ethernet port connected to WAN, not fixed to eth0 any more.

* Sat Sep 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-11
- fix a bug that we forgot to exclude umounting /sys when rebooting/halting in FC2/3/4.

* Fri Sep 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-10
- create md5sum for XF86Config-4 in firstboot in Debian, otherwise dpkg-reconfigure won't update the modified XF86Config-4.
- we need mount -n /dev/pts in /etc/rc.sysinit of client, so that we won't have an error "No more PTYs" (This make "none /dev/pts                devpts  gid=5,mode=620  0 0" works in /etc/fstab.

* Tue Sep 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-9
- just remove files under /tftpboot/nbi_img, not directory under that.

* Tue Sep 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-8
- do not just remove /tftpboot/* when uninstalling, we will skip some files which might be installed by RPM packages, like *netinstall* and etherboot

* Tue Sep 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-7
- make Debian 3.1 (dev.DBN3.1.tgz) (especially B2D) /dev/dsp* and /dev/mixer* mode: 666. For udev, we do NOT touch that.
- update drbl-client-switch so that it can use "-t" and "-k" in drbl-ocs.

* Fri Sep 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-6
- remove "set -e" setting sbin/gen_client_files.sh to avoid the error in FC4.

* Thu Sep 01 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-5
- add option -c and -r in mknbi-nic.

* Tue Aug 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-4
- fix a bug for copying some extra files in client's /var/lib... those are not necessary.

* Tue Aug 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-3
- fix a bug when output nisdomain to client's config file.

* Tue Aug 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-2
- fix a bug when there is no old clients files, the parameters input to gen_client_files.sh is wrong parsed.

* Tue Aug 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.3-1
- use sbin/gen_client_files.sh to create client's files in drblpush.
- update syslinux with 3.11-pre10

* Mon Aug 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.2-3
- forgot to put the VERSION in /opt/drbl/pkg/memtest86+/VERSION, add it now.

* Mon Aug 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.2-2
- add a memtest86+ version tag in /tftpboot/nbi_img.
- update code to make drbl-client-root-passwd work in SuSE.

* Sun Aug 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.2-1
- put memtest86+.bin as part of package "drbl" in drbl/pkg/memtest86+, so no more installing memtest86+ package when running drblsrv -i.
- add the COPYING and README files in drbl/pkg/*.
- update syslinux with 3.11-pre7.
 
* Sun Aug 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-6
- Add RCX_ROOTDIR and RCX_REL_INITD in drbl.conf so that clonezilla can work in SuSE.

* Sun Aug 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-5
- update syslinux with 3.11-pre6
- modify fbasename so that when sed is not in /usr/bin in Mandrake it still works.

* Sat Aug 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-4
- write a perl script gethostip.pl to replace the statically linked gethostip.

* Sat Aug 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-3
- Forgot to switch the new drblsrv files, do it.

* Sat Aug 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-2
- Fixed bugs when querying i586 packages in SuSE.

* Fri Aug 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.1-1
- remove the installation of package ipcalc and syslinux, we just collect the necessary files into this package "drbl".

* Fri Aug 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-6
- lftp should be installed ealier, it's necessary for checking i586 glibc 

* Fri Aug 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-5
- make all programs in /opt/drbl/{sbin,bin} work in SuSE.

* Fri Aug 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-4
- drblsrv will try to install the i586 glibc/db... when i586 arch is selected.
- fix a critical bug in Debian, /var/lib/nfs should exist and nfs-common should be started in clients.

* Mon Aug 22 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-3
- use -y --no-checksig when run "apt dist-upgrade" in SuSE.

* Sun Aug 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-2
- use "apt" instead of "apt-get" in SuSE so that we can use --no-checksig.
- show notes in SuSE when apt4rpm is not installed.

* Sat Aug 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.5.0-1
- Add SuSE supports.
- Add bin/socket.pl so that we do not need "socket" program.
- Move function install_RH_MDK_client_kernel (was install_client_kernel) ealier and will let user to choose which kernel (from release or updates).
- Do not link /proc/mounts to /etc/fstab for clients, and do not remove /etc/mtab in client's /etc/rc.d/rc.sysinit.
- Add /etc/fastboot in clients.

* Fri Jul 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-25
- update conf/drbl.conf

* Fri Jul 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-24
- add some parameters to make mandrake can do graphically installation

* Tue Jul 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-23
- do not remove dialog when uninstalling in Debian.
- check if /etc/environment exists before modify /etc/default/gdm
- check if /usr/sbin/gdmgreeter exists before modify gdm.conf in server.
- add discover in rcS.d for woody.
- copy some rc files (.bashrc, .bash_profile...) to client's root home directory

* Mon Jul 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-22
- if discover1 exists, we should not install discover.

* Mon Jul 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-21
- /etc/init.d/nfs-kernel-server does not read /etc/default/nfs-kernel-server in Woody, so modify the RPCNFSDCOUNT in /etc/init.d/nfs-kernel-server.

* Mon Jul 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-20
- add tftpd in inetd.conf if it's not available in standalone service.
- add inetd service in drbl_server_service_chklist.
- For Debian woody, it seems that /etc/networks is not automaticaly created. If we can not find it, just touch it
- This release should work in Woody.

* Sun Jul 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-19
- bug fixed for halting sarge machine, we should not put umountfs and replace some arguments in client's /etc/init.d/halt.

* Sun Jul 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-18
- bug fixed, we should not terminate drbl-powerful-thin-client when kdmrc is not found, maybe it's gdm.conf.
- update some prompt messages.

* Sun Jul 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-17
- move netinstall after kernel installation for Debian installation.
- add -o|--client_kernel_from for drblsrv for Debian.

* Sat Jul 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-16
- Now there are two options for installing client's kernel, local and apt repository in Debian-based distributions.

* Sat Jul 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-15
- relink some commands in /sbin (originally linked to init) to init.orig.
- remove -i in client's /etc/init.d/halt & /etc/init.d/reboot so it won't stop network before halting or rebooting system.
- This release works in B2DpureKDE20050603.

* Fri Jul 22 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-14
- bug fixed, in sbin/clean-dhcpd-lease add $DHCPDLEASE_DIR for dhcpd lease dir path 
- user dpkg -s instead of dpkg -l so we can get the correct retur code.

* Thu Jul 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-13
- Debian Sarge does not sync the locale setting of gdm with system. Do it for DRBL clients.
- bug fixed for wrong exec file name when stop drbl-clients-nat

* Thu Jul 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-12
- Make drblsrv work in Ubuntu. Ubuntu use the name "linux-image" instead of "kernel-image". Note! In this version, DRBL still does not work well in Ubuntu.
- Since the singature of drbl.deb is not available now, add an option -f|--force-yes for apt.
- Bug fixed in dcs - re-deploy when language en is choosed.
- include /var/lib space in sbin/check_drbl_setup_space.

* Tue Jul 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-11
- mknbi is not necessary, so do not install it.

* Tue Jul 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-10
- The tarball name is named version-release, no more date.
- Since mknbi is separated from mkinitrd-net, we need to install mknbi now.

* Mon Jul 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-9
- fixed a bug in drbl-client-reautologin in RH-like distribution.

* Mon Jul 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-8
- bug fixed, we should create "net.ipv4.ip_forward = 1" in /etc/sysctl.conf if not in /etc/sysctl.conf
- make mkswapfile/drblthincli work in Debian.
- add /usr/sbin/gdm-safe-restart for Debian.
- make 2 levels command available in dcs.
- add woody in generate-pxe-menu.

* Sun Jul 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-7
- add more commands in dcs.

* Sat Jul 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-6
- bug fixed - unable to shutdown/reboot in Debian.
- rewrite some scripts about output dhcp server's arguments.

* Fri Jul 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-5
- Supposed "udpcast" is put in the rpm spec's requirement of clonezilla. But alien fails to make that deps, so we add in drblsrv.

* Fri Jul 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-4
- update the file, pack wrong drblpush.

* Fri Jul 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-3
- Fixed bugs, client should have services in /etc/rcS.d.
- Fixed some bugs due to client's initrd cramfs format.
- Rewrite some scripts in {bin,sbin} with $SYSCONF_PATH.

* Wed Jul 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-2
- Revise more codes (/opt/drbl/{sbin,bin} to make it work in Debian.

* Wed Jul 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.4.0-1
- merge some codes for Debian, now one package drbl should work in RH/FC/MDK/CentOS/Debian.

* Tue Jun 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-19
- update the GDM theme with org.tw, and use new logo.

* Sun Jun 26 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-18
- remove some useless codes in drblsrv.
- fix the bug for RH9, the tcp over NFS is not supported in the running kernel 2.4.20-8, so we have to use drbl-nfs-conf to switch it.

* Fri Jun 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-17
- exit 1 should be after $SETCOLOR_NORMAL in mknbi-nic
- update some usage message in mknbi-nic

* Thu Jun 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-16
- bug fixed in check_drbl_setup_space, should exclude something like /mnt/tftpboot.

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-15
- bug fixed in mkswapfile, should use variable instead of /tmp/hda1.

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-14
- use "drbl-terminal" instead of "drbl-thin-client" in pxelinux config and dcs.

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-13
- append vt7 in X -query so that the keyboard will work in terminal mode with FC3/4

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-12
- update the MENU local with "Local operation system (if available), this is easier to see, and more appropriate. Not always HD, maybe it's floppy or cdrom.

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-11
- use variables $powerful_client_menu_label and $thin_client_menu_label in sbin/generate-pxe-menu.

* Tue Jun 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-10
- update the message for Mandriva 2005/MDK 10.2 kernel-i586-up-1GB.

* Mon Jun 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-9
- replace description "thin-client" with "terminal mode", this is more appropriate.

* Mon Jun 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-8
- replace OS_Version name "MDK10.2" with "MDV2005"
- now use urpmi for all MDK version, including MDK 9.2/10.0/10.1 and MDV2005.

* Sun Jun 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-7
- forgot to add add OS_version in remote-linux of dcs, added that.

* Thu Jun 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-6
- fix the halt bug in FC4.
- add OS_version so that dcs will show OS_Version in pxelinux's default.
- check yum repository before using it.
- add batch mode for drbl4imp.

* Thu Jun 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-5
- add -t -a -n -m -x -c -g -k options for drblsrv so we can run it in batch mode.
- add -p in drblpush so that we can assign the default client no in each NIC port.
* Thu Jun 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-4
- a bug is fixed: unable to filter i586 or i686 kernel rpm.

* Thu Jun 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-3
- put distribution code name in pxelinux menu (generate-pxe-menu).
- query dev, MAKEDEV and kernel rpm before downloading it.

* Tue Jun 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-2
- fix some bugs in rc.sysinit.drbl, drblsrv (i386 glibc/openssl).

* Tue Jun 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.11-1
- initial release for FC4.

* Sat Jun 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-36
- fix a bug for no menus in MDK 10.2 clients, now add /var/lib/menu /var/lib/menu-xdg for MDK 10.2

* Fri Jun 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-35
- Bug fixed, there is no i386 arch form MDK.

* Fri Jun 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-34
- Skip extra driver question, since it's been a long time we did not create those driver.
- Fix the bug to refer DRBL server's kernel arch.

* Fri Jun 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-33
- Process the special case! Makdrake 10.1/10.2 uses kernel-i586-up-1GB for 586 CPU, The kernel rpm kernel-2.6.11.6mdk-1-1mdk.i586.rpm is only working with i686 CPU. Since Mandrake does NOT want to fix the bug... We have to take care by ourselves! Put UGLY code for Mandrake 10.1/10.2.

* Thu Jun 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-32
- add reiserfs in RH/FC append so that reiserfs will be enabled when installing.

* Thu Jun 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-31
- drop woody, now only sarge netinstall.

* Thu Jun 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-30
- add extra append options in generate-pxe-menu for Debian Sarge netinstall

* Tue Jun 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-29
-  add warning if i386 glibc or openssl rpm is not installed

* Tue Jun 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-28
- make glibc and openssl upgrade as default so that the consistency will be better.

* Mon Jun 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-27
- add selinux=0 in the template of generate-pxe-menu

* Wed Jun 01 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-26
- add a function to check DRBL client's kernel arch.
- fix a bug. In mknic-nbi, it should check client's kernel arch, not server's.

* Wed Jun 01 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-25
- make dcs without -f for drbl-ocs, now -f is the default option for drbl-ocs.

* Tue May 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-24
- convert the uppercase kernel tag to lowercase tag, like X86_64 -> x86_64 in check_kernel_cpu_arch.

* Tue May 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-23
- move smp question easier.

* Tue May 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-22
- replace "drbl" for "drbl-setup" in the language files. 

* Tue May 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-21
- update the echo message in mknic-nbi

* Tue May 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-20
- fix the bug for turn off all PXELinux menus, otherwise client will have problem: boot: EL entries found in configuration file!
- fix the bug for mknic-nbi, now it will update kernel first and check if arch matches.

* Mon May 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-19
- update doc/Known_issues.txt

* Mon May 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-18
- fix the bug, forget setting client's nsswitch.conf nis auth for MDK.

* Sun May 08 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-17
- initial release for MDK 10.2 

* Fri May 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-16
- Circles is the standard shipped theme, it works for RH/FC/MDK. Use it when uninstalling.

* Tue May 03 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-15
- update some lang files for clonezilla clients+time-to-wait mode.

* Tue May 03 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-14
- update some lang files for clonezilla clients+time-to-wait mode.

* Tue May 03 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-13
- fix the bug when running drblsrv 2nd time, unable to check if the kernel arch fits client's requirement.

* Tue May 03 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-12
- fixed a bug when long device name (LVM) check_drbl_setup_space will fail.

* Mon May 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-11
- add version table for MDK 10.1 community 

* Sun May 01 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-10
- update some descriptions for drblsrv.
- put a solution for sis900 NIC in doc/Known_issues.txt.

* Sat Apr 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-9
- fix a bug: lvm2-stop.sh mode is wrong.

* Fri Apr 29 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-8
- add script lvm2-stop.sh in /opt/drbl/sbin

* Sun Apr 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-7
- fix the bug for unable to get right kernel when run "mknic-nbi -a"

* Sun Apr 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-6
- update Makefile and some doc files.

* Sat Apr 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-5
- update AUTHORS/ChangeLog.txt

* Sat Apr 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-4
- recontruct the file archi in /opt/drbl, add dir /opt/drbl/doc.
- use Makefile for the drbl tarball.

* Sat Apr 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-3
- put drbl-setup in the Obsoletes in drbl.spec.

* Sat Apr 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-2
- fix the bugs for forgeting to rename drbl-script and drbl-gdm in drblsrv and drblpush. 

* Sat Apr 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.10-1
- drbl-setup is merged with drbl-script, drbl-gdm, then rename it as package name "drbl"

* Thu Apr 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-26
- update some descriptions for drblsrv.

* Thu Apr 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-25
- fix the bug for unable to download updated kernel in CentOS4.

* Thu Apr 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-24
- update some descriptions for drblpush.

* Thu Apr 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-23
- fix the bug when client's IP last set digits > 100, the hostnames are blank.

* Wed Apr 20 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-22
- force select_repository="yes" in MDK 10.1

* Tue Apr 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-21
- make select yum repository as an option for some distribution
- fix the bug of drbl-client-root-passwd in x86_64
- set client hostname rule as "hostname_prefix[NO]", no more hostname_prefix-[NO] i.e. remove "-". If user want that, he can enter that like "fc3-"

* Tue Apr 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-20
- remove drbl-extra, it's not easy to maintain in so many distributions.

* Tue Apr 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-19
- fix a bug which not putting yum-repos to /opt/drbl/setup.

* Tue Apr 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-18
- use drbl-*-mirror-lists in ayo server when run drblsrv -i -s. So now user does not have to write drbl related yum repository.

* Mon Apr 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-17
- update drblpush with some descriptions.

* Sun Apr 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-16
- update some descriptions for drblsrv.

* Fri Apr 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-15
- update some descriptions for ocs.

* Fri Apr 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-14
- Add some descriptions for ocs.

* Thu Apr 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-13
- Update the description for optimization CPU kernel of client.

* Wed Apr 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-12
- Make x86_64 machine search the right url.

* Tue Apr 12 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-11
- change nbi description in lang/bash.
- fix the bug for unable to hide fdos initially.

* Mon Apr 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-10
- update some description.

* Mon Apr 11 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-9
- update language files

* Sun Apr 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-8
- move language files to /opt/drbl/conf

* Thu Apr 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-7
- update the boot hints in drblpush.

* Thu Apr 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-6
- update the boot hints in drblpush.

* Thu Apr 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-5
- update some echo.

* Thu Apr 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-4
- add code to change PXE menu label when mode drbl is switch to clonezilla.

* Wed Apr 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-3
- remove the code for generate fdos.nbi since etherboot 5.4.0 is released. No more *.nbi.

* Wed Apr 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-2
- bug fixed for wrong url path.

* Wed Apr 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.9-1
- make drblsrv and work without setting up yum/apt/urpmi repository
- add CentOS4 support.
- update rc.sysinit.FC3.drbl and rc.sysinit.default-RH.drbl since rc.sysinit in FC3 is updated.
- drop etherboot config in dhcpd.conf, since etherboot 5.4.0 is released, it can almost fit PXE server except localboot. Now client machine must use etherboot 5.4.0 or newer.

* Thu Mar 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.8-5
- remove the stale file /etc/init.d/ocs when uninstallation.

* Thu Mar 31 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.8-4
- update some descriptions
- do not install perl-IO-LockedFile, we do not need this with new clonezilla.

* Wed Mar 30 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.8-3
- change $ocsroot/ocsmgrd.lock to $ocsroot/clonezilla.lock

* Mon Mar 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.8-2
- Rename some functions name in drbl-function.

* Sun Mar 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.8-1
- Use the simple menu format for pxelinux

* Fri Mar 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-19
- fix the bug for not including drblthincli mkswapfile in client services

* Thu Mar 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-18
- precisely list the class B private IP address 
- fix the bug for unable to copy the mac address file to working directory.

* Thu Mar 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-17
- change the description when generating PXE config file.

* Tue Mar 22 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-16
- move the checking of drbl-script and others packages to the beginning of drblpush.
- remove ntp when uninstalling.

* Mon Mar 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-15
- rename some config files when uninstalling.

* Mon Mar 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-14
- bug fixed, the MAC address file with full path specified by user now works.

* Fri Mar 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-13
- bug fixed for netinstall in MDK.
- add code to clean urpmi and yum setting.

* Fri Mar 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-12
- make netinstall image installation more flexable.

* Wed Mar 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-11
- use generate-pxe-menu to create the PXE menu instead of coding in drblsrv

* Tue Mar 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-10
- Add more specific warning messages when tcp wrapper is set in server.

* Tue Mar 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-9
- remove the /etc/reconfigSys in client's common root

* Tue Mar 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-8
- Support Class A/B/C private IP of DRBL clients.
- Add drbl-yp-securenets to gentrate the /var/yp/securenet.
- Use /opt/drbl/bin/get_ip instead of writing ugly code in perl.
- Keep drbl-setup when running drblsrv -i.
- Fixed bug when libapt-pkg0 is installed while trying to install it.

* Mon Mar 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-7
- use urpmi --auto instead of urpmi --force (MDK bugzilla #14583)

* Mon Mar 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-6
- add drbl-extra option for yum repository.

* Sun Mar 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-5
- use update_client_kernel_from_server.sh in drblsrv and mknbi-nic

* Sun Mar 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-4
- Add a tag of client kernel arch in /tftpboot/nbi_img
- Before rsync kernel module (/lib/modules -> /tftpboot/node_root), check if the arch matches.

* Sat Mar 12 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-3
- Make drblpush more generic, not depends on OS_Version.
- Rewrite the code to run authconfig in /tftpboot/node_root

* Thu Mar 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-2
- Add check and install udev if necessary.
- The services for cleint to run will be checked before them are put into client's /etc/init.d
- Add an option to use existing yum core/updates config instead of overwritting it.

* Wed Mar 9 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.7-1
- Add x86_64 support for FC3.

* Tue Mar 8 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-36
- Add removing dhcp-server, yptools...  when uninstalling drbl in MDK.

* Tue Mar 8 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-35
- For MDK 10.1, use urpmi as the default installer.

* Mon Mar 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-34
- set yum as the default installer for FC3.

* Mon Mar 7 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-33
- fix the bug for unable to separate the drbl-testing and drbl-unstable yum repository.

* Sun Mar 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-32
- Separate the OS and DRBL repository choices for RH/FC/MDK.
- Bugs fixed.

* Wed Mar 2 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-31
- Let wget/glibc/openssl/kernel installation works without apt.
- add code to download dev and MAKEDEV rpm without apt-get.

* Fri Feb 25 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-30
- put client_kernel_install_option in drbl.conf so that it's easier to set it without touching drblsrv.

* Thu Feb 24 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-29
- separate the repository url to url_drbl and url_os.
- now we can find and install the latest kernel without apt.

* Wed Feb 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-28
- bug fixed, when kernel is not available in RPMS.os/RPMS.core, program won't stop, it will try to find it in RPMS.updates.

* Wed Feb 23 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-27
- add code to install client's kernel by rpm only, no apt-get or yum.

* Tue Feb 22 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-26
- merge drblsrv-rh and drblsrv-mdk to drblsrv, we do not separate them.

* Mon Feb 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-25
- rewrite drblsrv-rh using shell scripts only.

* Fri Feb 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-24
- Do NOT set the locale by "export LC_ALL=C" in drbl-functions. It will make dialog distortation.

* Fri Feb 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-23
- correct tyops.
- remove "-w, --website     Browse the NCHC DRBL website" in drblsrv-rh.
- reformat the Usage both in drblsrv-rh and drblsrv-mdk.

* Thu Feb 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-22
- For MDK, the arch is only i586, so add default setting apt_archi_set="i586" in drblsrv-mdk.sh.

* Thu Feb 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-21
- The kernel arch in the server should meet the client's requirement.

* Wed Feb 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-20
- if the latest kernel exists in the server, just copy it to common root, if else, apt-get install it.
- clean $ocsroot/ocsmgrd.lock when uninstalling.

* Wed Feb 16 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-19
- add /tftpboot/node_root/media and tmpfs mount in client's /etc/fstab, we need this for automount USB disk.

* Tue Feb 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-18
- add services - haldaemon messagebus for FC3... we need that for usb automount.

* Tue Feb 15 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-17
- move stop_ocs_if_necessry to drbl-client-switch from drbl-functions.

* Mon Feb 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-16
- fixed the bug - the HOST_OPT1 "$HOST_OPT2" does NOT work when drbl-client-switch run without "-h $IP_LIST"

* Mon Feb 14 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-15
- the hostname of client will use "-" instead of "_", which follows the rule when installing Fedora Core.
- update some functions in drbl-functions to make "drbl-client-switch --list-host" work.

* Sun Feb 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-14
- update drbl.conf.

* Sun Feb 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-13
- reduce one tab before the prompt "DRBL for Mandrake" in rc.sysinit.

* Sun Feb 6 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-12
- initial release for Mandrake Linux 10.1.

* Wed Feb 2 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-11
- the hostname of client will use "_" instead of "-"
- add code to delete the empty line and those comment line of MAC address file.
- add ddrescue isntallation.

* Fri Jan 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-10
- bug fixed.

* Fri Jan 28 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-9
- if unstable is chosen, we must set drbl_test_answer to yes.

* Thu Jan 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-8
- fix the bug when entered MAC file is not name as macadr-eth* 

* Thu Jan 27 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-7
- minor bugs fixed.
- add netgroup generation so that it's easier to add some export directory

* Sat Jan 22 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-6
- add a function to check the input MAC file.

* Fri Jan 21 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-5
- fix the bug for not allowing dot as domainname.

* Wed Jan 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-4
- fix the bugs for "ldd /sbin/depmod" and "ldd /sbin/chkconfig" in MDK 10.0

* Wed Jan 19 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-3
- add checking if initial digits in hostname prefix.
- follow Fedora Project Developer's Guide, turn off the standard output when installing drbl-setup.

* Tue Jan 18 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-2
- add drbl.sf.net + freshrpms.net (RH/Fedora) and drbl.sf.net + distro.ibiblio.org (MDK) as one of the sources when setup DRBL env.

* Mon Jan 17 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.6-1
- use the apt comes with MDK, no more made by DRBL.
- the freshrpms apt_dir is different to that of DRBL, use different name.
- turn off cups service in drbl clients.

* Thu Jan 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-26
- bug fixed, put cups in all versions if cups is on in the server.

* Thu Jan 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-25
- add /etc/sysconfig/drbl/client-extra-service so that use can specify services for clients before running drblpush -i.
- move purging client question to the end of prompt in drblpush.
- bug fixed, IIim in FC2, iiim in FC3, different names

* Thu Jan 13 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-24
- If cups and iiim is on in server, they will be on in the clients.
- fix the bug for searching latest kernel in Mandrake.

* Wed Jan 12 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-23
- add the new method to search latest_drbl_kernel_in_rep, now it will find the really latest kernel. 
- disable reconfiging ntp, user accounts... for clients... in /usr/sbin/firstboot in the firstboot service, we should not do it again in clients.

* Mon Jan 10 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-22
- add hints for yes/no options in the beginning.

* Sun Jan 09 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-21
- add some more notes.
- fix the bug of failing to show message $msg_install_kernel_might_take_several_minutes

* Fri Jan 07 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-20
- update some prompt in lang/bash

* Thu Jan 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-19
- force to remove /etc/sysconfig/firstboot in the common root initially.

* Thu Jan 06 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-18
- add drbl-extra as an option.
- remove xorg.conf in clients initially.

* Tue Jan 04 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-17
- add switch_all_clients_init in drbl-functions.

* Mon Jan 03 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-16
- Do not copy /dev/console, null, tty[0-5] from server to clients, now we use "mount -t tmpfs none /dev" in the beginning of initrd, so we will use mknode to create console, null, tty[0-5] runtime
- Add installing dos2unix in drblsrv-rh and drblsrv-mdk.

* Sun Jan 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-15
- fix the typo for if block.

* Sun Jan 02 2005 Steven Shiau <steven _at_ clonezilla org> 1.3.5-14
- add udev support.
- works for FC3.

* Mon Dec 27 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-13
- change the sources.list to new dir arch for MDK in drbl-setup

* Mon Dec 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-12
- fix wget check bug
- comment the rpm-src, if user need that, just edit sources.list by himself.

* Mon Dec 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-11
- fix the config loading bug in drblsrv-mdk.
- filter the kernel with test lable (in contrib), we do not want that kernel for clients.

* Mon Dec 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-10
- forget to change the file names, like init.RHFC1.drbl -> init.FC1.drbl

* Mon Dec 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-9
- fix the version name bug for drblsrv

* Mon Dec 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-8
- Add installing parted in drblsrv-mdk.sh
- new code to install wget, chaget the RH*_wget_rpm to wget_rpm_RH8_0, wget_rpm_RH9

* Fri Dec 10 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-7
- Bug fixed, we should check the server's kernel config file for CONFIG_NFSD_TCP, not the one for clients.

* Fri Dec 10 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-6
- Copy the macadr-eth*.txt to temp working directory before changing dir.
- Check the kernel config file so we can know if server supports NFS over TCP or not. If not, just use NFS over UDP... So for Redhat 9, it will automatically got it's udp, not tcp...
- Add drbl-unstable option

* Sun Dec 5 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-5
- Add l10n for drbl-powerful-thin-switch.

* Sat Dec 4 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-4
- Fix the bug for not writting timeout in pexlinux.cfg/default.
- Some minor bugs fixed.

* Sat Dec 4 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-3
- Move the drbl-powerful-thin-switch to the last part of drblpush.
- Just ask user to restart/logout kdm/gdm to make the xdmcp config active.
- No more maintain firefly rpms, so skip that in drblsrv.

* Tue Nov 30 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-2
- Add thin client mode prompt in drblpush and option in drbl-client-system-select.

* Tue Nov 30 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.5-1
- Add thin client mode.

* Wed Nov 24 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.4-2
- Fix the bug for checking return code in space check.

* Tue Nov 23 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.4-1
- Add parameters common_root_dir and buffer_ratio_for_client_space in drbl.conf
- Add checking the harddisk space is enough or not

* Mon Nov 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-7
- The pre-saved collected MAC files now can dance with "drblpush -c /etc/sysconfig/drbl/drblpush.conf"

* Mon Nov 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-6
- Make it quiet when removing DRBL old setting files.

* Mon Nov 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-5
- fix the bug for unable to clean /tftpboot/* when uninstalling.

* Mon Nov 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-4
- check if the network card for DRBL environment uses dhcp or static IP, if dhcp, program stop!

* Mon Nov 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-3
- fix the bug for public IP.
- the drblpush.conf and public_ip_list will be copied to /etc/sysconfig/drbl, not /etc/drbl.

* Fri Nov 19 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-2
- unlink the drbl_range temp file when drbl.pl finishes.
- rename the config.interactive to be $DRBLPUSH_CONF="drblpush.conf";
- no more use the current working directory as the working directory. Use temp working directory in drblpush, so the temp created files will be cleaned clearly.
- copy the drblpush.conf to /etc/drbl, so we can re-run drblpush like "drblpush -c /etc/drbl/drblpush.conf"
- exclude the "." in hostname prefix

* Thu Nov 18 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.3-1
- move more setting from drbl-scripts to drbl-ocs. 
- add  a file: drbl-conf-functions

* Thu Nov 11 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.2-3
- add diskless.nchc.org.tw as one of the repository.

* Sat Nov 6 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.2-2drbl
- no more drbl kernel search, use regular kernel from distributions.

* Sat Nov 6 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.2-1drbl
- move stop_ocs_if_necessar() from drbl-ocs to drbl-functions.
- add active_proc_partitions().

* Wed Nov 3 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.1-3drbl
- add active_proc_partitions in drbl-functions so that SCSI devices can be found in drbl-ocs.

* Tue Nov 2 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.1-2drbl
- change the function name set_clients_rc1_passwd in drbl-functions

* Tue Nov 2 2004 Steven Shiau <steven _at_ clonezilla org> 1.3.1-1drbl
- write and move more functions from drbl-ocs to drbl-functions.

* Sat Oct 30 2004 Steven Shiau <steven _at_ clonezilla org> 1.3-1drbl
- Rewrite the program, add /opt/drbl/conf/drbl.conf, /opt/drbl/sbin/drbl-functions and /opt/drbl/sbin/drbl-perl-functions

* Sun Oct 17 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-10drbl
- Use "rsync -a -u" to update files for clients, so now it's not necessary to reboot clients when run "drblpush -i" and select keep the setting. The sshd and other auth mechanism still work without rebooting.

* Mon Oct 11 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-9drbl
- add LC_ALL=C to ` ` in drblpush, thanks to Abdellah Soubaa from France for providing the envorinment to test.

* Sat Oct 9 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-8drbl
- add LC_ALL=C to drblpush system().

* Fri Sep 24 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-7drbl
- fix the bug for SMP.

* Thu Sep 9 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-6drbl
- more clear prompt sentence.

* Thu Sep 9 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-5drbl
- more clear prompt sentence.

* Wed Sep 8 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-4drbl
- write more clear sentence about the dhcp server will provide the same IP address...

* Mon Sep 6 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-3drbl
- fix the bug for unable to get username in drblpush in Mandrake.

* Sat Aug 21 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-2drbl
- when uninstall in mandrake, do not using apt-get remove to remove the kernel in server! Now the kernel is installed directly in /tftpboot/node_root.

* Sat Aug 21 2004 Steven Shiau <steven _at_ clonezilla org> 1.2-1drbl
- drbl kernel is installed into /tftpboot/node_root directly, so now server
and clients can use same version kernel but different archi.
- add ntpd in DRBL server, and client will sync with DRBL server and pool.ntp.org
- fix some bugs.

* Fri Aug 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-7drbl
- fix the bug when uninstalling drbl, the language parameter was empty.

* Sun Aug 01 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-6drbl
- add more descriptions when asking collecting MAC address.
- update the MDK 10.0 official version tag.

* Sat Jul 24 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-5drbl
- add -l|--language option for drblsrv and drblpush so that the language will be consistent with drbl4imp.
- add woody-netinstall in PXE menu.

* Fri Jul 23 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-4drbl
- Add pause in drbl4imp when user chooses to go.
- Make client's hostname shorter.

* Thu Jul 22 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-3drbl
- Add drbl4imp (drbl 4 impatient) to let those impatient to setup DRBL server with default values.

* Tue Jul 20 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-2drbl
- Add codes to exclude /etc,/var,/dev in /etc/init,d/halt of clients.

* Tue Jul 20 2004 Steven Shiau <steven _at_ clonezilla org> 1.1-1drbl
- Add codes for Fedora Core 2, now drbl-setup runs ok in FC2.

* Mon Jul 19 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-40drbl
- Fix the typo in client's rc.local, it's detect_cdrom, not detect-cdrom.

* Mon Jul 19 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-39drbl
- Add drblsrv wrapper script to take care drblsrv-rh and drblsrv-mdk.

* Mon Jul 19 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-38drbl
- Add notes after installing drbl-setup.

* Mon Jul 19 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-37drbl
- Make menu for PXE clients more precise.

* Sat Jul 17 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-36drbl
- Fix the bug for PXE menu, option 1 should be Linux, while "enter" key is system assigned by DRBL server.

* Sat Jul 17 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-35drbl
- Add question for setting boot prompt for PXE client or not.

* Fri Jul 16 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-34drbl
- Freedos use new name fdos1440.img instead of boot1440.img, use this new name.

* Fri Jul 16 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-33drbl
- Fix the exportfs bug by remove creating, exporting and mounting directories /home/partimag and /tftpboot/node_root/home/partimag for clonezilla in script drblpush

* Fri Jul 16 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-32drbl
- Add creating, exporting and mounting directories /home/partimag and /tftpboot/node_root/home/partimag for clonezilla in script drblpush
- Add detect cdrom in rc.local for Mandrake, since harddrake does create /dev/cdrom when client boot.
- Use the same timesync file for client and server.
- Client now has 4 options of system when using PXE to boot, i.e. system assigned by server, system in local harddrive, memtest, freedos.

* Sun Jun 27 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-31drbl
- Let Chinese characters shown when asking language. It's easier to choose the right one with readable characters.

* Sun Jun 20 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-30drbl
- fix the bug for hostname like fc1-1-00, which should be fc1-1-001. We need to get the ip_start from range.
- change the NTP server to be stdtime.sinica.edu.tw.

* Mon Jun 14 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-29drbl
- add the default value prompt of language option in drblsrv-rh, drblsrv-mdk, drblpush.

* Tue Jun 08 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-28drbl
- change the order of NFS mount parameters, fix it as r[ow],...,tcp,nolock or r[ow,...tcp,defaults so that it's easier to change the parameters by script.

* Tue Jun 08 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-27drbl
- Use the tcp options for client to mount the NFS directory, this will be betterwhen there is packet loss in LAN, maybe due to the collision in one single switch for 40 clients.
- clean the kernel.sys of freeDOS when program finishs.

* Tue Jun 01 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-26drbl
- add /var/spool/mail for client to use, now user in clent can access his/her email by using mutt.

* Fri May 28 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-25drbl
- touch the drbl client template: /tftpboot/node_root/etc/modules.conf

* Fri May 28 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-24drbl
- fix the bug, we need to add yppasswdd ypxfrd to chkconfig --add for server. 

* Fri May 21 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-23drbl
- no more the fuzzy description of the last set of digits in the IP address....

* Fri May 21 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-22drbl
- user can specify the apt repository by himself in MDK (drblsrv-mdk).

* Tue May 11 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-21drbl
- force to upgrade gpm when user has FC1, this will avoid the bug of dialog, so clonezilla will work well.

* Tue May 04 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-20drbl
- add check if DRBL kernel is available, if not found, program stop.

- fix the bug when checking alias public IP address, 0 and 255 can not only be the first and last digit, it's only for IP checking, not netmask.
* Mon May 03 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-19drbl
- fix the bug when checking alias public IP address, 0 and 255 can not only be the first and last digit, it's only for IP checking, not netmask.

* Sun May 02 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-18drbl
- fix the bug when checking alias public IP address, 0 and 255 can not only be the first and last digit.

* Wed Apr 21 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-17drbl
- recompiled.

* Sun Apr 18 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-16drbl
- it's cdialog and reiserfsprogs in MDK, not dialog and resierfs-utils

* Sun Apr 18 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-15drbl
- add code to detect if apt is compatible with DRBL in drblsrv-mdk

* Sat Apr 17 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-14drbl
- add -o RPM::Hold::="apt" when use apt-get upgrade in drblsrv-mdk.sh

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-13drbl
- fix the bug with no initial value for exist_size_in_MB in mkswapfile.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-12drbl
- if ethernet port is not available for DRBL environment, program stop.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-11drbl
- add option to remove kernel.*drbl when uninstalling drbl in mdk.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-10drbl
- force to run mknic-nbi with smp option if user specifies smp kernel.
- rewrite kernel searching method for mandrake, now DRBL for Mandrake only uses kernel with tag "drbl"

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-9drbl
- when uninstall, ask if want to remove drbl-setup or not.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-8drbl
- when uninstall, remove drbl-setup.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-7drbl
- when user uses local HD as /tmp, rc.sysinit will not mkdir /boot/tmp.

* Tue Apr 13 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-6drbl
- add bc package in drblsrv-mdk.sh and drblsrv.sh.

* Fri Apr 09 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-5drbl
- let mkpxeinitrd-net take care of the copy and link for vmlinuz-pxe and initrd-net, not in drblsrv-rh or drblsrv-mdk.

* Mon Apr 05 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-4drbl
- add codes to compute the sizes of swap partition and swap file together, so that it meets the /etc/sysconfig/mkswapfile in clients.

* Sun Apr 04 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-3drbl
- Fix bug for drblsrv-mdk, we need to add $drbl_setup_path for dev path.

* Fri Apr 02 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-2drbl
- Fix typos in lang/perl/tw.Big5, and add more directories in /var/lib for clients.

* Thu Apr 01 2004 Steven Shiau <steven _at_ clonezilla org> 1.0-1drbl
- Write drbl setup scripts as rpm package, first release.
