Name:           fedtestc
Version:        1.0
Release:        1%{?dist}
Summary:        Fedora packaging chain build test
License:        MIT

URL:            https://gitlab.eso.org/fpellegr/koji-chain-tests
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libfedtestb-devel

Requires:       libfedtestb

%description
Test program C

%prep
%autosetup -n fed-test-c

%build
make

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%{_bindir}/*


%changelog
* Mon Jul 03 2023 Federico Pellegrin <fpellegr@eso.org> - 1.0
- First release
