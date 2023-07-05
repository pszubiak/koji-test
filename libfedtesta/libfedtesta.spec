Name:           libfedtesta
Version:        1.0
Release:        3%{?dist}
Summary:        Fedora packaging chain build test
License:        MIT

URL:            https://gitlab.eso.org/fpellegr/koji-chain-tests
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Test library A

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n fed-test-a

%build
make

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%{_libdir}/*

%files devel
%{_includedir}/*


%changelog
* Mon Jul 03 2023 Federico Pellegrin <fpellegr@eso.org> - 1.0
- First release
