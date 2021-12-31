%define goarch unknown

%if %{_build_arch} == "x86_64"
%define goarch amd64
%endif

%if %{_build_arch} == "aarch64"
%define goarch arm64
%endif

Summary: Idempotent MySQL/PostgreSQL schema management by SQL
Name: sqldef
Version: 0.11.16
Release: 1
URL: https://github.com/k0kubun/sqldef
Source0: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/mssqldef_linux_%{goarch}.tar.gz
Source1: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/mysqldef_linux_%{goarch}.tar.gz
Source2: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/psqldef_linux_%{goarch}.tar.gz
Source3: https://github.com/itamae-kitchen/mitamae/releases/download/v%{version}/sqlite3def_linux_%{goarch}.tar.gz
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The easiest idempotent MySQL/PostgreSQL/SQLite3/SQL Server schema management by SQL.

This is inspired by Ridgepole but using SQL, so there's no need to remember Ruby DSL.

%prep

%build
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
tar xzvf %{SOURCE2}
tar xzvf %{SOURCE3}

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 -p mssqldef %{buildroot}/%{_bindir}/mssqldef
%{__install} -m 755 -p mysqldef %{buildroot}/%{_bindir}/mysqldef
%{__install} -m 755 -p psqldef %{buildroot}/%{_bindir}/psqldef
%{__install} -m 755 -p sqlite3def %{buildroot}/%{_bindir}/sqlite3def

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mssqldef
%{_bindir}/mysqldef
%{_bindir}/psqldef
%{_bindir}/sqlite3def

%changelog
* Fri Dec 31 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.16

* Sun Dec 12 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.15

* Mon Nov 15 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.14

* Sat Nov 6 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.13

* Sat Nov 6 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.12

* Sun Oct 31 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.11

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.10

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.9

* Sat Oct 16 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.8

* Wed Sep 29 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.7

* Tue Sep 28 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.6

* Tue Sep 28 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.5

* Thu Sep 23 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.4

* Sun Sep 19 2021 Ichnose Shogo <shogo82148@gmail.com>
- bump v0.11.3

* Sun Sep 19 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.2

* Sat Sep 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.1

* Sat Sep 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.11.0

* Sun Jul 18 2021 Ichinose Shogo <shogo82148@gmail.com>
- bump v0.10.16
