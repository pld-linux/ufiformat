Summary:	Low-level (physical) formatting tool for USB-FDD
Summary(pl.UTF-8):	Narzędzie do formatowania niskopoziomowego dla stacji FDD podłączanych przez USB
Name:		ufiformat
Version:	0.9.9
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: http://www.geocities.jp/tedi_world/format_usbfdd_e.html
Source0:	http://www.geocities.jp/tedi_world/%{name}-%{version}.tar.gz
# Source0-md5:	18e41a189b81b1599a38ce8640698b7f
URL:		http://www.geocities.jp/tedi_world/format_usbfdd_e.html
# libext2fs
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low-level (physical) formatting tool for USB floppy drives.

%description -l pl.UTF-8
Narzędzie do niskopoziomowego (fizycznego) formatowania dyskietek w
stacjach dyskietek podłączanych przez USB.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ufiformat
%{_mandir}/man8/ufiformat.8*
