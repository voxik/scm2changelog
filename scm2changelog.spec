Name: scm2changelog
# Go with incremental number, ignoring Release
Version: 1
Release: 1%{?dist}
Summary: scm2changelog
License: MIT
Source0: macros.scm2changelog
Source1: git2changelog
Requires: %{_bindir}/git
Requires: %{_bindir}/sed
BuildArch: noarch

%description
Provides RPM macros to generate changelog from SCM log.


%prep

%build

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{rpmmacrodir}

mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}

%check
# No tests yet :/

%files
%{rpmmacrodir}/macros.scm2changelog
%{_bindir}/git2changelog

%changelog
