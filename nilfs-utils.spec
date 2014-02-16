Summary:	Tools for the NILFS filesystem
Name:		nilfs-utils
Version:	2.1.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.nilfs.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	3d8166ba2346b61ac8dd83a64e92ae0f
URL:		http://www.nilfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmount-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NILFS is a log-structured file system supporting versioning of the
entire file system and continuous snapshotting which allows users to
even restore files mistakenly overwritten or destroyed just a few
seconds ago.

This package provides utilities for NILFS.

%package libs
Summary:	NILFS library
Group:		Libraries

%description libs
NILFS library.

%package devel
Summary:	Header files for NILFS
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for NILFS.

%prep
%setup -q

%{__sed} -i 's|chown|# chowm|g' sbin/*/Makefile.am
%{__sed} -i 's|/sbin|%{_sbindir}|g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/nilfs_cleanerd.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

