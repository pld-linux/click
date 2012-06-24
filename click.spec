Summary:	Click Modular Router
Summary(pl):	Click - modularny router
Name:		click
Version:	22_03_2004_one
Release:	0.1
License:	MIT
Group:		Networking/Admin
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-cvs_%{version}.tar.gz
# Source0-md5:	a31f932eeb2b285d294f7bef70bac7a3
URL:		http://pdos.lcs.mit.edu/click/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Click is a modular software router developed by MIT LCS Parallel and 
Distributed Operating Systems group, Mazu Networks, the ICSI Center for 
Internet Research, and now UCLA. Click routers are flexible, configurable,
and easy to understand. 

A Click router is an interconnected collection of modules called elements; 
elements control every aspect of the routers behavior, from communicating 
with devices to packet modification to queueing, dropping policies and packet 
scheduling. Individual elements can have surprisingly powerful behavior, and 
it's easy to write new ones in C++. You write a router configuration by 
gluing elements together with a simple language.

%description -l pl
Click to modularny router rozwijany przez grup� MIT LCS Parallel and
Distributed Operating Systems, Mazu Networks, ICSI Center for Internet
Research, a obecnie UCLA. Routery Click s� elastyczne, konfigurowalne
i �atwe do zrozumienia.

Router Click to po��czony zestaw modu��w nazywanych elementami;
elementy kontroluj� ka�dy aspekt zachowania router�w, od komunikacji z
urz�dzeniami do modyfikowania pakiet�w, kolejkowania, polityki
porzucania oraz schedulingu pakiet�w. Poszczeg�lne elementy mog� mie�
zaskakuj�co pot�ne zachowanie i �atwo pisa� nowe w C++. Konfiguracj�
routera tworzy si� przez sklejanie element�w w prostym j�zyku.

%prep
%setup -q -n one

%build
%{__autoconf}
%{__aclocal}
%configure \
	--enable-nsclick \
	--enable-snmp \
	--enable-analysis \
	--enable-ipsec \
	--enable-ip6 \
	--enable-etherswitch \
	--enable-radio \
	--enable-local \
	--enable-test  \
	--enable-grid        #   include Grid elements (see FAQ)
#  --disable-int64	\

# empty LDLIBS - don't link with -lresolv, it's not necessary
%{__make} \
	LDLIBS=""

#%{__make} man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,/bin}

#install arping clockdiff rdisc tracepath tracepath6 traceroute6 \
#	$RPM_BUILD_ROOT%{_sbindir}

#install ping ping6 $RPM_BUILD_ROOT/bin

install doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so tracepath.8" > $RPM_BUILD_ROOT%{_mandir}/man8/tracepath6.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man8/*
