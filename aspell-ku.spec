Summary:	Kurdish dictionary for aspell
Summary(pl.UTF-8):	Słownik kurdyjski dla aspella
Name:		aspell-ku
Version:	0.20
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ku/aspell5-ku-%{version}-%{subv}.tar.bz2
# Source0-md5:	8d714169b131fc6ca8a783c6acc471ae
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kurdish dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik kurdyjski (lista słów) dla aspella.

%prep
%setup -q -n aspell5-ku-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
