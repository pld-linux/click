Summary:	Click Modular Router
Summary(pl.UTF-8):	Click - modularny router
Name:		click
Version:	1.4.3
Release:	0.1
License:	MIT
Group:		Networking/Admin
#Source0Download: http://www.read.cs.ucla.edu/click/download
Source0:	http://www.read.cs.ucla.edu/click/%{name}-%{version}.tar.gz
# Source0-md5:	f719412d7baf4ff874af826a66e3254c
URL:		http://www.read.cs.ucla.edu/click/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Click is a modular software router developed by MIT LCS Parallel and
Distributed Operating Systems group, Mazu Networks, the ICSI Center
for Internet Research, and now UCLA. Click routers are flexible,
configurable, and easy to understand.

A Click router is an interconnected collection of modules called
elements; elements control every aspect of the routers behavior, from
communicating with devices to packet modification to queueing,
dropping policies and packet scheduling. Individual elements can have
surprisingly powerful behavior, and it's easy to write new ones in
C++. You write a router configuration by gluing elements together with
a simple language.

%description -l pl.UTF-8
Click to modularny router rozwijany przez grupę MIT LCS Parallel and
Distributed Operating Systems, Mazu Networks, ICSI Center for Internet
Research, a obecnie UCLA. Routery Click są elastyczne, konfigurowalne
i łatwe do zrozumienia.

Router Click to połączony zestaw modułów nazywanych elementami;
elementy kontrolują każdy aspekt zachowania routerów, od komunikacji z
urządzeniami do modyfikowania pakietów, kolejkowania, polityki
porzucania oraz schedulingu pakietów. Poszczególne elementy mogą mieć
zaskakująco potężne zachowanie i łatwo pisać nowe w C++. Konfiguracją
routera tworzy się przez sklejanie elementów w prostym języku.

%package devel
Summary:	Development files for Click! modular router
Summary(pl.UTF-8):	Pliki programistyczne dla modularnego routera Click!
Group:		Development/Libraries

%description devel
Development files for Click! modular router.

%description devel -l pl.UTF-8
Pliki programistyczne dla modularnego routera Click!.

%prep
%setup -q

%build
%{__autoconf}
%{__aclocal}
%configure \
	--disable-linuxmodule \
	--enable-nsclick \
	--enable-snmp \
	--enable-analysis \
	--enable-ipsec \
	--enable-ip6 \
	--enable-etherswitch \
	--enable-radio \
	--enable-local \
	--enable-test \
	--enable-grid	# include Grid elements (see FAQ)
#	--disable-int64	\

# empty LDLIBS - don't link with -lresolv, it's not necessary
%{__make} \
	LDLIBS=""

#%{__make} man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,/bin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#echo ".so tracepath.8" > $RPM_BUILD_ROOT%{_mandir}/man8/tracepath6.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}/elementmap.xml
#/usr/share/click/srcdir
%{_infodir}/click.info*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/click
%{_includedir}/click/*.hh
%{_includedir}/click/*.h
%dir %{_includedir}/click/standard
%{_includedir}/click/standard/*.hh
%dir %{_includedir}/clicknet
%{_includedir}/clicknet/*.h
%dir %{_includedir}/clicktool
%{_includedir}/clicktool/*.hh
%{_libdir}/*.a
