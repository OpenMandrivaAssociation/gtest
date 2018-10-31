# ****ing python 2.x
%global _python_bytecompile_build 0

%define major	0
%define libname	%mklibname %{name} %{major}
%define mocklibname	%mklibname gmock %{major}
%define devname	%mklibname %{name} -d
%define mockdevname	%mklibname gmock -d

Summary:	Google's framework for writing C++ tests
Name:		gtest
Version:	1.8.0
Release:	2
License:	BSD
Group:		Development/C++
Url:		https://github.com/google/googletest
Source0:	https://github.com/google/googletest/archive/release-%{version}.tar.gz
Patch0:		googletest-1.8.0-sonames.patch
BuildRequires:	cmake ninja
%rename gmock

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

%package -n	%{mocklibname}
Summary:	Shared libraries for gmock
Group:		System/Libraries

%description -n	%{mocklibname}
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:

 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{mocklibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{mockdevname}

%description -n	%{devname}
This package contains development files for %{name}.

%package source
Summary:	Source code for the %{name} test suite
Group:		Development/C++

%description source
Source code for the %{name} test suite.

Many projects using %{name} require copying the source code into
the project tree rather than using a system wide copy.

%prep
%autosetup -n googletest-release-%{version} -p1

find . -name "*.py" -exec sed -i 's|/usr/bin/env python|%__python2|' {} \;

%cmake \
	-DBUILD_GMOCK:BOOL=ON \
	-DBUILD_GTEST:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-Dgtest_force_shared_crt:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_prefix}/src/%{name}
rm -rf build
cp -a * %{buildroot}%{_prefix}/src/%{name}/

%files -n %{libname}
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{mocklibname}
%{_libdir}/libgmock*.so.%{major}*

%files -n %{devname}
%{_libdir}/lib%{name}*.so
%{_libdir}/libgmock*.so
%{_includedir}/%{name}
%{_includedir}/gmock

%files source
%{_prefix}/src/%{name}
