%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	Google's framework for writing C++ tests
Name:		gtest
Version:	1.7.0
Release:	3
License:	BSD
Group:		Development/C++
Url:		http://code.google.com/p/googletest/
Source0:	http://googletest.googlecode.com/files/%{name}-%{version}.zip
Patch0:		gtest-1.6.0_install.patch

%description
Google's framework for writing C++ tests on a variety of platforms 
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based 
on the xUnit architecture. Supports automatic test discovery, a rich 
set of assertions, user-defined assertions, death tests, fatal and 
non-fatal failures, value- and type-parameterized tests, various 
options for running the tests, and XML test report generation.

%package -n	%{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based
on the xUnit architecture. Supports automatic test discovery, a rich
set of assertions, user-defined assertions, death tests, fatal and
non-fatal failures, value- and type-parameterized tests, various
options for running the tests, and XML test report generation.

This package contains the shared %{name} libraries.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains development files for %{name}.

%prep
%setup -q
%apply_patches

find . -name "*.py" -exec sed -i 's|/usr/bin/env python|%__python2|' {} \;

%build
%configure
%make LIBS='-lpthread'

%install
%makeinstall_std

%check
%make check

%files -n %{libname}
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{devname}
%doc README
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4

