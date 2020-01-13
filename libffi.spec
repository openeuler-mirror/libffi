Name:		libffi
Version:	3.3
Release:	2
Summary:	A Portable Foreign Function Interface Library
License:	MIT
URL:		http://sourceware.org/libff
Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libffi

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

%package -n libffi7
Summary:A Portable Foreign Function Interface Library

%description -n libffi7
libffi.so.7 for %{name}

%package -n libffi6
Summary:A Portable Foreign Function Interface Library

%description -n libffi6
libffi.so.6 for %{name}

%package        help
Summary:        libffi help
Requires:       info
BuildArch:      noarch

%description    help
The help package contains man files.

%prep
%autosetup -n %{name}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
%delete_la

cp -a %{_libdir}/libffi.so.6* %{buildroot}%{_libdir}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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
%{_libdir}/*.so.*

%files -n libffi7
%{_libdir}/*.so.7*

%files -n libffi6
%{_libdir}/*.so.6*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ffi*.h
%{_libdir}/*.so

%files help
%{_mandir}/man3/*.gz
%{_infodir}/libffi.info.gz

%changelog
* Tue Jan 13 2020 chengquan<chengquan3@huawei.com> - 3.3-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:fix bug in update dynamic library

* Wed Jan 8 2020 chengquan<chengquan3@huawei.com> - 3.3-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update softwre to 3.3

* Fri Oct 11 2019 hanzhijun<hanzhijun1@huawei.com> - 3.2.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update to 3.2.1

* Mon Sep 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1-19
- Package init
