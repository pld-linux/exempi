Summary:	An XMP support library
Summary(pl.UTF-8):	Biblioteka obsługująca XMP
Name:		exempi
Version:	1.99.4
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	7efeb1c35d19016607911d4ba89c3745
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libstdc++-devel
BuildConflicts:	boost-test-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMP parsing and IO library.

%description -l pl.UTF-8
Biblioteka do analizy oraz wejścia/wyjścia XMP.

%package devel
Summary:	Header files for exempi
Summary(pl.UTF-8):	Pliki nagłówkowe exempi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95
Requires:	libstdc++-devel

%description devel
Header files for exempi.

%description devel -l pl.UTF-8
Pliki nagłówkowe exempi.

%package static
Summary:	Static exempi library
Summary(pl.UTF-8):	Statyczna biblioteka exempi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static exempi library.

%description static -l pl.UTF-8
Statyczna biblioteka exempi.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libexempi.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexempi.so
%{_libdir}/libexempi.la
%{_includedir}/exempi-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libexempi.a
