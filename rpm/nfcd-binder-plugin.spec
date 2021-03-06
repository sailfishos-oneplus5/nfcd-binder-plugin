Name: nfcd-binder-plugin
Version: 1.1.3
Release: 0
Summary: Binder-based NFC plugin
License: BSD
URL: https://github.com/mer-hybris/nfcd-binder-plugin
Source: %{name}-%{version}.tar.bz2

%define libgbinder_version 1.0.30
%define nfcd_version 1.0.20

BuildRequires: pkgconfig(libncicore)
BuildRequires: pkgconfig(libnciplugin)
BuildRequires: pkgconfig(libgbinder) >= %{libgbinder_version}
BuildRequires: pkgconfig(nfcd-plugin) >= %{nfcd_version}
Requires: libgbinder >= %{libgbinder_version}
Requires: nfcd >= %{nfcd_version}

%define plugin_dir /usr/lib/nfcd/plugins

%description
Binder-based NFC plugin for Android 8+.

%prep
%setup -q

%build
make %{_smp_mflags} KEEP_SYMBOLS=1 release

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post
systemctl reload-or-try-restart nfcd.service ||:

%postun
systemctl reload-or-try-restart nfcd.service ||:

%files
%defattr(-,root,root,-)
%dir %{plugin_dir}
%{plugin_dir}/*.so
