#
# Conditional build:
# _without_tracker_registration         -build without supporting registration with a tracker
# _without_find                         -build without suppor for /find & /exec
# _with_client                          -build with client
#
Summary:	HotlineX (hx) serwer
Summary(pl):	Serwer HotlineX (hx)
Name:		hxd
Version:	0.2.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://hx.fortyoz.org/%{name}-%{version}.tar.gz
URL:		http://hx.fortyoz.org/
%{?_with_client:BuildRequires:        libreadline-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HotlineX (hx) is an implementation of the Hotline protocol for un*x
based systems.

%description -l pl
Jest to pakiet pozwalaj±cy na udostêpnianie zasobów hotline pod
systemami z X w nazwie, BSD te¿ siê licz±.

%prep
%setup -q 

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
./configure --prefix=%{_prefix} \
%{!?_without_tracker_registration:	--enable-tracker-register 	} \
%{!?_without_tracker_registration:	--enable-exec	 		} \
%{?_with_client:			--enable-hotline-client		}
# 	--with-socks
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -m755 -d $RPM_BUILD_ROOT%{_datadir}/{bin,man/man1}
install -d $RPM_BUILD_ROOT%{_bindir}
install src/hxd/hxd $RPM_BUILD_ROOT%{_bindir}
#install  $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf ChangeLog AUTHORS INSTALL COPYING NEWS PROBLEMS README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz AUTHORS.gz INSTALL.gz COPYING.gz 
%doc NEWS.gz PROBLEMS.gz README*.gz
%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man1/*
