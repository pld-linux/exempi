Summary:	An XMP support library
Name:		exempi
Version:	1.99.4
Release:	1.1
License:	BSD
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	7efeb1c35d19016607911d4ba89c3745
BuildRequires:	boost-devel
BuildRequires:	expat
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMP parsing and IO library

%package devel
Summary:	Header files fox exempi
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for exempi.

%package static
Summary:	Static exempi libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static exempi libraries.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libexempi.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexempi.so
%{_libdir}/libexempi.la
%{_includedir}/exempi-2.0/*
%{_prefix}/%{_lib}/pkgconfig/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libexempi.a
