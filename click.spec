Summary:	Click Modular Router
Summary(pl):	Click modularny router
Name:		click
Version:	22_03_2004_one
Release:	0.1
License:	MIT
Group:		Networking/Admin
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-cvs_%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Click Modular Router Project

%description -l pl
Click projekt modularnego routera

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

%{__make} man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,/bin}

install arping clockdiff rdisc tracepath tracepath6 traceroute6 \
	$RPM_BUILD_ROOT%{_sbindir}

install ping ping6 $RPM_BUILD_ROOT/bin

install doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so tracepath.8" > $RPM_BUILD_ROOT%{_mandir}/man8/tracepath6.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_sbindir}/tracepat*
%attr(0755,root,root) %{_sbindir}/rdisc
%attr(4754,root,adm) %{_sbindir}/traceroute6
%attr(4754,root,adm) %{_sbindir}/arping
%attr(4754,root,adm) %{_sbindir}/clockdiff
%{_mandir}/man8/arping.8*
%{_mandir}/man8/clockdiff.8*
%{_mandir}/man8/rdisc.8*
%{_mandir}/man8/tracepath*.8*
%{_mandir}/man8/traceroute6.8*
%{_mandir}/man8/pg3.8*
