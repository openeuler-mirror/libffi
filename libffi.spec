%global target_arch %{ix86} x86_64

Name:		libffi
Version:	3.2.1
Release:	1
Summary:	A Portable Foreign Function Interface Library
License:	MIT
URL:		http://sourceware.org/libffi

Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h
Patch0:		libffi-3.1-fix-include-path.patch
Patch1:		libffi-aarch64-rhbz1174037.patch
Patch2:		libffi-3.1-aarch64-fix-exec-stack.patch

Patch6004:0053-aarch64-Improve-is_hfa.patch
Patch6005:0054-aarch64-Always-distinguish-LONGDOUBLE.patch
Patch6006:0055-aarch64-Simplify-AARCH64_STACK_ALIGN.patch
Patch6007:0056-aarch64-Reduce-the-size-of-register_context.patch
Patch6008:0058-aarch64-Treat-void-return-as-not-passed-in-registers.patch
Patch6009:0059-aarch64-Tidy-up-abi-manipulation.patch

Patch6010:0199-Define-_GNU_SOURCE-on-Linux-for-mremap.patch
Patch6011:0208-Don-t-dereference-ecif-before-NULL-check.patch
Patch6012:0252-Fix-misaligned-memory-access-in-ffi_call_int.patch
Patch6013:0333-Fully-allocate-file-backing-writable-maps-389.patch

BuildRequires: gcc

%description
Compilers for high level languages generate code that follows certain conventions. These
conventions are necessary, in part, for separate compilation to work. One such convention
is the "calling convention". The "calling convention" is a set of assumptions made by the
compiler about where function arguments will be found on entry to a function. A "calling
convention" also specifies where the return value for a function is found.

Some programs may not know at the time of compilation what arguments are to be passed to a
function. For instance, an interpreter may be told at run-time about the number and types
of arguments used to call a given function. Libffi can be used in such programs to provide
a bridge from the interpreter program to compiled code.

The libffi library provides a portable, high level programming interface to various calling
conventions. This allows a programmer to call any function specified by a call interface
description at run-time.

FFI stands for Foreign Function Interface. A foreign function interface is the popular name
for the interface that allows code written in one language to call code written in another
language. The libffi library really only provides the lowest, machine dependent layer of a
fully featured foreign function interface. A layer must exist above libffi that handles type
conversions for values passed between the two languages.

%package	devel
Summary:	Development files for libffi
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The devel package with header files and libraries is for developing apps which needs libffi.

%package        help
Summary:        libffi help
Requires:       info
BuildArch:      noarch

%description    help
The help package contains man files.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

base=%{_arch}
%ifarch %{ix86}
base=i386
%endif

mkdir -p $RPM_BUILD_ROOT%{_includedir}
%ifarch %{target_arch}
mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/ffi.h $RPM_BUILD_ROOT%{_includedir}/ffi-${base}.h
mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/ffitarget.h $RPM_BUILD_ROOT%{_includedir}/ffitarget-${base}.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/ffitarget.h
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/ffi.h
%else
mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/{ffi,ffitarget}.h $RPM_BUILD_ROOT%{_includedir}
%endif
rm -rf $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}


%ldconfig_scriptlets

%check
make check

%post help
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/libffi.info.gz || :

%preun help
if [ $1 = 0 ] ;then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/libffi.info.gz || :
fi


%files
%license LICENSE
%doc README
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ffi*.h
%{_libdir}/*.so

%files help
%{_mandir}/man3/*.gz
%{_infodir}/libffi.info.gz

%changelog
* Fri Oct 11 2019 hanzhijun<hanzhijun1@huawei.com> - 3.2.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update to 3.2.1

* Mon Sep 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1-19
- Package init
