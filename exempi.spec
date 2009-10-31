Summary:	An XMP support library
Summary(pl.UTF-8):	Biblioteka obsługująca XMP
Name:		exempi
Version:	2.1.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	62ecb5a01387b9f940a5429b3df67e65
URL:		http://libopenraw.freedesktop.org/wiki/Exempi
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libstdc++-devel
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

%package samples
Summary:	Sample exempi programs
Summary(pl.UTF-8):	Przykładowe programy exempi
Group:		Applications/Archiving
# doesn't require base, statically linked with exempi code

%description samples
Sample programs using exempi library.

%description devel -l pl.UTF-8
Przykładowe programy używające biblioteki exempi.

%prep
%setup -q

%build
# configure fails on boost linking check
%configure \
	ax_cv_boost_unit_test_framework=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/source/{dumpmainxmp,dumpxmp,xmpcoverage,xmpfilescoverage} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libexempi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexempi.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexempi.so
%{_libdir}/libexempi.la
%{_includedir}/exempi-2.0
%{_pkgconfigdir}/exempi-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libexempi.a

%files samples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
