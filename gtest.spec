%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d
%define staticdevelname	%mklibname %{name} -d -s

Name:			gtest
Summary:		Google's framework for writing C++ tests
Version:		1.4.0
Release:		%mkrel 1
License:		BSD
Group:			Development/C++
URL:			http://code.google.com/p/googletest/
Source0:		http://googletest.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:		python
BuildRoot:		%{_tmppath}/%{name}-buildroot

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
Requires:		%{name} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}

%description -n		%{develname}
This package contains development files for %{name}.

%package -n		%{staticdevelname}
Summary:		Static development files for %{name}
Group:			Development/C++
Requires:		%{develname} = %{version}-%{release}
Provides:		%{name}-static-devel = %{version}-%{release}

%description -n		%{staticdevelname}
This package contains static development files for %{name}.

%prep
%setup -q

%build
autoreconf -f -i
%configure
%make

%check
%make check

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n		%{libname}
%defattr(-,root,root,-)
%doc README CHANGES CONTRIBUTORS COPYING
%{_libdir}/lib%{name}*.so.*

%files -n		%{develname}
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}*.la
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4

%files -n		%{staticdevelname}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}*.a

