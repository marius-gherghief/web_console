Name:           web-console
Version:        0.1.1
Release:        0
Summary:        Symmetry Apps - Web Console
Group:          Applications/Multimedia
License:        GPL
URL:            https://github.com/symmetry-apps/web_console
Vendor:         Symmetry Apps
Source0:        web-console.tar.gz
BuildRoot:      %{_tmppath}/%{name}-root

Requires(post): info
Requires(preun):info

%description
Slack Bot ssh interface for distributed environments

%prep
%setup

%build
make PREFIX=/usr %{?_smp_mflags}

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/cacert.pem
%{_bindir}/config-sample.ini
%{_bindir}/web-console
%{_bindir}/web-console.service

%changelog
