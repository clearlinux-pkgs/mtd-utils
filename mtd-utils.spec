#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xBCE5DC3C741A02D1 (david.oberhollenzer@sigma-star.at)
#
Name     : mtd-utils
Version  : 2.1.6
Release  : 9
URL      : https://infraroot.at/pub/mtd/mtd-utils-2.1.6.tar.bz2
Source0  : https://infraroot.at/pub/mtd/mtd-utils-2.1.6.tar.bz2
Source1  : https://infraroot.at/pub/mtd/mtd-utils-2.1.6.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: mtd-utils-bin = %{version}-%{release}
Requires: mtd-utils-libexec = %{version}-%{release}
Requires: mtd-utils-license = %{version}-%{release}
Requires: mtd-utils-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : buildreq-configure
BuildRequires : lzo-dev
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
UBIFS File System - Make File System program
* crc16.h and crc16.c were copied from the linux kernel.
* crc32.h and crc32.c were copied from mtd-utils and amended.
* ubifs.h is a selection of definitions from fs/ubifs/ubifs.h from the linux kernel.
* key.h is copied from fs/ubifs/key.h from the linux kernel.
* defs.h is a bunch of definitions to smooth things over.
* lpt.c is a selection of functions copied from fs/ubifs/lpt.c from the linux kernel, and amended.
* hashtable/* was downloaded from http://www.cl.cam.ac.uk/~cwc22/hashtable/

%package bin
Summary: bin components for the mtd-utils package.
Group: Binaries
Requires: mtd-utils-libexec = %{version}-%{release}
Requires: mtd-utils-license = %{version}-%{release}

%description bin
bin components for the mtd-utils package.


%package libexec
Summary: libexec components for the mtd-utils package.
Group: Default
Requires: mtd-utils-license = %{version}-%{release}

%description libexec
libexec components for the mtd-utils package.


%package license
Summary: license components for the mtd-utils package.
Group: Default

%description license
license components for the mtd-utils package.


%package man
Summary: man components for the mtd-utils package.
Group: Default

%description man
man components for the mtd-utils package.


%prep
%setup -q -n mtd-utils-2.1.6
cd %{_builddir}/mtd-utils-2.1.6
pushd ..
cp -a mtd-utils-2.1.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693432699
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1693432699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mtd-utils
cp %{_builddir}/mtd-utils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/mtd-utils/74a8a6531a42e124df07ab5599aad63870fa0bd4 || :
cp %{_builddir}/mtd-utils-%{version}/lib/LICENSE.libiniparser %{buildroot}/usr/share/package-licenses/mtd-utils/bd77637feb8e3f23bd137fce23e6720a816d4263 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/doc_loadbios
/V3/usr/bin/docfdisk
/V3/usr/bin/fectest
/V3/usr/bin/flash_erase
/V3/usr/bin/flash_lock
/V3/usr/bin/flash_otp_dump
/V3/usr/bin/flash_otp_erase
/V3/usr/bin/flash_otp_info
/V3/usr/bin/flash_otp_lock
/V3/usr/bin/flash_otp_write
/V3/usr/bin/flash_unlock
/V3/usr/bin/flashcp
/V3/usr/bin/ftl_check
/V3/usr/bin/ftl_format
/V3/usr/bin/jffs2dump
/V3/usr/bin/jffs2reader
/V3/usr/bin/lsmtd
/V3/usr/bin/mkfs.jffs2
/V3/usr/bin/mkfs.ubifs
/V3/usr/bin/mtd_debug
/V3/usr/bin/mtdinfo
/V3/usr/bin/mtdpart
/V3/usr/bin/nanddump
/V3/usr/bin/nandflipbits
/V3/usr/bin/nandtest
/V3/usr/bin/nandwrite
/V3/usr/bin/nftl_format
/V3/usr/bin/nftldump
/V3/usr/bin/recv_image
/V3/usr/bin/rfddump
/V3/usr/bin/rfdformat
/V3/usr/bin/serve_image
/V3/usr/bin/sumtool
/V3/usr/bin/ubiattach
/V3/usr/bin/ubiblock
/V3/usr/bin/ubicrc32
/V3/usr/bin/ubidetach
/V3/usr/bin/ubiformat
/V3/usr/bin/ubihealthd
/V3/usr/bin/ubimkvol
/V3/usr/bin/ubinfo
/V3/usr/bin/ubinize
/V3/usr/bin/ubirename
/V3/usr/bin/ubirmvol
/V3/usr/bin/ubirsvol
/V3/usr/bin/ubiscan
/V3/usr/bin/ubiupdatevol
/usr/bin/doc_loadbios
/usr/bin/docfdisk
/usr/bin/fectest
/usr/bin/flash_erase
/usr/bin/flash_eraseall
/usr/bin/flash_lock
/usr/bin/flash_otp_dump
/usr/bin/flash_otp_erase
/usr/bin/flash_otp_info
/usr/bin/flash_otp_lock
/usr/bin/flash_otp_write
/usr/bin/flash_unlock
/usr/bin/flashcp
/usr/bin/ftl_check
/usr/bin/ftl_format
/usr/bin/jffs2dump
/usr/bin/jffs2reader
/usr/bin/lsmtd
/usr/bin/mkfs.jffs2
/usr/bin/mkfs.ubifs
/usr/bin/mount.ubifs
/usr/bin/mtd_debug
/usr/bin/mtdinfo
/usr/bin/mtdpart
/usr/bin/nanddump
/usr/bin/nandflipbits
/usr/bin/nandtest
/usr/bin/nandwrite
/usr/bin/nftl_format
/usr/bin/nftldump
/usr/bin/recv_image
/usr/bin/rfddump
/usr/bin/rfdformat
/usr/bin/serve_image
/usr/bin/sumtool
/usr/bin/ubiattach
/usr/bin/ubiblock
/usr/bin/ubicrc32
/usr/bin/ubidetach
/usr/bin/ubiformat
/usr/bin/ubihealthd
/usr/bin/ubimkvol
/usr/bin/ubinfo
/usr/bin/ubinize
/usr/bin/ubirename
/usr/bin/ubirmvol
/usr/bin/ubirsvol
/usr/bin/ubiscan
/usr/bin/ubiupdatevol

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/mtd-utils/JitterTest
/V3/usr/libexec/mtd-utils/checkfs
/V3/usr/libexec/mtd-utils/flash_readtest
/V3/usr/libexec/mtd-utils/flash_speed
/V3/usr/libexec/mtd-utils/flash_stress
/V3/usr/libexec/mtd-utils/flash_torture
/V3/usr/libexec/mtd-utils/free_space
/V3/usr/libexec/mtd-utils/fstest_monitor
/V3/usr/libexec/mtd-utils/ftrunc
/V3/usr/libexec/mtd-utils/fwrite00
/V3/usr/libexec/mtd-utils/gcd_hupper
/V3/usr/libexec/mtd-utils/integ
/V3/usr/libexec/mtd-utils/integck
/V3/usr/libexec/mtd-utils/io_basic
/V3/usr/libexec/mtd-utils/io_paral
/V3/usr/libexec/mtd-utils/io_read
/V3/usr/libexec/mtd-utils/io_update
/V3/usr/libexec/mtd-utils/makefiles
/V3/usr/libexec/mtd-utils/mkvol_bad
/V3/usr/libexec/mtd-utils/mkvol_basic
/V3/usr/libexec/mtd-utils/mkvol_paral
/V3/usr/libexec/mtd-utils/nandbiterrs
/V3/usr/libexec/mtd-utils/nandpagetest
/V3/usr/libexec/mtd-utils/nandsubpagetest
/V3/usr/libexec/mtd-utils/orph
/V3/usr/libexec/mtd-utils/pdfrun
/V3/usr/libexec/mtd-utils/perf
/V3/usr/libexec/mtd-utils/plotJittervsFill
/V3/usr/libexec/mtd-utils/rmdir00
/V3/usr/libexec/mtd-utils/rndrm00
/V3/usr/libexec/mtd-utils/rndrm99
/V3/usr/libexec/mtd-utils/rndwrite00
/V3/usr/libexec/mtd-utils/rsvol
/V3/usr/libexec/mtd-utils/stress_1
/V3/usr/libexec/mtd-utils/stress_2
/V3/usr/libexec/mtd-utils/stress_3
/V3/usr/libexec/mtd-utils/test_1
/V3/usr/libexec/mtd-utils/test_2
/V3/usr/libexec/mtd-utils/volrefcnt
/usr/libexec/mtd-utils/JitterTest
/usr/libexec/mtd-utils/checkfs
/usr/libexec/mtd-utils/filljffs2.sh
/usr/libexec/mtd-utils/flash_readtest
/usr/libexec/mtd-utils/flash_speed
/usr/libexec/mtd-utils/flash_stress
/usr/libexec/mtd-utils/flash_torture
/usr/libexec/mtd-utils/free_space
/usr/libexec/mtd-utils/fs_help_all.sh
/usr/libexec/mtd-utils/fs_run_all.sh
/usr/libexec/mtd-utils/fs_stress00.sh
/usr/libexec/mtd-utils/fs_stress01.sh
/usr/libexec/mtd-utils/fstest_monitor
/usr/libexec/mtd-utils/ftrunc
/usr/libexec/mtd-utils/fwrite00
/usr/libexec/mtd-utils/gcd_hupper
/usr/libexec/mtd-utils/integ
/usr/libexec/mtd-utils/integck
/usr/libexec/mtd-utils/io_basic
/usr/libexec/mtd-utils/io_paral
/usr/libexec/mtd-utils/io_read
/usr/libexec/mtd-utils/io_update
/usr/libexec/mtd-utils/load_nandsim.sh
/usr/libexec/mtd-utils/makefiles
/usr/libexec/mtd-utils/mkvol_bad
/usr/libexec/mtd-utils/mkvol_basic
/usr/libexec/mtd-utils/mkvol_paral
/usr/libexec/mtd-utils/nandbiterrs
/usr/libexec/mtd-utils/nandpagetest
/usr/libexec/mtd-utils/nandsubpagetest
/usr/libexec/mtd-utils/orph
/usr/libexec/mtd-utils/pdfrun
/usr/libexec/mtd-utils/perf
/usr/libexec/mtd-utils/plotJittervsFill
/usr/libexec/mtd-utils/rmdir00
/usr/libexec/mtd-utils/rndrm00
/usr/libexec/mtd-utils/rndrm99
/usr/libexec/mtd-utils/rndwrite00
/usr/libexec/mtd-utils/rsvol
/usr/libexec/mtd-utils/runubitests.sh
/usr/libexec/mtd-utils/stress_1
/usr/libexec/mtd-utils/stress_2
/usr/libexec/mtd-utils/stress_3
/usr/libexec/mtd-utils/test_1
/usr/libexec/mtd-utils/test_2
/usr/libexec/mtd-utils/ubi-stress-test.sh
/usr/libexec/mtd-utils/volrefcnt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mtd-utils/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/mtd-utils/bd77637feb8e3f23bd137fce23e6720a816d4263

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mkfs.jffs2.1
/usr/share/man/man8/lsmtd.8
/usr/share/man/man8/ubinize.8
