Summary:	Click Modular Router
Summary(pl):	Click modularny router
Name:		click
Version:	22_03_2004_one
Release:	0.1
License:	MIT
URL:		http://pdos.lcs.mit.edu/click/
Group:		Networking/Admin
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-cvs_%{version}.tar.gz
# Source0-md5:	a31f932eeb2b285d294f7bef70bac7a3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	libstdc++-devel

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

#%description -l pl
#Click to modularny  router.
#
#BLA BLA BLA niech ktos to przetulaczy, ja ide spac.

%prep
%setup  -q -n one

%build
%{__autoconf}
%{__aclocal}
%configure	\
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
%doc  %{_mandir}/man8/*
