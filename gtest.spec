%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:			gtest
Summary:		Google's framework for writing C++ tests
Version:		1.6.0
Release:		1
License:		BSD
Group:			Development/C++
URL:			http://code.google.com/p/googletest/
Source0:		http://googletest.googlecode.com/files/%{name}-%{version}.zip
Patch0:			gtest-1.6.0_install.patch

%description
Google's framework for writing C++ tests on a variety of platforms 
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based 
on the xUnit architecture. Supports automatic test discovery, a rich 
set of assertions, user-defined assertions, death tests, fatal and 
non-fatal failures, value- and type-parameterized tests, various 
options for running the tests, and XML test report generation.

%package -n		%{libname}
Summary:		Shared libraries for %{name}
Group:			System/Libraries

%description -n 	%{libname}
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based
on the xUnit architecture. Supports automatic test discovery, a rich
set of assertions, user-defined assertions, death tests, fatal and
non-fatal failures, value- and type-parameterized tests, various
options for running the tests, and XML test report generation.

This package contains the shared %{name} libraries.

%package -n		%{develname}
Summary:		Development files for %{name}
Group:			Development/C++
Requires:		%{libname} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}

%description -n		%{develname}
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make LIBS='-lpthread'

%install
%makeinstall_std

%check
%make check

%files -n %{libname}
%doc README COPYING
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4


%changelog
* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.6.0-1
+ Revision: 708348
- fixed build with p0
- fixed source name
- new version 1.6.0
  dropped static build
  cleaned up spec

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-2
+ Revision: 664941
- mass rebuild

* Tue Feb 22 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.0-1
+ Revision: 639300
- New version: 1.5.0
- Fix underlinking problem
- Use configure2_5x

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-3mdv2011.0
+ Revision: 605506
- rebuild

* Sat Nov 14 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.0-2mdv2010.1
+ Revision: 466108
- fix Requires name in the devel subpackage

* Sat Nov 14 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.0-1mdv2010.1
+ Revision: 466063
- fix groups
- add a %%check section (+ needed python BR)
- import gtest

