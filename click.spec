Summary:	Click Modular Router
Name:		click
Version:	1.3
%define pre 1
Release:	0.%{pre}.0
License:	MIT
Group:		Networking/Admin
Source0:	http://www.pdos.lcs.mit.edu/click/%{name}-%{version}pre%{pre}.tar.gz
# Source0-md5:	4ab6660d7c0753cfec8bd3df49835f25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Click Modular Router Project

%prep
%setup  -q -n %{name}-%{version}pre%{pre}


%build
%{__autoconf}
%{__aclocal}
%configure
  --enable-nsclick \
  --enable-snmp \
  --enable-analysis \
  --enable-ipsec \
  --enable-ip6 \
  --enable-etherswitch \
  --enable-radio \
  --enable-local \
  --enable-test \
#  --enable-grid        #   include Grid elements (see FAQ)

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
