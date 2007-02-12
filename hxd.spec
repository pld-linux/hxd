#
# Conditional build:
%bcond_without	tracker_registration	# build without supporting registration with a tracker
%bcond_without	find			# build without suppor for /find & /exec
%bcond_with	client			# build with client
#
Summary:	HotlineX (hx) serwer
Summary(pl.UTF-8):   Serwer HotlineX (hx)
Name:		hxd
Version:	0.2.18
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://hx.fortyoz.org/%{name}-%{version}.tar.gz
# Source0-md5:	0fc15f90c6de03740add84b95bc69915
Patch0:		%{name}-curses.patch
URL:		http://hx.fortyoz.org/
%{?with_client:BuildRequires:	libreadline-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HotlineX (hx) is an implementation of the Hotline protocol for un*x
based systems.

%description -l pl.UTF-8
Jest to pakiet pozwalający na udostępnianie zasobów hotline pod
systemami z X w nazwie, BSD też się liczą.

%prep
%setup -q

%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
./configure --prefix=%{_prefix} \
%{?with_tracker_registration:	--enable-tracker-register 	} \
%{?with_tracker_registration:	--enable-exec	 		} \
%{?with_client:			--enable-hotline-client		}
# 	--with-socks
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -m755 -d $RPM_BUILD_ROOT%{_datadir}/{bin,man/man1}
install -d $RPM_BUILD_ROOT%{_bindir}
install src/hxd/hxd $RPM_BUILD_ROOT%{_bindir}
#install  $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS INSTALL NEWS PROBLEMS README*
%attr(755,root,root) %{_bindir}/*
#%%{_mandir}/man1/*
