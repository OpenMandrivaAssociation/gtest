%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d
%define staticdevelname	%mklibname %{name} -d -s

Name:			gtest
Summary:		Google's framework for writing C++ tests
Version:		1.6.0
Release:		1
License:		BSD
Group:			Development/C++
URL:			http://code.google.com/p/googletest/
Source0:		http://googletest.googlecode.com/files/%{name}-%{version}.zip
BuildRequires:		python

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

%build

# pz: Since 1.5.0 we have an underlinking problem. There are 2 ways to fix it:
#     - %define _disable_ld_no_undefined 1
#     - export LDFLAGS="-lpthread"
# Maybe we can also fix this by changing the autoconf macro that selects the
# pthread flags...
#define _disable_ld_no_undefined 1

#autoreconf -f -i
%configure2_5x --disable-static
%make

%check
%make check

%install
rm -rf %{buildroot}
%makeinstall

find %{buildroot} -type f -name "*.la" -delete

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc README CHANGES CONTRIBUTORS COPYING
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
